from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from seleniumrequests import Chrome
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')  # 크롬 화면 숨기기
chrome_options.add_argument("no-sandbox")  #
chrome_options.add_argument('window-size=1920x1080')  # 해상도 설정
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("disable-gpu")  # 가속 사용 x
chrome_options.add_argument("lang=ko_KR")  # 가짜 플러그인 탑재
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) "
                            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")  # user-agent 이름 설정
driver = Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

headers = {
    "Host": "cloud.eais.go.kr",
    "Referer": 'https://cloud.eais.go.kr/moct/awp/abb01/AWPABB01F01',
    "Content-Type": "application/json;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
}

datas = {'loginId': "haul1115", 'loginPwd': "ks05090818@"}

driver.get("https://cloud.eais.go.kr/moct/awp/abb01/AWPABB01F01")
driver.implicitly_wait(5)

a = driver.request('POST', 'https://cloud.eais.go.kr/awp/AWPABB01R01', headers=headers, json=datas)
print('a: ', a.text)
print('b: ', a.history)



