import sys
import pandas as pd
import clipboard as clip
import module.open_api_pars as pars
import module.issuance_building_ledger as ibl

from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QGraphicsOpacityEffect, QGraphicsDropShadowEffect
from PySide6.QtGui import QFontMetrics, Qt, QIcon, QColor
from PySide6.QtCore import QRect, QObject, Signal, QEvent, QTimer, QPropertyAnimation, QSize
from ui.main.ui_info import Ui_BuildingInfo
from interface.sub_interface import address_details
from module.open_api_pars import OpenApiRequest


class BuildingInfo(QMainWindow, Ui_BuildingInfo):
    def __init__(self):
        super(BuildingInfo, self).__init__()

        self.BULIDING_API_KEY = 'sfSPRX+xNEExRUqE4cdhNjBSk4uXIv8F1CfLen06hdPGn5cflLJqy/nxmh48uF8fvdGk68k6Z5jWsU1n6BeNPA=='
        self.VIOL_KEY = '68506e6c486a736e35377562445658'

        self.activation, self.opened, self.first, self.msg_timer = False, False, False, False
        self.data_basic, self.data_basic_all = None, None
        self.base_list = []

        self.get_building_thread, self.issuance_thread = None, None     # 토지, 지역지구, 공시지가 스레드
        self.binfo, self.address = None, None
        self.select_building, self.total_buildings = None, None
        self.detail, self.exact_detail = None, None  # 상세 (호, 층)
        self.owners, self.prices, self.pk = None, None, None  # 소유자, 공시가격, 건축물대장 PK

        self._init_ui()

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

    # UI 세팅
    def _init_ui(self):
        self._setupUi(self)

        self.btn_search.setIcon(QIcon('../../data/img/button/search_icon.png'))
        self.btn_search.setIconSize(QSize(30, 30))

        self.msg_background = QLabel(self)
        self.msg_background.setAlignment(Qt.AlignCenter)
        self.msg_background.setStyleSheet("QLabel{background-color: rgba(0,0,0,150);"
                                          "font: 14px \uc6f0\ucef4\uccb4 Regular;"
                                          "color: white;"
                                          "padding-top: 3px;}")
        self.msg_background.hide()

        self.edt_address.installEventFilter(self)
        self.btn_viol.installEventFilter(self)
        self.btn_sharing.installEventFilter(self)
        self.btn_add.installEventFilter(self)
        self.btn_issuance.installEventFilter(self)

        self.show()

    # 상호작용 세팅
    def _init_interaction(self):
        self.edt_address.mousePressEvent = self.clicked_address_edit
        self.edt_address.returnPressed.connect(self.clicked_address_edit)
        self.btn_search.clicked.connect(self.clicked_address_edit)
        self.btn_details.clicked.connect(self.clicked_details_btn)
        self.cbx_rooms.activated.connect(self.insert_room_info)
        self.btn_viol.clicked.connect(self.clicked_viol_btn)
        self.btn_issuance.clicked.connect(self.clicked_issuance_btn)

        for dic in [self.labels, self.labels_detail, self.labels_park, self.labels_land]:
            for i in dic: mouse_double_clicked(dic[i]).connect(self.clicked_labels)

    # 이벤트 필터
    def eventFilter(self, obj, event):
        objs = {self.btn_viol: 'sub_button',
                self.btn_sharing: 'main_button',
                self.btn_add: 'main_button',
                self.btn_issuance: 'main_button',
                self.edt_address: 'edit'}
        if obj not in objs.keys(): return

        if event.type() == QEvent.HoverEnter:
            obj.setGraphicsEffect(self.set_shadow(objs[obj]))

        elif event.type() == QEvent.HoverLeave:
            obj.setGraphicsEffect(self.set_shadow('reset'))

        return super(BuildingInfo, self).eventFilter(obj, event)

    # 그림자 세팅
    def set_shadow(self, kind):
        shadow = QGraphicsDropShadowEffect(self)

        if kind == 'main_button':
            shadow.setBlurRadius(20)
            shadow.setXOffset(0)
            shadow.setYOffset(0)
            shadow.setColor(QColor(40, 104, 176, 250))

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

    ##### 시그널 이벤트
    ########################################################################################################

    # 항목 클립보드에 복사
    def clicked_labels(self, widget):
        item_text = widget.text().rstrip(' ㎡').rstrip(' %').rstrip(' 대')
        if item_text != '':
            clip.copy(item_text)
            self.info_msg(1, "클립보드에 복사 되었습니다.\n( 단축키 Ctrl + V 로 붙혀넣기 가능)")

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
    def clicked_issuance_btn(self):
        if not self.activation: return
        address = self.address

        if address['지'] == "0":
            old = "%s %s %s" % (address['시군구'], address['읍면동'], address['번'])
        else: old = "%s %s %s-%s" % (address['시군구'], address['읍면동'], address['번'], address['지'])

        if self.binfo['타입'] == '집합':
            ho = self.exact_detail.loc[self.cbx_rooms.currentIndex()]['호명칭'].rstrip("호")
            self.issuance_thread = ibl.IssuanceBuildingLedger(old, address['도로명주소'], ho, 2, 0, 'haul1115', 'ks05090818@')
            self.issuance_thread.start()

        elif self.binfo['타입'] == '일반':
            self.issuance_thread = ibl.IssuanceBuildingLedger(old, address['도로명주소'], '', 1, 0, 'haul1115', 'ks05090818@')
            self.issuance_thread.start()

    ##### 데이터 입력
    ########################################################################################################

    # 기본 데이터 입력
    def insert_base_info(self):
        building = self.select_building
        address = self.address

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

    # 알림 메세지
    def info_msg(self, sec, content):
        if self.msg_background.isHidden():
            self.msg_background.show()

        if self.msg_timer:
            self.timer.stop()
            self.msg_timer = False

        self.msg_timer = True
        self.msg_background.setText(content)
        font_size = self.msg_background.fontMetrics().boundingRect(content)

        if '\n' in content:
            line_width = []
            for i in content.split('\n'):
                line_width.append(self.msg_background.fontMetrics().boundingRect(i).width())
            w = max(line_width)
        else: w = font_size.width()

        h = font_size.height() * (content.count('\n') + 1)
        self.msg_background.resize(w + 20, h + 14)

        x = round((self.width() / 2) - (self.msg_background.width() / 2))
        y = round((self.height() / 2) - (self.msg_background.height() / 2))

        self.msg_background.move(x, y)

        effect = QGraphicsOpacityEffect(self.msg_background)
        self.msg_background.setGraphicsEffect(effect)

        self.anim = QPropertyAnimation(effect, b"opacity")
        self.anim.setStartValue(0)
        self.anim.setEndValue(1)
        self.anim.setDuration(100)
        self.anim.start()

        self.timer = QTimer(self)
        self.timer.start(sec * 1300)
        self.timer.timeout.connect(self.hide_msg)

    # 메세지 타이머 종료
    def hide_msg(self):
        effect = QGraphicsOpacityEffect(self.msg_background)
        self.msg_background.setGraphicsEffect(effect)

        self.anim = QPropertyAnimation(effect, b"opacity")
        self.anim.setStartValue(1)
        self.anim.setEndValue(0)
        self.anim.setDuration(500)
        self.anim.start()

        self.timer.stop()
        self.msg_timer = False


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
