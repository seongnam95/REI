import sys

from ui.dialog.ui_register import Ui_Dialog
from PySide6.QtWidgets import QDialog, QLabel, QListWidgetItem, QMessageBox, QWidget, \
    QGridLayout, QApplication, QGraphicsOpacityEffect, QGraphicsDropShadowEffect

from PySide6.QtGui import QColor


class RegisterPopUp(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

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

        self.cbx_rooms.addItem("aa")
        self.cbx_rooms.addItem("aa")

        self.show()

    def set_shadow(self):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(30)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        shadow.setColor(QColor(0, 0, 0, 70))
        return shadow


# 예외 오류 처리
def my_exception_hook(exctype, value, traceback):
    sys.excepthook(exctype, value, traceback)


sys._excepthook = sys.excepthook
sys.excepthook = my_exception_hook


app = QApplication()
window = RegisterPopUp()
app.exec()
