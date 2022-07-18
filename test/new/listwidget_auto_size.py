from PySide6.QtWidgets import *
import sys


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 100)

        self.item_type = QLabel(self)
        self.item_type.setText('안녕')
        self.item_type2 = QLabel(self)
        self.item_type.setText('안녕')
        self.pushButton3 = QPushButton("Button3")

        layout = QHBoxLayout()
        layout.addWidget(self.item_type)
        layout.addWidget(self.item_type2)
        layout.addWidget(self.pushButton3)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()