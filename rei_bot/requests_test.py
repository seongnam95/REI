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
        self.recp_no, self.file_id, self.reportkey = None, None, None
        self.address, self.referer = address, referer
        self.driver, self.cookies = driver, cookies
        print(address, referer)
        # Requests에 로그인 세션 넘기기
        self.s = requests.Session()
        self.s.verify = False

    def run(self):
        for cookie in self.cookies:
            self.s.cookies.set(cookie['name'], cookie['value'])

        self.reportkey = self.get_reportkey(self.address)

        pages = [self.request_page(0)]
        print(find_owners(pages[0]))

        # content_sort = json.dumps(pages[0], indent=4)
        # print(parse.unquote(content_sort))

        page_cnt = int(pages[0][8][2][0][0][3][1][0][0][0][1][0][1])
        print("cnt", page_cnt)

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
            print(result_count)

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
                time.sleep(0.5)
                uid = res.text.split("uid':'")[1].split("'")[0]

                print(res.text)
                return uid

    def request_page(self, page_num):
        clip = '{"reportkey":"%s","isMakeDocument":true,"pageMethod":%s}' % (self.reportkey, page_num)

        d = "ClipID=R03&uid=%s&clipUID=%s" % (self.reportkey, self.reportkey)
        self.s.post(url='https://cloud.eais.go.kr/report/RPTCAA02R02', headers=self.headers, data=d)
        time.sleep(0.5)

        d = "uid=%s&clipUID=%s&ClipType=DocumentPageView&ClipData=%s" % (self.reportkey, self.reportkey, parse.quote(clip))
        time.sleep(0.5)
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


# ref = 'https://cloud.eais.go.kr/report/BCIAAA04V01?param=U2FsdGVkX1%2BQSTMCyDp7lAayu0QGv%2B1QNPqyUEb5feEipZ23KITeiAtzxZ9UmySBnBxv8LLEJBQq0Ul%2F3A%2BLqzgP1fzId6Ew4uwXjo3wvYxAVf0q2SaoS24CulFugGIDy6hK8rpemiYs8pfNvj4jpBhYt%2F5331AePJ9S0FQAFaJ1g%2B%2BFn6YCxNky1RDN%2B9B1kM9gznVgf7TxUej%2FnZHGAyO2dNC2HN5YfBA23E4JCpHrjkK1dINzfs8FVoS21Xq1%2FbLL2Qss%2BmOQVlV6e2iKp0r4NiLVDVwUr4FGX87DiS5EJdRxGC6PR8Vm14N8ol11i6hSo1R%2FCp9eQKkXvpiTpKucq3Ccv7DhVSjInm5faEPe6kWmV1gxTFX0I6N3OiQCZnny5%2Fjo5fTYoDgPQ%2FaoVvCd6FKRFxbrIXNYUXNq6v4KEBi%2BzIgNXcI0uXeS8uoAdTPBKGq4Utzi7dM45giT8DS4acFFnCh74lWm5rummkPuGwfkKZ3Ghfm5IpgvRZ5kcO7vyxxqn8%2BvwpFY6GjCyMq%2BleAzTF%2BLbFeTBgvg2Ncxxu9CW%2FUJlkb7ltucyyyKVDGq2eFNHEtWc7Uuq5pp6vbH0tivd04dcn3Vm7s%2BjoDheOmtKojIgdHicQhXFmBYrAUXADNjkqdqWd8BxYds%2FhZu%2BsTCcooBeRwJLDv8qfNcxDbiG%2FE%2BchMzMxuR744M&actionId=BCIAAA04L01'
# RegisterScraping('상봉동 88-85', ref)

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