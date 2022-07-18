from PySide6.QtCore import QSize
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import *
from interface.main.resources.ui.item_widget import Item


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__(parent=None)
        self.resize(1200, 200)
        self.grid_layout = QGridLayout(self)

        data = {'type': '다가구',
                'kind': '전세',
                'price': '2억 3,000만',
                'address': '서울특별시 중랑구 봉우재로154, 702호sdsadsadsa(다원빌)',
                'room': '2개',
                'bath': '1개',
                'tot': '35.72㎡',
                'area': '28.25㎡',
                'num_1': '010-9386-7937',
                'num_2': '010-2486-1307',
                'pet': '불가',
                'parking': '가능',
                'ev': '있음'
                }
        # self.table = QListWidget(self)
        self.item1 = Item(data)
        self.item2 = Item(data)
        self.grid_layout.addWidget(self.item1, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.item2, 1, 0, 1, 1)

        # custom_item = Item(data)
        # item = QListWidgetItem(self.table)
        # item.setSizeHint(QSize(custom_item.width(), 65))
        # self.table.setItemWidget(item, custom_item)

    def resizeEvent(self, event):

        super(Window, self).resizeEvent(event)


if __name__ == '__main__':

    import sys
    app = QApplication()
    window = Window()
    window.show()
    sys.exit(app.exec())
