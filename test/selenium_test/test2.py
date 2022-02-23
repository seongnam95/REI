
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


import requests
import urllib.request as req
import urllib3
import time

options = webdriver.ChromeOptions()

# options.add_argument('headless')    # 크롬 화면 숨기기
options.add_argument("no-sandbox")  #
# options.add_argument('window-size=1920x1080') # 해상도 설정
options.add_argument("disable-gpu")   # 가속 사용 x
options.add_argument("lang=ko_KR")    # 가짜 플러그인 탑재
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36')  # user-agent 이름 설정

old_address = '면목동 90-27'
new_address = '봉우재로154'
ho = ['702']

driver = webdriver.Chrome('./chromedriver_98.0.4758.102.exe', chrome_options=options)

driver.get("http://cloud.eais.go.kr/moct/awp/abb01/AWPABB01F01?returnUrl=%2F")
driver.implicitly_wait(2)
try:
    driver.find_element(By.CSS_SELECTOR,
                        'body > div.swal-overlay.swal-overlay--show-modal > div > div.swal-footer > div:nth-child(2) > button').click()
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
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, 'body > div.swal-overlay.swal-overlay--show-modal > div > div.swal-footer > div:nth-child(2) > button').click()
except:
    pass
time.sleep(2)
driver.execute_script("window.scrollTo(0, 700)")
print('로그인')


def find_ho():
    driver.find_element(By.CLASS_NAME, 'bldreDiv.bldre1').click()
    driver.find_element(By.CLASS_NAME, 'btnAddrSrch').click()
    driver.find_element(By.CSS_SELECTOR, '#keyword').send_keys('봉우재로154')
    driver.find_element(By.CLASS_NAME, 'btnNext.btnSolid.btnNormal.btn_dark').click()

    listt = driver.find_element(By.CLASS_NAME, 'addrList').find_element(By.TAG_NAME, 'ul')
    time.sleep(2)
    for n, i in enumerate(listt.find_elements(By.TAG_NAME, 'li')):
        adr = i.text.split('\n선택')[0]
        if old_address in adr:
            i.find_element(By.TAG_NAME, 'button').click()
            break
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div[2]/div[1]/div[3]/ul/li[5]/a').click()
    time.sleep(1)
    lst = driver.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div[2]/div[1]/div[3]/div/div[5]/table/tbody/div/div/div[1]/div[2]/div[3]/div[2]/div/div')

    # 전유부 클릭
    ho_count, breaker = 0, False
    for a, b in enumerate(lst.find_elements(By.TAG_NAME, 'div')):
        if b.get_attribute("row-id"):
            for n, i in enumerate(b.find_elements(By.TAG_NAME, 'div')):
                if i.get_attribute('col-id') == 'hoNm':
                    if i.get_attribute("innerText") in ho:
                        ho_count += 1
                        b.find_element(By.XPATH, 'div[1]/div/div/div/div[2]').find_element(By.TAG_NAME, 'input').click()
                    if ho_count == len(ho):
                        breaker = True
                        break
            if breaker: break
    driver.save_screenshot('a.png')
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'btnAddCart').click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'btnSubmit.mt10').click()
    driver.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div[2]/ul/li/ul/li[2]').click()
    driver.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div[5]/button[2]').click()   # 민원 신청


find_ho()
# driver.find_element(By.CLASS_NAME, 'bldreDiv.bldre3').click() # 발급현황 ㅋㄹ릭
time.sleep(3)
driver.refresh()
time.sleep(1)
lst = driver.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div[4]/table/tbody')

breaker = False
for i in lst.find_elements(By.TAG_NAME, 'tr'):
    print('1번 for', i)
    content = i.get_attribute("innerText")
    if old_address in content:
        if '열람' in content:
            i.find_element(By.XPATH, 'td[5]/a').click()
            breaker = True

            # for t in i.find_elements(By.TAG_NAME, 'td'):
            #     print('2번 for', t)
            #     try:
            #         t.find_element(By.TAG_NAME, 'a').click()
            #         breaker = True
            #         break
            #     except: pass

    if breaker: break
if breaker:
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.CLASS_NAME, 'report_menu_button.report_menu_print_button.report_menu_print_button_svg').click()
    select = Select(driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/select'))
    select.select_by_visible_text('PDF')
    print('여까지')
    driver.find_element(By.CLASS_NAME, 'report_view_button').click()
time.sleep(3)

# driver.quit()

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
