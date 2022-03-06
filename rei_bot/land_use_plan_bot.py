import webbrowser
from urllib.parse import urlencode

url = 'http://www.eum.go.kr/web/ar/lu/luLandDetPrintPop.jsp?'
params = urlencode({'isNoScr': 'script',
                    'mode': 'search',
                    'pnu': '1126010200100880085'})

webbrowser.open_new(url + params)
