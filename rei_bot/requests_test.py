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
import cv2
import numpy as np
from PIL import Image


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


# 소유자 조회
def find_owners(content):
    owners_table = content[0][6]
    owners = []
    for o in owners_table:
        row = o[6][0][0][2]
        owner_list = []
        for r in row:
            columns = r
            for c in columns:
                if type(c) == list and len(c) > 3:
                    result = parse.unquote(c[7]).replace('+', ' ').lstrip(' ')
                    owner_list.append(result)
        owner = {'성명': owner_list[0], '주소': owner_list[1], '지분': owner_list[2],
                 '변동일': owner_list[3], '번호': owner_list[4], '변동원인': owner_list[5]}
        owners.append(owner)
    return owners


# 기본 개요 테이블
def find_basic_table(content):
    result = []
    basic = content[4][2]
    for columns in basic:
        for c in columns:
            if type(c) == list and len(c) > 3:
                data = parse.unquote(c[7]).replace('+', ' ')
                result.append(data)

    dic = {'고유번호': result[1], '건물명칭': result[3], '호가구세대': result[5],
           '주소': '%s %s' % (result[8], (result[10].split(' 외')[0])), '도로명주소': result[12],
           '대지면적': result[14], '연면적': result[17], '지역': result[22], '지구': result[23], '구역': result[24],
           '건축면적': result[26], '용적률산정용연면적': result[33], '주구조': result[34], '주용도': result[35],
           '층수(지하)': (result[36].replace(' ', '').split('층/')[0].split('지하')[1]),
           '층수(지상)': (result[36].replace(' ', '').split('지상')[1].split('층')[0]),
           '건폐율': result[38], '용적률': result[41], '높이': result[44]}
    return dic


# 층
def find_floors_1(pages, page_3=None):
    result = []
    floors = pages[2][6]

    for floor in floors:
        floor_path = floor[6][0][0][2][0]
        flr = []
        for f in floor_path:
            if type(f) == list and len(f) > 3:
                data = parse.unquote(f[7]).replace('+', ' ')
                flr.append(data)
        result.append(flr)

    if page_3:
        for floor in page_3:
            floor_path = floor[6][0][0][2][0]
            flr = []
            for f in floor_path:
                if type(f) == list and len(f) > 3:
                    data = parse.unquote(f[7]).replace('+', ' ')
                    flr.append(data)
            result.append(flr)

    for i in result:
        print(i)
    return


class RegisterScraping:
    def __init__(self, referer, reportkey):

        self.payload = {'uid': reportkey,
                        'clipUID': reportkey,
                        'ClipType': 'DocumentPageView'}

        self.clip_data = {"reportkey": reportkey,
                          "isMakeDocument": 'True'}
        self.headers = {
            "Referer": referer,
            "Host": "cloud.eais.go.kr",
            "Content-Type": "application/json;charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
        }

    def request_page(self, page_num):
        clip = self.clip_data
        clip['pageMethod'] = page_num

        datas = self.payload
        datas['ClipData'] = parse.quote(json.dumps(clip).replace(' ', ''))

        res = requests.post('https://cloud.eais.go.kr/report/RPTCAA02R02', headers=self.headers, json=datas)
        print(res.text)
        data = json.loads(res.text)

        dec = base64.b64decode(data['viewData'])
        content = json.loads(dec)['pageList'][0]
        result = content[2]['b'][0]

        return result

ref = 'https://cloud.eais.go.kr/report/BCIAAA04V01?param=U2FsdGVkX19vbKyRlpCMlY%2FJrcE%2FNCgFyoBRlPxcJcn6ryhh7vZ5EGQDI%2BfqPPWvTro%2BBjNeHDaYcfePSfIvZYSGK2XZLnXPmrowLfdyciXefqhPAtEaccEN%2ByGDwwAIOrA9mFLjNda7OitBOGp7a6m2XOLFJ6vCwp%2Bg38BZOhD29FDnlYu5srrztYKw5jJc3SguYlvRXFbOWwvhAg0FmnH2SNw%2B4BHjzJ43mwYUPiUSHGdjHzk5pniavuC4%2BE4ttK2UhK%2FoikwH4u1oZI7WjEDszHIRAs5tzcGthZG6%2Bqt9cp50e8ti0ikl2YVbkVKfojMESLq1PxVf9ujzRsZ6LGboCsmaBYTk1Hr%2Fj2Sn7hZ64%2FD%2FyIsfDFZG0py%2FKptxu0G%2F3Gil%2FoVsIXK19t4Jfw8yLuacOPyjXAx4RYJmbxjE0R%2Bnq4PmrErGqfah%2BM0a6helj9SaSMCJ7vlZlsyZ1U8QhhQdO%2FeS1LOMh58RoyN7WRmEXgA%2BWnafKEMg00JA%2FeNugVSSnYThWDzKIT9DWwgpNc3g46pu7CSTO4Wo7XlZx9XhpaICBUjtZeg%2BInU5COZKb0spzq7p4cBHEqjBqV%2B1b3J0rXRvL1Xi%2F7LjABPx6srWXWZsrwpdkWBuv2Ha0MZVgkf2XDb5xJlfutelsNDn87JeUgfdvuy0PjEUUt8BW9yd4QXJwmoKCMlOUR%2Bt&actionId=BCIAAA04L01'
key = 'c94c86bd42c304524b3210a8ca52e7632'
report = RegisterScraping(ref, key)
result = report.request_page(1)

print(find_owners(result))
#
# page_1 = base64.b64decode(Path("test_1p.txt").read_text())
# page_1 = json.loads(page_1)['pageList'][0]
# page_1 = page_1['d'][2]['b'][0]
#
# page_2 = base64.b64decode(Path("test_2p.txt").read_text())
# page_2 = json.loads(page_2)['pageList'][0]
# page_2 = page_2['d'][2]['b'][0]
#
# page_3 = None
#
# page_cnt = int(page_1[8][2][0][0][3][1][0][0][0][1][0][1])
# page_cnt = 3
# if page_cnt > 2:
#     page_3 = base64.b64decode(Path("test_3p.txt").read_text())
#     page_3 = json.loads(page_3)['pageList'][0]
#     page_3 = page_3['d'][2]['b'][0][1][6]
#     # content_sort = json.dumps(page_3, indent=4)
#     # print(parse.unquote(content_sort))



# find_floors_1(page_1, page_3) if page_3 else find_floors_1(page_1)
# content_sort = json.dumps(content, indent=4)
# print(parse.unquote(content_sort))


# data = parse.unquote(output_image)
# res = data.replace('+', ' ')
# print(res)
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
