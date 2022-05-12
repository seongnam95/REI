import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect
from PySide6.QtGui import QIcon, QColor
from ui.main.ui_add_room import Ui_AddRoom

class AddRoom(QMainWindow, Ui_AddRoom):
    def __init__(self):
        super(AddRoom, self).__init__()
        self.setupUi(self)
        self._init_shadows()
        self._init_interaction()
        self.show()

    def _init_interaction(self):
        self.btn_back.clicked.connect(lambda: self.page_change_event(self.stackedWidget.currentIndex() - 1))
        self.btn_next.clicked.connect(lambda: self.page_change_event(self.stackedWidget.currentIndex() + 1))

        self.btn_page_1.clicked.connect(lambda: self.page_change_event(0))
        self.btn_page_2.clicked.connect(lambda: self.page_change_event(1))
        self.btn_page_3.clicked.connect(lambda: self.page_change_event(2))

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

    def page_change_event(self, page):
        self.stackedWidget.setCurrentIndex(page)

        page_btn = {0: self.btn_page_1, 1: self.btn_page_2, 2: self.btn_page_3}
        current_idx = self.stackedWidget.currentIndex()

        for btn in page_btn.values():
            btn.setChecked(False)
            page_btn[current_idx].setChecked(True)

# 예외 오류 처리
def my_exception_hook(exctype, value, traceback):
    sys.excepthook(exctype, value, traceback)


sys._excepthook = sys.excepthook
sys.excepthook = my_exception_hook

app = QApplication()
window = AddRoom()
app.exec()
