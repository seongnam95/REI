import json
import sys
import requests
import module.bot.bld_register as ibl

from PySide6.QtCore import Qt, QSize, QObject, Signal, QThread
from PySide6.QtGui import QColor, QIcon
from PySide6.QtWidgets import QDialog, QGraphicsDropShadowEffect

from interface.public.get_address_lite import GetAddressLite
from ui.custom.LoadingBox import LoadingBox
from interface.info.resources.ui.ui_ledger import UiLedger


class IssuanceLedger(QDialog, UiLedger):
    def __init__(self, driver=None, login_cookies=None, address=None, data=None):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.existing, self.expos, self.success = None, None, False
        self.address, self.target_bld, self.target_ho = None, {}, {}
        self.total, self.bld_nml, self.bld_set = None, None, None
        self.issuance_thread = None

        # 셀러리움 세팅
        self.driver, self.login_cookies = None, None

        self._init_ui()
        self._init_interaction()

        if driver is None:
            self.issuance_thread = ibl.SetChrome('haul1115', 'ks05090818@')
            self.issuance_thread.threadEvent.chromeDriver.connect(self.get_chrome_driver)
            self.issuance_thread.start()
        else:
            self.driver, self.login_cookies = driver, login_cookies
            self.btn_issuance.setEnabled(True)

        if data is not None:
            self.existing, self.address = data, address

            bjr_nm = '' if address['법정리'] == '' else ' %s' % address['법정리']
            old = "%s %s %s%s %s" % (address['시도'], address['시군구'], address['읍면동'], bjr_nm, address['번'])
            if address['지'] != '0': old = "%s-%s" % (old, address['지'])

            self.edt_address.setText(old)

            self.loading_box.show_loading()
            self.get_title_thread = GetTitlesThread(self.address)
            self.get_title_thread.start()
            self.get_title_thread.threadEvent.doneEvent.connect(self.add_building_list)

    # UI 세팅
    def _init_ui(self):
        self.set_shadow()
        self.loading_box = LoadingBox(self)

        self.btn_search.setIcon(QIcon('../resources/img/search_icon.png'))
        self.btn_search.setIconSize(QSize(25, 25))

    # 시그널 세팅
    def _init_interaction(self):
        self.edt_address.mousePressEvent = self.clicked_address_edit
        self.edt_address.returnPressed.connect(self.clicked_address_edit)
        self.btn_search.clicked.connect(self.clicked_address_edit)

        self.cbx_buildings.activated.connect(self.select_building)
        self.cbx_rooms.activated.connect(self.select_room)

        self.btn_issuance.clicked.connect(self.clicked_issuance_btn)

    # 셀러리움 로그인 정보
    def get_chrome_driver(self, driver):
        self.driver = driver
        self.login_cookies = driver.get_cookies()
        self.btn_issuance.setEnabled(True)
        
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
        shadow.setBlurRadius(40)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        shadow.setColor(QColor(0, 0, 0, 60))
        self.btn_issuance.setGraphicsEffect(shadow)

    # 주소 검색
    def clicked_address_edit(self, e=None):
        address = self.edt_address.text()
        dialog = GetAddressLite(address)
        dialog.exec()

        if dialog.result is None: return
        if len(dialog.result) != 0:
            self.existing, self.success = None, False
            self.address = address = dialog.result

            bjr_nm = '' if address['법정리'] == '' else ' %s' % address['법정리']
            old = "%s %s %s%s %s" % (address['시도'], address['시군구'], address['읍면동'], bjr_nm, address['번'])
            if address['지'] != '0': old = "%s-%s" % (old, address['지'])

            self.edt_address.setText(old)
            self.edt_address.clearFocus()

            self.loading_box.show_loading()
            self.get_title_thread = GetTitlesThread(self.address)
            self.get_title_thread.start()
            self.get_title_thread.threadEvent.doneEvent.connect(self.add_building_list)

    # 주소 정보 입력
    def add_building_list(self, titles):
        self.loading_box.hide_loading()
        if not titles: return

        self.cbx_buildings.clear()
        self.cbx_rooms.clear()
        self.cbx_rooms.addItem('( 상세주소 / 호 )')

        # 총괄표제부, 일반/표제부 분리
        self.total, self.bld_nml, self.bld_set = None, [], []
        for i in titles:
            if '1' == i['regstrKindCd']: self.total = i
            elif '2' == i['regstrKindCd']: self.bld_nml.append(i)
            elif '3' == i['regstrKindCd']: self.bld_set.append(i)

        # 총괄 표제부 / 라디오 버튼
        self.rbtn_total.setEnabled(False) if self.total is None else self.rbtn_total.setEnabled(True)
        self.rbtn_building.setEnabled(True)

        # 일반 건물일 경우
        if self.bld_nml:
            self.cbx_rooms.hide()
            self.rbtn_building.setChecked(True)
            self.rbtn_room.setEnabled(False)
            self.cbx_buildings.resize(321, self.cbx_buildings.height())

            # 아이템 추가
            for i in self.bld_nml:
                bld_nm = i['bldNm']
                dong_nm = i['dongNm']

                if '없음' in bld_nm and '없음' in dong_nm: item = i['mainPrposNm']
                elif '없음' in dong_nm: item = '%s (%s)' % (bld_nm, i['mainPrposNm'])
                elif '없음' in dong_nm: item = dong_nm
                else: item = '%s (%s)' % (dong_nm, bld_nm)

                self.cbx_buildings.addItem(item)

            if self.existing:
                self.edt_address.clearFocus()

                for n, i in enumerate(self.bld_nml):
                    if str(i['bldrgstSeqno']) == str(self.existing['표제부PK']):
                        self.cbx_buildings.setCurrentIndex(n)
                        break

                self.cbx_buildings.setEnabled(True)
                self.select_building()
                return

            # 건물이 하나일 경우
            if len(self.bld_nml) == 1:
                self.target_bld = self.bld_nml[0]
                self.cbx_buildings.setEnabled(False)
                self.success = True

            else:
                self.cbx_buildings.setEnabled(True)
                self.cbx_buildings.showPopup()

        # 집합 건물일 경우
        elif self.bld_set:
            self.cbx_rooms.show()
            self.rbtn_room.setChecked(True)
            self.rbtn_room.setEnabled(True)
            self.cbx_buildings.resize(161, self.cbx_buildings.height())

            # 아이템 추가
            for i in self.bld_set:
                bld_nm = i['bldNm']
                dong_nm = i['dongNm']

                if '없음' in bld_nm and '없음' in dong_nm: item = i['mainPrposNm']
                elif '없음' in dong_nm: item = bld_nm
                elif '없음' in dong_nm: item = dong_nm
                else: item = '%s (%s)' % (dong_nm, bld_nm)

                self.cbx_buildings.addItem(item)

            if self.existing:
                self.edt_address.clearFocus()
                for n, i in enumerate(self.bld_set):
                    print(str(i['bldrgstSeqno']))
                    if str(i['bldrgstSeqno']) == str(self.existing['표제부PK']):
                        self.cbx_buildings.setCurrentIndex(n)
                        break

                self.cbx_buildings.setEnabled(True)
                self.select_building()
                return

            # 건물이 하나일 경우
            if len(self.bld_set) == 1:
                self.cbx_buildings.setEnabled(False)
                self.select_building()

            else:
                self.cbx_buildings.setEnabled(True)
                self.cbx_buildings.showPopup()

    # 호 리스트 추가
    def add_room_list(self, expos):
        self.loading_box.hide_loading()
        self.expos = expos
        self.cbx_rooms.clear()

        for i in self.expos:
            item = i['hoNm'].rstrip('호')
            self.cbx_rooms.addItem(f"{item}호")

        if self.existing:
            for n, i in enumerate(self.expos):
                print(str(i['bldrgstSeqno']))
                if str(i['bldrgstSeqno']) == str(self.existing['전유부PK']):
                    print(n)
                    self.cbx_rooms.setCurrentIndex(n)
                    break
            self.select_room()
            return

        self.cbx_rooms.showPopup()

    # 동 선택
    def select_building(self):
        if self.bld_nml:
            self.target_bld = dict(self.bld_nml[self.cbx_buildings.currentIndex()])
            self.success = True
            return

        self.target_bld = dict(self.bld_set[self.cbx_buildings.currentIndex()])

        self.loading_box.show_loading()
        self.get_expos_thread = GetExposThread(self.address, self.target_bld['bldrgstSeqno'])
        self.get_expos_thread.start()
        self.get_expos_thread.threadEvent.doneEvent.connect(self.add_room_list)

    # 호 선택
    def select_room(self):
        self.target_ho = self.expos[self.cbx_rooms.currentIndex()]
        self.loading_box.hide_loading()
        self.success = True

    # 발급 버튼 클릭
    def clicked_issuance_btn(self):
        if not self.success: return

        target_data = None
        if self.rbtn_total.isChecked(): target_data = self.total
        elif self.rbtn_building.isChecked(): target_data = self.target_bld
        elif self.rbtn_room.isChecked(): target_data = self.target_ho
            
        self.btn_issuance.setEnabled(False)

        self.loading_box.show_loading()
        self.issuance_thread = ibl.IssuanceBuildingLedger(target_data, self.driver, self.login_cookies)
        self.issuance_thread.threadEvent.workerThreadDone.connect(self.issuance_done_event)
        self.issuance_thread.start()

    # REQUEST
    #################################################################################################

    # 건축물대장 발급 스레드, 완료시
    def issuance_done_event(self):
        self.loading_box.hide_loading()
        self.btn_issuance.setEnabled(True)
        self.close()
        
    # 다이얼로그 엔터키 막기
    def keyPressEvent(self, event):
        if ((not event.modifiers() and
             event.key() == Qt.Key_Return) or
                (event.modifiers() == Qt.KeypadModifier)):
            event.accept()
        else: super(IssuanceLedger, self).keyPressEvent(event)


class ThreadSignal(QObject):
    doneEvent = Signal(object)


# 표제부, 일반건축물 조회
class GetTitlesThread(QThread):
    def __init__(self, address):
        super().__init__()
        self.threadEvent = ThreadSignal()

        self.s = requests.Session()
        self.headers = {
            "Referer": "https://cloud.eais.go.kr/moct/bci/aaa02/BCIAAA02L01",
            "Content-Type": "application/json;charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
        }

        sigungu = address['주소코드'][:5]
        self.datas = {"addrGbCd": "1", "bldrgstCurdiGbCd": "0", "reqSigunguCd": sigungu, "roadNmCd": address['도로명코드'],
                      "bldMnnm": address['건물본번'], "bldSlno": address['건물부번']}

    def run(self):
        response_title = self.s.post('https://cloud.eais.go.kr/bci/BCIAAA02R01', headers=self.headers, json=self.datas)
        json_data = json.loads(response_title.text)

        result = json_data['jibunAddr']

        self.s.close()
        self.threadEvent.doneEvent.emit(result)


# 전유부 조회
class GetExposThread(QThread):
    def __init__(self, address, pk):
        super().__init__()
        self.threadEvent = ThreadSignal()

        self.s = requests.Session()
        self.headers = {
            "Referer": "https://cloud.eais.go.kr/moct/bci/aaa02/BCIAAA02L01",
            "Content-Type": "application/json;charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
        }

        sigungu = address['주소코드'][:5]
        self.datas = {"inqireGbCd": "0", "reqSigunguCd": sigungu, "bldrgstCurdiGbCd": "0", "upperBldrgstSeqno": pk}

    def run(self):
        response_title = self.s.post('https://cloud.eais.go.kr/bci/BCIAAA02R04', headers=self.headers, json=self.datas)
        result = json.loads(response_title.text)['findExposList']

        self.s.close()
        self.threadEvent.doneEvent.emit(result)


# 예외 오류 처리
def my_exception_hook(exctype, value, traceback):
    sys.excepthook(exctype, value, traceback)


sys._excepthook = sys.excepthook
sys.excepthook = my_exception_hook


# app = QApplication()
# window = IssuanceLedger()
# app.exec()
