import sys
import re

from PySide6.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect
from PySide6.QtGui import QColor, QIntValidator, QDoubleValidator

from interface.sub_interface import find_address_details
from ui.main.ui_add_room import Ui_AddRoom


class AddRoom(QMainWindow, Ui_AddRoom):
    def __init__(self):
        super(AddRoom, self).__init__()
        self.setupUi(self)

        self._init_ui()
        self._init_shadows()
        self._init_interaction()

        self.show()

    def _init_ui(self):
        self.btn_back.hide()
        self.edt_purpose.hide()
        self.edt_relationship.hide()

    # UI 상호작용 설정
    def _init_interaction(self):
        self.edt_address.mousePressEvent = self.clicked_address_edit

        self.cbx_type.activated.connect(self.type_change_event)

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

        self.edt_price.textChanged.connect(lambda: self.edt_price.setText(mask_money(self.edt_price.text())))
        self.edt_admin_cost.textChanged.connect(lambda: self.edt_admin_cost.setText(mask_money(self.edt_admin_cost.text())))
        self.edt_sub_1_1.textChanged.connect(lambda: self.edt_sub_1_1.setText(mask_money(self.edt_sub_1_1.text())))
        self.edt_sub_1_2.textChanged.connect(lambda: self.edt_sub_1_2.setText(mask_money(self.edt_sub_1_2.text())))
        self.edt_sub_2.textChanged.connect(lambda: self.edt_sub_2.setText(mask_money(self.edt_sub_2.text())))

        self.edt_client_num_1.textChanged.connect(lambda: self.edt_client_num_1.setText(mask_phone(self.edt_client_num_1.text())))
        self.edt_client_num_2.textChanged.connect(lambda: self.edt_client_num_2.setText(mask_phone(self.edt_client_num_2.text())))

        all_int = QIntValidator()
        self.edt_room_num.setValidator(all_int)
        self.edt_bathroom.setValidator(all_int)
        self.edt_layer.setValidator(all_int)
        self.edt_total_layer.setValidator(all_int)
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
            self.binfo = dict(dialog.binfo)
            for i, n in self.binfo.items():
                print(i, n)

    # UI 기능
    ####################################################################################################################

    # 거래 유형 변경 이벤트
    def type_change_event(self):
        if self.cbx_type.currentIndex() == 0:
            self.name_price.setText('매매가')
            self.name_sub_1.setText('기보증금')

            self.edt_sub_1_1.resize(76, 30)
            self.edt_sub_1_2.show()
            self.label_15.show()

            self.sub_1_frame.show()

        elif self.cbx_type.currentIndex() == 1:
            self.name_price.setText('전세가')
            self.sub_1_frame.hide()

        elif self.cbx_type.currentIndex() == 2:
            self.name_price.setText('보증금')
            self.name_sub_1.setText('월 차임')

            self.edt_sub_1_1.resize(151, 30)
            self.edt_sub_1_2.hide()
            self.label_15.hide()

            self.sub_1_frame.show()

    # '직접입력' 이벤트
    def show_hide_edt_event(self, kind):
        if kind == '건축물용도':
            widget = self.focusWidget()
            if widget.currentText() == '( 직접입력 )':
                self.edt_purpose.show()
                self.edt_purpose.setFocus()
            else: self.edt_purpose.hide()

        elif kind == '관계':
            widget = self.focusWidget()
            if widget.currentText() == '( 직접입력 )':
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
