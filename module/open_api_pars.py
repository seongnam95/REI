from urllib.parse import quote_plus

import bs4
import requests
import pandas as pd

from PySide6.QtCore import QThread, QObject, Signal
from multiprocessing.pool import ThreadPool
from datetime import datetime


class OpenApiRequest:
    @classmethod
    def request_data(cls, url, params, column, keyword):
        try:
            response = requests.get(url, params=params).text.encode('utf-8')
            xml_obj = bs4.BeautifulSoup(response, 'xml')

            rows = xml_obj.find_all(keyword)
            if len(rows) == 0: return None

            row_list = []
            result = pd.DataFrame(columns=list(column))

            column_values = list(column.values())
            list_append = row_list.append
            for i in range(len(rows)):
                for tag in column_values:
                    item = rows[i].find(tag)
                    if item is None: list_append("")
                    else: list_append(item.text.strip())
                result.loc[i] = row_list
                row_list.clear()
            return result

        except: return None

    # 주소 조회
    @classmethod
    def get_address(cls, key, address):
        url = 'https://www.juso.go.kr/addrlink/addrLinkApi.do'
        params = {'confmKey': key, 'currentPage': '1', 'countPerPage': '20', 'resultType': 'xml', 'keyword': address}
        column = {'주소코드': 'admCd', '시도': 'siNm', '시군구': 'sggNm', '읍면동': 'emdNm', '지하여부': 'udrtYn', '공동주택여부': 'bdKdcd',
                  '번': 'lnbrMnnm', '지': 'lnbrSlno', '동': 'detBdNmList', '건물명칭': 'bdNm',
                  '도로명주소': 'roadAddrPart1', '도로명코드': 'rnMgtSn', '건물본번': 'buldMnnm', '건물부번': 'buldSlno'}
        result = cls.request_data(url, params, column, 'juso')

        try:
            if '-' in address:
                bunji = address.split(' ')[-1].split('-')
                re_result = result[(result["번"].item() == bunji[0]) & (result["지"].item() == bunji[1])]
                if len(re_result) != 0: return re_result
        finally: return result

    # 상세 주소 조회
    @classmethod
    def get_address_detail(cls, key, binfo, dong=''):
        url = 'https://www.juso.go.kr/addrlink/addrDetailApi.do'
        params = {'confmKey': key, 'admCd': binfo['주소코드'], 'rnMgtSn': binfo['도로명코드'], 'udrtYn': binfo['지하여부'],
                  'buldMnnm': binfo['건물본번'], 'buldSlno': binfo['건물부번'],
                  'searchType': 'floorho', 'dongNm': dong, 'resultType': 'xml'}
        column = {'동명칭': 'dongNm', '층번호': 'floorNm', '호명칭': 'hoNm'}
        result = cls.request_data(url, params, column, 'juso')
        return result

    # 위반 건축물 조회
    @classmethod
    def get_viol(cls, key, pk):
        xml_url = "http://openapi.seoul.go.kr:8088/%s/xml/bigDjyBldRgstInfo/1/5/%s" % (key, pk)
        response = requests.get(xml_url).text.encode('utf-8')
        xmlobj = bs4.BeautifulSoup(response, 'xml')

        val = xmlobj.find('VIOL_BLD_YN')
        if val is None: return None
        if len(val) == 0: return None

        return val.get_text()

    # 사무소 조회
    @classmethod
    def get_company(cls, key, code, company, boss):

        url = 'http://openapi.nsdi.go.kr/nsdi/EstateBrkpgService/attr/getEBBrokerInfo'
        params = {'authkey': key, 'ldCode': code, 'bsnmCmpnm': company, 'brkrNm': boss, 'format': 'xml', 'numOfRows': '100'}
        column = {'시군구코드': 'ldCode', '등록번호': 'jurirno', '상호명': 'bsnmCmpnm',
                  '대표자명': 'brkrNm', '직위구분명': 'ofcpsSeCodeNm', '중개업자종별명': 'brkrAsortCodeNm'}
        result = cls.request_data(url, params, column, 'field')

        return result


class ThreadSignal(QObject):
    workerThreadDone = Signal(object)

class BuildingRegisterThread(QThread):
    def __init__(self, binfo, parsing_type_list, parent=None):
        super().__init__()
        self.main = parent
        self.threadEvent = ThreadSignal()
        self.parsing_type_list = parsing_type_list

        self.key = 'sfSPRX+xNEExRUqE4cdhNjBSk4uXIv8F1CfLen06hdPGn5cflLJqy/nxmh48uF8fvdGk68k6Z5jWsU1n6BeNPA=='
        self.sigungu = binfo['주소코드'][:5]
        self.bjdong = binfo['주소코드'][5:10]
        self.bun, self.ji = binfo['번'], binfo['지']
        self.dong = binfo['동명칭']

    def run(self):
        result_data = []
        parsing_type, column = None, None
        pnu = self.sigungu + self.bjdong + '1' + self.bun + self.ji

        year = datetime.now().year
        pool = ThreadPool(processes=4)

        for ty in self.parsing_type_list:
            keyword = 'field'
            if ty == '토지':
                url = 'http://apis.data.go.kr/1611000/nsdi/LandUseService/attr/getLandUseAttr'
                column = {'용도지역지구명': 'prposAreaDstrcCodeNm'}
                params = {'serviceKey': self.key, 'pnu': pnu, 'cnflcAt': '1', 'format': 'xml', 'numOfRows': '10'}

            elif ty == '공동주택가격':
                url = 'http://apis.data.go.kr/1611000/nsdi/ApartHousingPriceService/attr/getApartHousingPriceAttr'
                column = {'동명칭': 'dongNm', '호명칭': 'hoNm', '공동주택가격': 'pblntfPc', '공시일자': 'lastUpdtDt'}
                params = {'serviceKey': self.key, 'pnu': pnu, 'stdrYear': year, 'format': 'xml', 'numOfRows': '1000'}

            elif ty == '개별주택가격':
                url = 'http://apis.data.go.kr/1611000/nsdi/IndvdHousingPriceService/attr/getIndvdHousingPriceAttr'
                column = {'개별주택가격': 'housePc', '공시일자': 'lastUpdtDt'}
                params = {'serviceKey': self.key, 'pnu': pnu, 'stdrYear': year, 'format': 'xml', 'numOfRows': '10'}

            elif ty == '공시지가':
                url = 'http://apis.data.go.kr/1611000/nsdi/IndvdLandPriceService/attr/getIndvdLandPriceAttr'
                column = {'공시지가': 'pblntfPclnd', '공시일자': 'pblntfDe'}
                params = {'serviceKey': self.key, 'pnu': pnu, 'stdrYear': year, 'format': 'xml', 'numOfRows': '10'}

            elif ty == '소유자':
                keyword = 'item'
                url = 'http://apis.data.go.kr/1611000/OwnerInfoService/getArchitecturePossessionInfo'
                column = {'동명칭': 'dong_nm', '호명칭': 'ho_nm', '소유자명': 'nm', '소유구분명': 'own_gb_nm',
                          '주민구분명': 'jm_gb_nm', '소유권지분': 'ownsh_quota', '지분1': 'quota1', '지분2': 'quota2'}
                params = {'serviceKey': self.key, 'sigungu_cd': self.sigungu, 'bjdong_cd': self.bjdong,
                          'bun': self.bun, 'ji': self.ji, 'plat_gb_cd': '0', 'numOfRows': '1000'}

            else:
                keyword = 'item'
                if ty == '표제부':
                    parsing_type = 'getBrTitleInfo'
                    column = {'대장종류': 'regstrKindCdNm', '대장구분': 'regstrGbCdNm', '주부속구분': 'mainAtchGbCdNm',
                              '주용도': 'mainPurpsCdNm', '기타용도': 'etcPurps', '주구조': 'strctCdNm', '기타구조': 'etcStrct',
                              '대지면적': 'platArea', '연면적': 'totArea', '건축면적': 'archArea', '높이': 'heit',
                              '건폐율': 'bcRat', '용적률': 'vlRat', '내진설계적용여부': 'rserthqkDsgnApplyYn', '내진능력': 'rserthqkAblty',
                              '지상층수': 'grndFlrCnt', '지하층수': 'ugrndFlrCnt',
                              '옥내기계식대수': 'indrMechUtcnt', '옥외기계식대수': 'oudrMechUtcnt',
                              '옥내자주식대수': 'indrAutoUtcnt', '옥외자주식대수': 'oudrAutoUtcnt',
                              '승강기': 'rideUseElvtCnt', '비상용승강기': 'emgenUseElvtCnt',
                              '사용승인일': 'useAprDay', '건축물대장PK': 'mgmBldrgstPk',
                              '건물명칭': 'bldNm', '동명칭': 'dongNm',
                              '호수': 'hoCnt', '가구수': 'fmlyCnt', '세대수': 'hhldCnt'}

                elif ty == '총괄표제부':
                    parsing_type = 'getBrRecapTitleInfo'
                    column = {'옥내기계식대수': 'indrMechUtcnt', '옥외기계식대수': 'oudrMechUtcnt',
                              '옥내자주식대수': 'indrAutoUtcnt', '옥외자주식대수': 'oudrAutoUtcnt',
                              '총주차수': 'totPkngCnt'}

                elif ty == '전유부':
                    parsing_type = 'getBrExposPubuseAreaInfo'
                    column = {'동명칭': 'dongNm', '호명칭': 'hoNm', '전용면적': 'area', '전유공용구분': 'exposPubuseGbCdNm',
                              '주구조': 'strctCdNm', '기타구조': 'etcStrct', '주용도': 'mainPurpsCdNm', '기타용도': 'etcPurps',
                              '건축물대장PK': 'mgmBldrgstPk', '층구분': 'flrGbCdNm', '층번호': 'flrNo', '층번호명': 'flrNoNm'}

                elif ty == '층별':
                    parsing_type = 'getBrFlrOulnInfo'
                    column = {'층구분': 'flrGbCdNm', '층번호': 'flrNo', '층명칭': 'flrNoNm', '층면적': 'area',
                              '주구조': 'strctCdNm', '기타구조': 'etcStrct', '주용도': 'mainPurpsCdNm', '기타용도': 'etcPurps'}

                elif ty == '지역지구':
                    parsing_type = 'getBrJijiguInfo'
                    column = {'기타지역지구구역': 'etcJijigu'}

                url = 'http://apis.data.go.kr/1613000/BldRgstService_v2/' + parsing_type
                params = {'serviceKey': self.key, 'sigunguCd': self.sigungu, 'bjdongCd': self.bjdong,
                          'bun': self.bun, 'ji': self.ji, 'platGbCd': '0', 'format': 'xml', 'numOfRows': '10000'}
                if ty == '전유부': params['dongNm'] = self.dong

            result_data.append(pool.apply_async(OpenApiRequest.request_data, (url, params, column, keyword, )))

        for n, _ in enumerate(result_data):
            result_data[n] = result_data[n].get()
        pool.close()
        self.threadEvent.workerThreadDone.emit(result_data)


class SetParsingThread(QThread):
    def __init__(self, binfo, key, dong_count, dong='', parent=None):
        super().__init__()

        if dong_count == 1: dong = ''
        self.main = parent
        self.threadEvent = ThreadSignal()

        # 건물 정보
        sigungu = binfo['code'][:5]
        bjdong = binfo['code'][5:10]
        bun = binfo['bun']
        ji = binfo['ji']

    def run(self):
        pool = ThreadPool(processes=4)
        result_data = pool.apply_async(self.request_data, (self.url_data, self.columns_data,))

        result_name = pool.apply_async(self.request_data, (self.url_name, self.columns_name,))

        result_price = pool.apply_async(self.request_data, (self.url_price, self.columns_price,))

        return_price = result_price.get()
        if return_price is not None:
            return_price = return_price.fillna('')
            return_price = self.convert_ho_name(return_price)

            if self.dong_count > 1:
                return_price_try = return_price[return_price['dongNm'] == self.dong]

                # self.dong 의 동 이름이 다를 경우 '동' 제거 후 검색
                if len(return_price_try) == 0:
                    return_price_try = return_price[return_price['dongNm'] == self.dong.rstrip('동')]

                    # 둘 다 없을 경우
                    if len(return_price_try) == 0:
                        return_price = None
                    else:
                        return_price = return_price_try
                else:
                    return_price = return_price_try

        return_name = result_name.get()
        return_name.columns = ['dongNm', 'hoNm', 'nm', 'own_gb_nm', 'jm_gb_nm']
        self.convert_ho_name(return_name)
        return_name = return_name.drop_duplicates(['hoNm'])     # 소유자명 1명만 필터
        return_data = self.convert_ho_name(result_data.get())

        # 리턴 된 데이터 한 데이터프레임에 합치기
        for i in range(len(return_data)):
            ho = return_data.loc[i]['convert_ho']
            name = return_name[return_name['convert_ho'] == ho]['nm'].item()
            jmgb = return_name[return_name['convert_ho'] == ho]['jm_gb_nm'].item()
            return_data.loc[return_data['convert_ho'] == ho, 'nm'] = name
            return_data.loc[return_data['convert_ho'] == ho, 'jm_gb_nm'] = jmgb

            if return_price is not None:
                if return_price['convert_ho'] == ho:
                    price = return_price[return_price['convert_ho'] == ho]['pblntfPc'].item()
                    price_day = return_price[return_price['convert_ho'] == ho]['lastUpdtDt'].item()
                    return_data.loc[return_data['convert_ho'] == ho, 'pblntfPc'] = price
                    return_data.loc[return_data['convert_ho'] == ho, 'lastUpdtDt'] = price_day
                else:
                    return_data.loc[return_data['convert_ho'] == ho, 'pblntfPc'] = ''
                    return_data.loc[return_data['convert_ho'] == ho, 'lastUpdtDt'] = ''
            else:
                return_data.loc[return_data['convert_ho'] == ho, 'pblntfPc'] = ''
                return_data.loc[return_data['convert_ho'] == ho, 'lastUpdtDt'] = ''
        self.threadEvent.workerThreadDone.emit(return_data)

    @classmethod
    def convert_ho_name(cls, df):
        df['convert_ho'] = df['hoNm']
        df['convert_ho'] = df['convert_ho'].str.rstrip('호')
        df['convert_ho'] = df['convert_ho'].str.replace('층', '0').str.replace('지', 'B') \
            .str.replace('비', 'B').str.replace('B', '-')
        regex = r"([-+]?\d*\.*\d+|\d+)"
        df['convert_ho'] = df.convert_ho.astype('str').str.extract(regex, expand=False)
        df['convert_ho'] = df['convert_ho'].astype(int)
        df = df.sort_values(by=['convert_ho'], axis=0)

        df.reset_index(drop=True, inplace=True)
        return df


class GenParsingThread(QThread):
    def __init__(self, binfo, key, data, dong='', parent=None):
        super().__init__()

        self.main, self.key, self.data, self.dong, = parent, key, data, dong
        self.threadEvent = ThreadSignal()

        # 건물 정보
        self.sigungu = binfo['code'][:5]
        self.bjdong = binfo['code'][5:10]
        self.bun = binfo['bun']
        self.ji = binfo['ji']

        pnu = self.sigungu + self.bjdong + '1' + self.bun + self.ji
        year = datetime.now().year

        # 층별 조회

        # 소유자 정보

        # 주택 가격

    def run(self):

        data = self.data.copy()
        return_flr = "result_flr.get()"
        return_price = "result_price.get()"
        return_name = "result_name.get()"
        return_name.columns = ['dongNm', 'nm', 'own_gb_nm', 'jm_gb_nm']
        return_name = return_name.drop_duplicates(['dongNm'])  # 소유자명 1명만 필터

        # 리턴 된 데이터 한 데이터프레임에 합치기
        if data['dongNm'] == '':
            data['nm'] = return_name['nm'].item()
            data['jm_gb_nm'] = return_name['jm_gb_nm'].item()

            if return_price is not None:
                data['housePc'] = return_price['housePc'].item()
                data['lastUpdtDt'] = return_price['lastUpdtDt'].item()
            else:
                data['housePc'] = ''
                data['lastUpdtDt'] = ''
        else:
            dong = data['dongNm']
            return_flr = return_flr[return_flr['dongNm'] == dong]
            data['nm'] = return_name[return_name['dongNm'] == dong].nm.item()
            data['jm_gb_nm'] = return_name[return_name['dongNm'] == dong].jm_gb_nm.item()

            if return_price is not None:
                data['housePc'] = return_price['housePc'].item()
                data['lastUpdtDt'] = return_price['lastUpdtDt'].item()
            else:
                data['housePc'] = ''
                data['lastUpdtDt'] = ''

        return_data = [data, self.flr_re_index(return_flr)]
        self.threadEvent.workerThreadDone.emit(return_data)

    @classmethod
    def flr_re_index(cls, df):
        low = df[df.flrGbCdNm == '지하'].sort_values(by=['flrNoNm'], axis=0)
        mid = df[df.flrGbCdNm == '지상'].sort_values(by=['flrNoNm'], axis=0)
        top = df[df.flrGbCdNm == '옥탑'].sort_values(by=['flrNoNm'], axis=0)
        df = pd.concat([low, mid, top])
        df.reset_index(drop=True, inplace=True)
        return df
