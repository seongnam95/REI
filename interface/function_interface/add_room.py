import sys
import re

from PySide6.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect
from PySide6.QtGui import QColor, QIntValidator, QDoubleValidator
from PySide6.QtCore import QPoint

from interface.sub_interface import find_address_details
from ui.main.ui_add_room import Ui_AddRoom


class AddRoom(QMainWindow, Ui_AddRoom):
    def __init__(self):
        super(AddRoom, self).__init__()
        self.setupUi(self)

        self._init_ui()
        self._init_shadows()
        self._init_interaction()

        self.binfo = dict
        self.edt_list = {'공급면적': self.edt_supply_area, '전용면적': self.edt_area, '주차대수': self.edt_parking,
                         '총층': self.edt_total_floor, '해당층': self.edt_crt_floor, '세대수': self.edt_household,
                         '대지지분1': self.edt_land_share_1, '대지지분2': self.edt_land_share_2,
                         '사용승인일': [self.edt_day_1, self.edt_day_2, self.edt_day_3]}

        self.kind_change_event()
        self.show()

    def _init_ui(self):
        self.btn_back.hide()
        self.edt_purpose.hide()
        self.edt_relationship.hide()

    # UI 상호작용 설정
    def _init_interaction(self):
        self.edt_address.mousePressEvent = self.clicked_address_edit

        self.cbx_type.activated.connect(self.type_change_event)
        self.cbx_kind_1.activated.connect(self.kind_change_event)

        self.btn_back.clicked.connect(lambda: self.page_change_event(self.stackedWidget.currentIndex() - 1))
        self.btn_next.clicked.connect(lambda: self.page_change_event(self.stackedWidget.currentIndex() + 1))
        self.btn_page_1.clicked.connect(lambda: self.page_change_event(0))
        self.btn_page_2.clicked.connect(lambda: self.page_change_event(1))
        self.btn_page_3.clicked.connect(lambda: self.page_change_event(2))

        self.btn_parking_true.clicked.connect(lambda: self.parking_toggle_event(True))
        self.btn_parking_false.clicked.connect(lambda: self.parking_toggle_event(False))

        self.rbtn_in_date_1.toggled.connect(self.day_toggle_event)
        self.rbtn_in_date_2.toggled.connect(self.day_toggle_event)

        self.cbx_purpose.activated.connect(lambda: self.show_hide_edt_event('건축물용도'))
        self.cbx_relationship.activated.connect(lambda: self.show_hide_edt_event('관계'))
        #
        # self.edt_price.textChanged.connect(lambda: self.edt_price.setText(mask_money(self.edt_price.text())))
        # self.edt_admin_cost.textChanged.connect(lambda: self.edt_admin_cost.setText(mask_money(self.edt_admin_cost.text())))
        # self.edt_sub_1_1.textChanged.connect(lambda: self.edt_sub_1_1.setText(mask_money(self.edt_sub_1_1.text())))
        # self.edt_sub_1_2.textChanged.connect(lambda: self.edt_sub_1_2.setText(mask_money(self.edt_sub_1_2.text())))
        # self.edt_sub_2.textChanged.connect(lambda: self.edt_sub_2.setText(mask_money(self.edt_sub_2.text())))

        self.edt_client_num_1.textChanged.connect(lambda: self.edt_client_num_1.setText(mask_phone(self.edt_client_num_1.text())))
        self.edt_client_num_2.textChanged.connect(lambda: self.edt_client_num_2.setText(mask_phone(self.edt_client_num_2.text())))

        all_int = QIntValidator()
        self.edt_room_num.setValidator(all_int)
        self.edt_bathroom.setValidator(all_int)
        self.edt_crt_floor.setValidator(all_int)
        self.edt_total_floor.setValidator(all_int)
        self.edt_household.setValidator(all_int)
        self.edt_parking.setValidator(all_int)
        self.edt_day_1.setValidator(all_int)
        self.edt_day_2.setValidator(all_int)
        self.edt_day_3.setValidator(all_int)
        self.edt_in_date_1.setValidator(all_int)
        self.edt_in_date_2.setValidator(all_int)
        self.edt_in_date_3.setValidator(all_int)

        double_int = QDoubleValidator()
        self.edt_supply_area.setValidator(double_int)
        self.edt_area.setValidator(double_int)
        self.edt_land_share_1.setValidator(double_int)
        self.edt_land_share_2.setValidator(double_int)

    # 폼 그림자 설정
    def _init_shadows(self):
        frame_list = [self.address_frame, self.stackedWidget]

        for child in frame_list:
            shadow = QGraphicsDropShadowEffect(self)
            shadow.setBlurRadius(15)
            shadow.setXOffset(1)
            shadow.setYOffset(1)
            shadow.setColor(QColor(0, 0, 0, 35))
            child.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(20)
        shadow.setXOffset(1)
        shadow.setYOffset(1)
        shadow.setColor(QColor(123, 123, 255, 120))
        self.btn_next.setGraphicsEffect(shadow)

    #
    ####################################################################################################################

    # 소재지 찾기 에디트 클릭
    def clicked_address_edit(self, e=None):
        dialog = find_address_details.AddressDetails(self.edt_address.text())
        dialog.exec()

        if dialog.result:
            title, expos, expos_tot, total = dialog.title, dialog.expos, dialog.expos_tot, dialog.total
            self.input_auto_data(title, expos, expos_tot, total)

    def input_auto_data(self, title, expos, expos_tot, total):
        parking = str(sum(map(int, [title['옥내기계식대수'], title['옥내자주식대수'], title['옥외기계식대수'], title['옥외자주식대수']])))
        if total is not None:
            if parking == '0':
                parking = str(sum(map(int, [total['옥내기계식대수'], total['옥내자주식대수'],
                                            total['옥외기계식대수'], total['옥외자주식대수']])))

        area = expos['전용면적'] if title['대장구분'] == '집합' else ''
        area_tot = round(sum(map(float, list(expos_tot['전용면적']))), 2) if title['대장구분'] == '집합' else expos['층면적']

        layer = expos['층번호'].split('.')[0]
        layer_tot = title['지상층수']
        title['사용승인일'] = [title['사용승인일'][:4], title['사용승인일'][4:6].lstrip('0'), title['사용승인일'][6:].lstrip('0')]

        input_data = {'공급면적': area_tot, '전용면적': area, '주차대수': parking, '총층': layer_tot, '해당층': layer}

        # 에딧 입력
        for key, val in input_data.items(): self.edt_list[key].setText(str(val))
        for n, i in enumerate(self.edt_list['사용승인일']): i.setText(title['사용승인일'][n])

        # '주차 여부' 클릭
        if int(parking) > 0: self.btn_parking_true.click()
        else: self.btn_parking_false.click()

        # 용도 선택
        alone = ['단독', '다가구', '다중', '공관']
        public = ['아파트', '다세대', '연립', '공동주택']
        facility_1 = ['1종', '안마시술', '노래연습']
        facility_2 = ['2종', '일반음식점']
        work = ['사무소', '오피스텔']

        self.cbx_purpose.setCurrentIndex(5)
        for idx, lst in enumerate([alone, public, facility_1, facility_2, work]):
            for i in lst:
                if i in expos['주용도'] or i in expos['기타용도']:
                    self.cbx_purpose.setCurrentIndex(idx)

        print(input_data)

    # UI 기능
    ####################################################################################################################

    # 거래 유형 변경 이벤트
    def type_change_event(self):
        item = self.cbx_type.currentText()
        self.kind_change_event()

        if item == '매매':
            self.name_price.setText('매매가')

        elif item == '전세':
            self.name_price.setText('전세가')

        elif item == '월세':
            self.name_price.setText('보증금')

    def kind_change_event(self):
        kind = self.cbx_kind_1.currentText()
        self.cbx_kind_2.clear()
        self.hide_items()

        if kind == '아파트' or kind == '오피스텔':
            if kind == '아파트': sub_list = ['아파트', '주상복합', '재건축']
            else: sub_list = ['주거용', '업무용', '겸용', '숙박시설']
            self.cbx_kind_2.addItems(sub_list)
            self.set_price_ui(0)

        elif kind == '분양권':
            sub_list = ['아파트 분양권', '주상복합 분양권', '오피스텔 분양권']
            self.cbx_kind_2.addItems(sub_list)
            self.set_price_ui(3)

        elif kind == '재개발':
            sub_list = ['아파트', '연립', '빌라', '단독', '다세대', '다가구', '상가', '기타']
            self.cbx_kind_2.addItems(sub_list)
            self.set_price_ui(1)

        elif kind == '주택':
            sub_list = ['단독', '다가구', '다세대', '연립', '빌라', '상가주택', '전원주택', '한옥주택', '기타']
            self.cbx_kind_2.addItems(sub_list)
            self.set_price_ui(0)

        elif kind == '원룸':
            sub_list = ['일반원룸', '오피스텔', '원룸형 아파트', '도시형생활주택', '기타']
            self.cbx_kind_2.addItems(sub_list)
            self.set_price_ui(0)

        elif kind == '상가점포':
            sub_list = ['단지내상가', '일반상가', '복합상가']
            self.cbx_kind_2.addItems(sub_list)
            self.set_price_ui(2)

        elif kind == '사무실':
            sub_list = ['대형사무실', '중소형사무실', '오피스텔', '지식산업센터']
            self.cbx_kind_2.addItems(sub_list)
            self.set_price_ui(1)

        elif kind == '공장/창고':
            sub_list = ['공장', '창고', '기타']
            self.cbx_kind_2.addItems(sub_list)
            self.set_price_ui(1)

        elif kind == '빌딩 건물':
            sub_list = ['빌딩', '상업시설', '레저스포츠위탁', '여관/모텔/호텔', '콘도', '펜션', '고시텔', '상가건물', '빌딩건물 기타', '기타']
            self.cbx_kind_2.addItems(sub_list)
            self.set_price_ui(1)

        elif kind == '토지':
            sub_list = ["대", "전", "답", "임야", "공원", "구거", "도로", "염전", "제방", "하천", "유지", "묘지", "과수원",
                        "양어장", "주차장", "유원지", "광천지", "사적지", "잡종지", "공장용지", "창고용지", "학교용지", "종교용지",
                        "체육용지", "수도용지", "목장용지", "철도용지", "주유소용지", "기타"]
            self.cbx_kind_2.addItems(sub_list)
            self.set_price_ui(4)

    # '직접입력' 이벤트
    def show_hide_edt_event(self, kind):
        if kind == '건축물용도':
            if self.cbx_purpose.currentText() == '( 직접입력 )':
                self.edt_purpose.show()
                self.edt_purpose.setFocus()
            else: self.edt_purpose.hide()

        elif kind == '관계':
            if self.cbx_relationship.currentText() == '( 직접입력 )':
                self.edt_relationship.show()
                self.edt_relationship.setFocus()
            else: self.edt_relationship.hide()

    # 주차 가능, 불가능 토글
    def parking_toggle_event(self, toggle):
        if toggle:
            self.btn_parking_true.setChecked(True)
            self.btn_parking_false.setChecked(False)
        else:
            self.btn_parking_true.setChecked(False)
            self.btn_parking_false.setChecked(True)

    # 즉시입주, 날짜 지정 이벤트
    def day_toggle_event(self):
        radio = self.sender()
        if radio.isChecked():
            if radio.text() == '즉시입주':
                self.edt_in_date_1.clear()
                self.edt_in_date_2.clear()
                self.edt_in_date_3.clear()

                self.edt_in_date_1.setEnabled(False)
                self.edt_in_date_2.setEnabled(False)
                self.edt_in_date_3.setEnabled(False)
            else:
                self.edt_in_date_1.setEnabled(True)
                self.edt_in_date_2.setEnabled(True)
                self.edt_in_date_3.setEnabled(True)

                self.edt_in_date_1.setFocus()

    # 페이지 전환 이벤트
    def page_change_event(self, page):
        self.stackedWidget.setCurrentIndex(page)

        page_btn = {0: self.btn_page_1, 1: self.btn_page_2, 2: self.btn_page_3}
        current_idx = self.stackedWidget.currentIndex()

        for btn in page_btn.values():
            btn.setChecked(False)
            page_btn[current_idx].setChecked(True)

        if current_idx == 0: self.btn_back.hide()
        elif current_idx == 1: self.btn_back.show()
        elif current_idx == 2: self.btn_back.show()

    def set_price_ui(self, kind):
        item = self.cbx_type.currentText()

        # 주택
        if kind == 0:
            # 관리비
            self.f_admin_cost.show()
            self.f_admin_cost.move(self.get_item_pos(0, 1))

            # 관리비 항목
            self.f_cost_in.show()
            self.f_cost_in.move(self.get_item_pos(0, 3))

            if item == '매매':
                # 기보증금
                self.f_deposit.show()
                self.f_deposit.move(self.get_item_pos(1, 0))

                # 융자금
                self.f_loan.show()
                self.f_loan.move(self.get_item_pos(1, 1))

            elif item == '전세':
                self.name_price.setText('전세가')

                # 융자금
                self.f_loan.show()
                self.f_loan.move(self.get_item_pos(1, 0))

            elif item == '월세':
                self.name_price.setText('보증금')

                # 월차임
                self.f_rent.show()
                self.f_rent.move(self.get_item_pos(1, 0))

                # 융자금
                self.f_loan.show()
                self.f_loan.move(self.get_item_pos(1, 1))

        # 재개발/사무실/공장/창고/빌딩
        elif kind == 1:
            # 관리비
            self.f_admin_cost.show()
            self.f_admin_cost.move(self.get_item_pos(0, 1))

            if item == '매매':
                # 기보증금
                self.f_deposit.show()
                self.f_deposit.move(self.get_item_pos(1, 0))

                # 융자금
                self.f_loan.show()
                self.f_loan.move(self.get_item_pos(1, 1))

            elif item == '전세':
                self.name_price.setText('전세가')

                # 융자금
                self.f_loan.show()
                self.f_loan.move(self.get_item_pos(1, 0))

            elif item == '월세':
                self.name_price.setText('보증금')

                # 월차임
                self.f_rent.show()
                self.f_rent.move(self.get_item_pos(1, 0))

                # 융자금
                self.f_loan.show()
                self.f_loan.move(self.get_item_pos(1, 1))

        # 상가
        elif kind == 2:
            # 관리비
            self.f_admin_cost.show()
            self.f_admin_cost.move(self.get_item_pos(0, 1))

            if item == '매매':
                # 기보증금
                self.f_deposit.show()
                self.f_deposit.move(self.get_item_pos(1, 0))

                # 융자금
                self.f_loan.show()
                self.f_loan.move(self.get_item_pos(1, 1))

                # 권리금
                self.f_facility.show()
                self.f_facility.move(self.get_item_pos(0, 2))

            elif item == '전세':
                self.name_price.setText('전세가')

                # 융자금
                self.f_loan.show()
                self.f_loan.move(self.get_item_pos(1, 0))

                # 권리금
                self.f_facility.show()
                self.f_facility.move(self.get_item_pos(1, 1))

            elif item == '월세':
                self.name_price.setText('보증금')

                # 월차임
                self.f_rent.show()
                self.f_rent.move(self.get_item_pos(1, 0))

                # 융자금
                self.f_loan.show()
                self.f_loan.move(self.get_item_pos(1, 1))

                # 권리금
                self.f_facility.show()
                self.f_facility.move(self.get_item_pos(0, 2))

        # 분양권
        elif kind == 3:
            if item == '매매':
                # 분양가
                self.f_parcel.show()
                self.f_parcel.move(self.get_item_pos(1, 0))

                # 융자금
                self.f_loan.show()
                self.f_loan.move(self.get_item_pos(1, 1))

                # 프리미엄
                self.f_premium.show()
                self.f_premium.move(self.get_item_pos(0, 1))

                # 납입 중도금
                self.f_middle_pay.show()
                self.f_middle_pay.move(self.get_item_pos(0, 2))

                # 관리비
                self.f_admin_cost.show()
                self.f_admin_cost.move(self.get_item_pos(1, 2))

            elif item == '전세':
                self.name_price.setText('전세가')

                # 융자금
                self.f_loan.show()
                self.f_loan.move(self.get_item_pos(1, 1))

                # 납입 중도금
                self.f_middle_pay.show()
                self.f_middle_pay.move(self.get_item_pos(1, 0))

                # 관리비
                self.f_admin_cost.show()
                self.f_admin_cost.move(self.get_item_pos(0, 1))

            elif item == '월세':
                self.name_price.setText('보증금')

                # 월차임
                self.f_rent.show()
                self.f_rent.move(self.get_item_pos(1, 0))

                # 융자금
                self.f_loan.show()
                self.f_loan.move(self.get_item_pos(1, 1))

                # 납입 중도금
                self.f_middle_pay.show()
                self.f_middle_pay.move(self.get_item_pos(0, 1))

                # 관리비
                self.f_admin_cost.show()
                self.f_admin_cost.move(self.get_item_pos(0, 2))

        # 토지
        elif kind == 4:
            if item == '매매':
                # 기보증금
                self.f_deposit.show()
                self.f_deposit.move(self.get_item_pos(1, 0))

                # 융자금
                self.f_loan.show()
                self.f_loan.move(self.get_item_pos(0, 1))

            elif item == '전세':
                self.name_price.setText('전세가')

                # 융자금
                self.f_loan.show()
                self.f_loan.move(self.get_item_pos(1, 0))

            elif item == '월세':
                self.name_price.setText('보증금')

                # 월차임
                self.f_rent.show()
                self.f_rent.move(self.get_item_pos(1, 0))

                # 융자금
                self.f_loan.show()
                self.f_loan.move(self.get_item_pos(0, 1))

    def hide_items(self):
        items = [self.f_deposit, self.f_admin_cost, self.f_loan, self.f_cost_in, self.f_facility, self.f_parcel,
                 self.f_premium, self.f_rent, self.f_parcel_type, self.f_electricity, self.f_crt_purpose, self.f_rcmd_purpose,
                 self.f_land_items, self.f_use_area, self.f_middle_pay]

        for i in items: i.hide()

    @classmethod
    def get_item_pos(cls, pos_x, pos_y):
        x = {0: 30, 1: 330}
        y = {0: 20, 1: 60, 2: 100, 3: 105}
        pos = QPoint(x[pos_x], y[pos_y])
        return pos

# 돈 정규식
def mask_money(money):
    money = re.sub(r'[^0-9]', '', money)
    if money == '': return
    money = format(int(money), ',')
    return str(money)


# 폰 번호 정규식
def mask_phone(num):
    num = re.sub(r'[^0-9]', '', num)
    num = re.sub(r'(\d{3})(\d{3,4})(\d{4})', r'\1-\2-\3', num)
    return num


# 예외 오류 처리
def my_exception_hook(exctype, value, traceback):
    sys.excepthook(exctype, value, traceback)


sys._excepthook = sys.excepthook
sys.excepthook = my_exception_hook

app = QApplication()
window = AddRoom()
app.exec()
