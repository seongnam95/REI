from PySide6.QtCore import QThread, QObject, Signal
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
from seleniumrequests import Chrome
from pathlib import Path
from urllib import parse

import time
import webbrowser
import json
import requests
import base64
import urllib3
import numpy as np
import os
import xml.etree.ElementTree as Et

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# driver = Chrome(service=Service('chromedriver.exe'), options=chrome_options)

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
        if row is None: break

        owner_list = []
        for r in row:
            for c in r:
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
    def __init__(self, address, referer):
        self.headers = {
            "Referer": referer,
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
        }
        self.recp_no, self.file_id = None, None
        self.referer = referer

        # Requests에 로그인 세션 넘기기
        self.s = requests.Session()
        self.s.verify = False

        self.driver, cookies = sign_in_saumter()
        for cookie in cookies:
            self.s.cookies.set(cookie['name'], cookie['value'])

        self.reportkey = self.get_reportkey(address)

        # pages = [self.request_page(0)]
        # page_cnt = int(pages[0][8][2][0][0][3][1][0][0][0][1][0][1])
        # print(page_cnt)

        page = self.request_page(0)
        content_sort = json.dumps(page, indent=4)
        print(parse.unquote(content_sort))

        #
        # for i in range(page_cnt):
        #     if i == 0: continue
        #     pages.append(self.request_page(i))
        #
        # print(len(pages))
        # print(find_owners(pages[0]))

    # UID 조회
    def get_reportkey(self, address):
        headers = {
            "Referer": 'https://cloud.eais.go.kr/moct/bci/aaa04/BCIAAA04L01',
            "Content-Type": "application/json;charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
        }

        # 발급 목록 조회
        response_doc_list = self.s.post(url='https://cloud.eais.go.kr/bci/BCIAAA06R01', headers=headers, json={"recordSize": 20})
        result_list = json.loads(response_doc_list.text)['IssueReadHistList']

        # 해당 주소의 'pbsvcRecpNo' 파싱
        recp_no, iss_date = None, None
        for i in result_list:
            if address in i['locDetlAddr']:
                recp_no = i['pbsvcRecpNo']
                iss_date = i['recpDate'].split('-')
                break

        # 'File ID' 파싱
        file_id = None
        if recp_no:
            issue_read_date = "%s%s%s" % (iss_date[0], iss_date[1], iss_date[2])
            r = self.s.post(url='https://cloud.eais.go.kr/report/BCIAAA06R03', headers=headers,
                                            json={"issueReadAppDate": issue_read_date, "pbsvcRecpNo": recp_no})
            print(r.text)
            get_uid_json = self.s.post(url='https://cloud.eais.go.kr/bci/BCIAAA06R03', headers=headers,
                                         json={"issueReadAppDate": issue_read_date, "pbsvcRecpNo": recp_no})
            response = json.loads(get_uid_json.text)
            print(response)
            file_id = response['count']['FILE_ID']

        if file_id:
            data = f"""isEncoding=false&isBigData=false&isMemoryDump=false&ClipID=R01&oof=%3C%3Fxml%20version%3D'1.0'%20encoding%3D'utf-8'%3F%3E%3Coof%20version%3D'3.0'%3E%3Cdocument%20title%3D''%20enable-thread%3D'0'%3E%3Cfile-list%3E%3Cfile%20type%3D'crf.root'%20path%3D'%25root%25%2Fcrf%2Fbci%2FdjrBldrgstGnrl.crf'%3E%3C%2Ffile%3E%3C%2Ffile-list%3E%3Cconnection-list%3E%3Cconnection%20type%3D'file'%20namespace%3D'XML1'%3E%3Cconfig-param-list%3E%3Cconfig-param%20name%3D'path'%3E%2Fcais_data%2Fissue%2F{iss_date[0]}%2F{iss_date[1]}%2F{iss_date[2]}%2F{recp_no}%2F{recp_no}.xml%3C%2Fconfig-param%3E%3C%2Fconfig-param-list%3E%3Ccontent%20content-type%3D'xml'%20namespace%3D'*'%3E%3Ccontent-param%20name%3D'encoding'%3Eeuc-kr%3C%2Fcontent-param%3E%3Ccontent-param%20name%3D'root'%3E%7B%25dataset.xml.root%25%7D%3C%2Fcontent-param%3E%3C%2Fcontent%3E%3C%2Fconnection%3E%3C%2Fconnection-list%3E%3Cfield-list%20type%3D%22name%22%3E%3Cfield%20name%3D'ISSUE_READ_GB_CD'%20trim%3D'true'%3E0%3C%2Ffield%3E%3Cfield%20name%3D'FILE_ID'%20trim%3D'true'%3E{file_id}%3C%2Ffield%3E%3Cfield%20name%3D'CHANG_MATR_COUNT'%20trim%3D'true'%3E4%3C%2Ffield%3E%3Cfield%20name%3D'WCLF_INFO_COUNT'%20trim%3D'true'%3E1%3C%2Ffield%3E%3Cfield%20name%3D'BLD_CURST_INFO_COUNT'%20trim%3D'true'%3E4%3C%2Ffield%3E%3Cfield%20name%3D'RELAT_RNM_COUNT'%20trim%3D'true'%3E1%3C%2Ffield%3E%3Cfield%20name%3D'LC_INFO_COUNT'%20trim%3D'true'%3E1%3C%2Ffield%3E%3Cfield%20name%3D'RELAT_JIBUN_COUNT'%20trim%3D'true'%3E1%3C%2Ffield%3E%3Cfield%20name%3D'OWNR_CURST_INFO_COUNT'%20trim%3D'true'%3E1%3C%2Ffield%3E%3Cfield%20name%3D'ETC_RCD_MATR_COUNT'%20trim%3D'true'%3E1%3C%2Ffield%3E%3Cfield%20name%3D'SVR_GB'%20trim%3D'true'%3Epm3%3C%2Ffield%3E%3Cfield%20name%3D'SVR_HOST'%20trim%3D'true'%3E156.178%3A7000%3C%2Ffield%3E%3Cfield%20name%3D'FILE_PATH'%20trim%3D'true'%3E%2Fcais_data%2Fissue%2F{iss_date[0]}%2F{iss_date[1]}%2F{iss_date[2]}%2F{recp_no}%2F{recp_no}.png%3C%2Ffield%3E%3C%2Ffield-list%3E%3C%2Fdocument%3E%3C%2Foof%3E"""

            xml = Et.parse('oof.xml')
            root = xml.getroot()

            oof = Et.tostring(root).decode('utf-8')
            o = "<?xml version='1.0' encoding='utf-8'?>" + oof
            data = "isEncoding=false&isBigData=false&isMemoryDump=false&ClipID=R01&oof=" + parse.quote(o)
            headers = {
                "Referer": self.referer,
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
            }

            # uid 등록
            res = self.s.post(url='https://cloud.eais.go.kr/report/RPTCAA02R02', headers=headers, data=data)
            print(res.text)
            uid = res.text.split("uid':'")[1].split("'")[0]

            return uid

    def request_page(self, page_num):
        clip = '{"reportkey":"%s","isMakeDocument":true,"pageMethod":%s}' % (self.reportkey, page_num)

        d = "ClipID=R03&uid=%s&clipUID=%s" % (self.reportkey, self.reportkey)
        self.s.post(url='https://cloud.eais.go.kr/report/RPTCAA02R02', headers=self.headers, data=d)

        d = "uid=%s&clipUID=%s&ClipType=DocumentPageView&ClipData=%s" % (self.reportkey, self.reportkey, parse.quote(clip))
        res = self.s.post(url='https://cloud.eais.go.kr/report/RPTCAA02R02', headers=self.headers, data=d)

        data = json.loads(res.text)['resValue']
        dec = base64.b64decode(data['viewData'])
        content = json.loads(dec)['pageList'][0]

        result = content['d'][2]['b'][0]
        return result


# 세움터 로그인
def sign_in_saumter():
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

    # 로그인 페이지로 이동
    driver.get("https://cloud.eais.go.kr/moct/awp/abb01/AWPABB01F01")
    driver.implicitly_wait(5)

    # 로그인 이벤트
    driver.find_element(By.ID, 'membId').send_keys('haul1115')
    driver.find_element(By.ID, 'pwd').send_keys('ks05090818@')
    driver.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div/div[1]/div[1]/button').click()
    time.sleep(0.5)

    cookies = driver.get_cookies()
    return driver, cookies


# xml_path = root.find('document').find('connection-list').find('connection').find('config-param-list').find('config-param')
# con = root.find('document').find('field-list')
#
# # print(xml_path.text)
# a = root.iter('config-param')
#
# for neighbor in root.iter('config-param'):
#     print(neighbor.text)

# root = tree.getroot()
#
# ##수정할 부분
# target_tag = root.find("path")
#
# original = target_tag.text  # 원본 String
# modified = original.replace(r"/home/ailsb", r"C:\Users\lab_research")
# modified = modified.replace("/", "\\")
# target_tag.text = modified  # 수정
#
# tree.write(target_path)


a = "%3C%3Fxml%20version%3D'1.0'%20encoding%3D'utf-8'%3F%3E%3Coof%20version%3D'3.0'%3E%3Cdocument%20title%3D''%20enable-thread%3D'0'%3E%3Cfile-list%3E%3Cfile%20type%3D'crf.root'%20path%3D'%25root%25%2Fcrf%2Fbci%2FdjrBldrgstGnrl.crf'%3E%3C%2Ffile%3E%3C%2Ffile-list%3E%3Cconnection-list%3E%3Cconnection%20type%3D'file'%20namespace%3D'XML1'%3E%3Cconfig-param-list%3E%3Cconfig-param%20name%3D'path'%3E%2Fcais_data%2Fissue%2F2022%2F04%2F01%2F20223060000P106262%2F20223060000P106262.xml%3C%2Fconfig-param%3E%3C%2Fconfig-param-list%3E%3Ccontent%20content-type%3D'xml'%20namespace%3D'*'%3E%3Ccontent-param%20name%3D'encoding'%3Eeuc-kr%3C%2Fcontent-param%3E%3Ccontent-param%20name%3D'root'%3E%7B%25dataset.xml.root%25%7D%3C%2Fcontent-param%3E%3C%2Fcontent%3E%3C%2Fconnection%3E%3C%2Fconnection-list%3E%3Cfield-list%20type%3D%22name%22%3E%3Cfield%20name%3D'ISSUE_READ_GB_CD'%20trim%3D'true'%3E0%3C%2Ffield%3E%3Cfield%20name%3D'FILE_ID'%20trim%3D'true'%3E70961d3d-53c5-44ca-a6bf-9ecebea43265%3C%2Ffield%3E%3Cfield%20name%3D'CHANG_MATR_COUNT'%20trim%3D'true'%3E4%3C%2Ffield%3E%3Cfield%20name%3D'WCLF_INFO_COUNT'%20trim%3D'true'%3E1%3C%2Ffield%3E%3Cfield%20name%3D'BLD_CURST_INFO_COUNT'%20trim%3D'true'%3E4%3C%2Ffield%3E%3Cfield%20name%3D'RELAT_RNM_COUNT'%20trim%3D'true'%3E1%3C%2Ffield%3E%3Cfield%20name%3D'LC_INFO_COUNT'%20trim%3D'true'%3E1%3C%2Ffield%3E%3Cfield%20name%3D'RELAT_JIBUN_COUNT'%20trim%3D'true'%3E1%3C%2Ffield%3E%3Cfield%20name%3D'OWNR_CURST_INFO_COUNT'%20trim%3D'true'%3E1%3C%2Ffield%3E%3Cfield%20name%3D'ETC_RCD_MATR_COUNT'%20trim%3D'true'%3E1%3C%2Ffield%3E%3Cfield%20name%3D'SVR_GB'%20trim%3D'true'%3Epm3%3C%2Ffield%3E%3Cfield%20name%3D'SVR_HOST'%20trim%3D'true'%3E156.172%3A7000%3C%2Ffield%3E%3Cfield%20name%3D'FILE_PATH'%20trim%3D'true'%3E%2Fcais_data%2Fissue%2F2022%2F04%2F01%2F20223060000P106262%2F20223060000P106262.png%3C%2Ffield%3E%3C%2Ffield-list%3E%3C%2Fdocument%3E%3C%2Foof%3E"
print(parse.unquote(a))

ref = 'https://cloud.eais.go.kr/report/BCIAAA04V01?param=U2FsdGVkX1%2BjguSZLobNdP%2BwWhrVGfNBfBzUBOiyy2DElBx6UaS756begr9%2FwbM6awv%2FxxJKXS7q%2BgvG9b8PkqltaqPaWhQLWVW%2FjBkMZP%2F8eNukB4rPQcP22qtyc6m0%2BTTZoct1xTpsvPaLCkd5tPfMDy%2BIuzz%2FIetw8WezNlteaxf%2BMBHJI9ZKjXfidh5hDGElIP5%2FNW4bGf6BW0hlLVPTs%2Fsz6Ye3QA9zYyjAbW%2B0%2FPgoDa%2FAeh6OwKwd6%2FD8%2BagkyfEwQ%2FKEfXLS3ReKQw6gQQM7XL5Fqao5Z6tAy%2FIaHUl9%2BbA9uEbrr0CFscs5kD37kFLeFAO%2BBacEDSct61dXpfqzZFYiT2g3rDY%2BWoi%2FS6As5I%2BMSYhwzeM6nZy%2Bpz%2FNBjh%2BLCHvxQLTxB%2F8yxR%2B19Fmvx%2F3f49Uh1Us5Kx0iTn5NpYlYjbsTra5TDIcIjJAKtnIU6grajuhrHA8ytRO98rgY1BZkUk4wdAqEVy7EiKjCanKATBijtJmiyrwDyRNCeBlfbUq8paHhF%2FpLgjDjv6WCafUnlwCJ8PG9%2Fzq9feWf%2B4i3AHmZRsTLo8OML9vJ9CGZBDELLk1LhbG96yNMkAJSSnxXykcuAZ9LVfeQsF6DcYHmpAwYFFsXIeFmaTIBCnTHJYEcntPsQElJvxsyxB%2FiaORWbeq6nFsYp%2BFyvSew3Qy1Y4CidyT51B5&actionId=BCIAAA04L01'
RegisterScraping('서울특별시 중랑구 상봉동 111-51', ref)

# page_1 = base64.b64decode(Path("test.txt").read_text())
# page_1 = json.loads(page_1)['pageList'][0]
# page_1 = page_1['d'][2]['b'][0]
# content_sort = json.dumps(page_1, indent=4)
# print(parse.unquote(content_sort))

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