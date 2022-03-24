from PySide6.QtCore import QThread, QObject, Signal
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
from seleniumrequests import Chrome
from PIL import Image

import time
import webbrowser
import json
import requests
import base64
from pathlib import Path
from urllib import parse

headers = {
    "Host": "cloud.eais.go.kr",
    "Content-Type": "application/json;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
}
#
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
# driver = Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# driver.get(url)
# driver.implicitly_wait(5)

# a = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/table/tbody/tr/td/div/nobr')
# print(a.get_attribute("innerText"))

# base64_image = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/canvas').screenshot_as_base64
# output_image = base64.b64decode(base64_image)
# with open("test.txt") as f:
#     content = f.read().encode('utf-8')

content = Path("test.txt").read_text()
output_image = base64.b64decode(content)
data = parse.unquote(output_image)
res = data.replace('+', ' ')
print(res)

#
# img = Image.open('test1.png')
# img_rgb = img.convert('RGB')
# img_rgb.save('aa.pdf')
#
# with open("test.txt", 'wb') as f:
#     f.write(output_image)
#
# with open("test.pdf", 'wb') as f:
#     f.write(output_image)

#
# driver.find_element(By.ID, 'membId').send_keys('haul1115')
# driver.find_element(By.ID, 'pwd').send_keys('ks05090818@')
# driver.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div/div[1]/div[1]/button').click()
