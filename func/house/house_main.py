import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import os
from PIL import Image
# import pyautogui

FROM_CLASS = uic.loadUiType('./data/add_house.ui')[0]


class HouseMain(QDialog, FROM_CLASS):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bt_add.clicked.connect(self.clicked_add_bt)
        self.list_top.itemDoubleClicked.connect(self.test)
        # self.lw_img.model().rowsMoved.connect(self.test1)
        # self.a.png = QListWidget(self)

    def clicked_add_bt(self):
        img_dlg = QFileDialog.getOpenFileNames(self, '매물 사진 불러오기', os.path.expanduser('~'), '이미지 파일 (*.jpg *.png);;')
        print(img_dlg[0])
        for img in img_dlg[0]:
            custom_item = CustomListItem(img)
            item = QListWidgetItem(self.list_top)
            item.setSizeHint(custom_item.sizeHint())
            self.list_top.setItemWidget(item, custom_item)

    def test(self):
        print(self.list_top.currentRow())
        lst_item = self.list_top.selectedItems()
        for item in lst_item:
            print(item.text())

    def test1(self):
        print('a.png')

    # 예외 오류 처리
    def my_exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)

    sys._excepthook = sys.excepthook
    sys.excepthook = my_exception_hook

class CustomListItem(QWidget):
    def __init__(self, img):
        super(CustomListItem, self).__init__()

        i = Image.open(img)
        width, height = i.size

        self.pix = QPixmap(img)
        self.iconQLabel = QLabel()
        self.iconQLabel.setPixmap(self.pix.scaled(132, 99))

        if width > height:
            v = height * (500 / width)
            self.iconQLabel.setToolTip(
                "<a.png href=\"" + img + "\"><img src=\"" + img + "\" width=\"500\" height=\"" + str(v) + "\" /></a.png>")
        else:
            v = height * (400 / width)
            self.iconQLabel.setToolTip(
                "<a.png href=\"" + img + "\"><img src=\"" + img + "\" width=\"400\" height=\"" + str(v) + "\" /></a.png>")

        self.set_ui()

    def set_ui(self):
        grid_box = QGridLayout()
        grid_box.addWidget(self.iconQLabel)

        self.setLayout(grid_box)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = HouseMain()
    form.show()
    app.exec_()
