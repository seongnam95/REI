from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager

import requests
import ssl
import clipboard as clip
from bs4 import BeautifulSoup as bs
import time

ssl._create_default_https_context = ssl._create_unverified_context

LOGIN_INFO = {
    'loginId': 'haul1115',
    'loginPwd': 'ks05090818@'
}

header = {
    "Referer": "https://cloud.eais.go.kr/moct/awp/abb01/AWPABB01F01",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.104 Whale/3.13.131.36 Safari/537.36"
}

tt = {"inqireGbCd":"0","reqSigunguCd":"11260","bldrgstCurdiGbCd":"0","upperBldrgstSeqno":'100249270',"bldrgstSeqno":""}

# 'http://cloud.eais.go.kr/moct/bci/aaa02/BCIAAA02F01'

header2 = {"inqireGbCd":"0","reqSigunguCd":"11260","bldrgstCurdiGbCd":"0","upperBldrgstSeqno":'100249270',"bldrgstSeqno":""}

header3 = {"bldrgstSeqno":'100249277',"regstrGbCd":"4","regstrKindCd":"4","mjrfmlyIssueYn":"N","locSigunguCd":"11260","locBjdongCd":"10100","locPlatGbCd":"0","locDetlAddr":"서울특별시 중랑구 면목동 90-27 동명칭 없음 402","locBldNm":"다원빌","ownrYn":"N","multiUseBildYn":"N","bldrgstCurdiGbCd":"0"}

params = {
    "addrGbCd": "1",
    "inqireGbCd": "0",
    "bldrgstCurdiGbCd": "0",
    "bldrgstSeqno": "",
    "reqSigunguCd": "11260",
    "sidoClsfCd": "",
    "bjdongCd": "",
    "platGbCd": "", "mnnm": "",
    "slno": "",
    "splotNm": "",
    "blockNm": "",
    "lotNm": "",
    "roadNmCd": "112603106002",
    "bldMnnm": "154",
    "bldSlno": "0",
    "sigunguCd": ""
}

# chrome_options = webdriver.ChromeOptions()
# # chrome_options.add_argument('headless')  # 크롬 화면 숨기기
# chrome_options.add_argument("no-sandbox")  #
# chrome_options.add_argument('window-size=1920x1080')  # 해상도 설정
# chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("disable-gpu")  # 가속 사용 x
# chrome_options.add_argument("lang=ko_KR")  # 가짜 플러그인 탑재
# chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) "
#                             "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")  # user-agent 이름 설정
#
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
#
# # 로그인
# driver.get('http://cloud.eais.go.kr')
# driver.implicitly_wait(5)

# # 알림, 공지 팝업 제거
# notice_pop_up = driver.find_elements(By.CLASS_NAME, 'swal-button.swal-button--confirm')
# if len(notice_pop_up): notice_pop_up[0].click()
# notice_pop_up2 = driver.find_elements(By.CLASS_NAME, 'btnCloseToday')
# if len(notice_pop_up2): notice_pop_up2[0].click()
#
# # '로그인' 버튼 클릭
# WebDriverWait(driver, 3).until(
#     ec.presence_of_element_located((By.CLASS_NAME, 'btnLogin.btnLine.btnNormal.btnLine_blue'))).click()
#
# # ID, PW 입력 후 로그인인
# driver.find_element(By.ID, 'membId').send_keys(LOGIN_INFO['loginId'])
# driver.find_element(By.ID, 'pwd').send_keys(LOGIN_INFO['loginPwd'])
# driver.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div/div[1]/div[1]/button').click()
# time.sleep(0.5)
#
# driver.get('http://cloud.eais.go.kr')
# driver.implicitly_wait(5)

with requests.Session() as s:
    s.verify = False

    s.get('https://cloud.eais.go.kr/')

    login = {'loginId': 'ks050940', 'loginPwd': 'ks05090818@'}
    login_req = s.post('https://cloud.eais.go.kr/moct/awp/abb01/AWPABB01F01/', headers=header, json=login)
    print(login_req.json()['accessToken'])
    for c in login_req.cookies:
        print(f'aa: {c}')
        driver.add_cookie({'name': c.name, 'value': c.value, 'path': c.path, 'expiry': c.expires})

    headers = {
        "Referer": "https://cloud.eais.go.kr/moct/bci/aaa02/BCIAAA02L01",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.104 Whale/3.13.131.36 Safari/537.36"
    }

    aa = s.post('https://cloud.eais.go.kr/moct/bci/aaa02/BCIAAA02L01', headers=headers, data=params)

    params2 = {"bldrgstSeqno":'100249270',"regstrGbCd":"3","regstrKindCd":"3","mjrfmlyIssueYn":"N","locSigunguCd":"11260","locBjdongCd":"10100","locPlatGbCd":"0","locDetlAddr":"서울특별시 중랑구 면목동 90-27 동명칭 없음","locBldNm":"다원빌","ownrYn":"N","multiUseBildYn":"N","bldrgstCurdiGbCd":"0"}

    bbs = s.post('https://cloud.eais.go.kr/moct/bci/aaa02/BCIAAA02L01', headers=headers, data=params2)
    #print(bbs.content)

    # # 웹 드라이버 쿠키
    # for cookie in driver.get_cookies():
    #     c = {cookie['name']: cookie['value']}
    #     print(c)
    #     s.cookies.update(c)

    #
    # login_req1 = s.post('http://cloud.eais.go.kr/bci/BCIAAA02R01', data=params)
    #
    # login_req2 = s.post('http://cloud.eais.go.kr/bci/BCIAAA02R04', data=tt)
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
