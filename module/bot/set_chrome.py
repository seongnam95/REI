import time

from PySide6.QtCore import QThread, QObject, Signal
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class ThreadSignal(QObject):
    chromeDriver = Signal(object)


class SetChrome(QThread):
    def __init__(self, user_id, user_pw):
        super().__init__()
        self.threadEvent = ThreadSignal()

        self.driver = None
        self.user_id, self.user_pw = user_id, user_pw

    def run(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')  # 크롬 화면 숨기기
        chrome_options.add_argument("no-sandbox")  #
        chrome_options.add_argument('window-size=1920x1080')  # 해상도 설정
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("disable-gpu")  # 가속 사용 x
        chrome_options.add_argument("lang=ko_KR")  # 가짜 플러그인 탑재
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) "
                                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")  # user-agent 이름 설정
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        self.driver.get("https://cloud.eais.go.kr/moct/awp/abb01/AWPABB01F01")
        self.driver.implicitly_wait(5)

        time.sleep(0.5)
        self.driver.find_element(By.ID, 'membId').send_keys(self.user_id)
        self.driver.find_element(By.ID, 'pwd').send_keys(self.user_pw)
        self.driver.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div/div[1]/div[1]/button').click()
        time.sleep(0.5)

        self.threadEvent.chromeDriver.emit(self.driver)
