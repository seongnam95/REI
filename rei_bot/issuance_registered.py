import os
import base64
import requests

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5, AES


class IssuanceRegistered:
    def __init__(self):
        super(IssuanceRegistered, self).__init__()

        self.API_HOST = 'https://api.tilko.net/'
        self.API_KEY = '6062d22d48734cd3af82837f696730fb'
        self.headers = None

    def get_register_data(self, address, user_id, user_pw, num_1, num_2, num_pw):
        aesKey = os.urandom(16)
        aesIv = ('\x00' * 16).encode('utf-8')

        rsaPublicKey = getPublicKey(self.API_HOST, self.API_KEY)
        aesCipherKey = base64.b64encode(rsaEncrypt(rsaPublicKey, aesKey))

        self.headers = {"Content-Type": "application/json",
                        "API-KEY": self.API_KEY,
                        "ENC-KEY": aesCipherKey}

        # 등기 고유번호 조회
        url = {'조회': self.API_HOST + "api/v1.0/iros/risuconfirmsimplec",
               '발급': self.API_HOST + "api/v1.0/iros/risuretrieve"}

        res = requests.post(url['조회'], headers=self.headers, json={'Address': address})
        unique_no = res.json()['ResultList'][0]['UniqueNo']
        print(f'unique : {unique_no}')

        # 등기부등본 데이터 요청
        params = {"IrosID": aesEncrypt(aesKey, aesIv, user_id),
                  "IrosPwd": aesEncrypt(aesKey, aesIv, user_pw),
                  "EmoneyNo1": aesEncrypt(aesKey, aesIv, num_1),
                  "EmoneyNo2": aesEncrypt(aesKey, aesIv, num_2),
                  "EmoneyPwd": aesEncrypt(aesKey, aesIv, num_pw),
                  "UniqueNo": unique_no}

        res = requests.post(url['발급'], headers=self.headers, json=params)
        valid = validation(res.json()['Message'])

        if valid is True: return res.json()
        else: print(valid)

    def saved_pdf(self, transaction_key):
        url = self.API_HOST + "api/v1.0/iros/getpdffile"
        params = {"TransactionKey": transaction_key, "IsSummary": "Y"}

        # PDF 바이너리 요청
        res = requests.post(url, headers=self.headers, json=params)

        # 요청 된 바이너리 PDF 파일로 저장
        with open("new.pdf", "wb") as f:
            f.write(base64.b64decode(res.json()['Message']))

        print('saved sucess !')


def validation(msg):
    if '잔액이 부족합니다' in msg:
        return '잔액 부족'
    else:
        return True


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


ir = IssuanceRegistered()
data = ir.get_register_data('면목동 91-79', 'mogsin21', 'happy2588@', 'P3372711', '3234', 'kim2588')
if data:
    t_key = data['TransactionKey']
    ir.saved_pdf(t_key)
    print(f'transaction_key : {t_key}')

