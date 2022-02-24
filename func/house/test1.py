import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap

FROM_CLASS = uic.loadUiType('./data/test.ui')[0]

class HouseMain(QDialog, FROM_CLASS):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


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