from AES import AESCipher
import requests, base64, json, os


class APIHelper:
    _pubUrl = "https://api.tilko.net/api/Auth/GetPublicKey?APIkey={}"
    _paymentUrl = "https://api.tilko.net/api/v1.0/Nhis/jpaca00101/geongangboheom"
    _myDrugUrl = "https://api.tilko.net/api/v1.0/Hira/hiraa050300000100"
    _aes = None
    _apiKey = None

    def __init__(self, apiKey):
        self._apiKey = apiKey
        # AES초기화
        # self._aes = AESCipher(str('\x00' * 16), '\x00' * 16)
        self._aes = AESCipher(os.urandom(16), ('\x00' * 16).encode('utf-8'))

    # self._aes = AESCipher(str('\x00' * 16), '\x00' * 16)

    # get AES plain Key
    def getAesPlainKey(self):
        return self._aes.key

    # RSA공개키 요청 API호출
    def getRSAPubKey(self):
        headers = {'Content-Type': 'application/json'}
        response = requests.request("GET", self._pubUrl.format(self._apiKey), headers=headers)
        return response.text.encode('utf8')
