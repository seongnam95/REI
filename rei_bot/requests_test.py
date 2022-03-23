import webbrowser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from seleniumrequests import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from PySide6.QtWidgets import QMainWindow, QApplication

import json
import time
import sys
import requests


def CreateSession():
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
    return driver

class RequestTest:
    def __init__(self):
        super(RequestTest, self).__init__()
        #self.sign_in()
        self.test()

    def test(self):
        s = requests.Session()
        a = s.get('https://cloud.eais.go.kr/report/BCIAAA04V01?param=U2FsdGVkX1%2BqA5AzxoxpvUoAYB6RDJ7HH3CEG9w6eWwt0bd0CFXl%2Bv7v%2FPXX5v2gCa6IzdqPDLoRFpjHARXBcxW55NOV9x9zKVZEbq3vcKh92F0l0Ly83RoQ0KvzQkwLrd2%2BSBznfTBtNcXmWIcvPMiBC7Id5fUEcITsNRxbRwVzjD60pdfAF4oPdxtZeFlaIDvEHwZduPof1v4nPkm7xi%2FKhiQcJNsuPCTLqMFNagljqyT1E9HwVVuwHkNKt66kRtQdFJ7ZMIhRheYWBUfL1KqfyIP%2FIONxQxnXXizKcaYiwhz0glt3%2BFRXKNM0qdagVhsr4uvrIr7gBlyO%2BS2NnlN7M9HYv%2FcADC3X7AO1gJKQ9xxCreF6oVatafQMtcBpj7gfQnPY0rjzj9wB5H8zQrpbfAYlyhGAJsbYyhenokIKYMtA0VLfASknpkL%2BLacUWH8g7A552Y5G3qyb6%2FOcfISBqTOwFPSX8gKDzRMN0TkyxrEkK%2Fi3TLcgNh3Sr0IUw8G7ZR%2BsWOX0LUWywNXIjGdmSD30faPp%2FQXiO60ZyTMECn5rxTCA2RTFwwFBgHoiLnlq5xnDOADCUGz0nIG4sKO5fD8WIn3LPqKiTDOzzcg%3D&actionId=BCIAAA04L01')
        print(a.headers)

    def sign_in(self):
        self.s = CreateSession()

        self.s.get("https://cloud.eais.go.kr/moct/awp/abb01/AWPABB01F01")
        self.s.implicitly_wait(5)

        # ID, PW 입력 후 로그인
        self.s.find_element(By.ID, 'membId').send_keys('haul1115')
        self.s.find_element(By.ID, 'pwd').send_keys('ks05090818@')
        self.s.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div/div[1]/div[1]/button').click()
        time.sleep(0.5)

        cookies = self.s.get_cookies()
        self.s.close()

        s = requests.Session()
        for cookie in cookies:
            s.cookies.set(cookie['name'], cookie['value'])
        print('로그인 완료')

        headers = {"Host": "cloud.eais.go.kr", "Content-Type": "application/json;charset=UTF-8",
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36",
                   'Referer': "https://cloud.eais.go.kr/moct/bci/aaa02/BCIAAA02L01"}

        sigungu, seqno = '11260', '100249271'

        datas = {"inqireGbCd": "1", "bldrgstCurdiGbCd": "0", "reqSigunguCd": sigungu, "bldrgstSeqno": seqno}

        response_title = s.post('https://cloud.eais.go.kr/bci/BCIAAA02R04', headers=headers, json=datas)

        result = json.loads(response_title.text)['findExposList'][0]
        print(result)

        bun, ji = result['mnnm'].lstrip('0'), result['slno'].lstrip('0')
        if ji: ji = f'-{ji}'
        if {result["hoNm"]} is not None: ho = ' ' + result["hoNm"]

        address = f'{result["sigunguNm"]} {result["bjdongNm"]} {bun}{ji} {result["dongNm"]}{ho}'

        datas2 = {"bldrgstSeqno": result["bldrgstSeqno"],
                  "regstrGbCd": result["regstrGbCd"],
                  "regstrKindCd": result["regstrKindCd"],
                  "mjrfmlyIssueYn": "N",
                  "locSigunguCd": result["sigunguCd"],
                  "locBjdongCd": result["bjdongCd"],
                  "locPlatGbCd": result["platGbCd"],
                  "locDetlAddr": address,
                  "locBldNm": result["bldNm"],
                  "bldrgstCurdiGbCd": "0"}

        print(datas2)

        # 민원 담기 (담아야 응답 값 나옴)
        a = s.post('https://cloud.eais.go.kr/bci/BCIAAA02C01', headers=headers, json=datas2)
        print(a.text)

        # 담은 민원 처리 (응답 값 필요)
        response_put_in = s.post('https://cloud.eais.go.kr/bci/BCIAAA02R05', headers=headers)
        result = json.loads(response_put_in.text)
        print(result)




RequestTest()