from PySide6.QtWidgets import QWidget, QLabel, QPushButton
from PySide6.QtCore import QSize, QRect, Qt
import sys

class TitleBarWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.resize(QSize(parent.width(), 60))

        self.main_widget = QWidget(self)
        self.main_widget.resize(self.width(), self.height())
        self.main_widget.setStyleSheet("""QWidget { background-color: white;
                                        border-bottom: 1px solid;
                                        border-color: rgba(0, 0, 0, 50); }""")

        self.lb_title = QLabel(self.main_widget)
        self.lb_title.setAlignment(Qt.AlignHCenter)
        title_lb_x = int((self.main_widget.width() / 2) - 110)
        self.lb_title.setGeometry(QRect(title_lb_x, 5, 220, 28))
        self.lb_title.setStyleSheet("""QLabel{ background-color: white;
                                               font: 25px "웰컴체 Regular";
                                               color: rgba(0, 0, 0, 100);
                                               border: 0px; }""")

        self.lb_sub_title = QLabel(self.main_widget)
        self.lb_sub_title.setAlignment(Qt.AlignHCenter)
        sub_title_lb_x = int((self.main_widget.width() / 2) - 110)
        self.lb_sub_title.setGeometry(QRect(sub_title_lb_x, 32, 220, 20))
        self.lb_sub_title.setStyleSheet("""QLabel{ background-color: white;
                                                   font: 15px "웰컴체 Regular";
                                                   color: rgba(0, 0, 0, 120);
                                                   border: 0px; }""")

        self.btn_back = QPushButton(self.main_widget)
        self.btn_back.setGeometry(QRect(10, 10, 40, 40))

        next_btn_x = self.main_widget.width() - 50
        self.btn_next = QPushButton(self.main_widget)
        self.btn_next.setGeometry(QRect(next_btn_x, 10, 40, 40))

    def setSize(self, w, h):
        self.resize(w, h)

    def setTitle(self, text):
        self.lb_title.setText(text)

    def setSubTitle(self, text):
        self.lb_sub_title.setText("(  %s  )" % text)
