from PySide6.QtCore import QThread, QObject, Signal
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import rei_bot.requests_test as rt

import webbrowser
import requests
import json
import time
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class ThreadSignal(QObject):
    workerThreadDone = Signal(bool)
    progress = Signal(str)
    chromeDriver = Signal(object)


class SetChrome(QThread):
    def __init__(self, user_id, user_pw):
        super().__init__()
        self.threadEvent = ThreadSignal()

        self.driver = None
        self.user_id, self.user_pw = user_id, user_pw

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
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        self.driver.get("https://cloud.eais.go.kr/moct/awp/abb01/AWPABB01F01")
        self.driver.implicitly_wait(5)

        time.sleep(0.5)
        self.driver.find_element(By.ID, 'membId').send_keys(self.user_id)
        self.driver.find_element(By.ID, 'pwd').send_keys(self.user_pw)
        self.driver.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div/div[1]/div[1]/button').click()
        time.sleep(0.5)

        self.threadEvent.chromeDriver.emit(self.driver)


class IssuanceBuildingLedger(QThread):
    def __init__(self, pk, kind, driver, cookies):
        super().__init__()
        self.threadEvent = ThreadSignal()

        self.sigungu, self.seqno = pk.split('-')[0], pk.split('-')[1]   # PK
        self.kind, self.address, self.file_id = kind, '', ''     # 건물 타입, 대장 종류
        self.driver, self.cookies = driver, driver.get_cookies()

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
        # try:
        self.threadEvent.progress.emit('건축물대장 발급 요청중..')

        headers = self.headers
        headers['Referer'] = "https://cloud.eais.go.kr/moct/bci/aaa02/BCIAAA02L01"

        result, ho = None, ''
        if self.kind == 1:      # 표제부, 일반 건축물 요청
            datas = {"addrGbCd": 2, "bldrgstCurdiGbCd": "0", "sigunguCd": self.sigungu, "bldrgstSeqno": self.seqno}
            response_title = self.s.post('https://cloud.eais.go.kr/bci/BCIAAA02R01', headers=headers, json=datas)
            time.sleep(0.5)
            json_data = json.loads(response_title.text)
            result = json_data['jibunAddr'][0]

        elif self.kind == 2:    # 전유부 요청
            datas = {"inqireGbCd": "1", "bldrgstCurdiGbCd": "0", "reqSigunguCd": self.sigungu, "bldrgstSeqno": self.seqno}
            response_title = self.s.post('https://cloud.eais.go.kr/bci/BCIAAA02R04', headers=headers, json=datas)
            time.sleep(0.5)
            result = json.loads(response_title.text)['findExposList'][0]

        bun, ji = result['mnnm'].lstrip('0'), result['slno'].lstrip('0')
        if ji: ji = f'-{ji}'
        if "hoNm" in result: ho = ' ' + result["hoNm"]

        self.address = f'{result["sigunguNm"]} {result["bjdongNm"]} {bun}{ji} {result["dongNm"]}{ho}'

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

        # 1. 민원 담기 (담아야 2번 요청 시 응답 값 나옴)
        self.s.post('https://cloud.eais.go.kr/bci/BCIAAA02C01', headers=headers, json=datas)

        # 2. 담은 민원 처리 (응답 값 필요)
        response_put_in = self.s.post('https://cloud.eais.go.kr/bci/BCIAAA02R05', headers=headers)
        time.sleep(0.5)
        result = json.loads(response_put_in.text)
        print('## 담은 민원 처리중 ##\n', result)

        headers['Referer'] = "https://cloud.eais.go.kr/moct/bci/aaa02/BCIAAA02F01"
        datas = {"pbsvcResveDtls": result['findPbsvcResveDtls'],    # issueReadGbCd (0: 발급, 1: 열람)
                 "pbsvcRecpInfo": {"pbsvcGbCd": "01", "issueReadGbCd": "0", "pbsvcResveDtlsCnt": 1},
                 "appntInfo": {"appntGbCd": "01", "naAppntGrndUgrndGbCd": "0"}}

        # 3. 발급 신청, 담은 민원 제거
        self.s.post('https://cloud.eais.go.kr/bci/BCIAZA02S01', headers=headers, json=datas)
        time.sleep(0.5)
        self.s.post('https://cloud.eais.go.kr/bci/BCIAAA02D02', headers=headers,
                        json={'lastUpdusrId': result['findPbsvcResveDtls'][0]['lastUpdusrId']})
        time.sleep(0.5)
        print('## 발급 신청, 담은 민원 제거 ##')

        self.open_document()

        # except Exception as e:
        #     print('err: ', e)
        #     self.threadEvent.workerThreadDone.emit(False)

    # 문서 열기
    def open_document(self):
        # try:
        try_cnt = 0
        success = False

        self.driver.get('https://cloud.eais.go.kr/moct/bci/aaa04/BCIAAA04L01')
        self.driver.implicitly_wait(5)
        time.sleep(1)   # 리스트 로딩 대기

        while try_cnt < 10:
            self.threadEvent.progress.emit('발급 완료, 민원 처리 중..' + str(try_cnt))
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
            time.sleep(1)

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

        else:
            self.threadEvent.workerThreadDone.emit(False)
        # except:
        #     self.threadEvent.workerThreadDone.emit(False)

