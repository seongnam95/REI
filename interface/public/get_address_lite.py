import sys

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon, QColor
from PySide6.QtWidgets import QDialog, QLabel, QListWidgetItem, QWidget, QGridLayout, QGraphicsDropShadowEffect

import module.open_api_pars as pars
from ui.dialog.ui_address_lite import Ui_FindAddress
from ui.custom import BlackBoxMsg


class GetAddressLite(QDialog, Ui_FindAddress):
    def __init__(self, address=None):
        super().__init__()
        self.setupUi(self)
        if address: self.edt_address.setText(address)

        # OPEN API KEY
        self.ADDRESS_API_KEY = 'U01TX0FVVEgyMDIxMTIwMjEzNTc0MzExMTk4Mjc='
        self.address, self.result = None, None

        # INIT
        self._init_ui()
        self._init_interaction()
        self._init_shadow()

        self.show()

    # init UI
    def _init_ui(self):
        self.msg = BlackBoxMsg.BoxMessage(self)

        self.edt_address.setFocus()
        self.btn_search.setIcon(QIcon('../info/resources/img/search_icon.png'))
        self.btn_search.setIconSize(QSize(30, 30))

    # 상호작용
    def _init_interaction(self):
        self.edt_address.returnPressed.connect(self.get_address_request)
        self.btn_search.clicked.connect(self.get_address_request)
        self.btn_input.clicked.connect(self.select_address_event)
        self.list_address.clicked.connect(lambda: self.btn_input.setEnabled(True))

    # 프레임 그림자 효과
    def _init_shadow(self):
        for child in [self.address_frame, self.list_frame]:
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
        self.btn_input.setGraphicsEffect(shadow)

    ########################################################################################################

    # 주소 리스트 추가
    def get_address_request(self):
        if self.edt_address.text() == "": return
        self.list_address.clear()
        self.btn_input.setEnabled(False)

        # 주소 양끝 공백제거 후 파싱
        txt = self.edt_address.text().strip()
        self.address = pars.OpenApiRequest.get_address(self.ADDRESS_API_KEY, txt)

        if self.address is None: return

        self.lb_hint_2.hide()

        # 불러온 주소 리스트에 추가
        for i in range(len(self.address)):
            result = self.address.iloc[i]
            if result['건물명칭'] == "": bld_name = ""
            else: bld_name = " (%s)" % result['건물명칭']

            new = result['도로명주소'] + bld_name
            bjr_nm = '' if result['법정리'] == '' else ' %s' % result['법정리']
            old = "%s %s %s%s %s" % (result['시도'], result['시군구'], result['읍면동'], bjr_nm, result['번'])
            if result['지'] != '0': old = "%s-%s" % (old, result['지'])

            if len(new) > 33: new = new[0:33] + '···'

            custom_item = AddressListItem(new, old)
            item = QListWidgetItem(self.list_address)
            item.setSizeHint(custom_item.sizeHint())
            self.list_address.setItemWidget(item, custom_item)

    # 주소 선택
    def select_address_event(self):
        self.result = self.address.iloc[self.list_address.currentRow()]
        self.close()

    ########################################################################################################

    # 다이얼로그 엔터키 막기
    def keyPressEvent(self, event):
        if ((not event.modifiers() and
             event.key() == Qt.Key_Return) or
                (event.modifiers() == Qt.KeypadModifier)):
            event.accept()
        else: super(FindAddressLite, self).keyPressEvent(event)


class AddressListItem(QWidget):
    def __init__(self, new, old):
        super(AddressListItem, self).__init__()
        border_txt_old = """QLabel { font: 12px "웰컴체 Regular";
                        color: white;
                        border: none;
                        background: rgb(148,148,255);
                        padding-left: 5px;
                        padding-top: 3px;
                        border-radius: 5px;}"""

        border_txt_new = """QLabel { font: 12px "웰컴체 Regular";
                        color: white;
                        border: none;
                        background: rgb(148,148,255);
                        padding-left: 4px;
                        padding-top: 3px;
                        border-radius: 5px;}"""

        self.lb_old_icon = QLabel()
        self.lb_old_icon.setMaximumSize(44, 23)
        self.lb_old_icon.setText("지   번")
        self.lb_old_icon.setStyleSheet(border_txt_old)

        self.lb_old = QLabel()
        self.lb_old.setText(old)
        self.lb_old.setStyleSheet("""QLabel { font: 15px "웰컴체 Regular"; color: rgb(65,65,65); padding-top: 2px;}""")

        self.lb_new_icon = QLabel()
        self.lb_new_icon.setMaximumSize(44, 23)
        self.lb_new_icon.setText("도로명")
        self.lb_new_icon.setStyleSheet(border_txt_new)

        self.lb_new = QLabel()
        self.lb_new.setText(new)
        self.lb_new.setStyleSheet("""QLabel { font: 14px "웰컴체 Regular"; color: rgb(125,125,125); padding-left: 2px; padding-top: 2px;}""")

        self.set_ui()

    def set_ui(self):
        grid_box = QGridLayout()
        grid_box.addWidget(self.lb_old_icon, 0, 0)
        grid_box.addWidget(self.lb_new_icon, 1, 0)
        grid_box.addWidget(self.lb_old, 0, 1)
        grid_box.addWidget(self.lb_new, 1, 1)

        self.setLayout(grid_box)


# 예외 오류 처리
def my_exception_hook(exctype, value, traceback):
    sys.excepthook(exctype, value, traceback)


sys._excepthook = sys.excepthook
sys.excepthook = my_exception_hook
