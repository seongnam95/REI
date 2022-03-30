from PySide6.QtCore import QThread, QObject, Signal
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
from seleniumrequests import Chrome

import time
import webbrowser
import json


class ThreadSignal(QObject):
    workerThreadDone = Signal(bool)
    progress = Signal(str)


class IssuanceBuildingLedger(QThread):
    def __init__(self, pk, kind, user_id, user_pw):
        super().__init__()
        self.threadEvent = ThreadSignal()

        self.sigungu, self.seqno = pk.split('-')[0], pk.split('-')[1]   # PK
        self.kind = kind     # 건물 타입, 대장 종류
        self.user_id, self.user_pw = user_id, user_pw   # ID, PW
        self.address, self.driver = '', None

        self.headers = {
            "Host": "cloud.eais.go.kr",
            "Content-Type": "application/json;charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
        }

    def run(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')  # 크롬 화면 숨기기
        chrome_options.add_argument("no-sandbox")  #
        chrome_options.add_argument('window-size=1920x1080')  # 해상도 설정
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("disable-gpu")  # 가속 사용 x
        chrome_options.add_argument("lang=ko_KR")  # 가짜 플러그인 탑재
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) "
                                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")  # user-agent 이름 설정
        self.driver = Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.practice_sign_in()

    # 세움터 로그인
    def practice_sign_in(self):
        try:
            self.threadEvent.progress.emit('로그인 시작')

            self.driver.get("https://cloud.eais.go.kr/moct/awp/abb01/AWPABB01F01")
            self.driver.implicitly_wait(5)

            self.driver.find_element(By.ID, 'membId').send_keys(self.user_id)
            self.driver.find_element(By.ID, 'pwd').send_keys(self.user_pw)
            self.driver.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div/div[1]/div[1]/button').click()
            time.sleep(0.5)

            self.threadEvent.progress.emit('로그인 성공')

            self.issuance_document()

        except Exception as e:
            print(e)
            self.threadEvent.workerThreadDone.emit(False)

    # 문서 발급, 열람
    def issuance_document(self):
        # try:
        self.threadEvent.progress.emit('건축물대장 발급 요청중')

        headers = self.headers
        headers['Referer'] = "https://cloud.eais.go.kr/moct/bci/aaa02/BCIAAA02L01"

        result, ho = None, ''
        if self.kind == 0:
            datas = {"addrGbCd": 2, "bldrgstCurdiGbCd": "0", "sigunguCd": self.sigungu, "bldrgstSeqno": self.seqno}
            response_title = self.driver.request('POST', 'https://cloud.eais.go.kr/bci/BCIAAA02R01', verify=False, headers=headers, json=datas)
            result = json.loads(response_title.text)['jibunAddr'][0]

        elif self.kind == 1:
            datas = {"inqireGbCd": "1", "bldrgstCurdiGbCd": "0", "reqSigunguCd": self.sigungu, "bldrgstSeqno": self.seqno}
            response_title = self.driver.request('POST', 'https://cloud.eais.go.kr/bci/BCIAAA02R04', verify=False, headers=headers, json=datas)
            result = json.loads(response_title.text)['findExposList'][0]

        bun, ji = result['mnnm'].lstrip('0'), result['slno'].lstrip('0')
        if ji: ji = f'-{ji}'
        if "hoNm" in result: ho = ' ' + result["hoNm"]

        self.address = f'{result["sigunguNm"]} {result["bjdongNm"]} {bun}{ji} {result["dongNm"]}{ho}'

        datas2 = {"bldrgstSeqno": result["bldrgstSeqno"],
                  "regstrGbCd": result["regstrGbCd"],
                  "regstrKindCd": result["regstrKindCd"],
                  "mjrfmlyIssueYn": "N",
                  "locSigunguCd": result["sigunguCd"],
                  "locBjdongCd": result["bjdongCd"],
                  "locPlatGbCd": result["platGbCd"],
                  "locDetlAddr": self.address,
                  "locBldNm": result["bldNm"],
                  "bldrgstCurdiGbCd": "0"}

        # 민원 담기 (담아야 응답 값 나옴)
        a = self.driver.request('POST', 'https://cloud.eais.go.kr/bci/BCIAAA02C01', verify=False, headers=headers, json=datas2)
        print(a.text)

        # 담은 민원 처리 (응답 값 필요)
        response_put_in = self.driver.request('POST', 'https://cloud.eais.go.kr/bci/BCIAAA02R05', verify=False, headers=headers)
        result = json.loads(response_put_in.text)
        print(result)

        headers['Referer'] = "https://cloud.eais.go.kr/moct/bci/aaa02/BCIAAA02F01"
        datas = {"pbsvcResveDtls": result['findPbsvcResveDtls'],    # issueReadGbCd (0: 발급, 1: 열람)
                 "pbsvcRecpInfo": {"pbsvcGbCd": "01", "issueReadGbCd": "0", "pbsvcResveDtlsCnt": 1},
                 "appntInfo": {"appntGbCd": "01", "naAppntGrndUgrndGbCd": "0"}}

        # 발급 신청, 담은 민원 제거
        b = self.driver.request('POST', 'https://cloud.eais.go.kr/bci/BCIAZA02S01', verify=False, headers=headers, json=datas)
        c = self.driver.request('POST', 'https://cloud.eais.go.kr/bci/BCIAAA02D02', verify=False, headers=headers,
                            json={'lastUpdusrId': result['findPbsvcResveDtls'][0]['lastUpdusrId']})
        print(b.text)
        print(c.text)
        self.open_document()

        # except Exception as e:
        #     print('err: ', e)
        #     self.threadEvent.workerThreadDone.emit(False)

    # 문서 열기
    def open_document(self):
        # try:
        try_cnt = 0
        success = False
        time.sleep(1)   # 처리중 대기

        while try_cnt < 5:
            self.driver.get('https://cloud.eais.go.kr/moct/bci/aaa04/BCIAAA04L01')
            self.driver.implicitly_wait(5)

            self.threadEvent.progress.emit('발급 완료, 민원 처리 중..' + str(try_cnt))
            try_cnt += 1

            # 완료 처리 된 문서 열기
            list_form = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div[4]/table/tbody')
            document_list = list_form.find_elements(By.TAG_NAME, 'tr')  # 문서 리스트

            for i in document_list:    # 문서 리스트 Row 수만큼 반복
                content = i.get_attribute("innerText")
                print('1::', content)
                if self.address in content:  # 주소가 맞을 경우
                    print('2::', content)
                    if '발급' in content:   # '발급'인 항목 클릭
                        i.find_element(By.XPATH, 'td[5]/a').click()
                        success = True
                        break
            if success: break
            time.sleep(3)

        if success:
            self.threadEvent.progress.emit('처리 완료, 오픈 대기중')
            time.sleep(0.5)
            self.driver.switch_to.window(self.driver.window_handles[1])
            new_url = self.driver.current_url

            self.driver.quit()     # 기존 드라이브 종료

            webbrowser.open_new(new_url)
            self.threadEvent.progress.emit('건축물 대장 오픈')
            self.threadEvent.workerThreadDone.emit(True)

        else:
            self.threadEvent.workerThreadDone.emit(False)
        # except:
        #     self.threadEvent.workerThreadDone.emit(False)

