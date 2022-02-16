from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import QRect, QPoint
from ui.custom.TitleBarWidget import TitleBarWidget
from module.black_box_msg import BoxMessage
import sys


class MainLease(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainLease, self).__init__(*args, **kwargs)

        self.resize(500, 500)

        self.title_bar = TitleBarWidget(self)
        self.title_bar.setTitle("CONTRACT")
        self.title_bar.setSubTitle("계약서")

        self.title_bar.btn_next.clicked.connect(lambda: self.msg.show_msg(1500, QPoint(100, 100), "안녕하세요 반갑습니다 저는 장성남입니다\n헬로헬ㄹ\n헬호우"))
        self.title_bar.btn_back.clicked.connect(lambda: self.msg.show_msg(1500, 'top', "안녕하세요 반갑습니다 저는 장성남입니다\n헬로헬ㄹ\n헬호우"))

        self.msg = BoxMessage(self)

        self.show()

# 예외 오류 처리
def my_exception_hook(exctype, value, traceback):
    sys.excepthook(exctype, value, traceback)


sys._excepthook = sys.excepthook
sys.excepthook = my_exception_hook

app = QApplication()
window = MainLease()
app.exec()
