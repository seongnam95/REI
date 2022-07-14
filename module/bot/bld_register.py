from PySide6.QtCore import QThread, QObject, Signal
from selenium.webdriver.common.by import By

import webbrowser
import requests
import json
import time
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class ThreadSignal(QObject):
    workerThreadDone = Signal(bool)
    progress = Signal(str)


class IssuanceBuildingLedger(QThread):
    def __init__(self, pk, driver, cookies):
        super().__init__()
        self.threadEvent = ThreadSignal()
        self.target_data = pk
        self.kind, self.address, self.file_id = 'kind', '', ''     # 건물 타입, 대장 종류
        self.driver, self.cookies = driver, cookies

        self.s = requests.Session()
        self.s.verify = False

        for cookie in cookies:
            self.s.cookies.set(cookie['name'], cookie['value'])

        self.headers = {
            "Host": "cloud.eais.go.kr",
            "Content-Type": "application/json;charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
        }

    # 문서 발급, 열람
    def run(self):
        try:
            print('## 민원 요청 시작 ##')
            result, ho = self.target_data, ''
            headers = self.headers

            bun, ji = result['mnnm'].lstrip('0'), result['slno'].lstrip('0')
            if ji: ji = f'-{ji}'

            if "hoNm" in result: ho = ' ' + result["hoNm"].strip()
            if 'dongNm' in result.keys():
                dong_nm = result["dongNm"].strip()
                self.address = f'{result["sigunguNm"]} {result["bjdongNm"]} {bun}{ji} {dong_nm}{ho}'
            else: self.address = f'{result["sigunguNm"]} {result["bjdongNm"]} {bun}{ji}'

            # 1. 민원 담기 (담아야 2번 요청 시 응답 값 나옴)
            datas = {"bldrgstSeqno": result["bldrgstSeqno"],
                     "regstrGbCd": result["regstrGbCd"],
                     "regstrKindCd": result["regstrKindCd"],
                     "mjrfmlyIssueYn": "N",
                     "locSigunguCd": result["sigunguCd"],
                     "locBjdongCd": result["bjdongCd"],
                     "locPlatGbCd": result["platGbCd"],
                     "locDetlAddr": self.address,
                     "locBldNm": result["bldNm"],
                     "bldrgstCurdiGbCd": "0"}
            headers['Referer'] = "https://cloud.eais.go.kr/moct/bci/aaa02/BCIAAA02L01"
            self.s.post('https://cloud.eais.go.kr/bci/BCIAAA02C01', headers=headers, json=datas)

            # 2. 담은 민원 처리 (응답 값 필요)
            print('## 민원 처리중 ##')
            response_put_in = self.s.post('https://cloud.eais.go.kr/bci/BCIAAA02R05', headers=headers)
            result = json.loads(response_put_in.text)

            # 3. 발급 신청, 담은 민원 제거
            print('## 발급 신청 완료 ##')
            headers['Referer'] = "https://cloud.eais.go.kr/moct/bci/aaa02/BCIAAA02F01"
            datas = {"pbsvcResveDtls": result['findPbsvcResveDtls'],    # issueReadGbCd (0: 발급, 1: 열람)
                     "pbsvcRecpInfo": {"pbsvcGbCd": "01", "issueReadGbCd": "0", "pbsvcResveDtlsCnt": 1},
                     "appntInfo": {"appntGbCd": "01", "naAppntGrndUgrndGbCd": "0"}}
            self.s.post('https://cloud.eais.go.kr/bci/BCIAZA02S01', headers=headers, json=datas)
            self.s.post('https://cloud.eais.go.kr/bci/BCIAAA02D02', headers=headers,
                        json={'lastUpdusrId': result['findPbsvcResveDtls'][0]['lastUpdusrId']})

            self.open_document()

        except Exception as e:
            print('err: ', e)
            self.threadEvent.workerThreadDone.emit(False)

    # 문서 열기
    def open_document(self):
        # try:
        try_cnt = 0
        success = False

        print('## 열람 대기 ##')
        try:
            msg = self.driver.switch_to.alert
            msg.dismiss()
        except: pass

        self.driver.get('https://cloud.eais.go.kr/moct/bci/aaa04/BCIAAA04L01')
        self.driver.implicitly_wait(5)
        time.sleep(1)   # 리스트 로딩 대기

        while try_cnt < 10:
            print(f'## 민원 신청 완료, 오픈 대기중 (시도 횟수 : {str(try_cnt + 1)}) ##')
            try_cnt += 1

            # 완료 처리 된 문서 열기
            list_form = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div[4]/table/tbody')
            document_list = list_form.find_elements(By.TAG_NAME, 'tr')  # 문서 리스트
            for i in document_list:    # 문서 리스트 Row 수만큼 반복
                content = i.get_attribute("innerText")
                if self.address in content:  # 주소가 맞을 경우
                    if '발급' in content:   # '발급'인 항목 클릭
                        i.find_element(By.XPATH, 'td[5]/a').click()
                        success = True
                        break
            if success: break

            self.driver.save_screenshot('err.png')
            time.sleep(2)

        if success:
            self.threadEvent.progress.emit('처리 완료, 오픈 대기중..')
            time.sleep(0.5)
            self.driver.switch_to.window(self.driver.window_handles[1])
            new_url = self.driver.current_url

            # self.issuance_thread = rt.RegisterScraping(self.driver, self.cookies, self.address, new_url)
            # self.issuance_thread.start()

            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

            webbrowser.open_new(new_url)
            self.threadEvent.progress.emit('건축물 대장 오픈')
            self.threadEvent.progress.emit('END')
            self.threadEvent.workerThreadDone.emit(True)

        else: self.threadEvent.workerThreadDone.emit(False)

        # except Exception as e:
        #     print(type(e), e)
        #     self.threadEvent.workerThreadDone.emit(False)

