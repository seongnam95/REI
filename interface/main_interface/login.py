import sys
import register

from PySide6.QtWidgets import QMainWindow, QMessageBox, QApplication

from module.mysql import ReadMysqlData
from ui.main.ui_login import Ui_Login

class LoginMain(QMainWindow, Ui_Login):
    def __init__(self):
        super().__init__()
        self.sign = register.Register()
        self.mysql = ReadMysqlData()

        self.setupUi(self)
        self.init_interaction()

        self.edt_id.setFocus()

    def init_interaction(self):
        self.btn_register.clicked.connect(self.register_event)
        self.btn_login.clicked.connect(self.login_event)

        self.edt_id.returnPressed.connect(self.login_event)
        self.edt_pw.returnPressed.connect(self.login_event)

    def register_event(self):
        self.sign = register.Register()
        self.sign.show()

    def login_event(self):
        if self.mysql.login(self.edt_id.text(), self.edt_pw.text()):
            self.msg("basic", "로그인이 완료되었습니다.")
        else: self.msg("basic", "아이디 또는 패스워드를 확인해주세요.")

    # 메세지 함수
    def msg(self, ty, content):
        title = " "
        if ty == "basic":
            QMessageBox().about(self, title, content)
        elif ty == "info":
            QMessageBox().information(self, title, content, QMessageBox.Ok)
        elif ty == "warning":
            QMessageBox().warning(self, title, content, QMessageBox.Ok)
        elif ty == "critical":
            QMessageBox().critical(self, title, content, QMessageBox.Ok)

    # 예외 오류 처리
    def my_exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys.excepthook(exctype, value, traceback)

    sys._excepthook = sys.excepthook
    sys.excepthook = my_exception_hook


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = LoginMain()
    form.show()
    app.exec()
