from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from seleniumrequests import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from ui_test import Ui_Form
from PySide6.QtWidgets import QMainWindow, QApplication

import json
import time
import sys


def CreateSession():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')  # 크롬 화면 숨기기
    chrome_options.add_argument("no-sandbox")  #
    chrome_options.add_argument('window-size=1920x1080')  # 해상도 설정
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("disable-gpu")  # 가속 사용 x
    chrome_options.add_argument("lang=ko_KR")  # 가짜 플러그인 탑재
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) "
                                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")  # user-agent 이름 설정

    driver = Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver


class RequestData(QMainWindow, Ui_Form):
    def __init__(self):
        super(RequestData, self).__init__()

        self.s, self.pk = None, None
        self.result_address, self.result_dong, self.result_ho = [], [], []

        self.setupUi(self)
        self.show()
        self.sign_in()
        self.reset_content()
        self.headers = {
            "Host": "cloud.eais.go.kr",
            "Content-Type": "application/json;charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
        }

        self.find_title_id('a')

        self.btn_reset.clicked.connect(self.reset_content)
        self.btn_search.clicked.connect(self.select_address)

        self.cbx_address.activated.connect(self.select_dong)
        self.cbx_dong.activated.connect(self.select_ho)

    def reset_content(self):
        self.result_address.clear()
        self.result_dong.clear()
        self.result_ho.clear()

        self.edt_address.clear()
        self.edt_content.clear()
        self.edt_headers.clear()

        self.cbx_address.clear()
        self.cbx_ho.clear()
        self.cbx_dong.clear()

        self.cbx_address.addItem('(선택)')
        self.cbx_ho.addItem('(선택)')
        self.cbx_dong.addItem('(선택)')

    def sign_in(self):
        self.s = CreateSession()

        self.s.get("https://cloud.eais.go.kr/moct/awp/abb01/AWPABB01F01")
        self.s.implicitly_wait(5)

        # ID, PW 입력 후 로그인
        self.s.find_element(By.ID, 'membId').send_keys('haul1115')
        self.s.find_element(By.ID, 'pwd').send_keys('ks05090818@')
        self.s.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div/div[1]/div[1]/button').click()
        time.sleep(0.5)

        print('로그인 성공')

    def select_address(self, address):
        address = self.edt_address.text()

        headers = self.headers
        headers['Referer'] = "https://cloud.eais.go.kr/moct/bci/aaa02/BCIAAA02L01"

        datas = {"query": {"multi_match": {"query": address, "type": "cross_fields", "operator": "and",
                           "fields": ["jibunAddr", "roadAddr^3"], "tie_breaker": 0.3}}, "size": 50}

        response = self.s.request('POST', 'https://cloud.eais.go.kr/bldrgstmst/_search', headers=headers, json=datas)
        result = list(json.loads(response.text)['hits']['hits'])

        for i in result:
            print(i)
            address = {'id': i['_id'],
                       'pk': i['_source']['mgmUpperBldrgstPk'],
                       'old': i['_source']['jibunAddr'],
                       'new': i['_source']['roadAddr']}

            self.cbx_address.addItem('%s (%s)' % (address['old'], address['id']))
            self.result_address.append(address)

        self.cbx_address.showPopup()

    def select_dong(self, pk):
        if self.cbx_address.currentIndex() == 0: return

        address = dict(self.result_address[self.cbx_address.currentIndex() - 1])
        pk = address['pk']

        headers = self.headers
        headers['Referer'] = "https://cloud.eais.go.kr/moct/bci/aaa02/BCIAAA02L01"

        datas = {"sort": [{"dongNm": "asc"}],
                 "query": {"bool": {"filter": [{"term": {"mgmUpperBldrgstPk": pk}}]}}, "size": 100}

        response = self.s.request('POST', 'https://cloud.eais.go.kr/bldrgsttitle/_search', headers=headers, json=datas)
        result = list(json.loads(response.text)['hits']['hits'])

        for i in result:
            dong = {'pk': i['_id'],
                    'dong_nm': i['_source']['dongNm']}

            self.cbx_dong.addItem('%s (%s)' % (dong['dong_nm'], dong['pk']))
            self.result_dong.append(dong)

        self.cbx_dong.showPopup()

    def select_ho(self, pk):
        if self.cbx_dong.currentIndex() == 0: return

        address = dict(self.result_dong[self.cbx_dong.currentIndex() - 1])
        pk = address['pk']

        headers = self.headers
        headers['Referer'] = "https://cloud.eais.go.kr/moct/bci/aaa02/BCIAAA02L01"

        datas = {"sort": [{"hoNm": "asc"}], "query": {"bool": {"filter": [{"term": {"mgmUpperBldrgstPk": pk}}]}},
                 "size": 200}

        response = self.s.request('POST', 'https://cloud.eais.go.kr/bldrgstexpos/_search', headers=headers, json=datas)
        result = list(json.loads(response.text)['hits']['hits'])

        for i in result:
            ho = {'id': i['_id'],
                  'pk': i['_source']['mgmUpperBldrgstPk'],
                  'dong_nm': i['_source']['dongNm'],
                  'ho_nm': i['_source']['hoNm']}

            self.cbx_ho.addItem('%s, %s (%s)' % (ho['dong_nm'], ho['ho_nm'], ho['pk']))
            self.result_ho.append(ho)

        self.cbx_ho.showPopup()

    def find_title_id(self, address):
        # if self.cbx_ho.currentIndex() == 0: return
        address = {'시군구코드': '11260',
                   'pk': '100261327'}

        headers = self.headers
        headers['Referer'] = "https://cloud.eais.go.kr/moct/bci/aaa02/BCIAAA02L01"

        # 표제부
        datas = {"addrGbCd": 2, "inqireGbCd": "0", "bldrgstCurdiGbCd": "0",
                 "sigunguCd": address['시군구코드'], "bldrgstSeqno": address['pk']}

        # 주소 검색 (결과 값: 주소 정보)
        response_title = self.s.request('POST', 'https://cloud.eais.go.kr/bci/BCIAAA02R01', headers=headers, json=datas)
        result = json.loads(response_title.text)['jibunAddr'][0]

        bun, ji = result['mnnm'].lstrip('0'), result['slno'].lstrip('0')

        if ji:
            address = f'{result["sigunguNm"]} {result["bjdongNm"]} {bun}-{ji} {result["dongNm"]}'
        else:
            address = f'{result["sigunguNm"]} {result["bjdongNm"]} {bun} {result["dongNm"]}'

        datas2 = {"bldrgstSeqno": result["bldrgstSeqno"],
                  "regstrGbCd": result["regstrGbCd"],
                  "regstrKindCd": result["regstrKindCd"],
                  "mjrfmlyIssueYn": "N",
                  "locSigunguCd": result["sigunguCd"],
                  "locBjdongCd": result["bjdongCd"],
                  "locPlatGbCd": result["platGbCd"],
                  "locDetlAddr": address,
                  "locBldNm": result["bldNm"],
                  "ownrYn": "N",
                  "multiUseBildYn": "N",
                  "bldrgstCurdiGbCd": "0"}

        # 민원 담기 (담아야 응답 값 나옴)
        self.s.request('POST', 'https://cloud.eais.go.kr/bci/BCIAAA02C01', headers=headers, json=datas2)

        # 담은 민원 처리 (응답 값 필요)
        response_put_in = self.s.request('POST', 'https://cloud.eais.go.kr/bci/BCIAAA02R05', headers=headers)
        result = json.loads(response_put_in.text)

        self.issuance_data(result['findPbsvcResveDtls'])

    def issuance_data(self, dtls):
        headers = self.headers
        headers['Referer'] = "https://cloud.eais.go.kr/moct/bci/aaa02/BCIAAA02F01"

        datas = {
            "pbsvcResveDtls": dtls,

            "ownrExprsYn": "N",

            "pbsvcRecpInfo": {
                "pbsvcGbCd": "01",
                "issueReadGbCd": "0",
                "pbsvcResveDtlsCnt": 1},

            "appntInfo": {
                "appntGbCd": "01",
                "appntJmno1": "950509",
                "appntNm": "장성남",
                "naAppntGrndUgrndGbCd": "0"}}

        # 발급 신청
        self.s.request('POST', 'https://cloud.eais.go.kr/bci/BCIAZA02S01', headers=headers, json=datas)

        # 담은 민원 제거
        self.s.request('POST', 'https://cloud.eais.go.kr/bci/BCIAAA02D02', headers=headers,
                       json={'lastUpdusrId': dtls[0]['lastUpdusrId']})
        print('발급 처리 완료')

# 예외 오류 처리
def my_exception_hook(exctype, value, traceback):
    sys.excepthook(exctype, value, traceback)


sys._excepthook = sys.excepthook
sys.excepthook = my_exception_hook

app = QApplication()
window = RequestData()
app.exec()
