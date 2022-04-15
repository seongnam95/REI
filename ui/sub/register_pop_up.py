import os
import sys
import base64
import requests
import rei_bot.issuance_registered as ir

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5, AES
from PySide6.QtCore import QRect, QThread, QObject, Signal
from PySide6.QtWidgets import QComboBox, QFrame, QLabel, QPushButton, QRadioButton, QWidget, QFileDialog


class RegisterPopUp(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self._setup_ui()

        self.btn_save.clicked.connect(self.clicked_save_btn)
        self.btn_cancle.clicked.connect(self.hide_pop)

        self.api_data = {'HOST': 'https://api.tilko.net/',
                         'KEY': '6062d22d48734cd3af82837f696730fb'}
        self.user = {'user_id': 'mogsin21', 'user_pw': 'happy2588@',
                     'num_1': 'P3372711', 'num_2': '3234', 'num_pw': 'kim2588'}
        self.address, self.flag, self.kind = None, None, None

    def _setup_ui(self):
        self.resize(240, 180)
        self.setGeometry(QRect(0, 0, 240, 180))
        main_style = """
        QRadioButton {
            font: 14px "웰컴체 Regular";
            color: white;
        }
        QFrame {
            background: rgba(0,0,0,210);
            border-radius: 10px;
        }
        """
        self.setStyleSheet(main_style)

        self.lb_title = QLabel(self)
        self.lb_title.setGeometry(QRect(76, 11, 91, 20))
        self.lb_title.setText("등기부등본 발급")
        self.lb_title.setStyleSheet("""QLabel { font: 15px "웰컴체 Regular";
                                                color: white;
                                                background: rgba(0,0,0,0); } """)

        self.lb_name = QLabel(self)
        self.lb_name.setGeometry(QRect(20, 57, 71, 16))
        self.lb_name.setText("등기기록상태")
        self.lb_name.setStyleSheet("""QLabel { font: 14px "웰컴체 Regular";
                                               color: white;
                                               background: rgba(0,0,0,0); } """)

        cbx_style = """
        QComboBox {
            border: 1px solid gray;
            padding-top: 3px;
            padding-left: 5px;
            min-width: 6em;
            background: rgb(255, 255, 255);
            font: 14px "웰컴체 Regular";
            color: rgb(40, 40, 40);
        }

        QComboBox:focus {
            color: rgb(70, 70, 70);
        }

        QComboBox:hover {
            border: 1px solid #3498db;
        }

        QComboBox QAbstractItemView::item {
            min-height: 30px;
        }

        QComboBox::drop-down {
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 30px;

            border-left-width: 1px;
            border-left-style: solid;
            border-left-color: darkgray;
        }
        
        QFrame {
            background: white;
            border: 1px solid gray;
            border-radius: 0px;
        }
        """
        flag_items = ['현행', '폐쇄', '현행+폐쇄']
        self.cbx_flag = QComboBox(self)
        self.cbx_flag.addItems(flag_items)
        self.cbx_flag.setGeometry(QRect(100, 49, 121, 28))
        self.cbx_flag.setStyleSheet(cbx_style)

        self.rbtn_set = QRadioButton(self)
        self.rbtn_set.setGeometry(QRect(20, 90, 71, 16))
        self.rbtn_set.setText("집합건물")
        self.rbtn_set.setChecked(True)

        self.rbtn_building = QRadioButton(self)
        self.rbtn_building.setGeometry(QRect(105, 90, 51, 16))
        self.rbtn_building.setText("건 물")

        self.rbtn_land = QRadioButton(self)
        self.rbtn_land.setGeometry(QRect(170, 90, 51, 16))
        self.rbtn_land.setText("토 지")

        btn_style = """
        QPushButton {
            font: 15px "웰컴체 Bold";
            color: rgb(235,235,235);
            border-radius: 7px;
            padding-top: 3px;
            padding-left: 3px;
            background-color: rgb(77,161,192);
        }
        QPushButton:hover { background-color: rgb(97,181,212); }
        QPushButton:pressed { background-color: rgb(57,141,172); }
        """
        self.btn_save = QPushButton(self)
        self.btn_save.setGeometry(QRect(100, 133, 121, 35))
        self.btn_save.setStyleSheet(btn_style)
        self.btn_save.setText("PDF 저 장")

        btn_style = """
        QPushButton {
            font: 15px "웰컴체 Bold";
            color: rgb(235,235,235);
            border-radius: 7px;
            padding-top: 3px;
            padding-left: 3px;
            background-color: rgb(191,77,76);
        }
        QPushButton:hover { background-color: rgb(212,97,86); }
        QPushButton:pressed { background-color: rgb(171,57,56); } """
        self.btn_cancle = QPushButton(self)
        self.btn_cancle.setGeometry(QRect(20, 133, 71, 35))
        self.btn_cancle.setStyleSheet(btn_style)
        self.btn_cancle.setText("취 소")

        self.line_1 = QFrame(self)
        self.line_1.setGeometry(QRect(10, 35, 222, 1))
        self.line_1.setStyleSheet("""
        QFrame {
            background-color: rgba(255,255,255,90);
            color: rgba(255,255,255,90);
        }""")

        self.line_2 = QFrame(self)
        self.line_2.setGeometry(QRect(10, 120, 222, 1))
        self.line_2.setStyleSheet("""
        QFrame {
            background-color: rgba(255,255,255,90);
            color: rgba(255,255,255,90);
        }""")

        self.hide()

    def show_pop(self, address):
        self.address = address
        parent_w, parent_h = self.parent.width(), self.parent.height()
        x = (parent_w / 2) - (self.width() / 2)
        y = (parent_h / 2) - (self.height() / 2)
        self.move(int(x), int(y))

        self.show()

    def hide_pop(self):
        self.hide()

    def clicked_save_btn(self):
        flag = self.cbx_flag.currentIndex()

        if self.rbtn_set.isChecked(): kind = 1
        elif self.rbtn_building.isChecked(): kind = 2
        elif self.rbtn_land.isChecked(): kind = 3
        else: kind = 2

        self.issuance_thread = IssuanceRegistered(self.api_data, self.user, self.address, flag, kind)
        self.issuance_thread.threadEvent.workerThreadDone.connect(self.saved_pdf)
        self.issuance_thread.start()

    def saved_pdf(self, data):
        # 요청 된 바이너리 PDF 파일로 저장
        fileName = QFileDialog.getSaveFileName(self, self.tr("등기부등본 PDF 저장"), "./", self.tr("PDF 문서 (*.pdf)"))
        with open(fileName[0], "wb") as f:
            f.write(base64.b64decode(data.json()['Message']))


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
            if result['Status'] == 'OK':

                # PDF 바이너리 요청
                transaction_key = result['TransactionKey']

                url = self.API_HOST + "api/v1.0/iros/getpdffile"
                params = {"TransactionKey": transaction_key, "IsSummary": "Y"}
                response = requests.post(url, headers=self.headers, json=params)
                print(3, response.json())
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