import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QGraphicsEffect, QGraphicsDropShadowEffect
from PySide6.QtCore import *
from PySide6.QtGui import *
from ui.ui_test import Ui_MainWindow


class Principal(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()



app = QApplication([])
fontDB = QFontDatabase()
fontDB.addApplicationFont('./웰컴체 Regular.ttf')
print(fontDB.Korean)
app.setFont(QFont('웰컴체 Regular'))
p = Principal()
p.show()
app.exec_()
