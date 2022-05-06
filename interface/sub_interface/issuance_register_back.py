import os
import sys
import base64
import requests
import json
import pandas as pd
import rei_bot.issuance_registered as ir
import module.open_api_pars as pars

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5, AES

from PySide6.QtGui import QMovie, QColor, QIcon
from PySide6.QtCore import QRect, QThread, QObject, Signal, QByteArray, QSize
from PySide6.QtWidgets import QDialog, QApplication, QGraphicsDropShadowEffect, QWidget, QFileDialog, \
    QLabel, QPushButton, QGridLayout, QListWidgetItem

from interface.sub_interface import find_address_lite
from ui.dialog.ui_register import Ui_Register
from ui.custom.LoadingBox import LoadingBox


class IssuanceRegister(QDialog, Ui_Register):
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
            self.input_address_edit()

    # UI 세팅
    def _init_ui(self):
        self.loading = LoadingBox(self)
        self.loading.resize_loading()
        self._init_shadow()

        self.btn_search.setIcon(QIcon('../../data/img/button/search_icon.png'))
        self.btn_search.setIconSize(QSize(25, 25))
        self.list_frame.hide()

        self.show()

    # 시그널 세팅
    def _init_interaction(self):
        self.edt_address.mousePressEvent = self.clicked_address_edit
        self.edt_address.returnPressed.connect(self.clicked_address_edit)
        self.btn_search.clicked.connect(self.clicked_address_edit)
        self.btn_issuance.clicked.connect(self.search_register)

        self.cbx_buildings.activated.connect(self.add_room_list)
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
        dialog = find_address_lite.FindAddressLite(address)
        dialog.exec()

        if dialog.result is None: return
        if len(dialog.result) != 0:

            self.setFixedHeight(381)
            self.setMinimumHeight(381)
            self.setMaximumHeight(381)
            self.list_frame.hide()
            self.btn_issuance.show()

            self.existing = None
            self.address = dialog.result

            self.input_address_edit()
            self.edt_address.clearFocus()

    # 주소 정보 입력
    def input_address_edit(self):
        address = self.address

        old = "%s %s %s %s" % (address['시도'], address['시군구'], address['읍면동'], address['번'])
        if address['지'] != '0': old = "%s-%s" % (old, address['지'])
        self.select_address = {'주소': old, '도로명주소': address['도로명주소']}
        self.edt_address.setText(old)

        self.add_building_list()

    # 동 리스트 추가
    def add_building_list(self):

        # 일반 건축물일 경우
        if self.address['공동주택여부'] == '0':
            self.select_address['타입'] = '일반'
            self.cbx_buildings.clear()
            self.cbx_buildings.addItem('-- 항목없음 --')
            self.cbx_buildings.setEnabled(False)

            self.cbx_rooms.clear()
            self.cbx_rooms.addItem('-- 항목없음 --')
            self.cbx_rooms.setEnabled(False)

            self.rbtn_set.setEnabled(False)

            self.rbtn_building.setEnabled(True)
            self.rbtn_building.setChecked(True)

        # 집합 건축물일 경우
        else:
            self.select_address['타입'] = '집합'
            self.cbx_buildings.clear()
            self.cbx_rooms.clear()
            self.cbx_rooms.addItem('( 상세주소 / 호)')

            self.cbx_buildings.setEnabled(True)
            self.cbx_rooms.setEnabled(True)

            self.rbtn_set.setEnabled(True)
            self.rbtn_building.setEnabled(False)
            self.rbtn_set.setChecked(True)

            result = pars.OpenApiRequest.get_address_detail(self.DETAIL_ADDRESS_API_KEY, self.address, '동')
            dong_list = ['동명칭 없음' if i == '' else i for i in list(result['동명칭'])]
            self.building = dong_list

            # 동이 여러개일 경우
            if dong_list:
                for i in dong_list:
                    if self.address['건물명칭'] != '': item = '%s (%s)' % (i, self.address['건물명칭'])
                    else: item = i
                    self.cbx_buildings.addItem(item)

                if len(dong_list) == 1:
                    self.cbx_buildings.setCurrentIndex(0)
                    self.cbx_buildings.setEnabled(False)
                    self.add_room_list()
                    return

                else:
                    if self.existing:
                        existing_dong_nm = self.existing['동명칭'].rstrip('동')
                        for n, i in enumerate(dong_list):
                            if existing_dong_nm in i:
                                self.cbx_buildings.setCurrentIndex(n)
                                self.add_room_list()
                                return

                self.cbx_buildings.setEnabled(True)
                self.cbx_buildings.showPopup()

            # 동이 없을 경우
            else:
                if self.address['건물명칭'] != '': self.cbx_buildings.addItem(self.address['건물명칭'])
                else: self.cbx_buildings.addItem('건물 명칭 없음')
                self.cbx_buildings.setCurrentIndex(0)

                self.cbx_buildings.setEnabled(False)
                self.add_room_list()

    # 동 선택
    def add_room_list(self):
        if self.building: dong_nm = self.building[self.cbx_buildings.currentIndex()]
        else: dong_nm = ''
        dong_nm = '' if dong_nm == '동명칭 없음' else dong_nm

        self.select_address['동명칭'] = dong_nm

        self.cbx_rooms.clear()
        result = pars.OpenApiRequest.get_address_detail(self.DETAIL_ADDRESS_API_KEY, self.address, '호', dong_nm)
        self.expos = result

        ho_list = []
        for i in range(len(result)):
            ho_nm = result.loc[i]['호명칭']
            item = '%s | %s' % (result.loc[i]['층번호'], ho_nm)
            self.cbx_rooms.addItem(item)
            ho_list.append(ho_nm)

        if self.existing:
            existing_ho_nm = self.existing['호명칭'].rstrip('호')
            for n, i in enumerate(ho_list):
                if existing_ho_nm in i:
                    self.cbx_rooms.setCurrentIndex(n)
                    self.select_room()
                    return

        self.cbx_rooms.showPopup()

    # 호 선택
    def select_room(self):
        self.select_address['호명칭'] = self.expos.loc[self.cbx_rooms.currentIndex()]['호명칭']
        print('값:', self.select_address)

    def search_register(self, retry=False):
        flag = self.cbx_flag.currentIndex()

        if self.rbtn_set.isChecked(): kind = 1
        elif self.rbtn_building.isChecked(): kind = 2
        elif self.rbtn_land.isChecked(): kind = 3
        else: return

        self.loading.show_loading()
        address = self.select_address['주소']

        if self.select_address['타입'] == '집합':
            if '호명칭' not in self.select_address.keys(): self.select_room()
            if not retry:
                if self.select_address['동명칭'] != '':
                    dong = self.select_address['동명칭']
                    address = f'{address} {dong}'
            ho = self.select_address['호명칭']
            address = f'{address} {ho}'

        self.search_thread = SearchRegister(self.api_data, address, flag, kind)
        self.search_thread.threadEvent.searchDone.connect(self.issuance_response)
        self.search_thread.threadEvent.returnSignal.connect(self.search_register)
        self.search_thread.start()

    def issuance_response(self, data):
        self.loading.hide_loading()

        if data['TotalCount'] == 0:
            print('검색 결과 없음')

        if data['TotalCount'] == 1:
            result = data['ResultList'][0]
            result['aesKey'] = data['aesKey']
            result['headers'] = data['headers']
            self.request_binary(result)

        elif data['TotalCount'] > 1:
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
    searchDone = Signal(dict)
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

        # 검색 결과가 없을 시 재시도
        if result['TotalCount'] == 0: self.threadEvent.returnSignal.emit(True)
        else:
            result['aesKey'] = aesKey
            result['headers'] = self.headers
            self.threadEvent.searchDone.emit(result)


class IssuasnceRegistered(QThread):
    def __init__(self, api_data, user, data):
        super(IssuasnceRegistered, self).__init__()
        self.threadEvent = ThreadSignal()
        self.headers = None
        self.API_HOST, self.API_KEY = api_data['HOST'], api_data['KEY']
        self.user, self.data, self.aes_key, self.headers = user, data, data['aesKey'], data['headers']

    def run(self):
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

#
# app = QApplication()
# window = IssuanceRegister()
# app.exec()
