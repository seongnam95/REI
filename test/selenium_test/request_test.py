from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from seleniumrequests import Chrome

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import json
import time


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


class RequestData:
    def __init__(self):
        self.s = CreateSession()

        self.s.get("https://cloud.eais.go.kr/moct/awp/abb01/AWPABB01F01")
        self.s.implicitly_wait(5)

        # ID, PW 입력 후 로그인
        self.s.find_element(By.ID, 'membId').send_keys('haul1115')
        self.s.find_element(By.ID, 'pwd').send_keys('ks05090818@')
        self.s.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div/div[1]/div[1]/button').click()
        time.sleep(0.5)

        self.headers = {
            "Host": "cloud.eais.go.kr",
            "Content-Type": "application/json;charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
        }

        # self.select_address('상봉동 88-85')
        # self.select_dong('11260_10200_0_0088_0085')
        # self.select_ho('11260-100249270')
        self.find_id()
        # self.issuance_data()

    def select_address(self, address):
        headers = self.headers
        headers['Referer'] = "https://cloud.eais.go.kr/moct/bci/aaa02/BCIAAA02L01"

        datas = {"query": {"multi_match": {"query": address, "type": "cross_fields", "operator": "and",
                           "fields": ["jibunAddr", "roadAddr^3"], "tie_breaker": 0.3}}, "size": 50}

        response = self.s.request('POST', 'https://cloud.eais.go.kr/bldrgstmst/_search', headers=headers, json=datas)
        result = list(json.loads(response.text)['hits']['hits'])

        for i in result:
            address_id = i['_id']
            address_pk = i['_source']['mgmUpperBldrgstPk']
            address_old = i['_source']['jibunAddr']
            address_new = i['_source']['roadAddr']
            print(f'{address_id} ({address_pk}) :: {address_old} ({address_new})')

    def select_dong(self, pk):
        headers = self.headers
        headers['Referer'] = "https://cloud.eais.go.kr/moct/bci/aaa02/BCIAAA02L01"

        datas = {"sort": [{"dongNm": "asc"}],
                 "query": {"bool": {"filter": [{"term": {"mgmUpperBldrgstPk": pk}}]}}, "size": 100}

        response = self.s.request('POST', 'https://cloud.eais.go.kr/bldrgsttitle/_search', headers=headers, json=datas)
        result = list(json.loads(response.text)['hits']['hits'])
        print(json.loads(response.text))
        for i in result:
            dong_id = i['_id']
            dong_nm = i['_source']['dongNm']
            print(f'{dong_id} :: {dong_nm}')

    def select_ho(self, pk):
        headers = self.headers
        headers['Referer'] = "https://cloud.eais.go.kr/moct/bci/aaa02/BCIAAA02L01"

        datas = {"sort": [{"hoNm": "asc"}], "query": {"bool": {"filter": [{"term": {"mgmUpperBldrgstPk": pk}}]}},
                 "size": 200}

        response = self.s.request('POST', 'https://cloud.eais.go.kr/bldrgstexpos/_search', headers=headers, json=datas)
        result = list(json.loads(response.text)['hits']['hits'])

        for i in result:
            dong_nm = i['_source']['dongNm']
            ho_id = i['_id']
            ho_nm = i['_source']['hoNm']
            print(f'{ho_id} :: {dong_nm}, {ho_nm}')

    def find_id(self):
        headers = self.headers
        headers['Referer'] = "https://cloud.eais.go.kr/moct/bci/aaa02/BCIAAA02L01"

        datas = {"addrGbCd": "0", "inqireGbCd": "0", "bldrgstCurdiGbCd": "0", "bldrgstSeqno": "",
                 "reqSigunguCd": "11260", "sidoClsfCd": "", "bjdongCd": "10200", "platGbCd": "0", "mnnm": "88",
                 "slno": "85", "splotNm": "", "blockNm": "", "lotNm": "", "roadNmCd": "", "bldMnnm": "", "bldSlno": "",
                 "sigunguCd": "11260"}

        a = self.s.request('POST', 'https://cloud.eais.go.kr/bci/BCIAAA02R01', headers=headers, json=datas)
        result = json.loads(a.text)['jibunAddr'][0]

        bun = result["mnnm"].lstrip('0')
        ji = result["slno"].lstrip('0')

        address = f'{result["sigunguNm"]} {result["bjdongNm"]} {bun}-{ji} {result["dongNm"]}'

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

        b = self.s.request('POST', 'https://cloud.eais.go.kr/bci/BCIAAA02C01', headers=headers, json=datas2)
        print('B: ', b.text)

        c = self.s.request('POST', 'https://cloud.eais.go.kr/bci/BCIAAA02R05', headers=headers)
        print('C: ', c.text)

        print('\n\n')
        result = json.loads(c.text)
        print(result['findPbsvcResveDtls'])

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

        result = self.s.request('POST', 'https://cloud.eais.go.kr/bci/BCIAZA02S01', headers=headers, json=datas)
        print(result.text)


RequestData()

