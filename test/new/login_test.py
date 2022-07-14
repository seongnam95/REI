import random
from PySide6.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.table = QListWidget(self)
        self.button = QPushButton('Populate', self)
        layout = QGridLayout(self)
        layout.addWidget(self.table, 0, 0)
        layout.addWidget(self.button, 1, 0)

    def resizeEvent(self, event):
        print('a')
        super(Window, self).resizeEvent(event)


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.setGeometry(700, 150, 800, 400)
    window.show()
    sys.exit(app.exec_())
