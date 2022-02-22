
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import requests
import urllib.request as req
import urllib3
import time

options = webdriver.ChromeOptions()

options.add_argument('headless')
options.add_argument("no-sandbox")
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")   # 가속 사용 x
options.add_argument("lang=ko_KR")    # 가짜 플러그인 탑재
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 이름 설정

driver = webdriver.Chrome(r'C:/chromedriver/chromedriver.exe', chrome_options=options)

driver.get("http://www.gov.kr/nlogin")
driver.implicitly_wait(3)

driver.find_element('userId').send_keys('haul1115')
driver.find_element('password').send_keys('ks05090818@')
# driver.find_element_by_name('genLogin').click()
#
# driver.get_screenshot_as_file('ca.png')
driver.get_screenshot_as_file('a.png')
driver.quit()




# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# user = 'haul1115'
# pw = 'ks05090818@'
# sess = requests.session()
# login = {'userId': user, 'password': pw}
# url = 'http://www.gov.kr/nlogin'
# res = sess.post(url, data=login, verify=False)
# res.raise_for_status()
#
# print(res.text)
