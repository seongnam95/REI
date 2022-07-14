import os
import base64
import requests

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5, AES
from PySide6.QtCore import QThread, QObject, Signal


class ThreadSignal(QObject):
    workerThreadDone = Signal(bytes)
    workingMsg = Signal(str)


class CertificateOfTitle(QThread):
    def __init__(self, api_data, user, address, flag, kind):
        super(CertificateOfTitle, self).__init__()
        self.threadEvent = ThreadSignal()

        self.API_HOST = api_data['HOST']
        self.API_KEY = api_data['KEY']
        self.headers = None

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

        # 등기 고유번호 조회가 됐을 경우
        if result['Status'] == 'OK':
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

            # 등기 데이터가 정상 조회 되었을 경우
            if result['Status'] == 'OK':

                # PDF 바이너리 요청
                transaction_key = result['TransactionKey']
                url = self.API_HOST + "api/v1.0/iros/getpdffile"
                params = {"TransactionKey": transaction_key, "IsSummary": "Y"}
                response = requests.post(url, headers=self.headers, json=params)

                # 요청 된 바이너리 PDF 파일로 저장
                with open("new.pdf", "wb") as f:
                    f.write(base64.b64decode(response.json()['Message']))

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



