from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import QRect
from ui.custom.TitleBarWidget import TitleBarWidget
from aa import Ui_Form

import sys


class MainLease(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainLease, self).__init__(*args, **kwargs)

        self.resize(500, 500)

        self.title_bar = TitleBarWidget(self)
        self.title_bar.setTitle("CONTRACT")
        self.title_bar.setSubTitle("계약서")

        self.show()


# 예외 오류 처리
def my_exception_hook(exctype, value, traceback):
    sys.excepthook(exctype, value, traceback)


sys._excepthook = sys.excepthook
sys.excepthook = my_exception_hook

app = QApplication()
window = MainLease()
app.exec()
