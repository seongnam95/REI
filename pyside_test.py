import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from ui.main.tt import Ui_MainWindow


class MainLease(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainLease, self).__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.show()


# 예외 오류 처리
def my_exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    sys.excepthook(exctype, value, traceback)


sys._excepthook = sys.excepthook
sys.excepthook = my_exception_hook

app = QApplication()
window = MainLease()
window.show()
app.exec()
