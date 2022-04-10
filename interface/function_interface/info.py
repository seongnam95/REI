import sys

import clipboard as clip
import pandas as pd
from PySide6.QtCore import QObject, Signal, QEvent, QPropertyAnimation, QSize, QPoint, QParallelAnimationGroup
from PySide6.QtGui import Qt, QIcon, QColor, QMovie
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QGraphicsOpacityEffect, QGraphicsDropShadowEffect

import module.open_api_pars as pars
import rei_bot.issuance_register_of_building as ibl

from interface.sub_interface import address_details
from module.black_box_msg import BoxMessage
from module.open_api_pars import OpenApiRequest
from ui.main.ui_info import Ui_BuildingInfo
from module.menu_widget import MenuWidget


# import fluentapp.pyqt6.windowtools as wingui

# from BlurWindow.blurWindow import blur
# blur(self.winId())


class BuildingInfo(QMainWindow, Ui_BuildingInfo):
    def __init__(self):
        super(BuildingInfo, self).__init__()

        self.BULIDING_API_KEY = 'sfSPRX+xNEExRUqE4cdhNjBSk4uXIv8F1CfLen06hdPGn5cflLJqy/nxmh48uF8fvdGk68k6Z5jWsU1n6BeNPA=='
        self.VIOL_KEY = '68506e6c486a736e35377562445658'

        self.activation, self.opened, self.first, self.issuance = False, False, False, False
        self.data_basic, self.data_basic_all = None, None
        self.base_list = []

        self.get_building_thread, self.issuance_thread = None, None     # 토지, 지역지구, 공시지가 스레드
        self.binfo, self.address = None, None
        self.select_building, self.total_buildings = None, None
        self.detail, self.exact_detail = None, None  # 상세 (호, 층)
        self.owners, self.prices, self.pk = None, None, None  # 소유자, 공시가격, 건축물대장 PK
        self.driver, self.login_cookies = None, None
        self.issuance_data = {}

        self._init_ui()
        self._set_anim()
        self.btn_issuance.setEnabled(False)

        self.msg = BoxMessage(self)
        self.add_btn_tip = TipBox(self.top_bar)
        self.add_btn_tip.set_box(self.btn_add, '매물 등록', 'right')
        self.issuance_btn_tip = TipBox(self.bot_bar)
        self.issuance_btn_tip.set_box(self.btn_issuance, '건축물대장/등기부등본 발급', 'right')

        items = [{'name': '내 매물로 등록', 'img': '../../data/img/button/plus_icon.png'},
                 {'name': '매물 공유하기', 'img': '../../data/img/button/share_icon.png'},
                 {'name': '계약서 작성', 'img': '../../data/img/button/plus_icon.png'}]

        self.menu_widget = MenuWidget(self)
        self.menu_widget.add_item(items)
        self.menu_widget.set_size(self.menu_widget)
        self.menu_widget.itemClicked.connect(self.test)

        issuance_items = [{'name': '건축물대장(표제부)', 'img': '../../data/img/button/plus_icon.png'},
                          {'name': '건축물대장(총괄표제부)', 'img': '../../data/img/button/share_icon.png'},
                          {'name': '건축물대장(전유부)', 'img': '../../data/img/button/share_icon.png'},
                          {'name': '등기부등본(토지)', 'img': '../../data/img/button/share_icon.png'},
                          {'name': '등기부등본(건물)', 'img': '../../data/img/button/plus_icon.png'}]

        self.issuance_menu = MenuWidget(self)
        self.issuance_menu.add_item(issuance_items)
        self.issuance_menu.set_size(self.issuance_menu)
        self.issuance_menu.itemClicked.connect(self.test)

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

        self._init_interaction()

        self.issuance_thread = ibl.SetChrome('haul1115', 'ks05090818@')
        self.issuance_thread.threadEvent.chromeDriver.connect(self.get_chrome_driver)
        self.issuance_thread.start()

    def test(self):
        print(self.menu_widget.currentRow())

    # UI 세팅
    def _init_ui(self):
        self._setupUi(self)

        self.btn_search.setIcon(QIcon('../../data/img/button/search_icon.png'))
        self.btn_search.setIconSize(QSize(30, 30))
        self.btn_add.setIcon(QIcon('../../data/img/button/plus_icon.png'))
        self.btn_add.setIconSize(QSize(25, 25))
        self.btn_sharing.setIcon(QIcon('../../data/img/button/menu_icon.png'))
        self.btn_sharing.setIconSize(QSize(20, 20))
        self.btn_issuance.setIcon(QIcon('../../data/img/button/print_icon.png'))
        self.btn_search.setIconSize(QSize(23, 23))

        self.issuances.hide()

        self.edt_address.installEventFilter(self)
        self.btn_viol.installEventFilter(self)
        self.btn_sharing.installEventFilter(self)
        self.btn_add.installEventFilter(self)
        self.btn_issuance.installEventFilter(self)

        self.movie = QMovie("../../data/img/animation/btn_loading.gif")

        self.show()

    # 상호작용 세팅
    def _init_interaction(self):
        self.cbx_rooms.activated.connect(self.insert_room_info)
        self.edt_address.mousePressEvent = self.clicked_address_edit
        self.edt_address.returnPressed.connect(self.clicked_address_edit)

        self.btn_search.clicked.connect(self.clicked_address_edit)
        self.btn_details.clicked.connect(self.clicked_details_btn)
        self.btn_viol.clicked.connect(self.clicked_viol_btn)
        self.btn_sharing.clicked.connect(lambda: self.menu_widget.clicked_event(self.btn_sharing))

        # self.btn_issuance.clicked.connect(self.clicked_issuance_btn)
        self.btn_issuance.clicked.connect(lambda: self.issuance_menu.clicked_event(self.btn_issuance))
        # self.btn_issuance_1.clicked.connect(lambda: self.clicked_issuance_btns(0))
        # self.btn_issuance_2.clicked.connect(lambda: self.clicked_issuance_btns(1))
        # self.btn_issuance_3.clicked.connect(lambda: self.clicked_issuance_btns(2))

        for dic in [self.labels, self.labels_detail, self.labels_park, self.labels_land]:
            for i in dic: mouse_double_clicked(dic[i]).connect(self.clicked_labels)

    # 애니메이션 세팅
    def _set_anim(self):
        effect = QGraphicsOpacityEffect(self.issuances)
        self.issuances.setGraphicsEffect(effect)

        self.anim_move = QPropertyAnimation(self.issuances, b"pos")
        self.anim_move.setEndValue(QPoint(70, 18))
        self.anim_move.setDuration(150)

        self.anim_show = QPropertyAnimation(effect, b"opacity")
        self.anim_show.setStartValue(0)
        self.anim_show.setEndValue(1)
        self.anim_show.setDuration(110)

        self.anim_group = QParallelAnimationGroup()
        self.anim_group.addAnimation(self.anim_move)
        self.anim_group.addAnimation(self.anim_show)

        self.anim_hide = QPropertyAnimation(effect, b"opacity")
        self.anim_hide.setStartValue(1)
        self.anim_hide.setEndValue(0)
        self.anim_hide.setDuration(80)

    # 그림자 세팅
    def set_shadow(self, kind):
        shadow = QGraphicsDropShadowEffect(self)

        if kind == 'main_button':
            shadow.setBlurRadius(10)
            shadow.setXOffset(0)
            shadow.setYOffset(0)
            shadow.setColor(QColor(0, 0, 0, 70))

        elif kind == 'sub_button':
            shadow.setBlurRadius(20)
            shadow.setXOffset(0)
            shadow.setYOffset(0)
            shadow.setColor(QColor(255, 120, 90, 250))

        elif kind == 'edit':
            shadow.setBlurRadius(10)
            shadow.setXOffset(0)
            shadow.setYOffset(0)
            shadow.setColor(QColor(52, 152, 219, 150))

        elif kind == 'reset':
            shadow.setEnabled(False)

        return shadow

    # 셀러리움 로그인 소스
    def get_chrome_driver(self, driver):
        self.driver = driver
        self.login_cookies = driver.get_cookies()

        self.btn_issuance.setEnabled(True)
        print("로그인 OK")

    ##### 시그널 이벤트
    ########################################################################################################

    # 항목 클립보드에 복사
    def clicked_labels(self, widget):
        item_text = widget.text().rstrip(' ㎡').rstrip(' %').rstrip(' 대')
        if item_text != '':
            clip.copy(item_text)
            self.msg.show_msg(2000, 'center', "클립보드에 복사 되었습니다.\n( 단축키 Ctrl + V 로 붙혀넣기 가능)")

    # 소재지 찾기 에디트 클릭
    def clicked_address_edit(self, e=None):
        dialog = address_details.AddressDetails(1, self.edt_address.text())
        dialog.exec()

        if dialog.result:
            self.binfo, self.address = dialog.binfo, dialog.select_address
            self.detail, self.exact_detail = dialog.detail, dialog.exact_detail
            self.select_building, self.total_buildings = dialog.select_building, dialog.total_buildings
            self.owners, self.prices = dialog.owners, dialog.prices

            self.cbx_rooms.clear()
            self.cbx_rooms.addItems(dialog.detail_list)
            self.cbx_rooms.setCurrentIndex(dialog.select_index)

            self.activation, self.first = True, True
            self.insert_base_info()

            if self.opened: self.clicked_details_btn()

    # 위반 조회 버튼
    def clicked_viol_btn(self, viol=None):
        if self.lb_viol.text(): return

        if not self.cbx_rooms.currentText() == '( 상세주소 / 호 선택 )':
            # 집합일 경우
            if self.binfo['타입'] == '집합':
                viol = OpenApiRequest.get_viol(self.VIOL_KEY, self.pk)

            # 일반일 경우
            elif self.binfo['타입'] == '일반':
                viol = OpenApiRequest.get_viol(self.VIOL_KEY, self.pk)

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
            self.get_building_thread = pars.DataRequestThread(self.binfo, self.BULIDING_API_KEY, ['지역지구', '토지용도지역지구', '토지'])
            self.get_building_thread.start()
            self.get_building_thread.threadEvent.workerThreadDone.connect(self.insert_detail_info)
            self.first = False

        self.resize_form(self.opened)

    # 문서 발급 버튼
    def clicked_issuance_btns(self, kind, pk=''):
        if not self.activation: return

        # 표제부 버튼
        if kind == 0:
            self.clicked_issuance_btn()
            self.btn_issuance.setEnabled(False)

            pk = self.issuance_data['동_PK']

        # 전유부 버튼
        elif kind == 1:
            if self.binfo['타입'] == '집합':
                self.clicked_issuance_btn()
                self.btn_issuance.setEnabled(False)
                pk = self.issuance_data['호_PK']

            elif self.binfo['타입'] == '일반':
                self.msg.show_msg(2000, 'center', '전유부는 집합 건물만 발급할 수 있습니다')
                return

        # 등기부등본 버튼
        elif kind == 2:
            return

        self.issuance_thread = ibl.IssuanceBuildingLedger(pk, kind, self.driver, self.login_cookies)
        self.issuance_thread.threadEvent.workerThreadDone.connect(lambda: self.btn_issuance.setEnabled(True))
        self.issuance_thread.threadEvent.progress.connect(self.issuance_progress_event)
        self.issuance_thread.start()

    # 진행 메세지
    def issuance_progress_event(self, msg):
        print(msg)

    # 발급목록 열기 버튼
    def clicked_issuance_btn(self):
        if not self.cbx_rooms.currentText() == '( 상세주소 / 호 선택 )':
            if not self.issuance:
                if self.issuances.isHidden(): self.issuances.show()

                self.issuances.move(self.issuances.x()-20, self.issuances.y())
                self.anim_group.start()
                self.issuance_btn_tip.hide()
                self.issuance = True
            else:
                self.anim_hide.start()
                self.issuance = False
        else:
            self.msg.show_msg(3000, 'center', '건물 조회 후 발급이 가능합니다')

    # 이벤트 필터
    def eventFilter(self, obj, event):
        objs = {self.btn_viol: 'sub_button',
                self.btn_sharing: 'main_button',
                self.btn_add: 'main_button',
                self.btn_issuance: 'main_button',
                self.edt_address: 'edit'}
        if obj not in objs.keys(): return

        # ON
        if event.type() == QEvent.HoverEnter:
            obj.setGraphicsEffect(self.set_shadow(objs[obj]))

            if obj == self.btn_add: self.add_btn_tip.show()
            elif obj == self.btn_issuance:
                if not self.issuance:
                    self.issuance_btn_tip.show()

        # OFF
        elif event.type() == QEvent.HoverLeave:
            obj.setGraphicsEffect(self.set_shadow('reset'))

            if obj == self.btn_add: self.add_btn_tip.hide()
            elif obj == self.btn_issuance:
                if not self.issuance:
                    self.issuance_btn_tip.hide()

        return super(BuildingInfo, self).eventFilter(obj, event)

    ##### 데이터 입력
    ########################################################################################################

    # 기본 데이터 입력
    def insert_base_info(self):
        building = self.select_building
        address = self.address

        self.issuance_data = {'시군구코드': address['주소코드'][:5],
                              '법정동코드': address['주소코드'][5:],
                              '번': address['번'],
                              '지': address['지'],
                              '동_PK': building['건축물대장PK']}

        self.insert_room_info()
        if address['지'] == "0":
            old = "%s %s %s %s" % (address['시도'], address['시군구'], address['읍면동'], address['번'])
        else:
            old = "%s %s %s %s-%s" % (address['시도'], address['시군구'], address['읍면동'], address['번'], address['지'])

        layer = "-%s 층 / %s 층" % (building['지하층수'], building['지상층수'])
        elevator = "%s대 (비상 %s대)" % (building['승강기'], building['비상용승강기'])

        parking = int(building['옥내자주식대수']) + int(building['옥내기계식대수']) + \
                  int(building['옥외자주식대수']) + int(building['옥외기계식대수'])

        if self.total_buildings is not None:
            if parking == 0:
                total = self.total_buildings
                parking = int(total['옥내자주식대수'].values[0]) + int(total['옥내기계식대수'].values[0]) + \
                          int(total['옥외자주식대수'].values[0]) + int(total['옥외기계식대수'].values[0])

        room_count = "%s 호 / %s 가구 / %s 세대" % (building['호수'], building['가구수'], building['세대수'])
        day = "%s년 %s월 %s일" % (building['사용승인일'][0:4], building['사용승인일'][4:6], building['사용승인일'][6:8])

        base = {'소재지': old, '도로명': address['도로명주소'], '승강기': elevator, '주차장': str(parking) + " 대",
                '총층수': layer, '호가구세대': str(room_count), '사용승인일': day}

        # 같은 키에 값 입력
        for i in base:
            if i in self.labels: self.labels[i].setText(base[i])
        self.edt_address.setText(old)

        print(self.issuance_data)

    # 기본 데이터 룸/층별 입력
    def insert_room_info(self):
        if not self.activation: return

        address = self.address
        room, public_area, room_area, detail, price, price_day = None, None, None, None, None, None

        # 위반 건축물 라벨 초기화
        self.lb_viol.setText('')
        self.lb_viol.setStyleSheet('#lb_viol { background-color: rgb(245, 245, 245); }')

        #### 일반일 경우
        if self.binfo['타입'] == '일반':
            detail = self.detail.loc[self.cbx_rooms.currentIndex()]

            room_area, public_area = detail['층면적'], detail['층면적']
            room = "%s층" % detail['층명칭'].rstrip("층")
            self.pk = self.select_building['건축물대장PK']

            try:
                price = str("{:,}".format(int(self.prices['개별주택가격'])) + ' 원')
                price_day = self.prices['공시일자'].values[0].split('-')
                price_day = "(%s년 %s월)" % (price_day[0], price_day[1])
                self.base_name_13.setText(f"공시가격 {price_day}")

            except (ValueError, IndexError, TypeError):
                price = "조회 결과 없음"
                self.base_name_13.setText("공 시 가 격")

        #### 집합일 경우
        elif self.binfo['타입'] == '집합':
            detail = self.exact_detail.loc[self.cbx_rooms.currentIndex()]
            all_detail = self.detail[self.detail['호명칭'] == detail['호명칭']]
            self.pk = detail['건축물대장PK']
            self.issuance_data['호_PK'] = self.pk

            room_area = detail['전용면적']
            public_area = round(pd.to_numeric(all_detail['전용면적']).sum(), 2)
            room = "%s호" % detail['호명칭'].rstrip("호")
            if detail['동명칭']:
                room = "%s동 " % (detail['동명칭'].rstrip("동")) + room

            try:
                prices = self.prices[self.prices['호명칭'] == detail['호명칭']]
                price = str("{:,}".format(int(prices['공동주택가격'].values[0])) + ' 원')
                price_day = prices['공시일자'].values[0].split('-')
                price_day = "(%s년 %s월)" % (price_day[0], price_day[1])
                self.base_name_13.setText(f"공시가격 {price_day}")

            except (ValueError, IndexError, TypeError):
                price = "조회 결과 없음"
                self.base_name_13.setText("공 시 가 격")

        # 건물 명칭이 있을 경우
        if address['건물명칭']:
            room = "%s (%s)" % (room, address['건물명칭'])

        try:
            owners = self.owners[self.owners['건축물대장PK'] == self.pk]
            owner_count = len(owners)
            if owner_count == 1:
                owner = "%s | %s" % (owners.iloc[0]['소유자명'], owners.iloc[0]['소유구분명'])
            else:
                owner = "%s | %s 외 %s명" % (owners.iloc[0]['소유자명'], owners.iloc[0]['소유구분명'], str(len(owners) - 1))
        except (ValueError, TypeError, IndexError):
            owner = "소유자 확인 불가"

        base = {'상세주소': room, '주용도': detail['기타용도'], '공급면적': str(public_area) + " ㎡",
                '전용면적': str(room_area) + " ㎡", '소유자': owner, '공시가격': price}

        # 같은 키에 값 입력
        for i in base:
            if i in self.labels:
                self.labels[i].setText(base[i])

    # 상세 정보 로드
    def insert_detail_info(self, val):

        building = self.select_building

        in_land = int(building['옥내자주식대수'])
        in_mechanical = int(building['옥내기계식대수'])

        out_land = int(building['옥외자주식대수'])
        out_mechanical = int(building['옥외기계식대수'])

        # 용도지역지구
        if val[0] is None: jiji = '조회 결과 없음'
        else: jiji = ', '.join(val[0]['기타지역지구구역'])

        # 총괄 표제부 주차장
        if self.total_buildings is not None:
            total = self.total_buildings
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
                if (i[-2:] == '지구') or (i[-2:] == '지역'): land_jj.append(i)
                else: land_etc.append(i)

            land_jj = ', '.join(land_jj)
            land_etc = ', '.join(land_etc)

        price = str("{:,}".format(int(val[2]['공시지가'])) + ' 원 (㎡ 기준)')

        base = {'주구조': building['주구조'], '지역지구': jiji, '주용도': building['주용도'],
                '대지면적': val[2]['대지면적'].values[0] + ' ㎡', '건축면적': building['건축면적'] + ' ㎡', '건폐율': building['건폐율'] + ' %',
                '연면적': building['연면적'] + ' %', '높이': building['높이'], '용적률': building['용적률'] + ' %',
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

        self.btn_sharing.move(self.width() - 50, self.btn_sharing.y())

    # 폼 사이즈 변경
    def resize_form(self, opened):
        if opened:  # 열려있을 경우
            self.setMinimumWidth(430)   # 닫기
            self.setMaximumWidth(430)
            self.btn_details.setText("상세정보  >")
            self.opened = False
        else:
            self.setMinimumWidth(840)   # 열기
            self.setMaximumWidth(840)
            self.btn_details.setText("접 기  <")
            self.opened = True

        self.resize_title_bar()
        # x = (self.width() - self.btn_details.width()) - 10
        # self.btn_details.move(x, self.btn_details.y())


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


class TipBox(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("QLabel{background-color: rgba(0,0,0,120);"
                           "font: 14px \uc6f0\ucef4\uccb4 Regular;"
                           "color: white;"
                           "border-radius: 3px;"
                           "padding-top: 3px;}")
        self.hide()

    def set_box(self, widget, text, pos):
        self.setText(text)
        self.setAlignment(Qt.AlignCenter)

        font_size = self.fontMetrics().boundingRect(text)
        self.resize(font_size.width() + 10, 23)

        x, y = 0, 0
        if pos == 'right':
            x = widget.x() + widget.width() + 5
            y = widget.y() + ((widget.height() / 2) - (self.height() / 2))
        elif pos == 'left':
            x = widget.x() - self.width() - 5
            y = widget.y() + ((widget.height() / 2) - (self.height() / 2))
        elif pos == 'top':
            x = widget.x() + ((widget.width() / 2) - (self.width() / 2))
            y = widget.y() - 5
        elif pos == 'bot':
            x = widget.x() + ((widget.width() / 2) - (self.width() / 2))
            y = widget.y() + widget.height() + 5

        self.move(x, y)


sys._excepthook = sys.excepthook
sys.excepthook = my_exception_hook

app = QApplication()
window = BuildingInfo()
app.exec()
