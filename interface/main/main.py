from PySide6.QtCore import QSize
from PySide6.QtWidgets import *
from interface.main.resources.ui.item_widget import Item


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__(parent=None)

        self.table = QListWidget(self)
        layout = QGridLayout(self)
        layout.addWidget(self.table, 0, 0)

        data = {'type': '다가구',
                'kind': '전세',
                'price': '2억 3,000만',
                'address': '서울특별시 중랑구 봉우재로154, 702호 (다원빌)',
                'count': '방 2개 / 욕실 1개',
                'tot': '35.72㎡',
                'area': '28.25㎡',
                'num_1': '010-9386-7937',
                'num_2': '010-2486-1307',
                'pet': '불가',
                'parking': '가능',
                'ev': '있음'
                }

        custom_item = Item(data)
        item = QListWidgetItem(self.table)
        item.setSizeHint(QSize(custom_item.width(), 61))
        self.table.setItemWidget(item, custom_item)

    def resizeEvent(self, event):

        super(Window, self).resizeEvent(event)


if __name__ == '__main__':

    import sys
    app = QApplication()
    window = Window()
    window.show()
    sys.exit(app.exec_())
