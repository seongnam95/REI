import json
import sys

import pandas as pd
import requests
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QColor, QIcon
from PySide6.QtWidgets import QDialog, QApplication, QGraphicsDropShadowEffect

import rei_bot.issuance_register_of_building as ibl
from interface.sub_interface import find_address_lite
from ui.custom.LoadingBox import LoadingBox
from ui.dialog.ui_ledger import Ui_Ledger


class LedgerLedger(QDialog, Ui_Ledger):
    def __init__(self, data=None):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.address, self.info = None, {}
        self.title_pk, self.expos_pk = None, None
        self.issuance_thread = None

        # 리퀘스트, 셀러리움 세팅
        self.s = requests.Session()
        self.headers = {
            "Referer": "https://cloud.eais.go.kr/moct/bci/aaa02/BCIAAA02L01",
            "Content-Type": "application/json;charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
        }
        self.driver, self.login_cookies = None, None

        self._init_ui()
        self._init_interaction()

        if data is not None:
            self.address = data
            self.input_address_edit()

    # UI 세팅
    def _init_ui(self):
        self.loading_box = LoadingBox(self)

        self.set_shadow()
        self.btn_search.setIcon(QIcon('../../data/img/button/search_icon.png'))
        self.btn_search.setIconSize(QSize(25, 25))

        self.issuance_thread = ibl.SetChrome('haul1115', 'ks05090818@')
        self.issuance_thread.threadEvent.chromeDriver.connect(self.get_chrome_driver)
        self.issuance_thread.start()

    # 시그널 세팅
    def _init_interaction(self):
        self.edt_address.mousePressEvent = self.clicked_address_edit
        self.edt_address.returnPressed.connect(self.clicked_address_edit)
        self.btn_search.clicked.connect(self.clicked_address_edit)

        self.cbx_buildings.activated.connect(self.add_room_list)
        self.cbx_rooms.activated.connect(self.select_room)

        self.btn_issuance.clicked.connect(self.clicked_issuance_btn)

    # 셀러리움 로그인 정보
    def get_chrome_driver(self, driver):
        self.driver = driver
        self.login_cookies = driver.get_cookies()
        self.btn_issuance.setEnabled(True)
        print('로그인 완료 !')
        
    # UI 그림자 설정
    def set_shadow(self):
        for child in [self.address_frame, self.type_frame]:
            shadow = QGraphicsDropShadowEffect(self)
            shadow.setBlurRadius(15)
            shadow.setXOffset(1)
            shadow.setYOffset(1)
            shadow.setColor(QColor(0, 0, 0, 35))
            child.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(15)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        shadow.setColor(QColor(0, 0, 0, 80))
        self.btn_issuance.setGraphicsEffect(shadow)

    # 주소 검색
    def clicked_address_edit(self, e=None):
        address = self.edt_address.text()
        dialog = find_address_lite.FindAddressLite(address)
        dialog.exec()

        if dialog.result is None: return
        if len(dialog.result) != 0:
            self.address = dialog.result
            self.input_address_edit()
            self.edt_address.clearFocus()

            self.btn_issuance.setEnabled(True)

    # 주소 정보 입력
    def input_address_edit(self):
        address = self.address

        old = "%s %s %s %s" % (address['시도'], address['시군구'], address['읍면동'], address['번'])
        if address['지'] != '0': old = "%s-%s" % (old, address['지'])

        pk = self.get_address(old, address['도로명주소'])
        if pk:
            self.edt_address.setText(old)
            self.info['건물'] = pk

            self.add_building_list()

        else: print('검색 결과 없음')

    # 동 리스트 추가
    def add_building_list(self):
        self.title_pk = self.get_title(self.info['건물']['ID'])

        # 총괄표제부 표시 여부
        if '-' not in self.info['건물']['ID']: self.rbtn_total.setEnabled(False)
        else: self.rbtn_total.setEnabled(True)

        # 일반 건축물일 경우
        if self.title_pk.empty:
            self.info['타입'] = '일반'

            self.cbx_buildings.clear()
            self.cbx_buildings.addItem('-- 항목없음 --')
            self.cbx_buildings.setEnabled(False)

            self.cbx_rooms.clear()
            self.cbx_rooms.addItem('-- 항목없음 --')
            self.cbx_rooms.setEnabled(False)

            self.rbtn_room.setEnabled(False)
            self.rbtn_building.setEnabled(True)
            self.rbtn_building.setChecked(True)

            self.btn_issuance.setEnabled(True)

        # 집합 건축물일 경우
        else:
            self.info['타입'] = '집합'

            self.cbx_buildings.clear()
            self.cbx_rooms.clear()
            self.cbx_rooms.addItem('( 상세주소 / 호)')

            self.cbx_buildings.setEnabled(True)
            self.cbx_rooms.setEnabled(True)
            self.rbtn_room.setEnabled(True)

            self.rbtn_room.setChecked(True)

            for i in range(len(self.title_pk)):
                row = self.title_pk.loc[i]
                item = '%s (%s)' % (row['동명칭'], self.address['건물명칭']) if self.address['건물명칭'] else row['동명칭']
                self.cbx_buildings.addItem(item)

            if len(self.title_pk) == 1:
                self.add_room_list()
                return

            self.cbx_buildings.showPopup()

    # 호 리스트 추가
    def add_room_list(self):
        self.info['동'] = self.title_pk.loc[self.cbx_buildings.currentIndex()]
        self.expos_pk = self.get_expos(self.info['동']['PK'])

        self.cbx_rooms.clear()
        self.cbx_rooms.setEnabled(True)

        for i in range(len(self.expos_pk)):
            row = self.expos_pk.loc[i]
            self.cbx_rooms.addItem(f"{row['호명칭']} 호")

        self.cbx_rooms.showPopup()

    # 호 선택
    def select_room(self):
        self.info['호'] = self.expos_pk.loc[self.cbx_rooms.currentIndex()]
        self.btn_issuance.setEnabled(True)

    # 발급 버튼 클릭
    def clicked_issuance_btn(self):
        kind, pk = None, None

        if self.rbtn_total.isChecked():
            kind, pk = 0, self.info['건물']['ID']
            print(pk)

        elif self.rbtn_building.isChecked():
            kind, pk = 1, self.info['건물']['PK'] if self.info['타입'] == '일반' else self.info['동']['PK']
            
        elif self.rbtn_room.isChecked():
            kind, pk = 2, self.info['호']['PK']
            
        self.btn_issuance.setEnabled(False)
        self.loading_box.show_loading()

        self.issuance_thread = ibl.IssuanceBuildingLedger(pk, kind, self.driver, self.login_cookies)
        self.issuance_thread.threadEvent.workerThreadDone.connect(self.issuance_done_event)
        self.issuance_thread.threadEvent.progress.connect(self.issuance_progress_event)
        self.issuance_thread.start()

    # REQUEST
    #################################################################################################

    def get_address(self, old, new):
        datas = {"query": {"multi_match": {"query": new,
                                           "type": "cross_fields",
                                           "operator": "and",
                                           "fields": ["jibunAddr", "roadAddr^3"],
                                           "tie_breaker": 0.3}}, "size": 20}

        res = self.s.post('https://cloud.eais.go.kr/bldrgstmst/_search', headers=self.headers, json=datas)
        json_result = json.loads(res.text)['hits']

        for n, i in enumerate(json_result['hits']):
            res_old = i['_source']['jibunAddr']
            if old in res_old:
                info = i['_source']
                result = {'주소': info['jibunAddr'], '도로명주소': info['roadAddr'], 'ID': info['mgmUpperBldrgstPk'], 'PK': i['_id']}
                return result

    def get_title(self, pk):
        datas = {"sort": [{"dongNm": "asc"}], "query": {"bool": {"filter": [{"term": {"mgmUpperBldrgstPk": pk}}]}},
                 "size": 100}
        res = self.s.post('https://cloud.eais.go.kr/bldrgsttitle/_search', headers=self.headers, json=datas)
        json_result = json.loads(res.text)['hits']

        result = pd.DataFrame(columns=['동명칭', 'ID', 'PK'])

        for n, i in enumerate(json_result['hits']):
            result.loc[n] = {'동명칭': i['_source']['dongNm'], 'ID': i['_source']['mgmUpperBldrgstPk'], 'PK': i['_id']}

        result = result.sort_values(by=['동명칭'], axis=0)
        result.reset_index(drop=True, inplace=True)

        return result

    def get_expos(self, pk):
        datas = {"sort": [{"hoNm": "asc"}], "query": {"bool": {"filter": [{"term": {"mgmUpperBldrgstPk": pk}}]}},
                 "size": 200}
        res = self.s.post('https://cloud.eais.go.kr/bldrgstexpos/_search', headers=self.headers, json=datas)
        json_result = json.loads(res.text)['hits']

        result = pd.DataFrame(columns=['동명칭', '호명칭', 'PK'])

        for n, i in enumerate(json_result['hits']):
            info = i['_source']
            result.loc[n] = {'동명칭': info['dongNm'], '호명칭': info['hoNm'], 'PK': i['_id']}

        try: result['호명칭'] = pd.to_numeric(result['호명칭'])
        except: pass

        result = result.sort_values(by=['호명칭'], axis=0)
        result.reset_index(drop=True, inplace=True)

        return result

    #################################################################################################

    def issuance_done_event(self, success):
        self.btn_issuance.setEnabled(True)
        self.loading_box.hide_loading()
        
        if not success:
            print('오류 발생')

    # 진행 메세지
    def issuance_progress_event(self, msg):
        print(msg)
        
    # 다이얼로그 엔터키 막기
    def keyPressEvent(self, event):
        if ((not event.modifiers() and
             event.key() == Qt.Key_Return) or
                (event.modifiers() == Qt.KeypadModifier)):
            event.accept()
        else: super(LedgerLedger, self).keyPressEvent(event)



# 예외 오류 처리
def my_exception_hook(exctype, value, traceback):
    sys.excepthook(exctype, value, traceback)


sys._excepthook = sys.excepthook
sys.excepthook = my_exception_hook

#
# app = QApplication()
# window = LedgerLedger()
# app.exec()
