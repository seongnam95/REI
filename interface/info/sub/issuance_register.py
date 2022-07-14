import base64
import json
import os
import sys
import pandas as pd
import requests

from Crypto.Cipher import PKCS1_v1_5, AES
from Crypto.PublicKey import RSA

from PySide6.QtCore import QThread, QObject, Signal, QSize
from PySide6.QtGui import QColor, QIcon
from PySide6.QtWidgets import QDialog, QGraphicsDropShadowEffect, QWidget, QFileDialog, \
    QLabel, QGridLayout, QListWidgetItem

from interface.public.get_address_lite import GetAddressLite
from interface.info.resources.ui.ui_register import UiRegister
from ui.custom import LoadingBox, BlackBoxMsg


class IssuanceRegister(QDialog, UiRegister):
    def __init__(self, address=None, data=None):
        super().__init__()
        self.setupUi(self)

        self._init_ui()
        self._init_interaction()

        self.address, self.select_address, self.info = None, None, {}
        self.existing, self.building, self.expos, self.bld_data = None, None, None, {}
        self.flag, self.kind, self.ty, self.headers = None, None, None, None
        self.DETAIL_ADDRESS_API_KEY = 'U01TX0FVVEgyMDIxMTIyMzEzMTE1NzExMjA2MTU='

        self.api_data = {'HOST': 'https://api.tilko.net/',
                         'KEY': '6062d22d48734cd3af82837f696730fb'}
        self.user = {'user_id': 'mogsin21', 'user_pw': 'happy2588@',
                     'num_1': 'P3372711', 'num_2': '3234', 'num_pw': 'kim2588'}

        if data is not None:
            self.existing, self.address = data, address

            bjr_nm = '' if address['법정리'] == '' else ' %s' % address['법정리']
            old = "%s %s %s%s %s" % (address['시도'], address['시군구'], address['읍면동'], bjr_nm, address['번'])
            if address['지'] != '0': old = "%s-%s" % (old, address['지'])

            self.get_address = GetAddress(0, old, self.address['도로명주소'])
            self.get_address.threadEvent.doneSignal.connect(self.input_address_edit)
            self.get_address.start()

    # UI 세팅
    def _init_ui(self):
        self.msg = BlackBoxMsg.BoxMessage(self)
        self.loading = LoadingBox.LoadingBox(self)
        self.loading.resize_loading()
        self._init_shadow()

        self.btn_search.setIcon(QIcon('../resources/img/search_icon.png'))
        self.btn_search.setIconSize(QSize(25, 25))
        self.list_frame.hide()

        self.show()

    # 시그널 세팅
    def _init_interaction(self):
        self.edt_address.mousePressEvent = self.clicked_address_edit
        self.edt_address.returnPressed.connect(self.clicked_address_edit)
        self.btn_search.clicked.connect(self.clicked_address_edit)
        self.btn_issuance.clicked.connect(self.search_register)

        self.cbx_buildings.activated.connect(self.select_building)
        self.cbx_rooms.activated.connect(self.select_room)
        self.list_item.itemDoubleClicked.connect(self.clicked_address_list)

    # UI 그림자 설정
    def _init_shadow(self):
        for child in [self.address_frame, self.type_frame, self.list_frame]:
            shadow = QGraphicsDropShadowEffect(self)
            shadow.setBlurRadius(15)
            shadow.setXOffset(1)
            shadow.setYOffset(1)
            shadow.setColor(QColor(0, 0, 0, 35))
            child.setGraphicsEffect(shadow)

    # 주소 검색
    def clicked_address_edit(self, e=None):
        address = self.edt_address.text()
        dialog = GetAddressLite(address)
        dialog.exec()

        if dialog.result is None: return
        if len(dialog.result) != 0:

            self.setFixedHeight(381)
            self.setMinimumHeight(381)
            self.setMaximumHeight(381)
            self.list_frame.hide()
            self.btn_issuance.show()

            self.existing = None
            self.address = address = dialog.result

            bjr_nm = '' if address['법정리'] == '' else ' %s' % address['법정리']
            old = "%s %s %s%s %s" % (address['시도'], address['시군구'], address['읍면동'], bjr_nm, address['번'])
            if address['지'] != '0': old = "%s-%s" % (old, address['지'])

            self.edt_address.clearFocus()

            self.get_address = GetAddress(0, old, self.address['도로명주소'])
            self.get_address.threadEvent.doneSignal.connect(self.input_address_edit)
            self.get_address.start()

    # 주소 정보 입력
    def input_address_edit(self, data):
        address = self.address
        if not data: self.msg.show_msg(2000, 'center', '검색 결과 없음')

        old = "%s %s %s %s" % (address['시도'], address['시군구'], address['읍면동'], address['번'])
        if address['지'] != '0': old = "%s-%s" % (old, address['지'])
        self.select_address = {'주소': old, '도로명주소': address['도로명주소'], '타입': ''}
        self.edt_address.setText(old)

        self.get_titles = GetAddress(1, data['PK'])
        self.get_titles.threadEvent.doneSignal.connect(self.add_building_list)
        self.get_titles.start()

    # 동 리스트 추가
    def add_building_list(self, data):
        self.cbx_buildings.clear()
        self.building = data

        if len(data) > 0:

            # 동 콤보박스 아이템 추가
            for i in data:
                if self.address['건물명칭'] != '': item = '%s (%s)' % (i['동명칭'], self.address['건물명칭'])
                else: item = i['동명칭']
                self.cbx_buildings.addItem(item)

            self.cbx_rooms.clear()
            self.cbx_rooms.addItem('( 상세주소 / 호 )')
            self.cbx_rooms.setEnabled(True)

            self.rbtn_set.setChecked(True)
            self.rbtn_set.setEnabled(True)
            self.rbtn_building.setEnabled(False)

            self.cbx_buildings.setEnabled(True)

            if len(data) == 1:
                self.cbx_buildings.setCurrentIndex(0)
                self.cbx_buildings.setEnabled(False)
                self.select_building()
                return

            # 기존 데이터가 있을 경우
            if self.existing:
                existing_dong_nm = self.existing['동명칭'].rstrip('동')
                for n, i in enumerate(data):
                    if existing_dong_nm in i['동명칭']:
                        self.cbx_buildings.setCurrentIndex(n)
                        self.select_building()
                        return

            self.cbx_buildings.showPopup()

        else:
            self.cbx_buildings.clear()
            self.cbx_buildings.addItem('-- 항목 없음 --')
            self.cbx_buildings.setEnabled(False)

            self.cbx_rooms.clear()
            self.cbx_rooms.addItem('-- 항목 없음 --')
            self.cbx_rooms.setEnabled(False)

            self.rbtn_set.setEnabled(False)
            self.rbtn_building.setEnabled(True)
            self.rbtn_building.setChecked(True)

    # 동 선택
    def select_building(self):
        dong = self.building[self.cbx_buildings.currentIndex()]
        self.select_address['동명칭'] = dong['동명칭']

        self.get_expos = GetAddress(2, dong['PK'])
        self.get_expos.threadEvent.doneSignal.connect(self.add_room_list)
        self.get_expos.start()

    # 동 선택
    def add_room_list(self, data):
        self.expos = data
        self.cbx_rooms.clear()
        self.cbx_rooms.setEnabled(True)

        for i in range(len(data)):
            item = '%s호' % data.loc[i]['호명칭']
            self.cbx_rooms.addItem(item)

        if self.existing:
            existing_ho_nm = self.existing['호명칭'].rstrip('호')
            for n, i in enumerate(data):
                if existing_ho_nm in i['호명칭']:
                    self.cbx_rooms.setCurrentIndex(n)
                    self.select_room()
                    return

        self.cbx_rooms.showPopup()

    # 호 선택
    def select_room(self):
        self.select_address['호명칭'] = self.expos.loc[self.cbx_rooms.currentIndex()]['호명칭']
        self.select_address['타입'] = '집합'

        self.rbtn_set.setChecked(True)
        print('값:', self.select_address)

    def search_register(self, retry=False):
        flag = self.cbx_flag.currentIndex()

        if self.rbtn_set.isChecked(): kind = 1
        elif self.rbtn_building.isChecked(): kind = 2
        elif self.rbtn_land.isChecked(): kind = 3
        else: return

        self.loading.show_loading()
        address = self.select_address['도로명주소']

        if self.select_address['타입'] == '집합':
            if '호명칭' not in self.select_address.keys(): self.select_room()
            if not retry:
                if self.select_address['동명칭'] != '':
                    dong = self.select_address['동명칭']
                    address = f'{address} {dong}'
            ho = self.select_address['호명칭']
            address = f'{address} {ho}'

        self.search_thread = SearchRegister(self.api_data, address, flag, kind)
        self.search_thread.threadEvent.doneSignal.connect(self.issuance_response)
        self.search_thread.threadEvent.returnSignal.connect(self.search_register)
        self.search_thread.start()

    def issuance_response(self, data):
        self.loading.hide_loading()
        if not data: return

        if data['TotalCount'] == 0:
            self.msg.show_msg(2000, 'center', '검색 결과 없음')

        elif data['TotalCount'] == 1:
            result = data['ResultList'][0]
            result['aesKey'] = data['aesKey']
            result['headers'] = data['headers']
            self.request_binary(result)

        elif data['TotalCount'] > 1:
            result_list = list(data['ResultList'])
            if self.address['지'] != '':
                check_address = '%s %s-%s' % (self.address['읍면동'], self.address['번'], self.address['지'])
            else: check_address = '%s %s' % (self.address['읍면동'], self.address['번'])

            result = None
            for n, i in enumerate(result_list):
                if check_address in i['BudongsanSojaejibeon']:
                    result = result_list[n]

            if result:
                result['aesKey'] = data['aesKey']
                result['headers'] = data['headers']
                self.request_binary(result)

            else:
                self.setFixedHeight(562)
                self.setMinimumHeight(562)
                self.setMaximumHeight(562)
                self.list_frame.show()
                self.btn_issuance.hide()

                self.bld_data = data

                for i in list(data['ResultList']):
                    print(type(i), i)
                    custom_item = AddressListItem(i)
                    item = QListWidgetItem(self.list_item)
                    item.setSizeHint(custom_item.sizeHint())
                    self.list_item.setItemWidget(item, custom_item)

    def clicked_address_list(self):
        idx = self.list_item.currentRow()
        selected_item = dict(list(self.bld_data['ResultList'])[idx])
        selected_item['aesKey'] = self.bld_data['aesKey']
        selected_item['headers'] = self.bld_data['headers']
        self.request_binary(selected_item)

    def request_binary(self, data):
        self.loading.resize_loading()
        self.loading.show_loading()

        self.issuance_thread = IssuasnceRegistered(self.api_data, self.user, data)
        self.issuance_thread.threadEvent.issuasnceDone.connect(self.saved_pdf)
        self.issuance_thread.start()

    # 요청 된 바이너리 PDF 파일로 저장
    def saved_pdf(self, data):
        self.loading.hide_loading()

        address = self.select_address['주소']
        if self.select_address['타입'] == '집합':
            dong = self.select_address['동명칭']
            if dong != '': address = f'{address} {dong}'
            ho = self.select_address['호명칭']
            address = f'{address} {ho}'

        file_name = f'등기) {address}'
        save_path = QFileDialog.getSaveFileName(self, "등기부등본 PDF 저장", f"~/{file_name}.pdf", "PDF 문서 (*.pdf)")

        if save_path[0]:
            with open(save_path[0], "wb") as f:
                f.write(base64.b64decode(data.json()['Message']))

        self.close()


class ThreadSignal(QObject):
    doneSignal = Signal(object)
    returnSignal = Signal(bool)
    issuasnceDone = Signal(bytes)


class SearchRegister(QThread):
    def __init__(self, api_data, address, flag, kind):
        super(SearchRegister, self).__init__()
        self.threadEvent = ThreadSignal()

        self.headers = None
        self.API_HOST, self.API_KEY = api_data['HOST'], api_data['KEY']
        self.address, self.flag, self.kind = address, flag, kind

    def run(self):
        print('## 등기소 주소 검색 ##')
        aesKey = os.urandom(16)

        rsaPublicKey = getPublicKey(self.API_HOST, self.API_KEY)
        aesCipherKey = base64.b64encode(rsaEncrypt(rsaPublicKey, aesKey))

        self.headers = {"Content-Type": "application/json",
                        "API-KEY": self.API_KEY,
                        "ENC-KEY": aesCipherKey}

        # 등기 고유번호 조회
        url = self.API_HOST + "api/v1.0/iros/risuconfirmsimplec"
        datas = {'Address': self.address,    # 주소
                 'Sangtae': self.flag,       # 현행:0 / 폐쇄:1 / 현행폐쇄:2
                 'KindClsFlag': self.kind}   # 전체:0 / 집합건물:1 / 건물:2 / 토지:3

        response = requests.post(url, headers=self.headers, json=datas)
        result = response.json()

        if result['Status'] == 'Error':
            print(result['Message'])
            self.threadEvent.doneSignal.emit(None)
            return

        # 검색 결과가 없을 시 재시도
        if result['TotalCount'] == 0:
            self.threadEvent.returnSignal.emit(True)

        else:
            result['aesKey'] = aesKey
            result['headers'] = self.headers
            self.threadEvent.doneSignal.emit(result)


class IssuasnceRegistered(QThread):
    def __init__(self, api_data, user, data):
        super(IssuasnceRegistered, self).__init__()
        self.threadEvent = ThreadSignal()
        self.headers = None
        self.API_HOST, self.API_KEY = api_data['HOST'], api_data['KEY']
        self.user, self.data, self.aes_key, self.headers = user, data, data['aesKey'], data['headers']

    def run(self):
        print('## 등기 발급 ##')
        # 등기 고유번호 조회가 됐을 경우
        aesIv = ('\x00' * 16).encode('utf-8')
        unique_no = self.data['UniqueNo']

        # 등기부등본 데이터 요청
        url = self.API_HOST + "api/v1.0/iros/risuretrieve"
        params = {"IrosID": aesEncrypt(self.aes_key, aesIv, self.user['user_id']),
                  "IrosPwd": aesEncrypt(self.aes_key, aesIv, self.user['user_pw']),
                  "EmoneyNo1": aesEncrypt(self.aes_key, aesIv, self.user['num_1']),
                  "EmoneyNo2": aesEncrypt(self.aes_key, aesIv, self.user['num_2']),
                  "EmoneyPwd": aesEncrypt(self.aes_key, aesIv, self.user['num_pw']),
                  "UniqueNo": unique_no,
                  "ValidYn": "Y"}
        response = requests.post(url, headers=self.headers, json=params)
        result = response.json()    # 등기부등본 데이터

        # 등기 데이터가 정상 조회 되었을 경우
        if result['TransactionKey'] is not None:
            # PDF 바이너리 요청
            transaction_key = result['TransactionKey']

            url = self.API_HOST + "api/v1.0/iros/getpdffile"
            params = {"TransactionKey": transaction_key, "IsSummary": "Y"}
            response = requests.post(url, headers=self.headers, json=params)
            self.threadEvent.issuasnceDone.emit(response)


# 표제부, 일반건축물 조회
class GetAddress(QThread):
    def __init__(self, kind, *agrs):
        super().__init__()
        self.threadEvent = ThreadSignal()

        self.s = requests.Session()
        self.headers = {
            "Referer": "https://cloud.eais.go.kr/moct/bci/aaa02/BCIAAA02L01",
            "Content-Type": "application/json;charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.151 Whale/3.14.134.62 Safari/537.36"
        }

        self.kind = kind
        self.agrs = agrs

    def run(self):
        if self.kind == 0:
            old, new = self.agrs
            result = self.get_address(old, new)
            self.threadEvent.doneSignal.emit(result)

        elif self.kind == 1:
            pk = self.agrs[0]
            result = self.get_title(pk)
            self.threadEvent.doneSignal.emit(result)

        elif self.kind == 2:
            pk = self.agrs[0]
            result = self.get_expos(pk)
            self.threadEvent.doneSignal.emit(result)

    def get_address(self, old, new):
        url = 'https://cloud.eais.go.kr/bldrgstmst/_search'
        datas = {"query": {"multi_match": {"query": new, "type": "cross_fields", "operator": "and", "fields": ["jibunAddr", "roadAddr^3"], "tie_breaker": 0.3}}, "size": 20}
        response = self.s.post(url, headers=self.headers, json=datas)
        result = json.loads(response.text)['hits']['hits']

        address = None
        for i in result:
            info = i['_source']
            if old in info['jibunAddr']:
                kind = '일반' if info['regstrKindCd'] == '2' else '집합'
                address = {'주소': info['jibunAddr'], '도로명주소': info['roadAddr'], 'PK': info['mgmUpperBldrgstPk'], '타입': kind}
                break

        self.s.close()
        return address

    def get_title(self, pk):
        url = 'https://cloud.eais.go.kr/bldrgsttitle/_search'
        datas = {"sort": [{"dongNm": "asc"}], "query": {"bool": {"filter": [{"term": {"mgmUpperBldrgstPk": pk}}]}}, "size": 100}
        response = self.s.post(url, headers=self.headers, json=datas)
        result = json.loads(response.text)['hits']['hits']

        titles = []
        for i in result:
            info = i['_source']
            item = {'동명칭': info['dongNm'], 'PK': i['_id']}
            titles.append(item)

        return titles

    def get_expos(self, pk):
        url = 'https://cloud.eais.go.kr/bldrgstexpos/_search'
        datas = {"sort": [{"hoNm": "asc"}], "query": {"bool": {"filter": [{"term": {"mgmUpperBldrgstPk": pk}}]}}, "size": 200}
        response = self.s.post(url, headers=self.headers, json=datas)
        result = json.loads(response.text)['hits']['hits']

        # 아이템 데이터프레임에 담기
        titles = pd.DataFrame(columns=['호명칭', 'PK'])
        for n, i in enumerate(result):
            info = i['_source']
            item = [info['hoNm'], i['_id']]
            titles.loc[n] = item

        # 호명칭 int 변환
        titles['호명칭'] = titles['호명칭'].str.rstrip('호')
        try: titles['호명칭'] = pd.to_numeric(titles['호명칭'])
        except ValueError: pass

        # 호명칭 기준 정렬
        sort_data = titles.sort_values(by=["호명칭"], ascending=[True])
        sort_data.reset_index(drop=True, inplace=True)
        sort_data['호명칭'] = sort_data['호명칭'].apply(str)

        return sort_data


class AddressListItem(QWidget):
    def __init__(self, data):
        super(AddressListItem, self).__init__()

        self.bld_type = QLabel(self)
        self.bld_type.setStyleSheet("""QLabel { font: 15px "웰컴체 Regular"; color: rgb(128,128,255); padding-top: 2px;}""")
        self.bld_type.setText(data['Gubun'])

        self.unique_no_hint = QLabel(self)
        self.unique_no_hint.setText('고유번호')
        self.unique_no_hint.setMaximumSize(55, 20)
        self.unique_no_hint.setStyleSheet("""QLabel { font: 14px "웰컴체 Regular"; color: rgb(65,65,65); padding-top: 2px;}""")

        unique_no = '%s-%s-%s' % (data['UniqueNo'][:4], data['UniqueNo'][4:8], data['UniqueNo'][8:])
        self.unique_no = QLabel(self)
        self.unique_no.setMaximumSize(150, 20)
        self.unique_no.setText(unique_no)
        self.unique_no.setStyleSheet("""QLabel { font: 14px "웰컴체 Regular"; color: rgb(115,115,115); padding-top: 2px;}""")

        self.address = QLabel(self)
        self.address.setText(data['BudongsanSojaejibeon'])
        self.address.setStyleSheet("""QLabel { font: 14px "웰컴체 Regular"; color: rgb(95,95,95); padding-left: 2px; padding-top: 2px;}""")
        self.address.setMaximumSize(430, 38)
        self.address.setWordWrap(True)

        self.set_ui()

    def set_ui(self):
        grid_box = QGridLayout()
        grid_box.addWidget(self.bld_type, 0, 0)
        grid_box.addWidget(self.unique_no_hint, 0, 1)
        grid_box.addWidget(self.unique_no, 0, 2)
        grid_box.addWidget(self.address, 1, 0, 2, 0)
        # grid_box.addWidget(self.address, 0, 2, 1, 2)

        self.setLayout(grid_box)


# AES 암호화 함수
def aesEncrypt(key, iv, plainText):
    def pad(text):
        text_length = len(text)
        amount_to_pad = AES.block_size - (text_length % AES.block_size)

        if amount_to_pad == 0:
            amount_to_pad = AES.block_size

        aes_pad = chr(amount_to_pad)

        try:
            result = text + str(aes_pad * amount_to_pad).encode('utf-8')
        except Exception as e:
            result = text + str(aes_pad * amount_to_pad)

        return result

    if type(plainText) == str:
        plainText = plainText.encode('utf-8')

    plainText = pad(plainText)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    if type(plainText) == bytes:
        return base64.b64encode(cipher.encrypt(plainText)).decode('utf-8')
    else:
        return base64.b64encode(cipher.encrypt(plainText.encode('utf-8'))).decode('utf-8')


# RSA 암호화 함수(RSA 공개키로 AES키 암호화)
def rsaEncrypt(publicKey, aesKey):
    rsa = RSA.importKey(base64.b64decode(publicKey))
    cipher = PKCS1_v1_5.new(rsa.publickey())
    aesCipherKey = cipher.encrypt(aesKey)
    return aesCipherKey


# RSA 공개키(Public Key) 조회 함수
def getPublicKey(apiHost, apiKey):
    headers = {'Content-Type': 'application/json'}
    response = requests.get(apiHost + "/api/Auth/GetPublicKey?APIkey=" + apiKey, headers=headers)
    return response.json()['PublicKey']


# 예외 오류 처리
def my_exception_hook(exctype, value, traceback):
    sys.excepthook(exctype, value, traceback)


sys._excepthook = sys.excepthook
sys.excepthook = my_exception_hook


# app = QApplication()
# window = IssuanceRegister()
# app.exec()
