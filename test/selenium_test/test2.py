
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

driver = webdriver.Chrome(r'C:/chromedriver/chromedriver.exe') # , chrome_options=options)

driver.get("http://cloud.eais.go.kr/moct/awp/abb01/AWPABB01F01?returnUrl=%2F")
driver.implicitly_wait(2)
try:
    driver.find_element(By.CSS_SELECTOR,
                        'body > div.swal-overlay.swal-overlay--show-modal > div > div.swal-footer > div:nth-child(2) > button').click()
except:
    pass

try:
    driver.find_element(By.CSS_SELECTOR, '#noticeModal > div > div.noticeClose > ul > li:nth-child(2) > button').click()
except:
    pass

button = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#header > div.headerWrap > div.headerBtn > button.btnLogin.btnLine.btnNormal.btnLine_blue')))
button.click()

driver.find_element(By.ID, 'membId').send_keys('haul1115')
driver.find_element(By.ID, 'pwd').send_keys('ks05090818@')
driver.find_element(By.CSS_SELECTOR, '#container > div.content.pb80 > div > div > div.fl > div.loginForm > button').click()

try:
    driver.find_element(By.CSS_SELECTOR, '#container > div.content.pb80 > div > div > div.fr > div.btns > button.btnDaum.btnSolid.btnLarge').click()
    driver.find_element(By.CSS_SELECTOR, 'body > div.swal-overlay.swal-overlay--show-modal > div > div.swal-footer > div:nth-child(2) > button').click()
except:
    pass

driver.find_element(By.CSS_SELECTOR, '#section1 > div > div.mainInner > div.registerUi > div.bldreDiv.bldre1 > a').click()
driver.find_element(By.CSS_SELECTOR, '#container > div.content.clearFix > div > div.floatWarp.mt30.clearFix > div.contLeft > div.srchArchitecture > div.searchBuildingWarp > div.AddrSearch > button.btnAddrSrch').click()
driver.find_element(By.CSS_SELECTOR, '#keyword').send_keys('중랑구 봉우재로154')
driver.find_element(By.CSS_SELECTOR, '#container > div.content.clearFix > div > div.floatWarp.mt30.clearFix > div.contLeft > div.srchArchitecture > div.popAddrSearch > div > div.formIn > button').click()

listt = driver.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div[2]/div[1]/div[1]/div[3]/div/div[3]/ul')
for n, i in enumerate(listt.find_elements(By.TAG_NAME, 'li')):
    print(i.accessible_name)
    print(n, i.text)

time.sleep(3)
# //*[@id="container"]/div[2]/div/div[2]/div[1]/div[1]/div[3]/div/div[3]/ul/li[1]/text()
# container > div.content.pb80 > div > div > div.fl > div.loginForm > button
# driver.get("http://www.gov.kr/mw/AA020InfoCappView.do?CappBizCD=15000000098")
# button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'applyBtn')))
# button.click()
#
# button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div/div[1]/div[1]/a[2]')))
# button.click()
#
# button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, '주소검색')))
# button.click()
#
# time.sleep(2)
#
# driver.switch_to.window(driver.window_handles[1])
# driver.find_element(By.ID, 'txtRoad').send_keys('면목동 90')
# button = driver.find_element(By.CSS_SELECTOR, 'button')
# button.send_keys('\n')
# time.sleep(2)
# #pop-wrap > div > div.cont-box.addr-search-new > div > div.address-result-list > a:nth-child(1) > dl > dd > div:nth-child(1) > span
# #pop-wrap > div > div.cont-box.addr-search-new > div > div.address-result-list > a:nth-child(1) > dl > dd > div:nth-child(2) > span
# addreess_list = driver.find_elements(By.CSS_SELECTOR, '#pop-wrap > div > div.cont-box.addr-search-new > div > div.address-result-list')
# for i in addreess_list:
#
#
driver.get_screenshot_as_file('a.png')
driver.quit()
