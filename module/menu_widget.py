from PySide6.QtWidgets import QApplication, QMainWindow, QButtonGroup, QWidget, QLabel, QLineEdit, QComboBox, \
    QListWidget, QListWidgetItem, QGraphicsOpacityEffect
from PySide6.QtCore import QPropertyAnimation, Qt, QSize, QRegularExpression, QRect, QEvent, QTimer, QPoint
from PySide6.QtGui import QIcon, QRegularExpressionValidator, QPixmap


class BoxMessage(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("QWidget {background-color: rgba(0,0,0,150);"
                                          "font: 15px \uc6f0\ucef4\uccb4 Regular;"
                                          "color: white;"
                                          "border-radius: 3px;"
                                          "padding-top: 3px;}")


class MenuItem(QWidget):
    def __init__(self, txt, icon):
        super(MenuItem, self).__init__()

        self.lb_icon = QLabel(self)
        self.lb_icon.setPixmap()