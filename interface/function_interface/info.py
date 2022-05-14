import sys
import webbrowser
import psutil

import clipboard as clip
import pandas as pd
import module.open_api_pars as pars
import rei_bot.issuance_register_of_building as ibl

from urllib.parse import urlencode
from PySide6.QtCore import QObject, Signal, QEvent, QSize
from PySide6.QtGui import QIcon, QColor
from PySide6.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect, QFrame

from module.open_api_pars import OpenApiRequest
from interface.sub_interface import issuance_ledger, issuance_register, find_address_details, find_address_lite
from ui.custom import BlackBoxMsg, MenuWidget, LoadingBox
from ui.main.ui_info import Ui_BuildingInfo


# import fluentapp.pyqt6.windowtools as wingui

# from BlurWindow.blurWindow import blur
# blur(self.winId())


class BuildingInfo(QMainWindow, Ui_BuildingInfo):
    def __init__(self):
        super(BuildingInfo, self).__init__()

        self.BULIDING_API_KEY = 'sfSPRX+xNEExRUqE4cdhNjBSk4uXIv8F1CfLen06hdPGn5cflLJqy/nxmh48uF8fvdGk68k6Z5jWsU1n6BeNPA=='
        self.VIOL_KEY = '68506e6c486a736e35377562445658'

        # 기본 변수
        self.activation, self.opened, self.first, self.issuance = False, False, False, False
        self.data_basic, self.data_basic_all = None, None
        self.get_building_thread, self.issuance_thread = None, None  # 토지, 지역지구, 공시지가 스레드

        # 건축물 정보
        self.address, self.title, self.total = None, None, None         # 주소, 표제부, 총괄표제부
        self.res_exact_expos, self.res_expos = None, None               # ALL 전유부(전용), ALL 전유부/층(전용, 공용)
        self.land, self.owners, self.prices = None, None, None          # 전유부(단일), 토지, 소유자, 공시가
        self.expos, self.expos_tot = None, None                         # 전유부(전용), 전유부/층(전용, 공용)

        self.driver, self.login_cookies = None, None
        self.issuance_data = {}

        # 폼 설정
        self._init_ui()
        self._init_shadows()
        self._init_interaction()

        # self.btn_issuance.setEnabled(False)

        # self.login_progress(False)
        # self.issuance_thread = ibl.SetChrome('haul1115', 'ks05090818@')
        # self.issuance_thread.threadEvent.chromeDriver.connect(self.get_chrome_driver)
        # self.issuance_thread.start()

    # UI 세팅
    def _init_ui(self):
        self._setupUi(self)

        self.msg = BlackBoxMsg.BoxMessage(self)
        self.loading_box = LoadingBox.LoadingBox(self)

        self.block_frame = QFrame(self)
        self.block_frame.setStyleSheet("QFrame { background: rgba(0, 0, 0, 160)}")
        self.block_frame.hide()

        # 메뉴 위젯 설정
        items = [{'name': '내 매물로 등록', 'img': '../../data/img/button/plus_square_icon.png'},
                 {'name': '계약서 작성', 'img': '../../data/img/button/pen_icon.png'},
                 {'name': '광고 업로드', 'img': '../../data/img/button/upload_icon.png'},
                 {'name': '매물 공유하기', 'img': '../../data/img/button/share_icon.png'},
                 {'name': '설정', 'img': '../../data/img/button/setting_icon.png'}]

        self.main_menu = MenuWidget.MenuWidget(self)
        self.main_menu.add_item(items)
        self.main_menu.set_size(self.main_menu)

        issuance_items = [{'name': '건축물대장', 'img': None},
                          {'name': '등기부등본', 'img': None},
                          {'name': '토지이용계획', 'img': None}]
        self.issuance_menu = MenuWidget.MenuWidget(self)
        self.issuance_menu.add_item(issuance_items)
        self.issuance_menu.set_size(self.issuance_menu)

        # 버튼 이미지 설정
        self.btn_search.setIcon(QIcon('../../data/img/button/search_icon.png'))
        self.btn_search.setIconSize(QSize(30, 30))
        self.btn_menu.setIcon(QIcon('../../data/img/button/menu_icon.png'))
        self.btn_menu.setIconSize(QSize(20, 20))
        self.btn_issuance.setIcon(QIcon('../../data/img/button/print_icon.png'))
        self.btn_search.setIconSize(QSize(23, 23))

        # 이벤트 필터 (마우스 HOVER 시, 그림자 효과 관련)
        self.btn_viol.installEventFilter(self)
        self.btn_menu.installEventFilter(self)
        self.btn_issuance.installEventFilter(self)

        # 라벨 위젯 리스트에 추가
        self.labels = {'소재지': self.base_item_1,
                       '도로명': self.base_item_2,
                       '상세주소': self.base_item_3,
                       '주용도': self.base_item_4,
                       '공급면적': self.base_item_5,
                       '승강기': self.base_item_6,
                       '주차장': self.base_item_7,
                       '전용면적': self.base_item_8,
                       '총층수': self.base_item_9,
                       '소유자': self.base_item_10,
                       '호가구세대': self.base_item_11,
                       '사용승인일': self.base_item_12,
                       '공시가격': self.base_item_13}
        self.labels_detail = {'주구조': self.detail_item_1,
                              '지역지구': self.detail_item_2,
                              '주용도': self.detail_item_3,
                              '대지면적': self.detail_item_4,
                              '건축면적': self.detail_item_5,
                              '건폐율': self.detail_item_6,
                              '연면적': self.detail_item_7,
                              '높이': self.detail_item_8,
                              '용적률': self.detail_item_9}
        self.labels_park = {'옥내자주식': self.park_item_1,
                            '옥내기계식': self.park_item_2,
                            '옥외자주식': self.park_item_3,
                            '옥외기계식': self.park_item_4}
        self.labels_land = {'공시지가': self.land_item_1,
                            '토지지역지구': self.land_item_2,
                            '토지기타지역지구': self.land_item_3}

        self.show()

    def _init_shadows(self):
        frame_list = [self.address_frame, self.info_frame, self.detail_frame, self.parking_frame, self.land_frame]
        for child in frame_list:
            shadow = QGraphicsDropShadowEffect(self)
            shadow.setBlurRadius(15)
            shadow.setXOffset(1)
            shadow.setYOffset(1)
            shadow.setColor(QColor(0, 0, 0, 35))
            child.setGraphicsEffect(shadow)

    # 상호작용 세팅
    def _init_interaction(self):

        # 기타 상호작용 이벤트
        self.cbx_rooms.activated.connect(self.insert_room_info)
        self.edt_address.mousePressEvent = self.clicked_address_edit
        self.edt_address.returnPressed.connect(self.clicked_address_edit)

        # 버튼 클릭 이벤트
        self.btn_search.clicked.connect(self.clicked_address_edit)
        self.btn_details.clicked.connect(self.clicked_details_btn)
        self.btn_viol.clicked.connect(self.clicked_viol_btn)

        # 메뉴 클릭 이벤트
        self.btn_menu.clicked.connect(self.clicked_menu_btn)
        self.btn_issuance.clicked.connect(self.clicked_issuance_btn)
        self.main_menu.itemClicked.connect(self.test)
        self.issuance_menu.itemClicked.connect(self.clicked_issuance_menu)

        # 라벨 더블 클릭 이벤트
        for dic in [self.labels, self.labels_detail, self.labels_park, self.labels_land]:
            for i in dic: mouse_double_clicked(dic[i]).connect(self.clicked_labels)

    # 셀러리움 로그인 정보
    def get_chrome_driver(self, driver):
        self.driver = driver
        self.login_cookies = driver.get_cookies()
        print('로그인 완료')

    ##### 시그널 이벤트
    ########################################################################################################

    def test(self):
        print(self.main_menu.currentRow())

    # 항목 클립보드에 복사
    def clicked_labels(self, widget):
        item_text = widget.text().rstrip(' ㎡').rstrip(' %').rstrip(' 대')
        if item_text != '':
            clip.copy(item_text)
            self.msg.show_msg(2000, 'center', "클립보드에 복사 되었습니다.\n( 단축키 Ctrl + V 로 붙혀넣기 가능)")

    # 소재지 찾기 에디트 클릭
    def clicked_address_edit(self, e):
        dialog = find_address_details.AddressDetails(self.edt_address.text())
        dialog.exec()

        if dialog.result:
            self.address, self.title, self.total = dialog.address, dialog.title, dialog.total  # 주소, 표제부, 총괄표제부
            self.res_exact_expos, self.res_expos = dialog.res_exact_expos, dialog.res_expos    # ALL 전유부(전용), ALL 전유부/층(전용, 공용)
            self.land, self.owners, self.prices = dialog.land, dialog.owners, dialog.prices    # 토지, 소유자, 공시가
            self.expos, self.expos_tot = dialog.expos, dialog.expos_tot                        # 전유부(전용), 전유부/층(전용, 공용)
            
            # UI 세팅
            self.cbx_rooms.clear()
            self.cbx_rooms.addItems(dialog.expos_list)
            self.cbx_rooms.setCurrentIndex(dialog.select_index)

            self.activation, self.first = True, True
            self.insert_base_info()
            self.btn_issuance.setEnabled(True)

            if self.opened: self.clicked_details_btn()

    # 위반 조회 버튼
    def clicked_viol_btn(self):
        if self.lb_viol.text(): return

        if self.title['대장구분'] == '집합': viol = OpenApiRequest.get_viol(self.VIOL_KEY, self.expos['전유부PK'])
        else: viol = OpenApiRequest.get_viol(self.VIOL_KEY, self.title['표제부PK'])

        if viol == '0':
            self.lb_viol.setText('위반 없음')
            self.lb_viol.setStyleSheet("""#lb_viol {
                                        background-color: rgb(245, 245, 245);
                                        font: 15px "웰컴체 Regular";
                                        color: rgb(46, 204, 113);
                                        padding-top: 2px;
                                        border: 2px solid rgb(46, 204, 113);
                                        border-radius: 3px; }""")

        elif viol == '1':
            self.lb_viol.setText('위반 건축물')
            self.lb_viol.setStyleSheet("""#lb_viol {
                                        background-color: rgb(245, 245, 245);
                                        font: 15px "웰컴체 Regular";
                                        color: rgb(192, 57, 43);
                                        padding-top: 2px;
                                        border: 2px solid rgb(192, 57, 43);
                                        border-radius: 3px; }""")

        else:
            self.lb_viol.setText('조회 불가')
            self.lb_viol.setStyleSheet("""#lb_viol {
                                        background-color: rgb(245, 245, 245);
                                        font: 15px "웰컴체 Regular";
                                        color: rgb(127, 140, 141);
                                        padding-top: 2px;
                                        border: 2px solid rgb(127, 140, 141);
                                        border-radius: 3px; }""")

    # 상세정보 버튼 클릭
    def clicked_details_btn(self):
        if not self.activation: return

        # 처음 열 경우 정보 불러오기
        if self.first:
            self.get_building_thread = pars.DataRequestThread(self.address, self.BULIDING_API_KEY,
                                                              ['지역지구', '토지용도지역지구', '토지'])
            self.get_building_thread.start()
            self.get_building_thread.threadEvent.workerThreadDone.connect(self.insert_detail_info)
            self.first = False

        self.resize_form(self.opened)

    # 문서 발급 버튼
    def clicked_issuance_menu(self):
        # if not self.activation: return
        item_row = self.issuance_menu.currentRow()
        self.issuance_menu.hide_menu()

        # 건축물대장
        if item_row == 0:
            self.block_frame.setGeometry(0, 0, self.width(), self.height())
            self.block_frame.show()

            if self.issuance_data:
                dialog = issuance_ledger.IssuanceLedger(self.driver, self.login_cookies, self.address,
                                                        self.issuance_data)
            else:
                dialog = issuance_ledger.IssuanceLedger(self.driver, self.login_cookies)
            dialog.exec()

            self.block_frame.hide()

        # 등기부등본
        elif item_row == 1:
            self.block_frame.setGeometry(0, 0, self.width(), self.height())
            self.block_frame.show()

            if self.issuance_data:
                dialog = issuance_register.IssuanceRegister(self.address, self.issuance_data)
            else:
                dialog = issuance_register.IssuanceRegister()
            dialog.exec()

            self.block_frame.hide()

        # 토지이용계획
        elif item_row == 2:
            address = self.edt_address.text()
            dialog = find_address_lite.FindAddressLite(address)
            dialog.exec()

            if dialog.result is None: return
            if len(dialog.result) != 0:
                address = dialog.result
                code = address['주소코드']
                bun, ji = address['번'].zfill(4), address['지'].zfill(4)
                pnu = f'{code}1{bun}{ji}'

                url = 'http://www.eum.go.kr/web/ar/lu/luLandDetPrintPop.jsp?'
                params = urlencode({'isNoScr': 'script', 'mode': 'search', 'pnu': pnu})
                webbrowser.open_new(url + params)

    # 메뉴 열기 버튼
    def clicked_menu_btn(self):
        if self.main_menu.menu_toggle:
            self.main_menu.hide_menu()
        else:
            self.main_menu.show_menu(self.btn_menu)

    # 발급목록 열기 버튼
    def clicked_issuance_btn(self):
        if self.issuance_menu.menu_toggle:
            self.issuance_menu.hide_menu()
        else:
            self.issuance_menu.show_menu(self.btn_issuance)

    # 이벤트 필터 (버튼 이펙트)
    def eventFilter(self, obj, event):
        objs = {self.btn_viol: 'viol',
                self.btn_menu: 'menu',
                self.btn_issuance: 'menu'}
        if obj not in objs.keys(): return

        # 버튼 이펙트 (쉐도우)
        if event.type() == QEvent.HoverEnter:  # ON
            obj.setGraphicsEffect(self.set_shadow(objs[obj]))
        elif event.type() == QEvent.HoverLeave:  # OFF
            obj.setGraphicsEffect(self.set_shadow('reset'))

        return super(BuildingInfo, self).eventFilter(obj, event)

    # 그림자 세팅
    def set_shadow(self, kind):
        shadow = QGraphicsDropShadowEffect(self)

        if kind == 'menu':
            shadow.setBlurRadius(10)
            shadow.setXOffset(0)
            shadow.setYOffset(0)
            shadow.setColor(QColor(0, 0, 0, 70))

        elif kind == 'viol':
            shadow.setBlurRadius(20)
            shadow.setXOffset(0)
            shadow.setYOffset(0)
            shadow.setColor(QColor(255, 120, 90, 250))

        elif kind == 'reset':
            shadow.setEnabled(False)

        return shadow

    ##### 데이터 입력
    ########################################################################################################

    # 기본 데이터 입력
    def insert_base_info(self):
        address, title, total = self.address, self.title, self.total

        layer = "-%s 층 / %s 층" % (title['지하층수'], title['지상층수'])
        elevator = "%s대 (비상 %s대)" % (title['승강기'], title['비상용승강기'])
        room_count = "%s 호 / %s 가구 / %s 세대" % (title['호수'], title['가구수'], title['세대수'])
        day = "%s년 %s월 %s일" % (title['사용승인일'][0:4], title['사용승인일'][4:6], title['사용승인일'][6:8])

        parking = str(sum(map(int, [title['옥내기계식대수'], title['옥내자주식대수'],
                                    title['옥외기계식대수'], title['옥외자주식대수']])))
        if total is not None:
            if parking == '0':
                parking = str(sum(map(int, [total['옥내기계식대수'], total['옥내자주식대수'],
                                            total['옥외기계식대수'], total['옥외자주식대수']])))

        # 같은 키에 값 입력
        base = {'소재지': address['주소'], '도로명': address['도로명주소'],
                '승강기': elevator, '주차장': f"{parking} 대", '총층수': layer, '호가구세대': room_count, '사용승인일': day}

        for i in base:
            if i in self.labels:
                self.labels[i].setText(base[i])

        self.edt_address.setText(address['주소'])
        self.insert_room_info()

    # 기본 데이터 룸/층별 입력
    def insert_room_info(self):
        title = self.title

        # 위반 건축물 라벨 초기화
        self.lb_viol.setText('')
        self.lb_viol.setStyleSheet('#lb_viol { background-color: rgb(245, 245, 245); }')

        #### 일반일 경우
        if title['대장구분'] == '일반':
            expos = self.res_expos.loc[self.cbx_rooms.currentIndex()]
            room_area, public_area = expos['층면적'], ''
            room = "%s층" % expos['층명칭'].rstrip("층")
            if title['동명칭']: room = "%s동 %s" % (title['동명칭'].rstrip("동"), room)
            pk = title['표제부PK']

            try:
                print(self.prices)
                price_day = self.prices['공시일자'].values[0].split('-')
                price = str("{:,}".format(int(self.prices['개별주택가격'])) + ' 원')
                price = '%s (%s년 %s월)' % (price, price_day[0], price_day[1])

            except (ValueError, IndexError, TypeError):
                price = "조회 결과 없음"

        #### 집합일 경우
        else:
            expos = self.res_exact_expos.loc[self.cbx_rooms.currentIndex()]
            self.expos_tot = self.res_expos[self.res_expos['호명칭'] == expos['호명칭']]

            room_area = expos['전용면적']
            public_area = round(pd.to_numeric(self.expos_tot['전용면적']).sum(), 2)
            room = "%s호" % expos['호명칭'].rstrip("호")
            if expos['동명칭']: room = "%s동 " % (expos['동명칭'].rstrip("동")) + room
            pk = expos['전유부PK']

            try:
                print(self.prices)
                prices = self.prices[self.prices['호명칭'] == expos['호명칭']]
                price_day = prices['공시일자'].values[0].split('-')
                price = str("{:,}".format(int(prices['공동주택가격'].values[0])) + ' 원')
                price = '%s (%s년 %s월)' % (price, price_day[0], price_day[1])

            except (ValueError, IndexError, TypeError):
                price = "조회 결과 없음"

        # 건물 명칭이 있을 경우
        if title['건물명칭']:
            room = "%s (%s)" % (room, title['건물명칭'])

        try:
            owners = self.owners[self.owners['건축물대장PK'] == pk]
            owner_count = len(owners)
            if owner_count == 1: owner = "%s | %s" % (owners.iloc[0]['소유자명'], owners.iloc[0]['소유구분명'])
            else: owner = "%s명 (%s|%s)" % (str(len(owners)), owners.iloc[0]['소유자명'], owners.iloc[0]['소유구분명'])

        except (ValueError, TypeError, IndexError):
            owner = "소유자 확인 불가"

        base = {'상세주소': room, '주용도': expos['기타용도'], '공급면적': str(public_area) + " ㎡",
                '전용면적': str(room_area) + " ㎡", '소유자': owner, '공시가격': price}

        # 같은 키에 값 입력
        for i in base:
            if i in self.labels:
                self.labels[i].setText(base[i])

    # 상세 정보 입력
    def insert_detail_info(self, val):
        title = self.title

        in_land = int(title['옥내자주식대수'])
        in_mechanical = int(title['옥내기계식대수'])

        out_land = int(title['옥외자주식대수'])
        out_mechanical = int(title['옥외기계식대수'])

        # 용도지역지구
        if val[0] is None: jiji = '조회 결과 없음'
        else: jiji = ', '.join(val[0]['기타지역지구구역'])

        # 총괄 표제부 주차장
        if self.total is not None:
            total = self.total
            in_land += int(total['옥내자주식대수'])
            in_mechanical += int(total['옥내기계식대수'])

            out_land += int(total['옥외자주식대수'])
            out_mechanical += int(total['옥외기계식대수'])

        # 토지 이용
        if val[1] is None:
            land_jj = '조회 결과 없음'
            land_etc = '조회 결과 없음'

        else:
            land_jj, land_etc = [], []
            for i in val[1]['용도지역지구명']:
                if (i[-2:] == '지구') or (i[-2:] == '지역'):
                    land_jj.append(i)
                else:
                    land_etc.append(i)

            land_jj = ', '.join(land_jj)
            land_etc = ', '.join(land_etc)

        price = str("{:,}".format(int(val[2]['공시지가'])) + ' 원 (㎡ 기준)')

        base = {'주구조': title['주구조'], '지역지구': jiji, '주용도': title['주용도'],
                '대지면적': val[2]['대지면적'].values[0] + ' ㎡', '건축면적': title['건축면적'] + ' ㎡', '건폐율': title['건폐율'] + ' %',
                '연면적': title['연면적'] + ' %', '높이': title['높이'], '용적률': title['용적률'] + ' %',
                '옥내자주식': str(in_land) + ' 대', '옥내기계식': str(in_mechanical) + ' 대',
                '옥외자주식': str(out_land) + ' 대', '옥외기계식': str(out_mechanical) + ' 대',
                '공시지가': price, '토지지역지구': land_jj, '토지기타지역지구': land_etc}

        for i in base:
            if i in self.labels_detail:
                self.labels_detail[i].setText(base[i])
            if i in self.labels_park:
                self.labels_park[i].setText(base[i])
            if i in self.labels_land:
                self.labels_land[i].setText(base[i])

    ##### UI 세팅
    ########################################################################################################

    # 타이틀바 라벨 위치 세팅
    def resize_title_bar(self):
        title_x = (self.width() / 2) - (self.lb_title.width() / 2)
        self.lb_title.move(title_x, self.lb_title.y())

        sub_title_x = (self.width() / 2) - (self.lb_sub_title.width() / 2)
        self.lb_sub_title.move(sub_title_x, self.lb_sub_title.y())

        self.btn_menu.move(self.width() - 50, self.btn_menu.y())

    # 폼 사이즈 변경
    def resize_form(self, opened):
        if opened:  # 열려있을 경우
            self.setMinimumWidth(471)  # 닫기
            self.setMaximumWidth(471)
            self.btn_details.setText("상세정보  >")
            self.opened = False
        else:
            self.setMinimumWidth(921)  # 열기
            self.setMaximumWidth(921)
            self.btn_details.setText("접 기  <")
            self.opened = True

        self.resize_title_bar()

    # 메뉴 외부 영역 클릭시 메뉴 숨김
    def mousePressEvent(self, event):
        if self.issuance_menu.menu_toggle:
            self.issuance_menu.hide_menu()
        if self.main_menu.menu_toggle:
            self.main_menu.hide_menu()

    # 로그인 프로그래스 바
    def login_progress(self, active):
        if active:
            self.progress_bar.setMaximum(0)
            self.lb_progress.setText('세움터 로그인중..')
            self.lb_progress.setHidden(False)
            self.progress_bar.setHidden(False)
        else:
            self.lb_progress.setHidden(True)
            self.progress_bar.setHidden(True)

    def closeEvent(self, event):
        if self.driver:
            self.driver.quit()
            for proc in psutil.process_iter():
                PROCNAME = 'chromedriver.exe'
                if proc.name() == PROCNAME:
                    proc.kill()


# 더블 클릭 이벤트
def mouse_double_clicked(widget):
    class Filter(QObject):
        clicked = Signal(QObject)

        def eventFilter(self, obj, event):
            if obj == widget:
                if event.type() == QEvent.MouseButtonDblClick:
                    if obj.rect().contains(event.position().toPoint()):
                        self.clicked.emit(widget)
                        return True
            return False

    evt_filter = Filter(widget)
    widget.installEventFilter(evt_filter)
    return evt_filter.clicked
    ########################################################################################################


# 예외 오류 처리
def my_exception_hook(exctype, value, traceback):
    sys.excepthook(exctype, value, traceback)


sys._excepthook = sys.excepthook
sys.excepthook = my_exception_hook

app = QApplication()
window = BuildingInfo()
app.exec()
