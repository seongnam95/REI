import os
import json
import base64
import requests

from Crypto import PublicKey
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5, AES


class Register_Save_PDF:
    def __init__(self):
        super(Register_Save_PDF, self).__init__()

        self.API_HOST = 'https://api.tilko.net/'
        self.API_KEY = '6062d22d48734cd3af82837f696730fb'

        address = '중랑구 면목동 1545번지 101동 101호'

        self.saved_pdf(address)

    def saved_pdf(self, address, user_id, user_pw, num_1, num_2, num_pw):
        aesKey = os.urandom(16)
        aesIv = ('\x00' * 16).encode('utf-8')

        rsaPublicKey = getPublicKey(self.API_HOST, self.API_KEY)
        aesCipherKey = base64.b64encode(rsaEncrypt(rsaPublicKey, aesKey))

        url = {'조회': self.API_HOST + "api/v1.0/iros/risuconfirmsimplec",
               '발급': self.API_HOST + "api/v1.0/iros/risuretrieve",
               'PDF': self.API_HOST + "api/v1.0/iros/getpdffile"}

        headers = {"Content-Type": "application/json",
                        "API-KEY": self.API_KEY,
                        "ENC-KEY": aesCipherKey}

        res = requests.post(url['조회'], headers=headers, json={'Address': address})
        unique_no = res.json()['ResultList'][0]['UniqueNo']
        print(f'unique : {unique_no}')

        params = {"IrosID": aesEncrypt(aesKey, aesIv, user_id),
                  "IrosPwd": aesEncrypt(aesKey, aesIv, user_pw),
                  "EmoneyNo1": aesEncrypt(aesKey, aesIv, num_1),
                  "EmoneyNo2": aesEncrypt(aesKey, aesIv, num_2),
                  "EmoneyPwd": aesEncrypt(aesKey, aesIv, num_pw),
                  "UniqueNo": unique_no}

        res = requests.post(url['발급'], headers=headers, json=params)
        transaction_key = res.json()['TransactionKey']
        print(f'transaction_key : {transaction_key}')

        params = {"TransactionKey": transaction_key, "IsSummary": "Y"}
        res = requests.post(url['PDF'], headers=headers, json=params)

        with open("new.pdf", "wb") as f:
            f.write(base64.b64decode(res.json()['Message']))

        print('saved sucess !')


# AES 암호화 함수
def aesEncrypt(key, iv, plainText):
    def pad(text):
        text_length = len(text)
        amount_to_pad = AES.block_size - (text_length % AES.block_size)

        if amount_to_pad == 0:
            amount_to_pad = AES.block_size

        pad = chr(amount_to_pad)

        result = None
        try:
            result = text + str(pad * amount_to_pad).encode('utf-8')
        except Exception as e:
            result = text + str(pad * amount_to_pad)

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


Register_Save_PDF()
