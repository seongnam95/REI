import requests
import json


s = requests.session()
headers = {
    "Referer": "https://cloud.eais.go.kr/moct/awp/abb01/AWPABB01F01?returnUrl=%2F",
    "Content-Type": "application/json;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.57 Whale/3.14.133.23 Safari/537.36"
}
#
# response = s.post('https://cloud.eais.go.kr/awp/AWPABB01R12', headers=headers)
# result = json.loads(response.text)
# print(result)

datas = {'membNo': 'haul1115', 'pwd': 'ks05090818@'}
response_title = s.post('https://cloud.eais.go.kr/awp/AWPABB01R08', headers=headers, json=datas)
print(response_title)

datas = {"loginId": "haul1115", "loginPwd": "ks05090818@"}
headers['Referer'] = 'https://cloud.eais.go.kr/moct/awp/abb01/AWPABB01F01'
response_title = s.post('https://cloud.eais.go.kr/awp/AWPABB01R01', headers=headers, json=datas)
print(response_title)
result = json.loads(response_title.text)
print(result)
