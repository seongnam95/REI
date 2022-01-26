# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_SignUp(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(341, 571)
        MainWindow.setStyleSheet(u"QMessageBox{\n"
"	background-color: white;\n"
"}\n"
"\n"
"QMessageBox QLabel{\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(44,62,80);\n"
"	padding-right: 20px;\n"
"}\n"
"\n"
"QMessageBox QPushButton {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color:  rgb(64,82,100);\n"
"	border: 1px solid rgb(64,82,100);\n"
"	min-width: 60px;\n"
"	min-height: 23px;\n"
"	background-color: rgb(236, 240, 241);l\n"
"}\n"
"\n"
"QMessageBox QPushButton::hover {\n"
"	border: 2px solid #3498db;\n"
"}\n"
"\n"
"QMessageBox QPushButton:pressed {\n"
"	background-color: rgb(216, 220, 221);l\n"
"	border: 1px solid #3498db;\n"
"}\n"
"\n"
"QListView {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lb_titlebar = QLabel(self.centralwidget)
        self.lb_titlebar.setObjectName(u"lb_titlebar")
        self.lb_titlebar.setGeometry(QRect(0, 0, 341, 571))
        self.lb_titlebar.setStyleSheet(u"QLabel{\n"
"	background-color: white;\n"
"	font: 12px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgba(0, 0, 0, 120);\n"
"	padding-top: 8px;\n"
"	padding-left: 10px;\n"
"	border: 1px solid #ecf0f1;\n"
"}")
        self.lb_titlebar.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 219, 301, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.edt_name = QLineEdit(self.centralwidget)
        self.edt_name.setObjectName(u"edt_name")
        self.edt_name.setGeometry(QRect(100, 238, 221, 30))
        self.edt_name.setStyleSheet(u"QLineEdit {\n"
"    font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	border: 1px solid #34495e;\n"
"	padding-left: 4px;\n"
"	padding-top: 3px;\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"	border: 1px solid #3498db;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid #3498db;\n"
"}")
        self.edt_name.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(10, 20, 321, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.edt_phone = QLineEdit(self.centralwidget)
        self.edt_phone.setObjectName(u"edt_phone")
        self.edt_phone.setGeometry(QRect(100, 275, 221, 30))
        self.edt_phone.setStyleSheet(u"QLineEdit {\n"
"    font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	border: 1px solid #34495e;\n"
"	padding-left: 4px;\n"
"	padding-top: 3px;\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"	border: 1px solid #3498db;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid #3498db;\n"
"}")
        self.edt_phone.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.cbx_rank = QComboBox(self.centralwidget)
        self.cbx_rank.addItem("")
        self.cbx_rank.addItem("")
        self.cbx_rank.addItem("")
        self.cbx_rank.addItem("")
        self.cbx_rank.setObjectName(u"cbx_rank")
        self.cbx_rank.setGeometry(QRect(100, 312, 221, 30))
        self.cbx_rank.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid gray;\n"
"    padding: 3px 1px 1px 10px;\n"
"    min-width: 6em;\n"
"    background: rgb(255, 255, 255);\n"
"    font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"    color: rgb(44, 62, 80);\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    padding: 3px 1px 1px 10px;\n"
"    color: rgb(127, 140, 141);\n"
"}\n"
"\n"
"QComboBox:on { \n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item { \n"
"	min-height: 30px; \n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 35px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-style: solid;\n"
"    border-left-color: darkgray;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(./data/img/down_arrow.png);\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:hover {\n"
"    image: url(./data/img/down_arrow"
                        ".png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on {\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"QComboBox::setView {\n"
"    color: rgb(44, 62, 80);\n"
"    background-color: lightblue\n"
"}\n"
"comboBox->setView(view);\n"
"QListView::item:selected {\n"
"    color: rgb(44, 62, 80);\n"
"    background-color: lightblue\n"
"}\n"
"")
        self.edt_company_number = QLineEdit(self.centralwidget)
        self.edt_company_number.setObjectName(u"edt_company_number")
        self.edt_company_number.setGeometry(QRect(100, 188, 221, 30))
        self.edt_company_number.setStyleSheet(u"QLineEdit {\n"
"    font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	border: 1px solid #34495e;\n"
"	padding-left: 4px;\n"
"	padding-top: 3px;\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"	border: 1px solid #3498db;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid #3498db;\n"
"}")
        self.edt_company_number.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.edt_company_number.setReadOnly(True)
        self.edt_company_call = QLineEdit(self.centralwidget)
        self.edt_company_call.setObjectName(u"edt_company_call")
        self.edt_company_call.setGeometry(QRect(190, 151, 131, 30))
        self.edt_company_call.setStyleSheet(u"QLineEdit {\n"
"    font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	border: 1px solid #34495e;\n"
"	padding-left: 4px;\n"
"	padding-top: 3px;\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"	border: 1px solid #3498db;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid #3498db;\n"
"}")
        self.edt_company_call.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.edt_address = QLineEdit(self.centralwidget)
        self.edt_address.setObjectName(u"edt_address")
        self.edt_address.setEnabled(True)
        self.edt_address.setGeometry(QRect(100, 40, 221, 30))
        self.edt_address.setStyleSheet(u"QLineEdit {\n"
"    font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	border: 1px solid #34495e;\n"
"	padding-left: 4px;\n"
"	padding-top: 3px;\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"	border: 1px solid #3498db;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid #3498db;\n"
"}")
        self.edt_address.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.edt_address.setReadOnly(True)
        self.edt_company = QLineEdit(self.centralwidget)
        self.edt_company.setObjectName(u"edt_company")
        self.edt_company.setGeometry(QRect(100, 77, 221, 30))
        self.edt_company.setStyleSheet(u"QLineEdit {\n"
"    font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	border: 1px solid #34495e;\n"
"	padding-left: 4px;\n"
"	padding-top: 3px;\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"	border: 1px solid #3498db;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid #3498db;\n"
"}")
        self.edt_company.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.edt_company.setReadOnly(True)
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(20, 343, 301, 20))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 50, 56, 16))
        font = QFont()
        font.setFamilies([u"\uc6f0\ucef4\uccb4 Regular"])
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: #2c3e50;\n"
"}")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 87, 56, 16))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: #2c3e50;\n"
"}")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 124, 56, 16))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: #2c3e50;\n"
"}")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 161, 56, 16))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: #2c3e50;\n"
"}")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 198, 56, 16))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: #2c3e50;\n"
"}")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 248, 56, 16))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: #2c3e50;\n"
"}")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 285, 56, 16))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: #2c3e50;\n"
"}")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 321, 56, 16))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: #2c3e50;\n"
"}")
        self.btn_register = QPushButton(self.centralwidget)
        self.btn_register.setObjectName(u"btn_register")
        self.btn_register.setGeometry(QRect(20, 510, 301, 41))
        self.btn_register.setStyleSheet(u"QPushButton {\n"
"	font: 18px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: white;\n"
"	border: 0px;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(44,62,80);\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 0px;\n"
"	background-color: rgb(64,82,100);\n"
"	border-style: inset;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 0px;\n"
"	background-color: rgb(24,42,60);\n"
"	border-style: inset;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"E:/PyProject/Project/REI/building_info/image/bt_search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_register.setIcon(icon)
        self.btn_register.setIconSize(QSize(23, 23))
        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(10, 490, 321, 3))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 372, 56, 16))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: #2c3e50;\n"
"}")
        self.edt_id = QLineEdit(self.centralwidget)
        self.edt_id.setObjectName(u"edt_id")
        self.edt_id.setGeometry(QRect(100, 363, 131, 30))
        self.edt_id.setStyleSheet(u"QLineEdit {\n"
"    font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	border: 1px solid #34495e;\n"
"	padding-left: 4px;\n"
"	padding-top: 3px;\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"	border: 1px solid #3498db;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid #3498db;\n"
"}")
        self.edt_id.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 409, 56, 16))
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: #2c3e50;\n"
"}")
        self.edt_pw = QLineEdit(self.centralwidget)
        self.edt_pw.setObjectName(u"edt_pw")
        self.edt_pw.setGeometry(QRect(100, 400, 221, 30))
        self.edt_pw.setStyleSheet(u"QLineEdit {\n"
"    font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	border: 1px solid #34495e;\n"
"	padding-left: 4px;\n"
"	padding-top: 3px;\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"	border: 1px solid #3498db;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid #3498db;\n"
"}")
        self.edt_pw.setEchoMode(QLineEdit.Password)
        self.edt_pw.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.edt_pwre = QLineEdit(self.centralwidget)
        self.edt_pwre.setObjectName(u"edt_pwre")
        self.edt_pwre.setGeometry(QRect(100, 437, 221, 30))
        self.edt_pwre.setStyleSheet(u"QLineEdit {\n"
"    font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	border: 1px solid #34495e;\n"
"	padding-left: 4px;\n"
"	padding-top: 3px;\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"	border: 1px solid #3498db;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid #3498db;\n"
"}")
        self.edt_pwre.setEchoMode(QLineEdit.Password)
        self.edt_pwre.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 447, 75, 16))
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: #2c3e50;\n"
"}")
        self.cbx_company_call = QComboBox(self.centralwidget)
        self.cbx_company_call.addItem("")
        self.cbx_company_call.addItem("")
        self.cbx_company_call.addItem("")
        self.cbx_company_call.addItem("")
        self.cbx_company_call.addItem("")
        self.cbx_company_call.addItem("")
        self.cbx_company_call.addItem("")
        self.cbx_company_call.addItem("")
        self.cbx_company_call.addItem("")
        self.cbx_company_call.addItem("")
        self.cbx_company_call.addItem("")
        self.cbx_company_call.addItem("")
        self.cbx_company_call.addItem("")
        self.cbx_company_call.addItem("")
        self.cbx_company_call.addItem("")
        self.cbx_company_call.addItem("")
        self.cbx_company_call.addItem("")
        self.cbx_company_call.addItem("")
        self.cbx_company_call.setObjectName(u"cbx_company_call")
        self.cbx_company_call.setGeometry(QRect(100, 151, 81, 30))
        self.cbx_company_call.setMinimumSize(QSize(45, 0))
        self.cbx_company_call.setMaximumSize(QSize(100, 16777215))
        self.cbx_company_call.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid gray;\n"
"    padding: 3px 1px 1px 10px;\n"
"    min-width: 2em;\n"
"    background: rgb(255, 255, 255);\n"
"    font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"    color: rgb(44, 62, 80);\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    padding: 3px 1px 1px 10px;\n"
"    color: rgb(127, 140, 141);\n"
"}\n"
"\n"
"QComboBox:on { \n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item { \n"
"	min-height: 30px; \n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-style: solid;\n"
"    border-left-color: darkgray;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(./data/img/down_arrow.png);\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:hover {\n"
"    image: url(./data/img/down_arrow"
                        ".png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on {\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"QComboBox::setView {\n"
"    color: rgb(44, 62, 80);\n"
"    background-color: lightblue\n"
"}\n"
"comboBox->setView(view);\n"
"QListView::item:selected {\n"
"    color: rgb(44, 62, 80);\n"
"    background-color: lightblue\n"
"}\n"
"")
        self.cbx_company_call.setIconSize(QSize(0, 0))
        self.btn_id_check = QPushButton(self.centralwidget)
        self.btn_id_check.setObjectName(u"btn_id_check")
        self.btn_id_check.setGeometry(QRect(240, 363, 81, 30))
        self.btn_id_check.setStyleSheet(u"QPushButton {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: white;\n"
"	border: 0px;\n"
"	padding-top: 2px;\n"
"	background-color: rgb(44,62,80);\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 0px;\n"
"	background-color: rgb(64,82,100);\n"
"	border-style: inset;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 0px;\n"
"	background-color: rgb(24,42,60);\n"
"	border-style: inset;\n"
"}\n"
"")
        self.btn_id_check.setIcon(icon)
        self.btn_id_check.setIconSize(QSize(23, 23))
        self.btn_eye_re = QPushButton(self.centralwidget)
        self.btn_eye_re.setObjectName(u"btn_eye_re")
        self.btn_eye_re.setGeometry(QRect(294, 440, 24, 24))
        self.btn_eye_re.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0,0,0,0);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: rgb(0,0,0,0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0,0,0,0);\n"
"}\n"
"")
        self.btn_eye = QPushButton(self.centralwidget)
        self.btn_eye.setObjectName(u"btn_eye")
        self.btn_eye.setGeometry(QRect(294, 403, 24, 24))
        self.btn_eye.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0,0,0,0);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: rgb(0,0,0,0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0,0,0,0);\n"
"}\n"
"")
        self.lb_pwcheck = QLabel(self.centralwidget)
        self.lb_pwcheck.setObjectName(u"lb_pwcheck")
        self.lb_pwcheck.setEnabled(True)
        self.lb_pwcheck.setGeometry(QRect(99, 468, 131, 20))
        self.lb_pwcheck.setFont(font)
        self.lb_pwcheck.setStyleSheet(u"QLabel {\n"
"	font: 11px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"}")
        self.lb_pwcheck.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.edt_boss_name = QLineEdit(self.centralwidget)
        self.edt_boss_name.setObjectName(u"edt_boss_name")
        self.edt_boss_name.setGeometry(QRect(100, 114, 221, 30))
        self.edt_boss_name.setStyleSheet(u"QLineEdit {\n"
"    font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	border: 1px solid #34495e;\n"
"	padding-left: 4px;\n"
"	padding-top: 3px;\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"	border: 1px solid #3498db;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid #3498db;\n"
"}")
        self.edt_boss_name.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.edt_boss_name.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.edt_address, self.edt_company)
        QWidget.setTabOrder(self.edt_company, self.edt_boss_name)
        QWidget.setTabOrder(self.edt_boss_name, self.cbx_company_call)
        QWidget.setTabOrder(self.cbx_company_call, self.edt_company_call)
        QWidget.setTabOrder(self.edt_company_call, self.edt_company_number)
        QWidget.setTabOrder(self.edt_company_number, self.edt_name)
        QWidget.setTabOrder(self.edt_name, self.edt_phone)
        QWidget.setTabOrder(self.edt_phone, self.cbx_rank)
        QWidget.setTabOrder(self.cbx_rank, self.edt_id)
        QWidget.setTabOrder(self.edt_id, self.btn_id_check)
        QWidget.setTabOrder(self.btn_id_check, self.edt_pw)
        QWidget.setTabOrder(self.edt_pw, self.edt_pwre)
        QWidget.setTabOrder(self.edt_pwre, self.btn_register)
        QWidget.setTabOrder(self.btn_register, self.btn_eye)
        QWidget.setTabOrder(self.btn_eye, self.btn_eye_re)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lb_titlebar.setText(QCoreApplication.translate("MainWindow", u"SIGN-UP (\ud68c\uc6d0\uac00\uc785)", None))
        self.edt_phone.setText("")
        self.cbx_rank.setItemText(0, QCoreApplication.translate("MainWindow", u"(\uc120\ud0dd)", None))
        self.cbx_rank.setItemText(1, QCoreApplication.translate("MainWindow", u"\ub300\ud45c \uacf5\uc778\uc911\uac1c\uc0ac", None))
        self.cbx_rank.setItemText(2, QCoreApplication.translate("MainWindow", u"\uc18c\uc18d \uacf5\uc778\uc911\uac1c\uc0ac", None))
        self.cbx_rank.setItemText(3, QCoreApplication.translate("MainWindow", u"\uc911\uac1c\ubcf4\uc870\uc6d0", None))

        self.edt_address.setText("")
        self.edt_company.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\uc8fc \u3000 \uc18c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\uc0c1 \ud638 \uba85", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\ub300 \ud45c \uc790 \uba85", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\ub300 \ud45c \ubc88 \ud638", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\ub4f1 \ub85d \ubc88 \ud638", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\uc131 \u3000 \uba85", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\uc5f0 \ub77d \ucc98", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\uc9c1 \u3000 \uae09", None))
        self.btn_register.setText(QCoreApplication.translate("MainWindow", u"\ud68c \uc6d0 \uac00 \uc785", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\uc544 \uc774 \ub514", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\ube44 \ubc00 \ubc88 \ud638", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\uc7ac \ud655 \uc778", None))
        self.cbx_company_call.setItemText(0, QCoreApplication.translate("MainWindow", u"(\uc120\ud0dd)", None))
        self.cbx_company_call.setItemText(1, QCoreApplication.translate("MainWindow", u"02", None))
        self.cbx_company_call.setItemText(2, QCoreApplication.translate("MainWindow", u"031", None))
        self.cbx_company_call.setItemText(3, QCoreApplication.translate("MainWindow", u"032", None))
        self.cbx_company_call.setItemText(4, QCoreApplication.translate("MainWindow", u"033", None))
        self.cbx_company_call.setItemText(5, QCoreApplication.translate("MainWindow", u"041", None))
        self.cbx_company_call.setItemText(6, QCoreApplication.translate("MainWindow", u"042", None))
        self.cbx_company_call.setItemText(7, QCoreApplication.translate("MainWindow", u"043", None))
        self.cbx_company_call.setItemText(8, QCoreApplication.translate("MainWindow", u"044", None))
        self.cbx_company_call.setItemText(9, QCoreApplication.translate("MainWindow", u"051", None))
        self.cbx_company_call.setItemText(10, QCoreApplication.translate("MainWindow", u"052", None))
        self.cbx_company_call.setItemText(11, QCoreApplication.translate("MainWindow", u"053", None))
        self.cbx_company_call.setItemText(12, QCoreApplication.translate("MainWindow", u"054", None))
        self.cbx_company_call.setItemText(13, QCoreApplication.translate("MainWindow", u"055", None))
        self.cbx_company_call.setItemText(14, QCoreApplication.translate("MainWindow", u"061", None))
        self.cbx_company_call.setItemText(15, QCoreApplication.translate("MainWindow", u"062", None))
        self.cbx_company_call.setItemText(16, QCoreApplication.translate("MainWindow", u"063", None))
        self.cbx_company_call.setItemText(17, QCoreApplication.translate("MainWindow", u"064", None))

        self.btn_id_check.setText(QCoreApplication.translate("MainWindow", u"\uc911\ubcf5\ud655\uc778", None))
        self.btn_eye_re.setText("")
        self.btn_eye.setText("")
        self.lb_pwcheck.setText("")
    # retranslateUi

