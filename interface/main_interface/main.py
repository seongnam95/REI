
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize
from func.info.info_main import InfoMain

import sys
import configparser
from module.mysql import ReadMysqlData

config = configparser.ConfigParser()
config.read('./data/config.ini')
geometry = config['GEOMETRY']

FROM_CLASS = ''
if geometry['type'] == 'length':
    FROM_CLASS = uic.loadUiType('./data/uiMain/ui_widgets_length.ui')[0]

elif geometry['type'] == 'width':
    FROM_CLASS = uic.loadUiType('./data/uiMain/ui_widgets_width.ui')[0]


class ReiMain(QMainWindow, FROM_CLASS):
    def __init__(self):
        super().__init__()

        self.sys_value = ReadMysqlData().read_system_value()
        self.syscheck()

        self.form_settings = config['FORM']
        self.opacity = int(self.form_settings['opacity'])

        self.setupUi(self)
        self.setWindowOpacity(self.opacity/100)
        self.set_position(geometry['type'], geometry['position'])

        self.ui_setting()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

    def syscheck(self):
        ver = "0.1"
        version = self.sys_value[0]
        block = self.sys_value[1]
        block_msg = self.sys_value[2]

        if block:
            self.msg("warning", "경고", "관리자에 의하여 차단된 프로그램입니다.\n\nmsg: " + block_msg)
            exit()

        elif ver != version:
            self.msg("info", "정보", "새로운 버전이 업데이트 되었습니다. \n\n확인 버튼을 누르시면 다운로드가 시작툅니다.")

    # UI 세팅
    def ui_setting(self):
        self.slider.setValue(self.opacity)
        self.slider.valueChanged.connect(self.opacity_slider)

        self.bt_exit.setIcon(QIcon('../../data/img/button/exit.png'))
        self.bt_exit.setIconSize(QSize(22, 22))
        self.bt_exit.clicked.connect(self.clicked_exit)

        self.bt_max.setIcon(QIcon('../../data/img/button/maximize.png'))
        self.bt_max.setIconSize(QSize(13, 13))
        self.bt_max.clicked.connect(self.clicked_max_mini)

        self.bt_menu.setIcon(QIcon('../../data/img/button/menu.png'))
        self.bt_menu.setIconSize(QSize(12, 12))
        self.bt_menu.clicked.connect(self.clicked_menu)

        self.bt_info.clicked.connect(self.clicked_info)

    # 투명도 세팅
    def opacity_slider(self, val):
        self.setWindowOpacity(val/100)
        self.form_settings['opacity'] = str(val)

    # 포지션 세팅
    def set_position(self, ty, pos):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        desktop_height = QDesktopWidget().availableGeometry().height()
        desktop_width = QDesktopWidget().availableGeometry().width()
        qr.moveCenter(cp)
        result_x, result_y = '', ''

        if ty == 'length': self.setGeometry(0, 0, 80, 300)
        elif ty == 'width': self.setGeometry(0, 0, 275, 85)

        if pos == 'free': result_x, result_y = int(geometry['x']), int(geometry['y'])
        elif pos == 'center': result_x, result_y = qr.topLeft().x(), qr.topLeft().y()
        elif pos == 'top': result_x, result_y = qr.topLeft().x(), 0
        elif pos == 'bot': result_x, result_y = qr.topLeft().x(), desktop_height - self.height()
        elif pos == 'left_top': result_x, result_y = 0, 0
        elif pos == 'left_mid': result_x, result_y = 0, qr.topLeft().y()
        elif pos == 'left_bot': result_x, result_y = 0, desktop_height - self.height()
        elif pos == 'right_top': result_x, result_y = desktop_width - self.width(), 0
        elif pos == 'right_mid': result_x, result_y = desktop_width - self.width(), qr.topLeft().y()
        elif pos == 'right_bot': result_x, result_y = desktop_width - self.width(), desktop_height - self.height()

        self.move(result_x, result_y)

    # Exit 버튼
    def clicked_exit(self):
        with open('../../data/val/config.ini', 'w') as configfile:
            config.write(configfile)
        app.exit()

    # 메뉴 버튼
    def clicked_menu(self):
        return

    # 최소화 버튼
    def clicked_max_mini(self):
        self.showMinimized()
        return

    # 건축물 조회 버튼
    def clicked_info(self):
        self.qwe = InfoMain()
        self.qwe.show()

    # 메세지 함수
    def msg(self, ty, title, content):
        if ty == "basic":
            QMessageBox.about(self, title, content)
        elif ty == "info":
            QMessageBox.information(self, title, content, QMessageBox.Ok)
        elif ty == "warning":
            QMessageBox.warning(self, title, content, QMessageBox.Ok)
        elif ty == "critical":
            QMessageBox.critical(self, title, content, QMessageBox.Ok)

    # 폼 이동 이벤트
    def mousePressEvent(self, event):
        if event.btn_modify() == Qt.LeftButton:
            self.offset = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        try:
            desktop_height = QDesktopWidget().availableGeometry().height()
            desktop_width = QDesktopWidget().availableGeometry().width()

            if self.offset is not None and event.buttons() == Qt.LeftButton:
                pos = self.pos() + event.pos() - self.offset

                # 우측
                if (desktop_width - self.width() + 15) > pos.x() > (desktop_width - self.width() - 15):
                    if pos.y() < 10:
                        self.move(desktop_width - self.width(), 0)
                    elif (desktop_height - self.height() + 15) > pos.y() > (desktop_height - self.height() - 15):
                        self.move(desktop_width - self.width(), desktop_height - self.height())
                    else:
                        self.move(desktop_width - self.width(), pos.y())
                    return

                # 좌측
                if -15 < pos.x() < 15:
                    if pos.y() < 10:
                        self.move(0, 0)
                    elif (desktop_height - self.height() + 15) > pos.y() > (desktop_height - self.height() - 15):
                        self.move(0, desktop_height - self.height())
                    else:
                        self.move(0, pos.y())
                    return

                # 상단
                if (desktop_height - self.height() + 15) > pos.y() > (desktop_height - self.height() - 15):
                    self.move(pos.x(), desktop_height - self.height())
                    return

                # 하단
                if pos.y() < 15:
                    self.move(pos.x(), 0)
                    return

                self.move(pos)
            else:
                super().mouseMoveEvent(event)
        except AttributeError:
            return

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)

    # 예외 오류 처리
    def my_exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)

    sys._excepthook = sys.excepthook
    sys.excepthook = my_exception_hook


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = ReiMain()
    form.show()
    app.exec_()
