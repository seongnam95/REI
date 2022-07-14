import webbrowser
from urllib.parse import urlencode
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
from seleniumrequests import Chrome


chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('headless')  # 크롬 화면 숨기기
chrome_options.add_argument("no-sandbox")  #
chrome_options.add_argument('window-size=1920x1080')  # 해상도 설정
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("disable-gpu")  # 가속 사용 x
chrome_options.add_argument("lang=ko_KR")  # 가짜 플러그인 탑재
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) "
                            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")  # user-agent 이름 설정
driver = Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


url = 'http://www.eum.go.kr/web/ar/lu/luLandDetPrintPop.jsp?'
params = urlencode({'isNoScr': 'script',
                    'mode': 'search',
                    'pnu': '1126010100103670003'})

driver.get(url + params)
driver.implicitly_wait(10)

driver.execute_script("window.print();")

