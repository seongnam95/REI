import bs4
import requests
import pandas as pd

from urllib.parse import quote_plus, urlencode
from PyQt5.QtCore import QThread, pyqtSignal


# 공용 파싱 함수
def public_pars(url, clms):
    response = requests.get(url).text.encode('utf-8')
    xml_obj = bs4.BeautifulSoup(response, 'xml')

    rows = xml_obj.find_all('item')
    if len(rows) == 0:
        rows = xml_obj.find_all('field')
    if len(rows) == 0:
        return None

    row_list = []
    append = row_list.append
    df = pd.DataFrame(columns=clms)
    df_loc = df.loc
    for i in range(len(rows)):
        for tag in clms:
            item = rows[i].find(tag)
            if item is None: append('')
            else: append(item.text.strip())
        df_loc[i] = row_list
        row_list = []

    if len(df) == 0:
        err = xml_obj.find('returnAuthMsg')
        if err is None:
            return None
        else:
            err = err.get_text()
            return err
    return df

# 주소 파싱
def address_pars(juso, key):
    # 행정동코드, 지하 여부, 본번, 부번, 건물명
    # 도로명주소, 시, 시군구, 읍면동, 번, 지
    colm = ['code', 'under', 'bon', 'bu', 'nm',
            'new_address', 'siNm', 'sggNm', 'emdNm', 'bun', 'ji']
    pars = ['admCd', 'udrtYn', 'buldMnnm', 'buldSlno', 'bdNm',
            'roadAddrPart1', 'siNm', 'sggNm', 'emdNm', 'lnbrMnnm', 'lnbrSlno']

    xml_url = 'https://www.juso.go.kr/addrlink/addrLinkApi.do'
    query_params = '?' + urlencode(
        {
            quote_plus('confmKey'): key,
            quote_plus('currentPage'): '1',
            quote_plus('countPerPage'): '20',
            quote_plus('resultType'): 'xml',
            quote_plus('keyword'): juso
        }
    )
    response = requests.get(xml_url + query_params).text.encode('utf-8')
    xmlobj = bs4.BeautifulSoup(response, 'xml')

    rowlist = []
    df = pd.DataFrame(columns=colm)

    append = rowlist.append
    obj_find_all = xmlobj.find_all

    # 파싱 후 데이터프레임에 저장
    for i in range(len(colm)):
        append(i.strip() for i.text in obj_find_all(pars[i]))
        print(rowlist)
        df[colm[i]] = rowlist
        rowlist = []

    # 정확한 주소가 있다면 하나만 리턴
    try:
        if '-' in juso:
            res = juso.split(' ')[-1]
            res = res.split('-')
            redf = df[(df.lnbrMnnm == res[0]) & (df.lnbrSlno == res[1])]
            if len(redf) == 0:
                return df
            return redf
    except:
        return df
    return df

# 위반 건축물 파싱
def viol_pars(key, pk):
    xml_url = 'http://openapi.seoul.go.kr:8088/' + key + '/xml/bigDjyBldRgstInfo/1/5/' + pk

    response = requests.get(xml_url).text.encode('utf-8')
    xmlobj = bs4.BeautifulSoup(response, 'xml')
    val = xmlobj.find('VIOL_BLD_YN')
    if val is None:
        return None
    if len(val) == 0:
        return None
    return val.get_text()

class XmlParsingThread(QThread):
    threadEvent = pyqtSignal(object)

    def __init__(self, pnu, parsing_type_list, parent=None):
        super().__init__()
        self.main = parent
        self.parsing_type_list = parsing_type_list
        self.key = 'sfSPRX+xNEExRUqE4cdhNjBSk4uXIv8F1CfLen06hdPGn5cflLJqy/nxmh48uF8fvdGk68k6Z5jWsU1n6BeNPA=='
        self.sigungu = pnu[0][:5]
        self.bjdong = pnu[0][5:10]
        self.bun = pnu[1]
        self.ji = pnu[2]

    def run(self):
        result_data = []
        parsing_type, columns = '', ''
        repnu = self.sigungu + self.bjdong + '1' + self.bun + self.ji

        year = datetime.now().year
        pool = ThreadPool(processes=4)

        for ty in self.parsing_type_list:
            if ty == '토지':
                columns = ['prposAreaDstrcCodeNm']
                xml_url = 'http://apis.data.go.kr/1611000/nsdi/LandUseService/attr/getLandUseAttr'
                query_params = '?' + urlencode(
                    {
                        quote_plus('serviceKey'): self.key,
                        quote_plus('pnu'): repnu,
                        quote_plus('cnflcAt'): '1',
                        quote_plus('format'): 'xml',
                        quote_plus('numOfRows'): '10'
                    }
                )
            elif ty == '공시가격':
                columns = ['housePc', 'lastUpdtDt']
                xml_url = 'http://apis.data.go.kr/1611000/nsdi/IndvdHousingPriceService/attr/getIndvdHousingPriceAttr'
                query_params = '?' + urlencode(
                    {
                        quote_plus('serviceKey'): self.key,
                        quote_plus('pnu'): repnu,
                        quote_plus('stdrYear'): year,
                        quote_plus('format'): 'xml',
                        quote_plus('numOfRows'): '10'
                    }
                )
            elif ty == '공시지가':
                columns = ['pblntfPclnd']
                xml_url = 'http://apis.data.go.kr/1611000/nsdi/IndvdLandPriceService/attr/getIndvdLandPriceAttr'
                query_params = '?' + urlencode(
                    {
                        quote_plus('serviceKey'): self.key,
                        quote_plus('pnu'): repnu,
                        quote_plus('stdrYear'): year,
                        quote_plus('format'): 'xml',
                        quote_plus('numOfRows'): '10'
                    }
                )
            elif ty == '소유자':
                columns = ['dong_nm', 'ho_nm', 'nm', 'own_gb_nm', 'jm_gb_nm']
                xml_url = 'http://apis.data.go.kr/1611000/OwnerInfoService/getArchitecturePossessionInfo'
                query_params = '?' + urlencode(
                    {
                        quote_plus('serviceKey'): self.key,
                        quote_plus('numOfRows'): '1000',
                        quote_plus('sigungu_cd'): self.sigungu,
                        quote_plus('bjdong_cd'): self.bjdong,
                        quote_plus('plat_gb_cd'): '0',
                        quote_plus('bun'): self.bun,
                        quote_plus('ji'): self.ji,
                    }
                )
            else:
                if ty == '표제부':
                    parsing_type = 'getBrTitleInfo'
                    columns = ['rnum', 'mainPurpsCdNm', 'rideUseElvtCnt', 'emgenUseElvtCnt', 'ugrndFlrCnt',
                               'grndFlrCnt', 'indrMechUtcnt', 'oudrMechUtcnt', 'indrAutoUtcnt', 'oudrAutoUtcnt',
                               'hoCnt', 'fmlyCnt', 'hhldCnt', 'platArea', 'totArea', 'archArea', 'heit',
                               'bcRat', 'vlRat', 'useAprDay', 'strctCdNm', 'regstrGbCdNm', 'mainAtchGbCdNm',
                               'etcPurps', 'platPlc', 'bldNm', 'dongNm', 'newPlatPlc', 'mgmBldrgstPk']

                elif ty == '총괄표제부':
                    parsing_type = 'getBrRecapTitleInfo'
                    columns = ['indrMechUtcnt', 'oudrMechUtcnt', 'indrAutoUtcnt', 'oudrAutoUtcnt']

                elif ty == '층별':
                    parsing_type = 'getBrFlrOulnInfo'
                    columns = ['flrGbCdNm', 'flrNoNm', 'etcPurps', 'area']

                elif ty == '지역지구':
                    parsing_type = 'getBrJijiguInfo'
                    columns = ['etcJijigu']

                # URL
                xml_url = 'http://apis.data.go.kr/1613000/BldRgstService_v2/' + parsing_type
                query_params = '?' + urlencode(
                    {
                        quote_plus('serviceKey'): self.key,
                        quote_plus('numOfRows'): '1000',
                        quote_plus('sigunguCd'): self.sigungu,
                        quote_plus('bjdongCd'): self.bjdong,
                        quote_plus('platGbCd'): '0',
                        quote_plus('bun'): self.bun,
                        quote_plus('ji'): self.ji,
                    }
                )

            url = xml_url + query_params
            ld = LoadData()
            result_data.append(pool.apply_async(func.pars.get_data, (url, columns,)))

        for n, _ in enumerate(result_data):
            result_data[n] = result_data[n].get()

        self.threadEvent.emit(result_data)