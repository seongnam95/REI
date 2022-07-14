import sys
import re

from interface.sub_interface.address import Address
from ui.main.ui_sign_up import Ui_SignUp
from module.mysql import ReadMysqlData

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QListView, QLineEdit, QMessageBox
from PySide6.QtCore import QSize


class Register(QMainWindow, Ui_SignUp):
    def __init__(self):
        super().__init__()

        self.binfo, self.company = None, None
        self.eyepw, self.eyepwre = False, False
        self.mysql = ReadMysqlData()

        self.init_ui()
        self.init_interaction()

    # UI 설정
    def init_ui(self):
        self.setupUi(self)
        self.cbx_rank.setView(QListView())

        self.btn_eye.hide()
        self.btn_eye_re.hide()

        # 텍스트 힌트
        self.edt_address.setPlaceholderText("(클릭)")
        self.edt_company.setPlaceholderText("(주소 입력 후 클릭)")
        self.edt_company_call.setPlaceholderText("- 부호 생략 (자동입력)")
        self.edt_phone.setPlaceholderText("- 부호 생략 (자동입력)")
        self.edt_pwre.setPlaceholderText("비밀번호 재입력")
        self.edt_name.setPlaceholderText("2~10자리의 한글만 입력")
        self.edt_pw.setPlaceholderText("4자리 이상, 20자리 이하")

        # UI 아이콘 이미지 설정
        self.btn_eye.setIcon(QIcon('../../static/img/system/eye.png'))
        self.btn_eye.setIconSize(QSize(20, 20))
        self.btn_eye_re.setIcon(QIcon('../../static/img/system/eye.png'))
        self.btn_eye_re.setIconSize(QSize(20, 20))

    # UI 상호작용 컨넥트
    def init_interaction(self):
        self.edt_address.mousePressEvent = self.address_event
        self.edt_company.mousePressEvent = self.find_company_event

        # 텍스트 변경
        self.edt_address.textChanged.connect(self.company_check_reset)
        self.edt_company_call.textChanged.connect(self.numc_number)
        self.edt_phone.textChanged.connect(self.numc_phone)
        self.edt_id.textChanged.connect(self.id_check_reset)
        self.edt_pw.textChanged.connect(self.show_eye)
        self.edt_pwre.textChanged.connect(self.pw_check_event)

        # 엔터키
        self.edt_id.returnPressed.connect(self.id_check_event)
        self.edt_pwre.returnPressed.connect(self.register_event)

        # 버튼 클릭
        self.btn_id_check.clicked.connect(self.id_check_event)
        self.btn_register.clicked.connect(self.register_event)
        self.btn_eye.clicked.connect(self.show_pw)
        self.btn_eye_re.clicked.connect(self.show_pw_re)

    # --------- 상호작용 이벤트 ---------- #
    # # 주소 찾기 버튼
    def address_event(self, e):
        dialog = Address()
        dialog.exec()

        if dialog.result_data is None: return
        elif dialog.result_data['주소'] == "": return
        self.binfo = dialog.result_data['정보']
        self.edt_address.setText(dialog.result_data['주소'])

    # 사무소 찾기 버튼
    def find_company_event(self, e):
        if self.binfo is not None:
            key = 'ff8e71ba71f059c00ec57f'
            code = self.binfo['주소코드']

            dialog = func_dialog.Company(key, code[0:5])
            dialog.exec()

            if len(dialog.data) != 0:
                self.company = dialog.data
                self.edt_boss_name.setText(self.company[3])
                self.edt_company.setText(self.company[2])
                self.edt_company_number.setText(self.company[1])

    # 아이디 중복확인 버튼
    def id_check_event(self):
        txt = self.edt_id.text()
        if txt == "":
            self.msg("basic", "아이디를 입력해주세요.")
            return

        # DB 아이디 중복 확인
        if self.mysql.check_id(txt):
            self.msg("info", "이미 사용중인 아이디입니다.")
            self.edt_id.setFocus()
        else:
            self.msg("info", "사용 가능한 아이디입니다.")
            self.edt_pw.setFocus()
            self.btn_id_check.setText("인증완료")

    # 회원가입 버튼
    def register_event(self):
        if self.edit_check():
            company_call = self.cbx_company_call.currentText() + '-' + self.edt_company_call.text()
            data = (self.edt_id.text(), self.edt_pw.text(), self.edt_name.text(), self.edt_phone.text(),
                    self.cbx_rank.currentText(), self.edt_company.text(), self.edt_address.text(),
                    self.edt_boss_name.text(), company_call, self.edt_company_number.text())
            self.mysql.register(data)
            self.msg("info", "회원 가입이 완료되었습니다.")
            self.hide()

    # 종료 버튼
    def exit_event(self):
        self.hide()

    # 비밀번호 재확인
    def pw_check_event(self):
        if len(self.edt_pwre.text()) >= 1:
            self.btn_eye_re.show()
        else:
            self.btn_eye_re.hide()

        if len(self.edt_pw.text()) <= len(self.edt_pwre.text()):
            if self.edt_pw.text() != self.edt_pwre.text():
                self.lb_pwcheck.setText("패스워드가 일치하지 않습니다.")
                self.lb_pwcheck.setStyleSheet("""QLabel {font: 11px "웰컴체 Regular"; color: #c0392b;;}""")
            else:
                self.lb_pwcheck.setText("패스워드가 일치합니다.")
                self.lb_pwcheck.setStyleSheet("""QLabel {font: 11px "웰컴체 Regular"; color: #3498db;}""")
        else:
            self.lb_pwcheck.setText("")

    # --------- 위젯 이벤트 ---------- #
    def show_pw(self):
        if self.eyepw:
            self.edt_pw.setEchoMode(QLineEdit.Password)
            self.eyepw = False
        else:
            self.edt_pw.setEchoMode(QLineEdit.Normal)
            self.eyepw = True

    def show_pw_re(self):
        if self.eyepwre:
            self.edt_pwre.setEchoMode(QLineEdit.Password)
            self.eyepwre = False
        else:
            self.edt_pwre.setEchoMode(QLineEdit.Normal)
            self.eyepwre = True

    # 빈 에디터 확인
    def edit_check(self):
        if self.edt_address.text() == "":
            self.msg("info", "사무실 주소를 입력해주세요.")
            self.edt_address.setFocus()
        elif self.edt_company.text() == "":
            self.msg("info", "사무실 상호명을 입력해주세요.")
            self.edt_company.setFocus()
        elif self.edt_boss_name.text() == "":
            self.msg("info", "[ 조회 ] 버튼을 클릭하여 대표 공인중개사를 선택해주세요.")
            self.edt_boss_name.setFocus()
        elif self.cbx_company_call.currentText() == "(선택)":
            self.msg("info", "대표번호의 지역번호를 선택해주세요.")
            self.cbx_company_call.showPopup()
        elif not re.findall('^\d{3,4}-\d{4}', self.edt_company_call.text()):
            self.msg("info", "대표번호 형식이 올바르지 않습니다.")
            self.edt_company_call.setFocus()
        elif not re.findall('[가-힣]{2,10}', self.edt_name.text()):
            self.msg("info", "가입자의 성명을 확인해주세요. (2~10글자의 한글만 입력 가능)")
            self.edt_name.setFocus()
        elif not re.findall('^01\d{1}-\d{3,4}-\d{4}', self.edt_phone.text()):
            self.msg("info", "가입자의 핸드폰 번호 형식이 올바르지 않습니다.")
            self.edt_phone.setFocus()
        elif self.cbx_rank.currentText() == "(선택)":
            self.msg("info", "가입자의 직급을 선택해주세요.")
            self.cbx_rank.showPopup()
        elif self.edt_id.text() == "":
            self.msg("info", "사용하실 아이디 입력 후 중복확인 해주세요.")
            self.edt_id.setFocus()
        elif self.btn_id_check.text() == "중복확인":
            self.msg("info", "사용하실 아이디 입력 후 중복확인 해주세요.")
            self.edt_id.setFocus()
        elif self.edt_pw.text() == "":
            self.msg("info", "비밀번호를 입력해주세요.")
            self.edt_pw.setFocus()
        elif self.edt_pwre.text() == "":
            self.msg("info", "비밀번호를 입력해주세요.")
            self.edt_pwre.setFocus()
        elif self.edt_pw.text() != self.edt_pwre.text():
            self.msg("info", "비밀번호가 불일치합니다. 다시한번 확인해주세요.")
            self.edt_pwre.setText("")
            self.edt_pwre.setFocus()
        elif not self.mysql.check_phone(self.edt_phone):
            self.msg("info", "이미 회원 등록 된 연락처입니다. 회원 정보를 찾으려면 ID/PW찾기를 이용해주세요.")
            self.edt_phone.setFocus()
        else:
            return True

    # 눈 버튼 쇼/하이드
    def show_eye(self):
        if len(self.edt_pwre.text()) > 0:
            self.edt_pwre.setText("")
            self.lb_pwcheck.setText("")
        if len(self.edt_pw.text()) >= 1:
            self.btn_eye.show()
        else:
            self.btn_eye.hide()

    # ID 중복확인 리셋
    def id_check_reset(self):
        self.btn_id_check.setText("중복확인")

    # 사무소 찾기 리셋
    def company_check_reset(self):
        self.edt_company.setText("")
        self.edt_boss_name.setText("")
        self.edt_company_number.setText("")

    # 번호 정규식
    def numc_phone(self):
        phone = self.edt_phone.text()
        phone = re.sub("-", "", phone)
        phone = re.sub(r'(\d{3})(\d{3,4})(\d{4})', r'\1-\2-\3', phone)

        self.edt_phone.setText(phone)

    def numc_number(self):
        number = self.edt_company_call.text()
        number = re.sub("-", "", number)
        number = re.sub(r'(\d{3,4})(\d{4})', r'\1-\2', number)

        self.edt_company_call.setText(number)

    # --------- 기타 함수 ---------- #

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
