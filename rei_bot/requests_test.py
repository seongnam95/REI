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

        self.run()

    def run(self):
        for cookie in self.cookies:
            self.s.cookies.set(cookie['name'], cookie['value'])

        self.reportkey = self.get_reportkey(self.address)
        if self.reportkey is None: return

        # COUNT 값 파싱
        data = "ClipID=R03&uid=%s&clipUID=%s" % (self.reportkey, self.reportkey)
        cnt = self.s.post(url='https://cloud.eais.go.kr/report/RPTCAA02R02', headers=self.headers, data=data)
        time.sleep(0.5)
        self.page_cnt = int(cnt.text.split("'count':")[1].split(',')[0])
        print('PAGE_COUNT :: ', self.page_cnt)

        page_list = []
        for i in range(self.page_cnt):
            page_list.append(self.parsing_page(i))

        print('RESULT_PAGE_COUNT :: ', len(page_list))
        if self.page_cnt == 0: return
        elif self.page_cnt != len(page_list): return

        # title_name = parse.unquote(page_list[0][3][5])
        # print('대장명칭 :: ', title_name)
        #
        # viol = parse.unquote(page_list[0][5][5])        # 위반
        # print('위반 :: ', viol)

        # 페이지명 등록
        pages = [['PAGE_1', page_list[0]], ['PAGE_2', page_list[1]]]
        if self.page_cnt > 2:
            for i in range(2, self.page_cnt):
                sub_title_name = parse.unquote(page_list[i][2][5])
                sub_title_name = sub_title_name.split('을)')[1].replace('+', '')

                page = [sub_title_name, page_list[i]]
                pages.append(page)

        gp = GeneralParsing()

        for i in gp.find_owners(pages):
            print(i)

        print('#' * 100)

        for i in gp.find_floors(pages):
            print(i)

        for i in gp.find_public_area(pages):
            print(i)

        # content_sort = json.dumps(pages[0][1], indent=4)
        # print(parse.unquote(content_sort.replace('+', ' ')))

    # UID 조회
    def get_reportkey(self, address):
        headers = {
            "Referer": 'https://cloud.eais.go.kr/moct/bci/aaa04/BCIAAA04L01',
            "Content-Type": "application/json;charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
        }

        # 1. 발급 목록 조회
        response_doc_list = self.s.post(url='https://cloud.eais.go.kr/bci/BCIAAA06R01', headers=headers, json={"recordSize": 20})
        result = json.loads(response_doc_list.text)
        print('1', result)
        if '정상' in result['caisMessage']['resultMessage']: report_list = result['IssueReadHistList']
        else: return None

        # 해당 주소의 'pbsvcRecpNo', 'recpDate' 파싱
        recp_no, iss_date, kind_cd = None, None, None
        for i in report_list:
            if address in i['locDetlAddr']:
                recp_no = i['pbsvcRecpNo']
                iss_date = i['recpDate'].split('-')
                kind_cd = i['regstrKindCd']
                break

        issue_read_date = "%s%s%s" % (iss_date[0], iss_date[1], iss_date[2])

        # 2. 리포트 파일 네임 파싱
        file_nm_kind = {'2': 'djrBldrgstGnrl', '3': 'djrBldtitle', '4': 'djrBldexpos'}
        data = {"sysLocGbCd": "3", "reptNm": file_nm_kind[kind_cd], "recpDay": issue_read_date, "jobGbCd": "BC"}

        res = self.s.post(url='https://cloud.eais.go.kr/cba/CBAAZD04R01', headers=headers, json=data)
        result = json.loads(res.text)
        print('2', result)
        if '정상' in result['caisMessage']['resultMessage']: report_file_name = result['reportFileName']
        else: return None

        # 3. 파일 ID 파싱
        res_count = self.s.post(url='https://cloud.eais.go.kr/report/BCIAAA06R03', headers=headers,
                                json={"issueReadAppDate": issue_read_date, "pbsvcRecpNo": recp_no})
        result_count = json.loads(res_count.text)['count']

        # 4. 파일 등록
        ab = self.s.post(url='https://cloud.eais.go.kr/bci/BCIAAA06R03', headers=headers,
                         json={"issueReadAppDate": issue_read_date, "pbsvcRecpNo": recp_no})
        print('4', json.loads(ab.text))
        if '정상' not in result['caisMessage']['resultMessage']: return None

        # 5. uid 등록
        oof = get_oof(report_file_name, result_count, iss_date, recp_no)
        data = "isEncoding=false&isBigData=false&isMemoryDump=false&ClipID=R01&oof=" + oof
        res = self.s.post(url='https://cloud.eais.go.kr/report/RPTCAA02R02', headers=self.headers, data=data)
        print('5', res.text)
        uid = res.text.split("uid':'")[1].split("'")[0]

        return uid

    # 페이지 파싱
    def parsing_page(self, page_num):
        try:
            clip = '{"reportkey":"%s","isMakeDocument":true,"pageMethod":%s}' % (self.reportkey, page_num)
            data = "uid=%s&clipUID=%s&ClipType=DocumentPageView&ClipData=%s" % (self.reportkey, self.reportkey, parse.quote(clip))

            res = self.s.post(url='https://cloud.eais.go.kr/report/RPTCAA02R02', headers=self.headers, data=data)

            data = json.loads(res.text)['resValue']
            dec = base64.b64decode(data['viewData'])
            content = json.loads(dec)['pageList'][0]

            result = content['d'][2]['b'][0]
            return result

        except Exception as e:
            print('request_page_err :: ', e)
            return None


class GeneralParsing:
    # 소유자 조회
    @staticmethod
    def find_owners(pages):
        result = []
        for p in pages:
            owners = p[1][0][6] if p[0] == "PAGE_1" else p[1][1][6] if p[0] == "소유자현황" else None
            if owners is None: continue

            for owner in owners:       # 소유자 만큼 반복
                owner = owner[6][0][0][2]
                if owner is None: break

                items = []
                for rows in owner:    # 정보 파싱
                    for row in rows:
                        if type(row) == list and len(row) > 3:
                            item = parse.unquote(row[7]).replace('+', ' ').lstrip(' ')
                            items.append(item)

                if len(items) > 5:
                    dic_owner = {}
                    if p[0] == "PAGE_1":
                        dic_owner = {'성명': items[0], '번호': items[4], '주소': items[1],
                                     '지분': items[2], '변동일': items[3], '변동원인': items[5]}
                    elif p[0] == "소유자현황":
                        dic_owner = {'성명': items[0], '번호': items[1], '주소': items[2],
                                     '지분': items[3], '변동일': items[4], '변동원인': items[5]}
                    result.append(dic_owner)
        return result

    # 건축물 현황 (층별)
    @staticmethod
    def find_floors(pages):
        result = []
        for p in pages:
            floors = p[1][2][6] if p[0] == "PAGE_1" else p[1][1][6] if p[0] == "건축물현황" else None
            if floors is None: continue

            for floor in floors:
                if floor[6][0][0][5]: break

                floor = floor[6][0][0][2][0]
                if floor is None: break

                items = []
                for row in floor:
                    if type(row) == list and len(row) > 3:
                        item = parse.unquote(row[7]).replace('+', ' ')
                        items.append(item)

                if len(items) > 4:
                    dic_floor = {'구분': items[0], '층명칭': items[1], '구조': items[2], '용도': items[3], '면적': items[4]}
                    result.append(dic_floor)

        return result

    # 기본 개요 테이블
    @staticmethod
    def find_basic_table(page):
        value_list = []
        basic = page[4][2]
        for columns in basic:
            for c in columns:
                if type(c) == list and len(c) > 3:
                    data = parse.unquote(c[7]).replace('+', ' ')
                    value_list.append(data)

        result = {'고유번호': value_list[1], '건물명칭': value_list[3], '호가구세대': value_list[5],
                  '주소': '%s %s' % (value_list[8], (value_list[10].split(' 외')[0])), '도로명주소': value_list[12],
                  '대지면적': value_list[14], '연면적': value_list[17], '지역': value_list[22], '지구': value_list[23], '구역': value_list[24],
                  '건축면적': value_list[26], '용적률산정용연면적': value_list[33], '주구조': value_list[34], '주용도': value_list[35],
                  '층수(지하)': (value_list[36].replace(' ', '').split('층/')[0].split('지하')[1]),
                  '층수(지상)': (value_list[36].replace(' ', '').split('지상')[1].split('층')[0]),
                  '건폐율': value_list[38], '용적률': value_list[41], '높이': value_list[44]}
        return result

    @staticmethod
    def find_public_area(pages):
        pages = [pages[0], pages[1]]
        result = []

        # 모든 페이지 반복
        for p in pages:
            floors = p[1][1][6] if p[0] == "PAGE_1" else p[1][4][6] if p[0] == "PAGE_2" else None
            if floors is None: continue     # PAGE_1, PAGE_2만 파싱

            for floor in floors:    # 층 수 만큼 반복
                floor = floor[6][0][0][2][0]
                if floor is None: break

                items = []
                for row in floor:   # 해당 층의 항목 만큼 반복
                    if type(row) == list and len(row) > 3:
                        item = parse.unquote(row[7]).replace('+', ' ')
                        items.append(item)

                blank = not any("여백" in i for i in items)       # '이하여백' 여부
                if len(items) > 4 and blank:
                    dic_floor = {'구분': items[0], '층명칭': items[1], '구조': items[2], '용도': items[3], '면적': items[4]}
                    result.append(dic_floor)
        return result


def get_oof(file_nm, options, iss_date, recp_no):
    root = Et.parse('oof.xml').getroot()

    path = f"/cais_data/issue/{iss_date[0]}/{iss_date[1]}/{iss_date[2]}/{recp_no}/{recp_no}.xml"
    png = f"/cais_data/issue/{iss_date[0]}/{iss_date[1]}/{iss_date[2]}/{recp_no}/{recp_no}.png"
    options['FILE_PATH'] = png

    file_tag = root.iter('file')
    file_nm = f"%root%/crf/bci/{file_nm}.crf"
    for t in file_tag: t.attrib['path'] = file_nm

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


# 세움터 로그인
def sign_in_saumter():
    try:
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

    except:
        print('로그인 실패, 재시도')
        time.sleep(5)
        sign_in_saumter()


# d, c = sign_in_saumter()
a = '서울특별시 중랑구 면목동 1550 201동 601호'
r = 'https://cloud.eais.go.kr/report/BCIAAA04V01?param=U2FsdGVkX1%2FGfSBSVnFrB%2F6%2B50TlF5JA%2FtMWM1T%2BbjbsSkWvEMokcI5i%2B4nIuNwSRkyPmOOxfIeICOi3RMwXsZ9NipI4SyiGKghsPlz8ndqcYY7tWC9r%2FBARWxKRnDSlsyzNEpLV57%2FdPDwT58YZMXLZ8S%2FGW6DAy%2BQPUyIQ%2B80B9N0sOtcv6KXQ0aIh7PRwW3yQ2BOq0XrnogTKz5358NRG%2B8krY8ChbBnC8n%2FfEAthYY5XQe1CK3ire4lP6Jo3rhaeARRtFbqpsaYrTeyJ9L6UjEZZOy%2Btoo5M9MTUcQjFJV1uoK1CMu76ojJNTHEtZKeiaBUL1YtNDQeb9q1pBLuix%2F%2F46bJvDpcvrGq4Qwv%2BH36NleSX0nMjvuJrLIRhB5xGnI9jBVMx8VT3k8dQH1S%2Bf1%2BFCkIyBcfDAfhrB67oGxe8%2BYNYdufLrIAfSY0iaNm4Lq8IT58I13zqQTUBDN3O8tv6HC1Faq1nLRMAAdh4VKTS93NVALl%2FwZ7AhaF90BbHvIlj7xRYFeH9xvc6FCq1iVRCggnc5HYjTKxTzT6p7fDDPlkx2SaEE%2F51WmklF5uARc61s2NpR3X3rXkA0rWRI1tArVP7ew1aQdl6eEY%3D&actionId=BCIAAA04L01'

# RegisterScraping(d, c, a, r)
