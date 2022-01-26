import sys
import pandas as pd

from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QFontMetrics
from PySide6.QtCore import QRect

from ui.main.ui_info import Ui_BuildingInfo
from interface.sub_interface import address_details


class BuildingInfo(QMainWindow, Ui_BuildingInfo):
    def __init__(self, *args, **kwargs):
        super(BuildingInfo, self).__init__(*args, **kwargs)

        self.activation, self.opened = False, False
        self.data_basic, self.data_basic_all = None, None
        self.base_list = []

        self.binfo, self.address = None, None
        self.select_building, self.total_buildings = None, None
        self.detail, self.exact_detail = None, None  # 상세 (호, 층)
        self.owners, self.prices = None, None  # 소유자, 공시가격

        self._init_ui()
        self._init_interaction()

        self.labels = {'소재지': self.base_item_1.setText,
                       '도로명': self.base_item_2.setText,
                       '상세주소': self.base_item_3.setText,
                       '주용도': self.base_item_4.setText,
                       '공급면적': self.base_item_5.setText,
                       '승강기': self.base_item_6.setText,
                       '주차장': self.base_item_7.setText,
                       '전용면적': self.base_item_8.setText,
                       '총층수': self.base_item_9.setText,
                       '호가구세대': self.base_item_11.setText,
                       '사용승인일': self.base_item_12.setText,
                       '공시가격': self.base_item_13.setText}
        self.labels_detail = {'주구조': self.detail_item_1.setText,
                              '지역지구': self.detail_item_2.setText,
                              '주용도': self.detail_item_3.setText,
                              '대지면적': self.detail_item_4.setText,
                              '건축면적': self.detail_item_5.setText,
                              '건폐율': self.detail_item_6.setText,
                              '연면적': self.detail_item_7.setText,
                              '높이': self.detail_item_8.setText,
                              '용적률': self.detail_item_9.setText}
        self.labels_park = {'옥내자주식': self.park_item_1.setText,
                            '옥내기계식': self.park_item_2.setText,
                            '옥외자주식': self.park_item_3.setText,
                            '옥외기계식': self.park_item_4.setText}
        self.labels_land = {'공시지가': self.land_item_1.setText,
                            '지역지구': self.land_item_2.setText,
                            '기타지역지구': self.land_item_3.setText}

    # UI 세팅
    def _init_ui(self):
        self._setupUi(self)
        self.font()
        self.show()

    # 상호작용 세팅
    def _init_interaction(self):
        self.edt_address.mousePressEvent = self.clicked_address_edit
        self.btn_details.clicked.connect(self.clicked_details_btn)
        self.cbx_rooms.activated.connect(self.select_rooms_cbx)

    # 타이틀바 라벨 위치 세팅
    def title_bar_set(self):
        title_x = (self.width() / 2) - (self.lb_title.width() / 2)
        self.lb_title.move(title_x, self.lb_title.y())

        sub_title_x = (self.width() / 2) - (self.lb_sub_title.width() / 2)
        self.lb_sub_title.move(sub_title_x, self.lb_sub_title.y())

    # 상세정보 버튼 클릭
    def clicked_details_btn(self):
        if not self.activation: return

        # 상세정보가 활성화 된 경우
        if self.opened:
            self.setMinimumWidth(430)
            self.setMaximumWidth(430)
            self.btn_details.setText("상세정보  >")
            self.opened = False

        # 상세정보가 비활성화인 경우
        else:
            self.setMinimumWidth(840)
            self.setMaximumWidth(840)
            self.insert_detail_info()
            self.btn_details.setText("접 기  <")
            self.opened = True

        self.title_bar_set()
        x = (self.width() - self.btn_details.width()) - 10
        self.btn_details.move(x, self.btn_details.y())

    # 소재지 찾기 에디트 클릭
    def clicked_address_edit(self, e):
        dialog = address_details.AddressDetails(1)
        dialog.exec()

        if dialog.result is False: return

        self.binfo, self.address = dialog.binfo, dialog.select_address
        self.detail, self.exact_detail = dialog.detail, dialog.exact_detail
        self.select_building, self.total_buildings = dialog.select_building, dialog.total_buildings
        self.owners, self.prices = dialog.owners, dialog.prices

        self.cbx_rooms.clear()
        self.cbx_rooms.addItems(dialog.detail_list)
        self.cbx_rooms.setCurrentIndex(dialog.select_index)

        self.activation = True
        self.insert_base_info()

    # 기본 데이터 입력
    def insert_base_info(self):
        building = self.select_building
        address = self.address

        self.insert_room_info()

        old = "%s %s %s %s-%s" % (address['시도'], address['시군구'], address['읍면동'], address['번'], address['지'])

        layer = "-%s 층 / %s 층" % (building['지하층수'], building['지상층수'])
        elevator = "%s대 (비상 %s대)" % (building['승강기'], building['비상용승강기'])
        parking = int(building['옥내자주식대수']) + int(building['옥내기계식대수']) + \
                  int(building['옥내자주식대수']) + int(building['옥외기계식대수'])
        room_count = "%s 호 / %s 가구 / %s 세대" % (building['호수'], building['가구수'], building['세대수'])
        day = "%s 년  %s 월  %s 일" % (building['사용승인일'][0:4], building['사용승인일'][4:6], building['사용승인일'][6:8])

        base = {'소재지': old, '도로명': address['도로명주소'], '승강기': elevator, '주차장': str(parking) + " 대",
                '총층수': layer, '호가구세대': str(room_count), '사용승인일': day}

        # 같은 키에 값 입력
        for i in base:
            if i in self.labels: self.labels[i](base[i])
        self.edt_address.setText(old)

    # 상세주소 데이터 입력
    def insert_room_info(self, room=None, public_area=None, room_area=None, detail=None):
        address = self.address

        if self.binfo['타입'] == '일반':
            detail = self.detail.iloc[self.cbx_rooms.currentIndex()]
            room_area, public_area = detail['층면적'], detail['층면적']
            room = "%s층" % detail['층명칭'].rstrip("층")

        elif self.binfo['타입'] == '집합':  # 집합일 경우
            detail = self.exact_detail.iloc[self.cbx_rooms.currentIndex()]

            room_area = detail['전용면적']
            public_area = round(pd.to_numeric(detail['전용면적']).sum(), 2)

            room = "%s호" % detail['호명칭'].rstrip("호")
            if not detail['동명칭'].empty:
                room = "%s동 " % (detail['동명칭'].rstrip("동")) + room

        # 건물 명칭이 있을 경우
        if address['건물명칭']:
            room = "%s (%s)" % (room, address['건물명칭'])

        base = {'상세주소': room, '주용도': detail['기타용도'], '공급면적': str(public_area) + " ㎡",
                '전용면적': str(room_area) + " ㎡"}

        # 같은 키에 값 입력
        for i in base:
            if i in self.labels: self.labels[i](base[i])

        # old_width = self.base_item_1.fontMetrics().boundingRect(self.base_item_1.text()).width()
        # new_width = self.base_item_2.fontMetrics().boundingRect(self.base_item_2.text()).width()
        #
        # print(old_width, new_width)

    # 상세주소 콤보박스 클릭
    def select_rooms_cbx(self):
        self.insert_room_info()

        # 소유자 항목 추가
        # 공시가격 항목 추가

    def insert_detail_info(self):
        building = self.select_building
        print(building)
        base = {'주구조': building['주구조'], '주용도': building['주용도'],
                '대지면적': building['대지면적'], '건축면적': building['건축면적'], '건폐율': building['건폐율'],
                '연면적': building['연면적'], '높이': building['높이'], '용적률': building['용적률'],
                '옥내자주식': building['옥내자주식대수'], '옥내기계식': building['옥내기계식대수'],
                '옥외자주식': building['옥외자주식대수'], '옥외기계식': building['옥외기계식대수']}

        for i in base:
            if i in self.labels_detail:
                self.labels_detail[i](base[i])
            if i in self.labels_park:
                self.labels_park[i](base[i])


# 예외 오류 처리
def my_exception_hook(exctype, value, traceback):
    sys.excepthook(exctype, value, traceback)


sys._excepthook = sys.excepthook
sys.excepthook = my_exception_hook

app = QApplication()
window = BuildingInfo()
app.exec()
