import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *


class WindowClass(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._setup_ui()

        self.fontSize = 10

        # TextEdit과 관련된 버튼에 기능 연결
        self.btn_printTextEdit.clicked.connect(self.printTextEdit)
        self.btn_clearTextEdit.clicked.connect(self.fontBold)
        self.btn_setFont.clicked.connect(self.fontUnderLine)
        self.btn_setFontItalic.clicked.connect(self.fontItalic)
        self.btn_setFontColor.clicked.connect(self.fontColorRed)
        self.btn_fontSizeUp.clicked.connect(self.fontSizeUp)
        self.btn_fontSizeDown.clicked.connect(self.fontSizeDown)

    def _setup_ui(self):
        self.resize(400, 400)

        self.btn_printTextEdit = QPushButton(self)
        self.btn_printTextEdit.move(0, 0)
        self.btn_printTextEdit.setText('출력')

        self.btn_clearTextEdit = QPushButton(self)
        self.btn_clearTextEdit.move(0, 30)
        self.btn_clearTextEdit.setText('클리어')

        self.btn_setFont = QPushButton(self)
        self.btn_setFont.move(0, 60)
        self.btn_setFont.setText('볼드')

        self.btn_setFontItalic = QPushButton(self)
        self.btn_setFontItalic.move(0, 90)
        self.btn_setFontItalic.setText('기울기')

        self.btn_setFontColor = QPushButton(self)
        self.btn_setFontColor.move(0, 120)
        self.btn_setFontColor.setText('빨간색 변경')

        self.btn_fontSizeUp = QPushButton(self)
        self.btn_fontSizeUp.move(0, 150)
        self.btn_fontSizeUp.setText('사이즈 업')

        self.btn_fontSizeDown = QPushButton(self)
        self.btn_fontSizeDown.move(0, 180)
        self.btn_fontSizeDown.setText('사이즈 다운')

        self.textedit_Test = QTextEdit(self)
        self.textedit_Test.resize(200, 200)
        self.textedit_Test.move(0, 210)

    def printTextEdit(self):
        print(self.textedit_Test.toPlainText())
        print(self.textedit_Test.toHtml())

    def clearTextEdit(self):
        self.textedit_Test.clear()

    def fontBold(self):
        # print(self.textedit_Test.fontWeight)
        self.textedit_Test.setFontWeight(QFont.Bold)
        # self.textedit_Test.setFontWeight(QFont.Normal)

    def fontUnderLine(self):
        under = self.textedit_Test.fontUnderline()
        print(under)
        self.textedit_Test.setFontUnderline(False) if under else self.textedit_Test.setFontUnderline(True)

    def fontItalic(self):
        italic = self.textedit_Test.fontItalic()
        self.textedit_Test.setFontItalic(False) if italic else self.textedit_Test.setFontItalic(True)

    def fontColorRed(self):
        colorvar = QColor(255, 0, 0)
        self.textedit_Test.setTextColor(colorvar)

    def fontSizeUp(self):
        self.fontSize = self.fontSize + 1
        self.textedit_Test.setFontPointSize(self.fontSize)

    def fontSizeDown(self):
        self.fontSize = self.fontSize - 1
        self.textedit_Test.setFontPointSize(self.fontSize)


if __name__ == "__main__":
    app = QApplication()
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
