import sys

from PySide6.QtGui import QColor, QIcon
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QDialog, QApplication, QGraphicsDropShadowEffect
from ui.dialog.ui_register import Ui_Dialog

from interface.sub_interface import address_details
import rei_bot.issuance_register_of_building as ibl


class LedgerDialog(QDialog, Ui_Dialog):
    def __init__(self, data=None):
        super().__init__()
        self.setupUi(self)
        self.set_shadow()

        self.btn_issuance.clicked.connect(self.clicked_issuance_btn)

        self.edt_address.mousePressEvent = self.clicked_address_edit
        self.edt_address.returnPressed.connect(self.clicked_address_edit)

        self.btn_search.setIcon(QIcon('../../data/img/button/search_icon.png'))
        self.btn_search.setIconSize(QSize(25, 25))

        self.show()

    # UI 그림자 설정
    def set_shadow(self):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(30)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        shadow.setColor(QColor(0, 0, 0, 40))
        self.address_frame.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(30)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        shadow.setColor(QColor(0, 0, 0, 40))
        self.type_frame.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(30)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        shadow.setColor(QColor(0, 0, 0, 100))
        self.btn_issuance.setGraphicsEffect(shadow)

    def clicked_address_edit(self, e=None):
        dialog = address_details.AddressDetails(1, self.edt_address.text())
        dialog.exec()

        if dialog.result:
            self.binfo = dialog.binfo

            self.cbx_rooms.clear()
            self.cbx_rooms.addItems(dialog.detail_list)
            self.cbx_rooms.setCurrentIndex(dialog.select_index)

            address = dialog.select_address

            if address['지'] == "0": old = "%s %s %s %s" % (address['시도'], address['시군구'], address['읍면동'], address['번'])
            else: old = "%s %s %s %s-%s" % (address['시도'], address['시군구'], address['읍면동'], address['번'], address['지'])

            self.edt_address.setText(old)

    def clicked_issuance_btn(self):
        if self.binfo['타입'] == '집합':
            self.btn_issuance.setEnabled(False)
            pk = self.issuance_data['호_PK']

        elif self.binfo['타입'] == '일반':
            self.msg.show_msg(2000, 'center', '전유부는 집합 건물만 발급할 수 있습니다')
            return

        self.btn_issuance.setEnabled(False)
        pk = self.issuance_data['동_PK']

        self.issuance_thread = ibl.IssuanceBuildingLedger(pk, item_row, self.driver, self.login_cookies)
        self.issuance_thread.threadEvent.workerThreadDone.connect(lambda: self.btn_issuance.setEnabled(True))
        self.issuance_thread.threadEvent.progress.connect(self.issuance_progress_event)
        self.issuance_thread.start()

    # 다이얼로그 엔터키 막기
    def keyPressEvent(self, event):
        if ((not event.modifiers() and
             event.key() == Qt.Key_Return) or
                (event.modifiers() == Qt.KeypadModifier)):
            event.accept()
        else: super(LedgerDialog, self).keyPressEvent(event)

# 예외 오류 처리
def my_exception_hook(exctype, value, traceback):
    sys.excepthook(exctype, value, traceback)


sys._excepthook = sys.excepthook
sys.excepthook = my_exception_hook


app = QApplication()
window = LedgerDialog()
app.exec()
