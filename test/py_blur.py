import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QGraphicsEffect, QGraphicsDropShadowEffect
from PySide6.QtCore import *
from PySide6.QtGui import *
from ui.dialog.ui_address_lite import Ui_FindAddress

class Principal(QMainWindow, Ui_FindAddress):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.desenfoque = QGraphicsDropShadowEffect()
        self.desenfoque.setBlurRadius(0.4)
        self.setGraphicsEffect(self.desenfoque)

    def paintEvent(self, event=None):
        painter = QPainter(self)
        painter.setOpacity(0.7)
        painter.setBrush(Qt.white)
        painter.setPen(QPen(Qt.white))
        painter.drawRect(self.rect())


app = QApplication([])
p = Principal()
p.show()
app.exec_()
