from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager

import time


def set_chrome_driver(kind):
    chrome_options = webdriver.ChromeOptions()

    if kind == 0:
        # chrome_options.add_argument('headless')  # 크롬 화면 숨기기
        chrome_options.add_argument("no-sandbox")  #
        chrome_options.add_argument('window-size=1920x1080')  # 해상도 설정
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("disable-gpu")  # 가속 사용 x
        chrome_options.add_argument("lang=ko_KR")  # 가짜 플러그인 탑재
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) "
                                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")  # user-agent 이름 설정
    elif kind == 1:
        chrome_options.add_argument('window-size=1920x1080')  # 해상도 설정
        chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

class BuildingRead:
    def __init__(self, old, new, ho, work):
        self.old_address = old
        self.new_address = new
        self.ho = ho
        self.work_selection = work
        print('init')

        self.driver = set_chrome_driver(0)
        self.site_login()

    # 세움터 로그인
    def site_login(self):
        print('로그인 시작')
        self.driver.get("http://cloud.eais.go.kr/moct/awp/abb01/AWPABB01F01?returnUrl=%2F")
        self.driver.implicitly_wait(2)

        try:
            self.driver.find_element(By.CSS_SELECTOR,
                                     'body > div.swal-overlay.swal-overlay--show-modal > div > div.swal-footer > div:nth-child(2) > button').click()
            self.driver.find_element(By.CSS_SELECTOR, '#noticeModal > div > div.noticeClose > ul > li:nth-child(2) > button').click()
        except:
            self.driver.get("http://cloud.eais.go.kr")
            self.driver.implicitly_wait(2)

        button = WebDriverWait(self.driver, 3).until(ec.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#header > div.headerWrap > div.headerBtn > button.btnLogin.btnLine.btnNormal.btnLine_blue')))
        button.click()

        self.driver.find_element(By.ID, 'membId').send_keys('haul1115')
        self.driver.find_element(By.ID, 'pwd').send_keys('ks05090818@')
        self.driver.find_element(By.CSS_SELECTOR, '#container > div.content.pb80 > div > div > div.fl > div.loginForm > button').click()

        try:
            self.driver.find_element(By.CSS_SELECTOR, '#container > div.content.pb80 > div > div > div.fr > div.btns > button.btnDaum.btnSolid.btnLarge').click()
            time.sleep(1)
            self.driver.find_element(By.CSS_SELECTOR, 'body > div.swal-overlay.swal-overlay--show-modal > div > div.swal-footer > div:nth-child(2) > button').click()
        except:
            pass

        WebDriverWait(self.driver, 3).until(ec.presence_of_element_located((By.XPATH, '//*[@id="menu"]/li[2]/a'))).click()  # '건축물대장' 메뉴 클릭
        self.issuance_document()  # 문서 열람, 발급
        #
        # WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'bldreDiv.bldre3'))).click()     # '신청내역' 클릭
        # self.open_document()    # 대장 열기

    # 문서 열람, 발급
    def issuance_document(self):
        print('로그인 성공, 발급, 열람')
        try:
            WebDriverWait(self.driver, 5).until(
                ec.presence_of_element_located((By.CLASS_NAME, 'bldreDiv.bldre1'))).click()  # '건축물대장 발급' 버튼
            WebDriverWait(self.driver, 5).until(
                ec.presence_of_element_located((By.CLASS_NAME, 'btnAddrSrch'))).click()  # '도로명주소로 조회' 버튼
            self.driver.find_element(By.CSS_SELECTOR, '#keyword').send_keys(self.new_address)  # 도로명 주소 입력
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(
                (By.CLASS_NAME, 'btnNext.btnSolid.btnNormal.btn_dark'))).click()  # '조회하기' 버튼
        except:
            return

        # 주소 리스트
        address_form = WebDriverWait(self.driver, 3).until(ec.presence_of_element_located((By.CLASS_NAME, 'addrList'))).find_element(By.TAG_NAME, 'ul')
        for n, row in enumerate(address_form.find_elements(By.TAG_NAME, 'li')):
            adr = row.text.split('\n선택')[0]
            if self.old_address in adr:  # 구주소가 맞다면
                button = WebDriverWait(row, 3).until(ec.presence_of_element_located((By.TAG_NAME, 'button')))
                button.click()
                break

        base_xpath = '//*[@id="container"]/div[2]/div/div[2]/div[1]/div[3]'
        kind = 0

        # 표제부 담기
        if kind == 0:
            WebDriverWait(self.driver, 3).until(
                ec.presence_of_element_located((By.XPATH, "%s%s" % (base_xpath, '/ul/li[2]/a')))).click()  # '표제부' 버튼
            gen = self.driver.find_element(By.XPATH, "%s%s" % (base_xpath,
                                                               '/div/div[2]/table/tbody/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div'))
            breaker = False
            for r in gen.find_elements(By.TAG_NAME, 'div'):  # 태그네임 div의 수 만큼 반복
                print(r.get_attribute("row-id"), r.get_attribute("innerText"))
                if r.get_attribute("row-id"):  # Row-Id가 존재할 경우에만
                    print('들어옴')
                    r.find_element(By.XPATH, '/div[3]/div/div/div/div[2]').find_element(By.TAG_NAME, 'input').click()
                    if breaker: break
            time.sleep(10)
        # 전유부 호 리스트 담기
        elif kind == 1:
            WebDriverWait(self.driver, 3).until(
                ec.presence_of_element_located((By.XPATH, "%s%s" % (base_xpath, '/ul/li[5]/a')))).click()  # '전유부' 버튼
            ho_list = self.driver.find_element(By.XPATH, "%s%s" % (base_xpath,
                                                                   '/div/div[5]/table/tbody/div/div/div[1]/div[2]/div[3]/div[2]/div/div'))
            print('호리스트 뽑기', len(ho_list.find_elements(By.TAG_NAME, 'div')))
            breaker = False
            for r in ho_list.find_elements(By.TAG_NAME, 'div'):  # 태그네임 div의 수 만큼 반복
                if r.get_attribute("row-id"):  # Row-Id가 존재할 경우에만
                    for row in r.find_elements(By.TAG_NAME, 'div'):  # 실제 호수 리스트 반복
                        if row.get_attribute('col-id') == 'hoNm':  # 호 명칭만
                            if row.get_attribute("innerText") in self.ho:  # 사용자가 입력한 호수일 경우
                                # 해당 호수의 체크박스 클릭 후 반복문 종료
                                r.find_element(By.XPATH, 'div[1]/div/div/div/div[2]').find_element(By.TAG_NAME, 'input').click()
                                breaker = True
                                break
                    if breaker: break

        WebDriverWait(self.driver, 3).until(ec.presence_of_element_located((By.CLASS_NAME, 'btnAddCart'))).click()  # '신청할 민원 담기' 버튼
        WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.CLASS_NAME, 'btnSubmit.mt10'))).click()  #

        # 작업 선택 (발급, 열람)
        self.driver.find_elements(By.XPATH, '//*[@id="container"]/div[2]/div/div[2]/ul/li/ul/li')[self.work_selection].click()
        self.driver.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div[5]/button[2]').click()   # '신청하기' 버튼

        print('발급, 열람 완료')

        self.open_document()

    def open_document(self):
        print('신청된 문서 처리 대기중')
        work_selection = {0: '발급', 1: '열람'}[self.work_selection]

        time.sleep(2)
        self.driver.refresh()   # '처리중' 대기 후 새로고침
        time.sleep(2)

        print('새로고침 후 리스트 파싱 시작')

        list_form = WebDriverWait(self.driver, 3).until(ec.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[2]/div/div[4]/table/tbody')))

        document_list = list_form.find_elements(By.TAG_NAME, 'tr')  # 문서 리스트
        result = False
        for i in document_list:    # 문서 리스트 Row 수만큼 반복
            content = i.get_attribute("innerText")
            if self.old_address in content:  # 주소가 맞을 경우
                if work_selection in content:   # '열람', '발급'인 항목 클릭
                    print('결과 값 찾음')
                    i.find_element(By.XPATH, 'td[5]/a').click()
                    result = True
            if result: break

        if result:
            print('건축물대장 오픈 대기')
            time.sleep(1)
            self.driver.switch_to.window(self.driver.window_handles[1])
            new_url = self.driver.current_url
            self.driver.close()     # 기존 드라이브 종료

            new_driver = set_chrome_driver(1)
            new_driver.get(new_url)  # 새로운 페이지로 오픈
            print('건축물대장 오픈')
            time.sleep(50)
        else:
            print('실패')


old_address = '면목동 92-76'
new_address = '상봉로17길 22'
ho = '701'

BuildingRead(old_address, new_address, ho, 0)

