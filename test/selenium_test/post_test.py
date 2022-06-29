from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from seleniumrequests import Chrome

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
import json
import requests
import ssl
import clipboard as clip
from bs4 import BeautifulSoup as bs
import time

# ssl._create_default_https_context = ssl._create_unverified_context

LOGIN_INFO = {
    'email': 'haul1115@naver.com',
    'password': 'ks05090818@'
}

# create a session
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


s = CreateSession()

s.get("https://cloud.eais.go.kr/moct/awp/abb01/AWPABB01F01")
s.implicitly_wait(5)

# ID, PW 입력 후 로그인
s.find_element(By.ID, 'membId').send_keys('haul1115')
s.find_element(By.ID, 'pwd').send_keys('ks05090818@')
s.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div/div[1]/div[1]/button').click()
time.sleep(0.5)

s.get('https://cloud.eais.go.kr/moct/bci/aaa02/BCIAAA02L01')
s.implicitly_wait(5)

###################################################################################################################

header = {
    "Host": "cloud.eais.go.kr",
    "Content-Type": "application/json;charset=UTF-8",
    "Referer": "https://cloud.eais.go.kr/moct/bci/aaa02/BCIAAA02L01",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
}

datas3 = {"addrGbCd":"0","inqireGbCd":"0","bldrgstCurdiGbCd":"0","bldrgstSeqno":"","reqSigunguCd":"11260","sidoClsfCd":"","bjdongCd":"10100","platGbCd":"0","mnnm":"90","slno":"29","splotNm":"","blockNm":"","lotNm":"","roadNmCd":"","bldMnnm":"","bldSlno":"","sigunguCd":"11260"}
datas4 = {"bldrgstSeqno":2455,"regstrGbCd":"2","regstrKindCd":"2","mjrfmlyIssueYn":"N","locSigunguCd":"11260","locBjdongCd":"10100","locPlatGbCd":"0","locDetlAddr":"서울특별시 중랑구 면목동 90-29 동명칭 없음","locBldNm":"건물명 없음","ownrYn":"N","multiUseBildYn":"N","bldrgstCurdiGbCd":"0"}

c = s.request('POST', 'https://cloud.eais.go.kr/bci/BCIAAA02R01', headers=header, json=datas3)
time.sleep(0.5)
d = s.request('POST', 'https://cloud.eais.go.kr/bci/BCIAAA02R01', headers=header, json=datas4)
time.sleep(0.5)

header2 = {
    "Host": "cloud.eais.go.kr",
    "Content-Type": "application/json;charset=UTF-8",
    "Referer": "https://cloud.eais.go.kr/moct/bci/aaa02/BCIAAA02F01",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
}

header3 = {
    "Host": "cloud.eais.go.kr",
    "Content-Type": "application/json;charset=UTF-8",
    "Referer": "https://cloud.eais.go.kr/moct/bci/aaa04/BCIAAA04L01",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
}

datas7 = {"pbsvcResveDtls":[{"@id":"14b5cc1c-0716-4de2-a65d-fc7c3e73e0f6","rowStatus":"R","firstCrtnDt":"20220319214611","firstWrtrId":"210706162108haul1115","lastUpdtDt":"20220319214611","lastUpdusrId":"210706162108haul1115","untClsfCd":"1008","pbsvcResveDtlsSeqno":"1000000000000049377257","bldrgstSeqno":"2455","regstrGbCd":"2","regstrKindCd":"2","mjrfmlyIssueYn":"N","bldrgstCurdiGbCd":"0","ownrYn":"N","multiUseBildYn":"N","ownrExprsYn":"N","locSigunguCd":"11260","locBjdongCd":"10100","locPlatGbCd":"0","locDetlAddr":"서울특별시 중랑구 면목동 90-29 동명칭 없음","locBldNm":"건물명 없음"}],"ownrExprsYn":"N","pbsvcRecpInfo":{"pbsvcGbCd":"01","issueReadGbCd":"0","pbsvcResveDtlsCnt":1},"appntInfo":{"appntGbCd":"01","appntJmno1":"950509","appntJmno2":"","appntJmno":"","appntBizno":"","appntNm":"장성남","appntMtelno":"","appntSigunguCd":"","naAppntBjdongCd":"","naAppntRoadCd":"","naAppntMnnm":"","naAppntSlno":"","naAppntGrndUgrndGbCd":"0","naAppntDetlAddr":"","appntCorpno":"","appntCoprNm":""}}
datas8 = {"membNo":"","pbsvcGbCd":"","progStateFlagArr":["01"],"pbsvcProcessGbCd":"","firstSaveStartDate":"2022-02-19","firstSaveEndDate":"2022-03-19","pageNo":0,"recordSize":10}
# h = s.request('POST', 'https://cloud.eais.go.kr/bci/BCIAZA02S01', headers=header2, json=datas7)
#
print(c.text)
print(d.text)
# print(h.text)

# s.get("https://pro.dabangapp.com/")


# # ID, PW 입력 후 로그인
# driver.find_element(By.ID, 'membId').send_keys(LOGIN_INFO['loginId'])
# driver.find_element(By.ID, 'pwd').send_keys(LOGIN_INFO['loginPwd'])
# driver.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div/div[1]/div[1]/button').click()
# time.sleep(0.5)
#
# driver.get('http://cloud.eais.go.kr')
# driver.implicitly_wait(5)
# custom_header을 통해 아닌 것 처럼 위장하기
custom_header = {
    'referer' : 'http://http://finance.daum.net/quotes/A048410#home',
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'  }

#해당 접속 사이트가 아닌 원본데이터가 오는 url 추적. network에서 가지고 온다.
# url = "http://finance.daum.net/api/search/ranks?limit=10"
#
# req = requests.get(url, headers = custom_header)    #custom_header를 사용하지 않으면 접근 불가
#
# if req.status_code == requests.codes.ok:
#     print("접속 성공")
#     stock_data = json.loads(req.text)        #json에 반환된 데이터가 들어가 있다.
#     print(req.text)
#     for rank in stock_data['static']:         #stock_data는 'static' key값에 모든 정보가 들어가 있다.
#         print(rank['rank'], rank['symbolCode'], rank['name'], rank['tradePrice'])
#
# with requests.Session() as s:
#     s.verify = False
#
#     aas = s.get('https://cloud.eais.go.kr/', headers=header)
#
#     login = {'loginId': 'ks050940', 'loginPwd': 'ks05090818@'}
#     login_req = s.post('https://cloud.eais.go.kr/moct/awp/abb01/AWPABB01F01/', headers=header, json=login)
#
#     headers = {
#         "Referer": "https://cloud.eais.go.kr/moct/bci/aaa02/BCIAAA02L01",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.104 Whale/3.13.131.36 Safari/537.36"
#     }
#
#     aa = s.post('https://cloud.eais.go.kr/moct/bci/aaa02/BCIAAA02L01', headers=headers, static=params)
#
#     params2 = {"bldrgstSeqno":'100249270',"regstrGbCd":"3","regstrKindCd":"3","mjrfmlyIssueYn":"N","locSigunguCd":"11260","locBjdongCd":"10100","locPlatGbCd":"0","locDetlAddr":"서울특별시 중랑구 면목동 90-27 동명칭 없음","locBldNm":"다원빌","ownrYn":"N","multiUseBildYn":"N","bldrgstCurdiGbCd":"0"}
#
#     bbs = s.post('https://cloud.eais.go.kr/moct/bci/aaa02/BCIAAA02L01', headers=headers, static=params2)
    #print(bbs.content)

    # # 웹 드라이버 쿠키
    # for cookie in driver.get_cookies():
    #     c = {cookie['name']: cookie['value']}
    #     print(c)
    #     s.cookies.update(c)

    #
    # login_req1 = s.post('http://cloud.eais.go.kr/bci/BCIAAA02R01', static=params)
    #
    # login_req2 = s.post('http://cloud.eais.go.kr/bci/BCIAAA02R04', static=tt)
    # for i in login_req2.history:
    #     print(i.text)
    # for i in login_req.history:
    #     print(i.text)
    #
    # soup = bs(login_req.text, 'lxml')
    # print(soup.prettify())
#
#     #index2 = s.get('https://www.gov.kr/portal/myPublicPlner?Mcode=11009')
#
#     # print(index2.text.find('서수연'))  # 로그인이 정상적으로 되었는지 확인용도
#
#     clip.copy(a.text)
# <span>My Gov</span>
    # print(index2.text.find('My GOV')) #로그인이 정상적으로 되었는지 확인용도
    #if login_req.status_code == 200:
        #my_page = s.get('https://www.gov.kr/portal/myPublicPlner')
        # soup = bs(my_page.text, 'html.parser')
        # print(soup)
        # name = soup.select('#container > div > div > section.mygov-header > div.mygov-header-right > div > div > div > p.txt-infor > span')
        # print(name)
