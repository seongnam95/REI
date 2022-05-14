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

            if not rows: return None

            row_list = []
            result = pd.DataFrame(columns=list(column))

            column_values = list(column.values())
            list_append = row_list.append
            for i in range(len(rows)):
                for tag in column_values:
                    item = rows[i].find(tag)
                    if item is None:
                        list_append("")
                    else:
                        list_append(item.text.strip())
                result.loc[i] = row_list
                row_list.clear()
            return result

        except (ValueError, TypeError, IndexError) as e:
            print(f'error: {e}')
            return

        except Exception as e:
            print(f'error: {e}')
            return

    # 주소 조회
    @classmethod
    def get_address(cls, key, address):
        url = 'https://www.juso.go.kr/addrlink/addrLinkApi.do'
        params = {'confmKey': key, 'currentPage': '1', 'countPerPage': '20', 'resultType': 'xml', 'keyword': address}
        column = {'주소코드': 'admCd', '시도': 'siNm', '시군구': 'sggNm', '읍면동': 'emdNm', '법정리': 'liNm',
                  '지하여부': 'udrtYn', '번': 'lnbrMnnm', '지': 'lnbrSlno', '동': 'detBdNmList', '건물명칭': 'bdNm',
                  '도로명주소': 'roadAddrPart1', '도로명코드': 'rnMgtSn', '건물본번': 'buldMnnm', '건물부번': 'buldSlno'}
        result = cls.request_data(url, params, column, 'juso')

        try:
            if '-' in address:
                bunji = address.split(' ')[-1].split('-')
                re_result = result[(result["번"].item() == bunji[0]) & (result["지"].item() == bunji[1])]
                if re_result: return re_result

        finally: return result

    # 상세 주소 조회
    @classmethod
    def get_address_detail(cls, key, binfo, kind, dong=''):
        kind = 'dong' if kind == '동' else 'floorho'
        url = 'https://www.juso.go.kr/addrlink/addrDetailApi.do'
        params = {'confmKey': key, 'admCd': binfo['주소코드'], 'rnMgtSn': binfo['도로명코드'], 'udrtYn': binfo['지하여부'],
                  'buldMnnm': binfo['건물본번'], 'buldSlno': binfo['건물부번'],
                  'searchType': kind, 'dongNm': dong, 'resultType': 'xml'}

        column = {'동명칭': 'dongNm', '층번호': 'floorNm', '호명칭': 'hoNm'}
        result = cls.request_data(url, params, column, 'juso')
        return result

    # 위반 건축물 조회
    @classmethod
    def get_viol(cls, key, pk, result=None):
        try:
            xml_url = "http://openapi.seoul.go.kr:8088/%s/xml/bigDjyBldRgstInfo/1/5/%s" % (key, pk)
            response = requests.get(xml_url).text.encode('utf-8')
            xmlobj = bs4.BeautifulSoup(response, 'xml')
            val = xmlobj.find('VIOL_BLD_YN')

            result = val.get_text()
        finally:
            return result

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


class DataRequestThread(QThread):
    def __init__(self, binfo, key, parsing_type_list, parent=None):
        super().__init__()
        self.main = parent
        self.threadEvent = ThreadSignal()
        self.parsing_type_list = parsing_type_list

        self.key = key

        self.sigungu = binfo['주소코드'][:5]
        self.bjdong = binfo['주소코드'][5:10]
        self.bun, self.ji = binfo['번'].zfill(4), binfo['지'].zfill(4)
        self.dong = binfo['동명칭'] if '동명칭' in binfo.keys() else ''
        self.pnu = binfo['주소코드'] + '1' + self.bun + self.ji

    def run(self):
        result_data = []
        parsing_type, column = None, None

        pool = ThreadPool(processes=4)

        for ty in self.parsing_type_list:
            keyword = 'field'
            if ty == '공동주택가격':
                url = 'http://apis.data.go.kr/1611000/nsdi/ApartHousingPriceService/attr/getApartHousingPriceAttr'
                column = {'동명칭': 'dongNm', '호명칭': 'hoNm', '공동주택가격': 'pblntfPc', '공시일자': 'lastUpdtDt'}
                result_data.append(pool.apply_async(self.get_days_data, (url, column,)))

            elif ty == '개별주택가격':
                url = 'http://apis.data.go.kr/1611000/nsdi/IndvdHousingPriceService/attr/getIndvdHousingPriceAttr'
                column = {'개별주택가격': 'housePc', '공시일자': 'lastUpdtDt'}
                result_data.append(pool.apply_async(self.get_days_data, (url, column,)))

            elif ty == '토지':
                url = 'http://apis.data.go.kr/1611000/nsdi/LandCharacteristicsService/attr/getLandCharacteristics'
                column = {'지목': 'lndcgrCodeNm', '대지면적': 'lndpclAr', '공시지가': 'pblntfPclnd',
                          '공시기준년': 'stdrYear', '공시기준월': 'stdrMt'}
                result_data.append(pool.apply_async(self.get_days_data, (url, column,)))

            else:
                if ty == '토지용도지역지구':
                    url = 'http://apis.data.go.kr/1611000/nsdi/LandUseService/attr/getLandUseAttr'
                    column = {'용도지역지구명': 'prposAreaDstrcCodeNm'}
                    params = {'serviceKey': self.key, 'pnu':  self.pnu, 'cnflcAt': '1', 'format': 'xml', 'numOfRows': '10'}

                elif ty == '소유자':
                    keyword = 'item'
                    url = 'http://apis.data.go.kr/1611000/OwnerInfoService/getArchitecturePossessionInfo'
                    column = {'건축물대장PK': 'mgm_bldrgst_pk', '동명칭': 'dong_nm', '호명칭': 'ho_nm', '소유자명': 'nm', '소유구분명': 'own_gb_nm',
                              '주민구분명': 'jm_gb_nm', '소유권지분': 'ownsh_quota', '지분1': 'quota1', '지분2': 'quota2'}
                    params = {'serviceKey': self.key, 'sigungu_cd': self.sigungu, 'bjdong_cd': self.bjdong,
                              'bun': self.bun, 'ji': self.ji, 'dong_nm': self.dong, 'plat_gb_cd': '0', 'numOfRows': '10000'}

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
                                  '사용승인일': 'useAprDay', '표제부PK': 'mgmBldrgstPk',
                                  '건물명칭': 'bldNm', '동명칭': 'dongNm',
                                  '호수': 'hoCnt', '가구수': 'fmlyCnt', '세대수': 'hhldCnt'}

                    elif ty == '총괄표제부':
                        parsing_type = 'getBrRecapTitleInfo'
                        column = {'옥내기계식대수': 'indrMechUtcnt', '옥외기계식대수': 'oudrMechUtcnt',
                                  '옥내자주식대수': 'indrAutoUtcnt', '옥외자주식대수': 'oudrAutoUtcnt',
                                  '총주차수': 'totPkngCnt', '대지면적': 'platArea'}

                    elif ty == '전유부':
                        parsing_type = 'getBrExposPubuseAreaInfo'
                        column = {'동명칭': 'dongNm', '호명칭': 'hoNm', '전용면적': 'area', '전유공용구분': 'exposPubuseGbCdNm',
                                  '주구조': 'strctCdNm', '기타구조': 'etcStrct', '주용도': 'mainPurpsCdNm', '기타용도': 'etcPurps',
                                  '전유부PK': 'mgmBldrgstPk', '층구분': 'flrGbCdNm', '층번호': 'flrNo', '층번호명': 'flrNoNm'}

                    elif ty == '층별':
                        parsing_type = 'getBrFlrOulnInfo'
                        column = {'주부속구분': 'mainAtchGbCdNm', '층구분': 'flrGbCdNm', '층번호': 'flrNo', '층명칭': 'flrNoNm', '층면적': 'area',
                                  '주구조': 'strctCdNm', '기타구조': 'etcStrct', '주용도': 'mainPurpsCdNm', '기타용도': 'etcPurps'}

                    elif ty == '지역지구':
                        parsing_type = 'getBrJijiguInfo'
                        column = {'기타지역지구구역': 'etcJijigu'}

                    url = 'http://apis.data.go.kr/1613000/BldRgstService_v2/' + parsing_type
                    params = {'serviceKey': self.key, 'sigunguCd': self.sigungu, 'bjdongCd': self.bjdong,
                              'bun': self.bun, 'ji': self.ji, 'platGbCd': '0', 'format': 'xml', 'numOfRows': '10000'}
                    if ty == '전유부': params['dongNm'] = self.dong

                result_data.append(pool.apply_async(OpenApiRequest.request_data, (url, params, column, keyword, )))

        try:
            for n, _ in enumerate(result_data):
                result_data[n] = result_data[n].get()
            pool.close()

        except Exception as e:
            pool.close()
            print(f'error: {e}')
            return

        self.threadEvent.workerThreadDone.emit(result_data)

    def get_days_data(self, url, column):
        # 현재, 작년, 재작년
        years = [datetime.now().year, datetime.now().year - 1, datetime.now().year - 2]
        for y in years:
            params = {'serviceKey': self.key, 'pnu': self.pnu, 'stdrYear': y, 'format': 'xml', 'numOfRows': '1000'}
            result_data = OpenApiRequest.request_data(url, params, column, 'field')
            if result_data is not None:
                return result_data
        return None
