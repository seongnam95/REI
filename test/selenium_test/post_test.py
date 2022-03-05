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

ssl._create_default_https_context = ssl._create_unverified_context

LOGIN_INFO = {
    'loginId': 'haul1115',
    'loginPwd': 'ks05090818@'
}

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('headless')  # 크롬 화면 숨기기
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
# driver.get("http://www.gov.kr/nlogin/?Mcode=10003")
# driver.implicitly_wait(5)
#
# # 로그인
# driver.find_element(By.XPATH, '//*[@id="아이디"]').click()
# driver.find_element(By.ID, 'userId').send_keys(LOGIN_INFO['userId'])
# driver.find_element(By.ID, 'pwd').send_keys(LOGIN_INFO['pwd'])
# driver.find_element(By.CLASS_NAME, 'login-btn').find_element(By.TAG_NAME, 'button').click()

header = {
    "Referer": "https://cloud.eais.go.kr/moct/awp/abb01/AWPABB01F01?returnUrl=%2F",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.104 Whale/3.13.131.36 Safari/537.36"
}
#
# url = 'https://cloud.eais.go.kr/moct/awp/abb01/AWPABB01F01'
# r = requests.get(url, verify=False)
#
# print(r.text)

with requests.Session() as s:
    s.verify = False
    login_req = s.post('https://cloud.eais.go.kr/moct/awp/abb01/AWPABB01F01', headers=header, data=LOGIN_INFO)
    if login_req.status_code == 200:
        my_page = s.get('https://cloud.eais.go.kr/')
        soup = bs(my_page.text, 'html.parser')
        print(soup)
    #     s.headers.update(header)
#
#     s.post('https://cloud.eais.go.kr/moct/awp/abb01/AWPABB01F01', data=LOGIN_INFO)
#     a = s.get('https://cloud.eais.go.kr/moct/awp/abb01/AWPABB01F01')
#
#     # # 웹 드라이버 쿠키
#     # for cookie in driver.get_cookies():
#     #     c = {cookie['name']: cookie['value']}
#     #     s.cookies.update(c)
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
