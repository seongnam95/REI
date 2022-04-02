from PySide6.QtCore import QThread, QObject, Signal
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from seleniumrequests import Chrome
from urllib import parse

import time
import json
import requests
import base64
import urllib3
import xml.etree.ElementTree as Et

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# 소유자 조회
def find_owners(pages):
    owners = []
    for p in pages:
        if p[0] == 'PAGE_1':
            content = p[1][0][6]

            for c in content:       # 소유자 만큼 반복
                rows = c[6][0][0][2]
                if rows is None: break

                owner_list = []
                for row in rows:    # 정보 파싱
                    for r in row:
                        if type(r) == list and len(r) > 3:
                            result = parse.unquote(r[7]).replace('+', ' ').lstrip(' ')
                            owner_list.append(result)

                owner = {'성명': owner_list[0], '번호': owner_list[4], '주소': owner_list[1],
                         '지분': owner_list[2], '변동일': owner_list[3], '변동원인': owner_list[5]}
                owners.append(owner)

        elif p[0] == '소유자현황':
            content = p[1][1][6]

            for c in content:       # 소유자 만큼 반복
                rows = c[6][0][0][2]
                if rows is None: break

                owner_list = []
                for row in rows:    # 정보 파싱
                    for r in row:
                        if type(r) == list and len(r) > 3:
                            result = parse.unquote(r[7]).replace('+', ' ').lstrip(' ')
                            owner_list.append(result)

                owner = {'성명': owner_list[0], '번호': owner_list[1], '주소': owner_list[2],
                         '지분': owner_list[3], '변동일': owner_list[4], '변동원인': owner_list[5]}
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


def get_oof(options, iss_date, recp_no):
    root = Et.parse('oof.xml').getroot()

    path = f"/cais_data/issue/{iss_date[0]}/{iss_date[1]}/{iss_date[2]}/{recp_no}/{recp_no}.xml"
    png = f"/cais_data/issue/{iss_date[0]}/{iss_date[1]}/{iss_date[2]}/{recp_no}/{recp_no}.png"
    options['FILE_PATH'] = png

    path_tag = root.iter('config-param')
    for t in path_tag: t.text = path

    count_tag = root.iter('field')
    for t in count_tag:
        name = t.attrib['name']
        if name in options.keys():
            t.text = options[name]

    decode_oof = Et.tostring(root).decode('utf-8')
    oof = f"<?xml version='1.0' encoding='utf-8'?>{decode_oof}".strip('\n\t')
    return parse.quote(oof)


class RegisterScraping(QThread):
    def __init__(self, driver, cookies, address, referer):
        super().__init__()
        self.headers = {
            "Referer": referer,
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
        }
        self.recp_no, self.file_id, self.reportkey, self.page_cnt = None, None, None, 0
        self.address, self.referer = address, referer
        self.driver, self.cookies = driver, cookies

        # Requests에 로그인 세션 넘기기
        self.s = requests.Session()
        self.s.verify = False

    def run(self):
        for cookie in self.cookies:
            self.s.cookies.set(cookie['name'], cookie['value'])

        self.reportkey = self.get_reportkey(self.address)

        d = "ClipID=R03&uid=%s&clipUID=%s" % (self.reportkey, self.reportkey)
        cnt = self.s.post(url='https://cloud.eais.go.kr/report/RPTCAA02R02', headers=self.headers, data=d)
        time.sleep(0.5)
        self.page_cnt = int(cnt.text.split("'count':")[1].split(',')[0])
        print('PAGE_COUNT :: ', self.page_cnt)

        page_list = []
        for i in range(self.page_cnt):
            page_list.append(self.parsing_page(i))

        print('RESULT_PAGE_COUNT :: ', len(page_list))

        title_name = parse.unquote(page_list[0][3][5])
        print('대장명칭 :: ', title_name)

        viol = parse.unquote(page_list[0][5][5])        # 위반
        print('위반 :: ', viol)

        # 페이지명 등록
        pages = [['PAGE_1', page_list[0]], ['PAGE_2', page_list[1]]]
        if self.page_cnt > 2:
            for i in range(2, self.page_cnt):
                sub_title_name = parse.unquote(page_list[i][2][5])
                sub_title_name = sub_title_name.split('(을)')[1].replace('+', '')

                page = [sub_title_name, page_list[i]]
                pages.append(page)

        for i in find_owners(pages):
            print(i)

        # content_sort = json.dumps(pages[2][1], indent=4)
        # print(parse.unquote(content_sort.replace('+', ' ')))

    # UID 조회
    def get_reportkey(self, address):
        headers = {
            "Referer": 'https://cloud.eais.go.kr/moct/bci/aaa04/BCIAAA04L01',
            "Content-Type": "application/json;charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
        }

        # 발급 목록 조회
        response_doc_list = self.s.post(url='https://cloud.eais.go.kr/bci/BCIAAA06R01', headers=headers, json={"recordSize": 20})
        time.sleep(0.5)
        result_list = json.loads(response_doc_list.text)['IssueReadHistList']

        # 해당 주소의 'pbsvcRecpNo' 파싱
        recp_no, iss_date = None, None
        for i in result_list:
            if address in i['locDetlAddr']:
                recp_no = i['pbsvcRecpNo']
                iss_date = i['recpDate'].split('-')
                break

        # 'File ID' 파싱
        if recp_no:
            issue_read_date = "%s%s%s" % (iss_date[0], iss_date[1], iss_date[2])

            res_count = self.s.post(url='https://cloud.eais.go.kr/report/BCIAAA06R03', headers=headers,
                                    json={"issueReadAppDate": issue_read_date, "pbsvcRecpNo": recp_no})
            time.sleep(0.5)
            result_count = json.loads(res_count.text)['count']

            self.s.post(url='https://cloud.eais.go.kr/bci/BCIAAA06R03', headers=headers,
                        json={"issueReadAppDate": issue_read_date, "pbsvcRecpNo": recp_no})
            time.sleep(0.5)

            file_id = result_count['FILE_ID']

            if file_id:
                headers = {
                    "Referer": self.referer,
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
                }
                oof = get_oof(result_count, iss_date, recp_no)
                data = "isEncoding=false&isBigData=false&isMemoryDump=false&ClipID=R01&oof=" + oof

                # uid 등록
                res = self.s.post(url='https://cloud.eais.go.kr/report/RPTCAA02R02', headers=headers, data=data)
                time.sleep(1)
                uid = res.text.split("uid':'")[1].split("'")[0]

                print(uid)
                return uid

    # 페이지 파싱
    def parsing_page(self, page_num):
        # try:
        clip = '{"reportkey":"%s","isMakeDocument":true,"pageMethod":%s}' % (self.reportkey, page_num)

        d = "uid=%s&clipUID=%s&ClipType=DocumentPageView&ClipData=%s" % (self.reportkey, self.reportkey, parse.quote(clip))
        res = self.s.post(url='https://cloud.eais.go.kr/report/RPTCAA02R02', headers=self.headers, data=d)
        time.sleep(0.1)

        data = json.loads(res.text)['resValue']
        dec = base64.b64decode(data['viewData'])
        content = json.loads(dec)['pageList'][0]

        result = content['d'][2]['b'][0]
        return result

        # except Exception as e:
        #     print('request_page_err :: ', e)
        #     return None


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

