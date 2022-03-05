from PySide6.QtCore import QThread, QObject, Signal
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager

import time
import webbrowser


class ThreadSignal(QObject):
    workerThreadDone = Signal(bool)
    progress = Signal(str)


class IssuanceBuildingLedger:
    def __init__(self, old, new, dong, ho, work, sortation, kind, user_id, user_pw):
        super().__init__()
        self.threadEvent = ThreadSignal()

        self.old_address, self.new_address, self.dong, self.ho = old, new, dong, ho  # 주소, 호, 건물 구분
        # 발급열람여부 (발급, 열람) / 대장구분(일반, 집합) / 대장종류(총괄, 일반, 전유부)
        self.work, self.sortation, self.kind, = work, sortation, kind
        self.user_id, self.user_pw = user_id, user_pw   # ID, PW
        self.driver = None

        self.set_driver()

    def set_driver(self):
        self.threadEvent.progress.emit('건축물대장 발급 시작')

        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('headless')  # 크롬 화면 숨기기
        chrome_options.add_argument("no-sandbox")  #
        chrome_options.add_argument('window-size=1920x1080')  # 해상도 설정
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("disable-gpu")  # 가속 사용 x
        chrome_options.add_argument("lang=ko_KR")  # 가짜 플러그인 탑재
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) "
                                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")  # user-agent 이름 설정

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.practice_sign_in()

    # 로그인
    def practice_sign_in(self):
        self.driver.get("http://www.gov.kr/nlogin/?Mcode=10003")
        self.driver.implicitly_wait(5)

        # 로그인
        self.driver.find_element(By.XPATH, '//*[@id="아이디"]').click()
        self.driver.find_element(By.ID, 'userId').send_keys(self.user_id)
        self.driver.find_element(By.ID, 'pwd').send_keys(self.user_pw)
        self.driver.find_element(By.CLASS_NAME, 'login-btn').find_element(By.TAG_NAME, 'button').click()

        self.driver.get("http://www.gov.kr/mw/AA020InfoCappView.do?CappBizCD=15000000098&HighCtgCD=A02004002&Mcode=10205")
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, 'applyBtn').click()

        # 열람일 경우
        if self.work == 1:
            later = WebDriverWait(self.driver, 8).until(ec.presence_of_element_located((By.CLASS_NAME, 'element-tab')))
            later.find_elements(By.TAG_NAME, 'a')[self.work].click()    # 열람 버튼 클릭

        # 주소 검색 버튼
        self.driver.find_element(By.XPATH, '//*[@id="주소검색"]').click()
        self.driver.switch_to.window(self.driver.window_handles[1])

        # 주소 입력
        self.driver.find_element(By.ID, 'txtRoad').send_keys(self.new_address)
        self.driver.find_element(By.XPATH, '//*[@id="frm_popup"]/fieldset/div/div/span/button').click()

        search_count = self.driver.find_element(By.CLASS_NAME, 'all-num').find_element(By.TAG_NAME, 'span').text
        print(search_count)

        # 주소 리스트
        address_list = WebDriverWait(self.driver, 5).until(
            ec.presence_of_element_located((By.CLASS_NAME, 'address-result-list'))).find_elements(By.TAG_NAME, 'a')

        for i in range(len(address_list)):
            result = address_list[i].text.split('\n')
            if info['구주소'] in result[4]:
                address_list[i].click()
                WebDriverWait(self.driver, 3).until(
                    ec.presence_of_element_located((By.XPATH, '//*[@id="frm_popup"]/fieldset/div[2]/div[3]/a[2]'))).click()
                self.driver.switch_to.window(self.driver.window_handles[0])
                break

        # '대장구분' 선택 (0: 일반, 1: 집합)
        sortation_btn = self.driver.find_element(By.XPATH, '//*[@id="main"]/fieldset/div[1]/div[2]/div[2]/div[2]/div[2]')
        sortation_btn.find_elements(By.TAG_NAME, 'input')[self.sortation].click()

        # '대장종류' 선택 (0: 총괄, 1: 표제부, 2: 전유부)
        self.driver.find_element(By.ID, f'dis_{self.sortation + 1}').find_elements(By.TAG_NAME, 'input')[self.kind].click()
        print(f'대장종류 선택 (0: 총괄, 1: 표제부, 2: 전유부) = {self.kind}')

        # '총괄'일 경우 즉시 민원신청 클릭
        if self.kind == 0:
            self.open_document()
            return

        # 동 검색 버튼 (0: 발급, 1: 열람)
        if self.work == 0: self.driver.find_element(By.XPATH, '//*[@id="동명검색"]').click()    # 동명 검색 버튼
        elif self.work == 1: self.driver.find_element(By.ID, 'btn_end').click()     # 민원 신청 버튼

        # 동 검색 창 대기
        WebDriverWait(self.driver, 20).until(ec.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])

        # 건물명칭(동) 목록
        item_path = '/html/body/div/div/div/table/tbody'
        items = WebDriverWait(self.driver, 5).until(
            ec.presence_of_element_located((By.XPATH, item_path))).find_elements(By.TAG_NAME, 'tr')

        # 대장종류 일반일 경우
        if self.sortation == 0:
            for i in items:
                if '일반건축물' in i.text:
                    i.find_element(By.XPATH, 'td:nth-child(4) > span > button').click()
                    self.open_document()
                    break

        # 대장종류 집합일 경우
        elif self.sortation == 1:
            for i in items:
                if self.dong in i.text:
                    i.find_element(By.CSS_SELECTOR, 'td:nth-child(3) > span > button').click()
                    break

            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.find_element(By.XPATH, '//*[@id="호명검색"]').click()  # 동명 검색 버튼

            WebDriverWait(self.driver, 20).until(ec.number_of_windows_to_be(2))
            self.driver.switch_to.window(self.driver.window_handles[1])

            items = WebDriverWait(self.driver, 5).until(
                ec.presence_of_element_located((By.XPATH, item_path))).find_elements(By.TAG_NAME, 'tr')

            for i in items:
                if self.ho in i.text.split(' ')[1]:
                    i.find_element(By.CSS_SELECTOR, 'td:nth-child(3) > span > button').click()
                    break

            self.open_document()

    def open_document(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

        WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.ID, 'btn_end'))).click()
        WebDriverWait(self.driver, 20).until(ec.presence_of_element_located(
            (By.XPATH, '//*[@id="EncryptionAreaID_0"]/div[1]/table/tbody/tr[1]/td[4]/p[2]/span/a'))).click()

        WebDriverWait(self.driver, 20).until(ec.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])

        new_url = self.driver.current_url
        # self.driver.close()  # 기존 드라이브 종료
        time.sleep(30)
        webbrowser.open_new(new_url)


info = {'구주소': '면목동 1545',
        '신주소': '동일로92길 40',
        '동명칭': '101동',
        '호명칭': '101',
        '타입': '집합',
        '작업': '발급'}

# info = {'구주소': '상봉동 88-85',
#         '신주소': '봉우재로43길 28-7',
#         '호명칭': '702',
#         '타입': '일반',
#         '작업': '열람'}

IssuanceBuildingLedger(info['구주소'], info['신주소'], info['동명칭'], info['호명칭'], 0, 1, 2, 'haul1115', 'ks05090818@')