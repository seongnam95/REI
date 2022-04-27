import os
import sys
import base64
import requests
import json
import rei_bot.issuance_registered as ir

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5, AES

from PySide6.QtGui import QMovie, QColor, QIcon
from PySide6.QtCore import QRect, QThread, QObject, Signal, QByteArray, QSize
from PySide6.QtWidgets import QDialog, QApplication, QGraphicsDropShadowEffect, QWidget, QFileDialog

from interface.sub_interface import find_address_lite
from ui.dialog.ui_register import Ui_Register


class IssuanceRegister(QDialog, Ui_Register):
    def __init__(self, data=None):
        super().__init__()
        self.setupUi(self)
        self.show()

        self._init_ui()
        self._init_interaction()

        self.address, self.info = None, {}
        self.existing_pk, self.title_pk, self.expos_pk = None, None, None
        self.address, self.flag, self.kind, self.ty = None, None, None, None

        self.s = requests.Session()
        self.headers = {
            "Referer": "https://cloud.eais.go.kr/moct/bci/aaa02/BCIAAA02L01",
            "Content-Type": "application/json;charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
        }

        self.api_data = {'HOST': 'https://api.tilko.net/',
                         'KEY': '6062d22d48734cd3af82837f696730fb'}
        self.user = {'user_id': 'mogsin21', 'user_pw': 'happy2588@',
                     'num_1': 'P3372711', 'num_2': '3234', 'num_pw': 'kim2588'}

    # UI 세팅
    def _init_ui(self):
        self._init_shadow()
        self.btn_search.setIcon(QIcon('../../data/img/button/search_icon.png'))
        self.btn_search.setIconSize(QSize(25, 25))

    # 시그널 세팅
    def _init_interaction(self):
        self.edt_address.mousePressEvent = self.clicked_address_edit
        self.edt_address.returnPressed.connect(self.clicked_address_edit)
        self.btn_search.clicked.connect(self.clicked_address_edit)

        # self.cbx_buildings.activated.connect(self.add_room_list)
        # self.cbx_rooms.activated.connect(self.select_room)

    # UI 그림자 설정
    def _init_shadow(self):
        for child in [self.address_frame, self.type_frame]:
            shadow = QGraphicsDropShadowEffect(self)
            shadow.setBlurRadius(15)
            shadow.setXOffset(1)
            shadow.setYOffset(1)
            shadow.setColor(QColor(0, 0, 0, 35))
            child.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(40)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        shadow.setColor(QColor(0, 0, 0, 60))
        self.btn_issuance.setGraphicsEffect(shadow)

    # 주소 검색
    def clicked_address_edit(self, e=None):
        address = self.edt_address.text()
        dialog = find_address_lite.FindAddressLite(address)
        dialog.exec()

        if dialog.result is None: return
        if len(dialog.result) != 0:
            self.address = dialog.result
            print(self.address)
            self.input_address_edit()
            self.edt_address.clearFocus()

    # 주소 정보 입력
    def input_address_edit(self):
        address = self.address

        old = "%s %s %s %s" % (address['시도'], address['시군구'], address['읍면동'], address['번'])
        if address['지'] != '0': old = "%s-%s" % (old, address['지'])

        pk = self.get_address(old, address['도로명주소'])
        if pk:
            self.edt_address.setText(old)
            self.info['건물'] = pk

            self.add_building_list()

        else: print('검색 결과 없음')

    # 동 리스트 추가
    def add_building_list(self):
        self.title_pk = self.get_title(self.info['건물']['ID'])

        # 총괄표제부 표시 여부
        if '-' not in self.info['건물']['ID']: self.rbtn_total.setEnabled(False)
        else: self.rbtn_total.setEnabled(True)

        # 일반 건축물일 경우
        if self.title_pk.empty:
            self.info['타입'] = '일반'

            self.cbx_buildings.clear()
            self.cbx_buildings.addItem('-- 항목없음 --')
            self.cbx_buildings.setEnabled(False)

            self.cbx_rooms.clear()
            self.cbx_rooms.addItem('-- 항목없음 --')
            self.cbx_rooms.setEnabled(False)

            self.rbtn_room.setEnabled(False)
            self.rbtn_building.setChecked(True)

            self.btn_issuance.setEnabled(True)

        # 집합 건축물일 경우
        else:
            self.info['타입'] = '집합'

            self.cbx_buildings.clear()
            self.cbx_rooms.clear()
            self.cbx_rooms.addItem('( 상세주소 / 호)')

            self.cbx_buildings.setEnabled(True)
            self.cbx_rooms.setEnabled(True)
            self.rbtn_room.setEnabled(True)
            self.rbtn_room.setChecked(True)

            for i in range(len(self.title_pk)):
                row = self.title_pk.loc[i]
                item = '%s (%s)' % (row['동명칭'], self.address['건물명칭']) if self.address['건물명칭'] else row['동명칭']
                self.cbx_buildings.addItem(item)

            if len(self.title_pk) == 1:
                self.add_room_list()
                return

            if self.existing_pk:
                idx = self.title_pk.index[(self.title_pk['PK'] == self.existing_pk['동_PK'])]
                self.cbx_buildings.setCurrentIndex(idx[0])
                self.add_room_list()
                return

            self.cbx_buildings.showPopup()

    def clicked_save_btn(self):
        flag = self.cbx_flag.currentIndex()

        if self.rbtn_set.isChecked(): kind = 1
        elif self.rbtn_building.isChecked(): kind = 2
        elif self.rbtn_land.isChecked(): kind = 3
        else: kind = 2

        self.loading(True)

        self.issuance_thread = IssuanceRegistered(self.api_data, self.user, self.address, flag, kind)
        self.issuance_thread.threadEvent.workerThreadDone.connect(self.saved_pdf)
        self.issuance_thread.start()

    # 요청 된 바이너리 PDF 파일로 저장
    def saved_pdf(self, data):
        file_name = self.address.replace(' ', '_')
        save_path = QFileDialog.getSaveFileName(self, "등기부등본 PDF 저장", f"~/{file_name}.pdf", "PDF 문서 (*.pdf)")

        if save_path:
            with open(save_path[0], "wb") as f:
                f.write(base64.b64decode(data.json()['Message']))
        self.loading(False)

    def loading(self, whether):
        if whether:
            self.rbtn_set.setEnabled(False)
            self.rbtn_building.setEnabled(False)
            self.rbtn_land.setEnabled(False)
            self.cbx_flag.setEnabled(False)

            self.loading_icon.show()
            self.btn_save.setText('')
            self.btn_save.setDisabled(True)

        else:
            self.rbtn_set.setEnabled(True)
            self.rbtn_building.setEnabled(True)
            self.rbtn_land.setEnabled(True)
            self.cbx_flag.setEnabled(True)

            self.loading_icon.hide()
            self.btn_save.setText('PDF 저장')
            self.btn_save.setDisabled(False)

    def get_address(self, old, new):
        datas = {"query": {"multi_match": {"query": new,
                                           "type": "cross_fields",
                                           "operator": "and",
                                           "fields": ["jibunAddr", "roadAddr^3"],
                                           "tie_breaker": 0.3}}, "size": 20}

        res = self.s.post('https://cloud.eais.go.kr/bldrgstmst/_search', headers=self.headers, json=datas)
        json_result = json.loads(res.text)['hits']

        for n, i in enumerate(json_result['hits']):
            res_old = i['_source']['jibunAddr']
            if old in res_old:
                info = i['_source']
                result = {'주소': info['jibunAddr'], '도로명주소': info['roadAddr'], 'ID': info['mgmUpperBldrgstPk'],
                          'PK': i['_id']}
                return result

    def get_title(self, pk):
        datas = {"sort": [{"dongNm": "asc"}], "query": {"bool": {"filter": [{"term": {"mgmUpperBldrgstPk": pk}}]}},
                 "size": 100}
        res = self.s.post('https://cloud.eais.go.kr/bldrgsttitle/_search', headers=self.headers, json=datas)
        json_result = json.loads(res.text)['hits']

        result = pd.DataFrame(columns=['동명칭', 'ID', 'PK'])

        for n, i in enumerate(json_result['hits']):
            result.loc[n] = {'동명칭': i['_source']['dongNm'], 'ID': i['_source']['mgmUpperBldrgstPk'], 'PK': i['_id']}

        result = result.sort_values(by=['동명칭'], axis=0)
        result.reset_index(drop=True, inplace=True)

        return result


    def get_expos(self, pk):
        datas = {"sort": [{"hoNm": "asc"}], "query": {"bool": {"filter": [{"term": {"mgmUpperBldrgstPk": pk}}]}},
                 "size": 200}
        res = self.s.post('https://cloud.eais.go.kr/bldrgstexpos/_search', headers=self.headers, json=datas)
        json_result = json.loads(res.text)['hits']

        result = pd.DataFrame(columns=['동명칭', '호명칭', 'PK'])

        for n, i in enumerate(json_result['hits']):
            info = i['_source']
            result.loc[n] = {'동명칭': info['dongNm'], '호명칭': info['hoNm'], 'PK': i['_id']}

        try:
            result['호명칭'] = pd.to_numeric(result['호명칭'])
        except:
            pass

        result = result.sort_values(by=['호명칭'], axis=0)
        result.reset_index(drop=True, inplace=True)

        return result


class ThreadSignal(QObject):
    workerThreadDone = Signal(bytes)
    workingMsg = Signal(str)


class IssuanceRegistered(QThread):
    def __init__(self, api_data, user, address, flag, kind):
        super(IssuanceRegistered, self).__init__()
        self.threadEvent = ThreadSignal()

        self.headers = None
        self.API_HOST, self.API_KEY = api_data['HOST'], api_data['KEY']
        self.address, self.user, self.flag, self.kind = address, user, flag, kind

    def run(self):
        aesKey = os.urandom(16)
        aesIv = ('\x00' * 16).encode('utf-8')

        rsaPublicKey = getPublicKey(self.API_HOST, self.API_KEY)
        aesCipherKey = base64.b64encode(rsaEncrypt(rsaPublicKey, aesKey))

        self.headers = {"Content-Type": "application/json",
                        "API-KEY": self.API_KEY,
                        "ENC-KEY": aesCipherKey}

        datas = {'Address': self.address,    # 주소
                 'Sangtae': self.flag,       # 현행:0 / 폐쇄:1 / 현행폐쇄:2
                 'KindClsFlag': self.kind}   # 전체:0 / 집합건물:1 / 건물:2 / 토지:3
        print(self.address, self.flag, self.kind)
        # 등기 고유번호 조회
        url = {'조회': self.API_HOST + "api/v1.0/iros/risuconfirmsimplec",
               '발급': self.API_HOST + "api/v1.0/iros/risuretrieve"}

        response = requests.post(url['조회'], headers=self.headers, json=datas)
        result = response.json()
        print(1, result)

        # 등기 고유번호 조회가 됐을 경우
        if result['Message'] == '성공':
            unique_no = result['ResultList'][0]['UniqueNo']

            # 등기부등본 데이터 요청
            params = {"IrosID": aesEncrypt(aesKey, aesIv, self.user['user_id']),
                      "IrosPwd": aesEncrypt(aesKey, aesIv, self.user['user_pw']),
                      "EmoneyNo1": aesEncrypt(aesKey, aesIv, self.user['num_1']),
                      "EmoneyNo2": aesEncrypt(aesKey, aesIv, self.user['num_2']),
                      "EmoneyPwd": aesEncrypt(aesKey, aesIv, self.user['num_pw']),
                      "UniqueNo": unique_no,
                      "ValidYn": "Y"}
            response = requests.post(url['발급'], headers=self.headers, json=params)
            result = response.json()    # 등기부등본 데이터
            print(2, result)

            # 등기 데이터가 정상 조회 되었을 경우
            if result['TransactionKey'] is not None:

                # PDF 바이너리 요청
                transaction_key = result['TransactionKey']

                url = self.API_HOST + "api/v1.0/iros/getpdffile"
                params = {"TransactionKey": transaction_key, "IsSummary": "Y"}
                response = requests.post(url, headers=self.headers, json=params)
                print('PDF 바이너리 요청')
                self.threadEvent.workerThreadDone.emit(response)

            else:
                self.threadEvent.workingMsg.emit(result['Message'])
                return
        else:
            self.threadEvent.workingMsg.emit(result['Message'])
            return


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


app = QApplication()
window = IssuanceRegister()
app.exec()
