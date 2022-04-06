from PySide6.QtWidgets import QApplication, QMainWindow, QButtonGroup, QWidget, QLabel, QLineEdit, QComboBox, \
    QListWidget, QListWidgetItem, QGraphicsOpacityEffect, QHBoxLayout
from PySide6.QtCore import QPropertyAnimation, Qt, QSize, QRegularExpression, QRect, QEvent, QTimer, QPoint
from PySide6.QtGui import QIcon, QRegularExpressionValidator, QPixmap, QFont

class MainWidgetTest(QMainWindow):
    def __init__(self):
        super(MainWidgetTest, self).__init__()
        self.setGeometry(0, 0, 400, 400)

        self.bx = BoxMessage(self)
        self.bx.setGeometry(0, 0, 150, 200)
        self.bx.add_item('내 매물에 추가', 'a.png')
        self.bx.add_item('본 매물 공유하기', 'a.png')
        self.bx.add_item('매물 추가', 'a.png')

        self.bx.set_size(self.bx)

        self.show()


class BoxMessage(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setStyleSheet("""QListWidget {
                                font: 14px "웰컴체 Regular";
                                color: white;
                                background-color: rgba(0,0,0,150);
                                border-radius: 5px;
                                padding: 5px;
                                outline: none;
                            }
                            QListWidget:item {
                                border-radius: 5px;
                            }
                            QListWidget:item:hover {
                                background-color: rgba(255, 255, 255, 80);
                            }""")

    def add_item(self, txt, icon):
        custom_item = MenuItem(txt, icon)
        item = QListWidgetItem()
        item.setSizeHint(QSize(self.width() - 10, 30))
        self.addItem(item)
        self.setItemWidget(item, custom_item)

    def set_size(self, bx):
        h = (30 * bx.count()) + 10
        self.setFixedSize(bx.width(), h)


class MenuItem(QWidget):
    def __init__(self, txt, icon):
        super(MenuItem, self).__init__()

        icon = QPixmap(icon).scaled(23, 23)
        self.lb_icon = QLabel(self)
        self.lb_icon.setFixedSize(23, 23)
        self.lb_icon.setPixmap(icon)
        self.lb_icon.setGeometry(5, 3, 23, 23)

        self.lb_text = QLabel(self)
        self.lb_text.setFixedHeight(20)
        self.lb_text.setStyleSheet("QLabel {font: 14px '웰컴체 Regular'; color: white;}")
        self.lb_text.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.lb_text.setText(txt)
        self.lb_text.setGeometry(30, 6, 105, 25)


app = QApplication()
window = MainWidgetTest()
app.exec()
