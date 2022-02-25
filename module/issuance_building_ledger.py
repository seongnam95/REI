from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager

import time
import webbrowser


# 크롬 드라이버 세팅
def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')  # 크롬 화면 숨기기
    chrome_options.add_argument("no-sandbox")  #
    chrome_options.add_argument('window-size=1920x1080')  # 해상도 설정
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("disable-gpu")  # 가속 사용 x
    chrome_options.add_argument("lang=ko_KR")  # 가짜 플러그인 탑재
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) "
                                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")  # user-agent 이름 설정
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver


class IssuanceBuildingLedger:
    def __init__(self, old, new, ho, kind, work, user_id, user_pw):
        self.old_address, self.new_address, self.ho = old, new, ho  # 주소, 호
        self.kind, self.work_selection = kind, work     # 건물 타입, 대장 종류
        self.user_id, self.user_pw = user_id, user_pw   # ID, PW

        self.driver = set_chrome_driver()  # 크롬 드라이버 세팅
        self.practice_sign_in()

    # 세움터 로그인
    def practice_sign_in(self):
        print('로그인 시작')
        self.driver.get("http://cloud.eais.go.kr/moct/awp/abb01/AWPABB01F01?returnUrl=%2F")
        self.driver.implicitly_wait(5)

        # 알림, 공지 팝업 제거
        notice_pop_up = self.driver.find_elements(By.CLASS_NAME, 'swal-button.swal-button--confirm')
        if len(notice_pop_up): notice_pop_up[0].click()
        notice_pop_up2 = self.driver.find_elements(By.CLASS_NAME, 'btnCloseToday')
        if len(notice_pop_up2): notice_pop_up2[0].click()

        # '로그인' 버튼 클릭
        WebDriverWait(self.driver, 3).until(
            ec.presence_of_element_located((By.CLASS_NAME, 'btnLogin.btnLine.btnNormal.btnLine_blue'))).click()

        # ID, PW 입력 후 로그인인
        self.driver.find_element(By.ID, 'membId').send_keys(self.user_id)
        self.driver.find_element(By.ID, 'pwd').send_keys(self.user_pw)
        self.driver.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div/div[1]/div[1]/button').click()

        # 비밀번호 다음에 변경
        next_change_btn = WebDriverWait(self.driver, 3).until(
            ec.presence_of_all_elements_located((By.CLASS_NAME, 'btnDaum.btnSolid.btnLarge')))
        if len(next_change_btn):
            next_change_btn[0].click()
            WebDriverWait(self.driver, 30).until(
                ec.presence_of_element_located((By.CLASS_NAME, 'swal-button.swal-button--confirm'))).click()

        print('로그인 성공')
        self.issuance_document()  # 문서 열람, 발급

        # WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'bldreDiv.bldre3'))).click()     # '신청내역' 클릭
        # self.open_document()    # 대장 열기

    # 문서 발급, 열람
    def issuance_document(self):
        print('문서 발급, 열람')

        # 건축물대장 발급 페이지로 이동
        time.sleep(2)
        WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, '//*[@id="menu"]/li[2]/a'))).click()  # '건축물대장' 메뉴 클릭
        WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.CLASS_NAME, 'bldreDiv.bldre1'))).click()  # '건축물대장 발급' 버튼

        # 주소 입력
        WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.CLASS_NAME, 'btnAddrSrch'))).click()  # '도로명주소로 조회' 버튼
        self.driver.find_element(By.CSS_SELECTOR, '#keyword').send_keys(self.new_address)  # 도로명 주소 입력
        WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.CLASS_NAME, 'btnNext.btnSolid.btnNormal.btn_dark'))).click()  # '조회하기' 버튼

        # 주소 리스트 선택
        address_form = WebDriverWait(self.driver, 3).until(ec.presence_of_element_located((By.CLASS_NAME, 'addrList'))).find_element(By.TAG_NAME, 'ul')
        for n, row in enumerate(address_form.find_elements(By.TAG_NAME, 'li')):
            adr = row.text.split('\n선택')[0]
            if self.old_address in adr:  # 구주소가 맞다면 클릭
                button = WebDriverWait(row, 3).until(ec.presence_of_element_located((By.TAG_NAME, 'button')))
                button.click()
                break

        print('주소 선택 완료')

        # 베이스 XPATH

        result = False
        if self.kind == 0: result = self.bd_select()        # 표제부
        elif self.kind == 1: result = self.gen_select()     # 일반 건축물
        elif self.kind == 2: result = self.set_select()     # 전유부

        if result:
            print('선택 완료, 발급 신청')

            # 선택한 민원 발급처리
            WebDriverWait(self.driver, 3).until(ec.presence_of_element_located((By.CLASS_NAME, 'btnAddCart'))).click()  # '신청할 민원 담기'
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.CLASS_NAME, 'btnSubmit.mt10'))).click()  # '건축물대장 발급 신청'

            # 요청한 작업 선택후 신청 ( self.work_selection -> 발급: 0, 열람: 1 )
            self.driver.find_elements(By.XPATH, '//*[@id="container"]/div[2]/div/div[2]/ul/li/ul/li')[self.work_selection].click()
            self.driver.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div[5]/button[2]').click()   # '신청하기' 버튼

            print('발급 완료')

            self.open_document()

        else:
            self.driver.save_screenshot('fail.png')
            print('발급 실패')

    # 표제부
    def bd_select(self):
        print('표제부 선택중')

        base_xpath = '//*[@id="container"]/div[2]/div/div[2]/div[1]/div[3]'

        WebDriverWait(self.driver, 3).until(
            ec.presence_of_element_located((By.XPATH, "%s%s" % (base_xpath, '/ul/li[4]/a')))).click()  # '표제부' 버튼
        time.sleep(1)

        gen_xpath = "%s%s" % (base_xpath,
                              '/div/div[4]/table/tbody/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div/div[1]/div/div/div/div[2]')
        btn = self.driver.find_element(By.XPATH, gen_xpath).find_elements(By.TAG_NAME, 'input')
        if len(btn):
            btn[0].click()
            return True
        else: self.gen_select()

    # 일반건축물
    def gen_select(self):
        print('일반건축물 선택중')

        base_xpath = '//*[@id="container"]/div[2]/div/div[2]/div[1]/div[3]'

        WebDriverWait(self.driver, 3).until(
            ec.presence_of_element_located((By.XPATH, "%s%s" % (base_xpath, '/ul/li[2]/a')))).click()  # '표제부' 버튼
        time.sleep(1)

        gen_xpath = "%s%s" % (base_xpath,
                              '/div/div[2]/table/tbody/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div/div[1]/div/div/div/div[2]')
        btn = self.driver.find_element(By.XPATH, gen_xpath).find_elements(By.TAG_NAME, 'input')
        if len(btn):
            btn[0].click()
            return True
        else: self.gen_select()

    # 전유부
    def set_select(self):
        print('전유부 선택중')

        base_xpath = '//*[@id="container"]/div[2]/div/div[2]/div[1]/div[3]'

        WebDriverWait(self.driver, 3).until(
            ec.presence_of_element_located((By.XPATH, "%s%s" % (base_xpath, '/ul/li[5]/a')))).click()  # '전유부' 버튼
        time.sleep(1)

        ho_list = self.driver.find_element(By.XPATH, "%s%s" % (base_xpath,
                                                               '/div/div[5]/table/tbody/div/div/div[1]/div[2]/div[3]/div[2]/div/div'))
        breaker = False
        for r in ho_list.find_elements(By.TAG_NAME, 'div'):  # 태그네임 div의 수 만큼 반복
            if r.get_attribute("row-id"):  # Row-Id가 존재할 경우에만
                for row in r.find_elements(By.TAG_NAME, 'div'):  # 실제 호수 리스트 반복
                    if row.get_attribute('col-id') == 'hoNm':  # 호 명칭만
                        # print(breaker, row.get_attribute('col-id'), row.get_attribute("innerText"))
                        if row.get_attribute("innerText") in self.ho:  # 사용자가 입력한 호수일 경우
                            # 해당 호수의 체크박스 클릭 후 반복문 종료
                            r.find_element(By.XPATH, 'div[1]/div/div/div/div[2]').find_element(By.TAG_NAME, 'input').click()
                            breaker = True
                            break
                if breaker: return True
        return self.set_select()

    def open_document(self):
        print('신청된 문서 처리 대기중')

        work_selection = {0: '발급', 1: '열람'}[self.work_selection]

        time.sleep(2)
        self.driver.refresh()   # '처리중' 대기 후 새로고침
        time.sleep(1)

        print('처리 후 리스트 파싱 시작')

        list_form = WebDriverWait(self.driver, 3).until(ec.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[2]/div/div[4]/table/tbody')))

        document_list = list_form.find_elements(By.TAG_NAME, 'tr')  # 문서 리스트
        success = False
        for i in document_list:    # 문서 리스트 Row 수만큼 반복
            content = i.get_attribute("innerText")
            if self.old_address in content:  # 주소가 맞을 경우
                if work_selection in content:   # '열람', '발급'인 항목 클릭
                    print('결과 값 찾음')
                    i.find_element(By.XPATH, 'td[5]/a').click()
                    success = True
            if success: break

        if success:
            print('건축물대장 오픈 대기')
            time.sleep(1)
            self.driver.switch_to.window(self.driver.window_handles[1])
            new_url = self.driver.current_url

            self.driver.close()     # 기존 드라이브 종료

            print('건축물대장 오픈')
            webbrowser.open_new(new_url)
        else:
            print('오픈 실패')

