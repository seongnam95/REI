# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_bld.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QStackedWidget, QWidget)

class Ui_AddRoom(object):
    def setupUi(self, AddRoom):
        if not AddRoom.objectName():
            AddRoom.setObjectName(u"AddRoom")
        AddRoom.resize(1039, 686)
        AddRoom.setStyleSheet(u"#AddRoom {\n"
"	background: white;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 2px solid rgb(235,235,235);\n"
"    padding-top: 4px;\n"
"    padding-left: 10px;\n"
"    min-width: 3em;\n"
"    background: rgb(255, 255, 255);\n"
"    font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"    color: rgb(65, 65, 65);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView { \n"
"    border: 1px solid lightgray;\n"
"    outline: none;\n"
"    padding: 5px;\n"
"}      \n"
"\n"
"QComboBox QAbstractItemView::item { \n"
"    color: rgb(65, 65, 65);\n"
"    border-radius: 5px;\n"
"    padding-left: 10px;\n"
"    padding-top: 3px;\n"
"    min-height: 30px; \n"
"}    \n"
"\n"
"QComboBox QAbstractItemView::item:hover { \n"
"    selection-color: white;\n"
"    background-color: rgb(128,128,255);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    width: 20px;\n"
"\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(../../data/img/system/do"
                        "wn_arrow_icon.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    width: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"    background: rgb(235,235,235);\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QLabel {\n"
"	font: 15px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color:  rgb(65,65,65);\n"
"	padding-top: 2px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	font: 13;\n"
"	color:  rgb(85,85,85);\n"
"	border: 1px solid rgb(130,130,130);\n"
"	border-radius: 2px;\n"
"	padding-left: 5px;\n"
"	padding-top: 2px;\n"
"	padding-right: 22px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	color:  rgb(65,65,65);\n"
"	border: 1px solid rgb(148,148,255);\n"
"	border-radius: 2px;\n"
"	padding-right: 21px;\n"
"}\n"
"\n"
"QLineEdit:disabled{\n"
"	background: rgb(250,250,250);\n"
"}\n"
"\n"
"QCheckBox {\n"
"	font: 15px  \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(123,123,123);\n"
""
                        "}\n"
"\n"
"QCheckBox:checked {\n"
"	color: rgb(88,88,255);\n"
"}\n"
"\n"
"QRadioButton {\n"
"	font: 14px  \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(123,123,123);\n"
"}\n"
"\n"
"QRadioButton:checked {\n"
"	color: rgb(88,88,255);\n"
"}")
        self.centralwidget = QWidget(AddRoom)
        self.centralwidget.setObjectName(u"centralwidget")
        self.address_frame = QFrame(self.centralwidget)
        self.address_frame.setObjectName(u"address_frame")
        self.address_frame.setGeometry(QRect(20, 20, 601, 131))
        self.address_frame.setStyleSheet(u"#address_frame{\n"
"	background: white;\n"
"	border-radius: 15px;\n"
"}")
        self.address_frame.setFrameShape(QFrame.StyledPanel)
        self.address_frame.setFrameShadow(QFrame.Raised)
        self.edt_address = QLineEdit(self.address_frame)
        self.edt_address.setObjectName(u"edt_address")
        self.edt_address.setGeometry(QRect(30, 20, 541, 45))
        self.edt_address.setStyleSheet(u"QLineEdit {\n"
"    color: rgb(125,125,125);\n"
"    font: 16px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"    border: 2px solid rgb(128,128,255);\n"
"    border-radius: 5px;\n"
"    padding-top: 3px;\n"
"    padding-left: 10px;\n"
"    padding-right: 40px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    color: rgb(65,65,65);\n"
"}")
        self.name_type = QLabel(self.address_frame)
        self.name_type.setObjectName(u"name_type")
        self.name_type.setGeometry(QRect(30, 80, 61, 30))
        self.cbx_type = QComboBox(self.address_frame)
        self.cbx_type.addItem("")
        self.cbx_type.addItem("")
        self.cbx_type.addItem("")
        self.cbx_type.setObjectName(u"cbx_type")
        self.cbx_type.setGeometry(QRect(110, 80, 81, 30))
        self.name_kind = QLabel(self.address_frame)
        self.name_kind.setObjectName(u"name_kind")
        self.name_kind.setGeometry(QRect(230, 80, 61, 30))
        self.cbx_kind_1 = QComboBox(self.address_frame)
        self.cbx_kind_1.addItem("")
        self.cbx_kind_1.addItem("")
        self.cbx_kind_1.addItem("")
        self.cbx_kind_1.addItem("")
        self.cbx_kind_1.addItem("")
        self.cbx_kind_1.addItem("")
        self.cbx_kind_1.addItem("")
        self.cbx_kind_1.addItem("")
        self.cbx_kind_1.addItem("")
        self.cbx_kind_1.addItem("")
        self.cbx_kind_1.addItem("")
        self.cbx_kind_1.setObjectName(u"cbx_kind_1")
        self.cbx_kind_1.setGeometry(QRect(310, 80, 101, 30))
        self.cbx_kind_2 = QComboBox(self.address_frame)
        self.cbx_kind_2.setObjectName(u"cbx_kind_2")
        self.cbx_kind_2.setGeometry(QRect(420, 80, 151, 30))
        self.btn_next = QPushButton(self.centralwidget)
        self.btn_next.setObjectName(u"btn_next")
        self.btn_next.setGeometry(QRect(500, 530, 111, 41))
        self.btn_next.setStyleSheet(u"QPushButton {\n"
"    font: 18px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"    color: white;\n"
"    border: none;\n"
"    padding-top: 3px;\n"
"    padding-left: 2px;\n"
"    background: rgb(128,128,255);\n"
"    border-radius: 3px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(148,148,255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    padding-left: 4px;\n"
"    padding-top: 5px;\n"
"    background-color: rgb(108,108,235);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(166, 168, 171);\n"
"}")
        self.page_frame = QFrame(self.centralwidget)
        self.page_frame.setObjectName(u"page_frame")
        self.page_frame.setGeometry(QRect(30, 542, 101, 25))
        self.page_frame.setStyleSheet(u"QPushButton {\n"
"    font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"    color: rgb(105,105,105);\n"
"    border: 1px solid rgb(145,145,145);\n"
"    border-radius: 2px;\n"
"    outline: none;\n"
"    padding-top: 3px;\n"
"    padding-left: 2px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	color: white;\n"
"    border: 1px solid rgb(128,128,235);\n"
"    background-color: rgb(128,128,235);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(166, 168, 171);\n"
"}")
        self.page_frame.setFrameShape(QFrame.StyledPanel)
        self.page_frame.setFrameShadow(QFrame.Raised)
        self.btn_page_1 = QPushButton(self.page_frame)
        self.btn_page_1.setObjectName(u"btn_page_1")
        self.btn_page_1.setGeometry(QRect(0, 0, 25, 25))
        self.btn_page_1.setStyleSheet(u"")
        self.btn_page_1.setCheckable(True)
        self.btn_page_1.setChecked(True)
        self.btn_page_2 = QPushButton(self.page_frame)
        self.btn_page_2.setObjectName(u"btn_page_2")
        self.btn_page_2.setGeometry(QRect(35, 0, 25, 25))
        self.btn_page_2.setStyleSheet(u"")
        self.btn_page_2.setCheckable(True)
        self.btn_page_3 = QPushButton(self.page_frame)
        self.btn_page_3.setObjectName(u"btn_page_3")
        self.btn_page_3.setGeometry(QRect(70, 0, 25, 25))
        self.btn_page_3.setStyleSheet(u"")
        self.btn_page_3.setCheckable(True)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 160, 631, 341))
        self.stackedWidget.setStyleSheet(u"#money_frame{\n"
"	background: white;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"#info_frame{\n"
"	background: white;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"#building_frame{\n"
"	background: white;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"#building_frame_2{\n"
"	background: white;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"#day_frame{\n"
"	background: white;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"#owner_frame{\n"
"	background: white;\n"
"	border-radius: 15px;\n"
"}")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.money_frame = QFrame(self.page_1)
        self.money_frame.setObjectName(u"money_frame")
        self.money_frame.setGeometry(QRect(10, 10, 601, 151))
        self.money_frame.setFrameShape(QFrame.StyledPanel)
        self.money_frame.setFrameShadow(QFrame.Raised)
        self.f_deposit = QFrame(self.money_frame)
        self.f_deposit.setObjectName(u"f_deposit")
        self.f_deposit.setGeometry(QRect(330, 20, 241, 31))
        self.f_deposit.setFrameShape(QFrame.StyledPanel)
        self.f_deposit.setFrameShadow(QFrame.Raised)
        self.name_deposit = QLabel(self.f_deposit)
        self.name_deposit.setObjectName(u"name_deposit")
        self.name_deposit.setGeometry(QRect(0, 0, 61, 30))
        self.hint_deposit_1 = QLabel(self.f_deposit)
        self.hint_deposit_1.setObjectName(u"hint_deposit_1")
        self.hint_deposit_1.setGeometry(QRect(145, 0, 21, 30))
        self.hint_deposit_1.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.edt_deposit_1 = QLineEdit(self.f_deposit)
        self.edt_deposit_1.setObjectName(u"edt_deposit_1")
        self.edt_deposit_1.setGeometry(QRect(90, 0, 76, 30))
        self.edt_deposit_1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.hint_deposit_2 = QLabel(self.f_deposit)
        self.hint_deposit_2.setObjectName(u"hint_deposit_2")
        self.hint_deposit_2.setGeometry(QRect(220, 0, 31, 30))
        self.hint_deposit_2.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.edt_deposit_2 = QLineEdit(self.f_deposit)
        self.edt_deposit_2.setObjectName(u"edt_deposit_2")
        self.edt_deposit_2.setGeometry(QRect(171, 0, 70, 30))
        self.edt_deposit_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.edt_deposit_1.raise_()
        self.name_deposit.raise_()
        self.hint_deposit_1.raise_()
        self.edt_deposit_2.raise_()
        self.hint_deposit_2.raise_()
        self.f_loan = QFrame(self.money_frame)
        self.f_loan.setObjectName(u"f_loan")
        self.f_loan.setGeometry(QRect(330, 60, 241, 31))
        self.f_loan.setFrameShape(QFrame.StyledPanel)
        self.f_loan.setFrameShadow(QFrame.Raised)
        self.name_loan = QLabel(self.f_loan)
        self.name_loan.setObjectName(u"name_loan")
        self.name_loan.setGeometry(QRect(0, 0, 61, 30))
        self.edt_loan = QLineEdit(self.f_loan)
        self.edt_loan.setObjectName(u"edt_loan")
        self.edt_loan.setGeometry(QRect(90, 0, 151, 30))
        self.edt_loan.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.hint_loan = QLabel(self.f_loan)
        self.hint_loan.setObjectName(u"hint_loan")
        self.hint_loan.setGeometry(QRect(208, 0, 31, 30))
        self.hint_loan.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.f_cost_in = QFrame(self.money_frame)
        self.f_cost_in.setObjectName(u"f_cost_in")
        self.f_cost_in.setGeometry(QRect(30, 105, 541, 31))
        self.f_cost_in.setFrameShape(QFrame.StyledPanel)
        self.f_cost_in.setFrameShadow(QFrame.Raised)
        self.name_cost_in = QLabel(self.f_cost_in)
        self.name_cost_in.setObjectName(u"name_cost_in")
        self.name_cost_in.setGeometry(QRect(0, 0, 101, 30))
        self.ckb_cost_in_5 = QCheckBox(self.f_cost_in)
        self.ckb_cost_in_5.setObjectName(u"ckb_cost_in_5")
        self.ckb_cost_in_5.setGeometry(QRect(480, 0, 41, 30))
        self.ckb_cost_in_1 = QCheckBox(self.f_cost_in)
        self.ckb_cost_in_1.setObjectName(u"ckb_cost_in_1")
        self.ckb_cost_in_1.setGeometry(QRect(140, 0, 61, 30))
        self.ckb_cost_in_2 = QCheckBox(self.f_cost_in)
        self.ckb_cost_in_2.setObjectName(u"ckb_cost_in_2")
        self.ckb_cost_in_2.setGeometry(QRect(230, 0, 61, 30))
        self.ckb_cost_in_3 = QCheckBox(self.f_cost_in)
        self.ckb_cost_in_3.setObjectName(u"ckb_cost_in_3")
        self.ckb_cost_in_3.setGeometry(QRect(310, 0, 61, 30))
        self.ckb_cost_in_4 = QCheckBox(self.f_cost_in)
        self.ckb_cost_in_4.setObjectName(u"ckb_cost_in_4")
        self.ckb_cost_in_4.setGeometry(QRect(390, 0, 61, 30))
        self.f_admin_cost = QFrame(self.money_frame)
        self.f_admin_cost.setObjectName(u"f_admin_cost")
        self.f_admin_cost.setGeometry(QRect(30, 60, 241, 31))
        self.f_admin_cost.setFrameShape(QFrame.StyledPanel)
        self.f_admin_cost.setFrameShadow(QFrame.Raised)
        self.hint_admin_cost = QLabel(self.f_admin_cost)
        self.hint_admin_cost.setObjectName(u"hint_admin_cost")
        self.hint_admin_cost.setGeometry(QRect(220, 0, 21, 30))
        self.hint_admin_cost.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.name_admin_cost = QLabel(self.f_admin_cost)
        self.name_admin_cost.setObjectName(u"name_admin_cost")
        self.name_admin_cost.setGeometry(QRect(0, 0, 61, 30))
        self.edt_admin_cost = QLineEdit(self.f_admin_cost)
        self.edt_admin_cost.setObjectName(u"edt_admin_cost")
        self.edt_admin_cost.setGeometry(QRect(90, 0, 151, 30))
        self.edt_admin_cost.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.edt_admin_cost.raise_()
        self.hint_admin_cost.raise_()
        self.name_admin_cost.raise_()
        self.f_price = QFrame(self.money_frame)
        self.f_price.setObjectName(u"f_price")
        self.f_price.setGeometry(QRect(30, 20, 241, 31))
        self.f_price.setFrameShape(QFrame.StyledPanel)
        self.f_price.setFrameShadow(QFrame.Raised)
        self.hint_price = QLabel(self.f_price)
        self.hint_price.setObjectName(u"hint_price")
        self.hint_price.setGeometry(QRect(208, 0, 31, 30))
        self.hint_price.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.name_price = QLabel(self.f_price)
        self.name_price.setObjectName(u"name_price")
        self.name_price.setGeometry(QRect(0, 0, 61, 30))
        self.edt_price = QLineEdit(self.f_price)
        self.edt_price.setObjectName(u"edt_price")
        self.edt_price.setGeometry(QRect(90, 0, 151, 30))
        self.edt_price.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.edt_price.raise_()
        self.hint_price.raise_()
        self.name_price.raise_()
        self.f_rent = QFrame(self.money_frame)
        self.f_rent.setObjectName(u"f_rent")
        self.f_rent.setGeometry(QRect(610, 120, 241, 31))
        self.f_rent.setFrameShape(QFrame.StyledPanel)
        self.f_rent.setFrameShadow(QFrame.Raised)
        self.name_rent = QLabel(self.f_rent)
        self.name_rent.setObjectName(u"name_rent")
        self.name_rent.setGeometry(QRect(0, 0, 61, 30))
        self.edt_rent = QLineEdit(self.f_rent)
        self.edt_rent.setObjectName(u"edt_rent")
        self.edt_rent.setGeometry(QRect(90, 0, 151, 30))
        self.edt_rent.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.hint_rent = QLabel(self.f_rent)
        self.hint_rent.setObjectName(u"hint_rent")
        self.hint_rent.setGeometry(QRect(208, 0, 31, 30))
        self.hint_rent.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.f_facility = QFrame(self.money_frame)
        self.f_facility.setObjectName(u"f_facility")
        self.f_facility.setGeometry(QRect(610, 0, 241, 31))
        self.f_facility.setFrameShape(QFrame.StyledPanel)
        self.f_facility.setFrameShadow(QFrame.Raised)
        self.name_facility = QLabel(self.f_facility)
        self.name_facility.setObjectName(u"name_facility")
        self.name_facility.setGeometry(QRect(0, 0, 61, 30))
        self.edt_facility = QLineEdit(self.f_facility)
        self.edt_facility.setObjectName(u"edt_facility")
        self.edt_facility.setGeometry(QRect(90, 0, 151, 30))
        self.edt_facility.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.hint_facility = QLabel(self.f_facility)
        self.hint_facility.setObjectName(u"hint_facility")
        self.hint_facility.setGeometry(QRect(208, 0, 31, 30))
        self.hint_facility.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.f_premium = QFrame(self.money_frame)
        self.f_premium.setObjectName(u"f_premium")
        self.f_premium.setGeometry(QRect(610, 80, 241, 31))
        self.f_premium.setFrameShape(QFrame.StyledPanel)
        self.f_premium.setFrameShadow(QFrame.Raised)
        self.name_premium = QLabel(self.f_premium)
        self.name_premium.setObjectName(u"name_premium")
        self.name_premium.setGeometry(QRect(0, 0, 61, 30))
        self.edt_premium = QLineEdit(self.f_premium)
        self.edt_premium.setObjectName(u"edt_premium")
        self.edt_premium.setGeometry(QRect(90, 0, 151, 30))
        self.edt_premium.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.hint_premium = QLabel(self.f_premium)
        self.hint_premium.setObjectName(u"hint_premium")
        self.hint_premium.setGeometry(QRect(208, 0, 31, 30))
        self.hint_premium.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.f_parcel = QFrame(self.money_frame)
        self.f_parcel.setObjectName(u"f_parcel")
        self.f_parcel.setGeometry(QRect(610, 40, 241, 31))
        self.f_parcel.setFrameShape(QFrame.StyledPanel)
        self.f_parcel.setFrameShadow(QFrame.Raised)
        self.name_parcel = QLabel(self.f_parcel)
        self.name_parcel.setObjectName(u"name_parcel")
        self.name_parcel.setGeometry(QRect(0, 0, 61, 30))
        self.edt_parcel = QLineEdit(self.f_parcel)
        self.edt_parcel.setObjectName(u"edt_parcel")
        self.edt_parcel.setGeometry(QRect(90, 0, 151, 30))
        self.edt_parcel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.hint_parcel = QLabel(self.f_parcel)
        self.hint_parcel.setObjectName(u"hint_parcel")
        self.hint_parcel.setGeometry(QRect(208, 0, 31, 30))
        self.hint_parcel.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.f_middle_pay = QFrame(self.money_frame)
        self.f_middle_pay.setObjectName(u"f_middle_pay")
        self.f_middle_pay.setGeometry(QRect(610, 160, 241, 31))
        self.f_middle_pay.setFrameShape(QFrame.StyledPanel)
        self.f_middle_pay.setFrameShadow(QFrame.Raised)
        self.name_middle_pay = QLabel(self.f_middle_pay)
        self.name_middle_pay.setObjectName(u"name_middle_pay")
        self.name_middle_pay.setGeometry(QRect(0, 0, 71, 30))
        self.edt_middle_pay = QLineEdit(self.f_middle_pay)
        self.edt_middle_pay.setObjectName(u"edt_middle_pay")
        self.edt_middle_pay.setGeometry(QRect(90, 0, 151, 30))
        self.edt_middle_pay.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.hint_middle_pay = QLabel(self.f_middle_pay)
        self.hint_middle_pay.setObjectName(u"hint_middle_pay")
        self.hint_middle_pay.setGeometry(QRect(208, 0, 31, 30))
        self.hint_middle_pay.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.info_frame = QFrame(self.page_1)
        self.info_frame.setObjectName(u"info_frame")
        self.info_frame.setGeometry(QRect(10, 180, 601, 151))
        self.info_frame.setFrameShape(QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.f_room = QFrame(self.info_frame)
        self.f_room.setObjectName(u"f_room")
        self.f_room.setGeometry(QRect(30, 20, 241, 31))
        self.f_room.setFrameShape(QFrame.StyledPanel)
        self.f_room.setFrameShadow(QFrame.Raised)
        self.hint_room_num = QLabel(self.f_room)
        self.hint_room_num.setObjectName(u"hint_room_num")
        self.hint_room_num.setGeometry(QRect(220, 0, 21, 30))
        self.hint_room_num.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.edt_room_num = QLineEdit(self.f_room)
        self.edt_room_num.setObjectName(u"edt_room_num")
        self.edt_room_num.setGeometry(QRect(90, 0, 151, 30))
        self.edt_room_num.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.name_room_num = QLabel(self.f_room)
        self.name_room_num.setObjectName(u"name_room_num")
        self.name_room_num.setGeometry(QRect(0, 0, 61, 30))
        self.edt_room_num.raise_()
        self.hint_room_num.raise_()
        self.name_room_num.raise_()
        self.f_bathroom = QFrame(self.info_frame)
        self.f_bathroom.setObjectName(u"f_bathroom")
        self.f_bathroom.setGeometry(QRect(330, 20, 241, 31))
        self.f_bathroom.setFrameShape(QFrame.StyledPanel)
        self.f_bathroom.setFrameShadow(QFrame.Raised)
        self.hint_bathroom = QLabel(self.f_bathroom)
        self.hint_bathroom.setObjectName(u"hint_bathroom")
        self.hint_bathroom.setGeometry(QRect(220, 0, 21, 30))
        self.hint_bathroom.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.name_bathroom = QLabel(self.f_bathroom)
        self.name_bathroom.setObjectName(u"name_bathroom")
        self.name_bathroom.setGeometry(QRect(0, 0, 61, 30))
        self.edt_bathroom = QLineEdit(self.f_bathroom)
        self.edt_bathroom.setObjectName(u"edt_bathroom")
        self.edt_bathroom.setGeometry(QRect(90, 0, 151, 30))
        self.edt_bathroom.setEchoMode(QLineEdit.Normal)
        self.edt_bathroom.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.edt_bathroom.raise_()
        self.hint_bathroom.raise_()
        self.name_bathroom.raise_()
        self.f_direction = QFrame(self.info_frame)
        self.f_direction.setObjectName(u"f_direction")
        self.f_direction.setGeometry(QRect(330, 60, 241, 31))
        self.f_direction.setFrameShape(QFrame.StyledPanel)
        self.f_direction.setFrameShadow(QFrame.Raised)
        self.cbx_direction_2 = QComboBox(self.f_direction)
        self.cbx_direction_2.addItem("")
        self.cbx_direction_2.addItem("")
        self.cbx_direction_2.addItem("")
        self.cbx_direction_2.addItem("")
        self.cbx_direction_2.addItem("")
        self.cbx_direction_2.addItem("")
        self.cbx_direction_2.addItem("")
        self.cbx_direction_2.addItem("")
        self.cbx_direction_2.setObjectName(u"cbx_direction_2")
        self.cbx_direction_2.setGeometry(QRect(160, 0, 81, 30))
        self.cbx_direction_1 = QComboBox(self.f_direction)
        self.cbx_direction_1.addItem("")
        self.cbx_direction_1.addItem("")
        self.cbx_direction_1.setObjectName(u"cbx_direction_1")
        self.cbx_direction_1.setGeometry(QRect(90, 0, 62, 30))
        self.name_direction = QLabel(self.f_direction)
        self.name_direction.setObjectName(u"name_direction")
        self.name_direction.setGeometry(QRect(0, 0, 61, 30))
        self.f_heating = QFrame(self.info_frame)
        self.f_heating.setObjectName(u"f_heating")
        self.f_heating.setGeometry(QRect(30, 60, 241, 31))
        self.f_heating.setFrameShape(QFrame.StyledPanel)
        self.f_heating.setFrameShadow(QFrame.Raised)
        self.cbx_heating = QComboBox(self.f_heating)
        self.cbx_heating.addItem("")
        self.cbx_heating.addItem("")
        self.cbx_heating.addItem("")
        self.cbx_heating.setObjectName(u"cbx_heating")
        self.cbx_heating.setGeometry(QRect(90, 0, 151, 30))
        self.name_heating = QLabel(self.f_heating)
        self.name_heating.setObjectName(u"name_heating")
        self.name_heating.setGeometry(QRect(0, 0, 61, 30))
        self.f_fuel = QFrame(self.info_frame)
        self.f_fuel.setObjectName(u"f_fuel")
        self.f_fuel.setGeometry(QRect(30, 100, 241, 31))
        self.f_fuel.setFrameShape(QFrame.StyledPanel)
        self.f_fuel.setFrameShadow(QFrame.Raised)
        self.cbx_fuel = QComboBox(self.f_fuel)
        self.cbx_fuel.addItem("")
        self.cbx_fuel.addItem("")
        self.cbx_fuel.addItem("")
        self.cbx_fuel.addItem("")
        self.cbx_fuel.addItem("")
        self.cbx_fuel.addItem("")
        self.cbx_fuel.addItem("")
        self.cbx_fuel.addItem("")
        self.cbx_fuel.setObjectName(u"cbx_fuel")
        self.cbx_fuel.setGeometry(QRect(90, 0, 151, 30))
        self.name_fuel = QLabel(self.f_fuel)
        self.name_fuel.setObjectName(u"name_fuel")
        self.name_fuel.setGeometry(QRect(0, 0, 61, 30))
        self.f_options = QFrame(self.info_frame)
        self.f_options.setObjectName(u"f_options")
        self.f_options.setGeometry(QRect(330, 100, 241, 31))
        self.f_options.setFrameShape(QFrame.StyledPanel)
        self.f_options.setFrameShadow(QFrame.Raised)
        self.btn_options = QPushButton(self.f_options)
        self.btn_options.setObjectName(u"btn_options")
        self.btn_options.setGeometry(QRect(90, 0, 151, 31))
        self.btn_options.setStyleSheet(u"QPushButton {\n"
"    font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"    color: rgb(65,65,65);\n"
"    border: none;\n"
"    padding-top: 3px;\n"
"    padding-left: 2px;\n"
"	border: 1px solid rgb(130,130,130);\n"
"    border-radius: 2px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(185,185,255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    padding-left: 4px;\n"
"    padding-top: 5px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(166, 168, 171);\n"
"}")
        self.name_options = QLabel(self.f_options)
        self.name_options.setObjectName(u"name_options")
        self.name_options.setGeometry(QRect(0, 0, 61, 30))
        self.f_parcel_type = QFrame(self.info_frame)
        self.f_parcel_type.setObjectName(u"f_parcel_type")
        self.f_parcel_type.setGeometry(QRect(610, -40, 241, 31))
        self.f_parcel_type.setFrameShape(QFrame.StyledPanel)
        self.f_parcel_type.setFrameShadow(QFrame.Raised)
        self.rbtn_parcel_1 = QRadioButton(self.f_parcel_type)
        self.rbtn_parcel_1.setObjectName(u"rbtn_parcel_1")
        self.rbtn_parcel_1.setGeometry(QRect(10, 10, 90, 16))
        self.rbtn_parcel_2 = QRadioButton(self.f_parcel_type)
        self.rbtn_parcel_2.setObjectName(u"rbtn_parcel_2")
        self.rbtn_parcel_2.setGeometry(QRect(120, 10, 90, 16))
        self.f_rcmd_purpose = QFrame(self.info_frame)
        self.f_rcmd_purpose.setObjectName(u"f_rcmd_purpose")
        self.f_rcmd_purpose.setGeometry(QRect(610, 80, 241, 31))
        self.f_rcmd_purpose.setFrameShape(QFrame.StyledPanel)
        self.f_rcmd_purpose.setFrameShadow(QFrame.Raised)
        self.name_rcmd_purpose = QLabel(self.f_rcmd_purpose)
        self.name_rcmd_purpose.setObjectName(u"name_rcmd_purpose")
        self.name_rcmd_purpose.setGeometry(QRect(0, 0, 61, 30))
        self.edt_rcmd_purpose = QLineEdit(self.f_rcmd_purpose)
        self.edt_rcmd_purpose.setObjectName(u"edt_rcmd_purpose")
        self.edt_rcmd_purpose.setGeometry(QRect(90, 0, 151, 30))
        self.edt_rcmd_purpose.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.f_land_items = QFrame(self.info_frame)
        self.f_land_items.setObjectName(u"f_land_items")
        self.f_land_items.setGeometry(QRect(610, 120, 541, 31))
        self.f_land_items.setFrameShape(QFrame.StyledPanel)
        self.f_land_items.setFrameShadow(QFrame.Raised)
        self.ckb_land_items_5 = QCheckBox(self.f_land_items)
        self.ckb_land_items_5.setObjectName(u"ckb_land_items_5")
        self.ckb_land_items_5.setGeometry(QRect(440, 0, 101, 30))
        self.ckb_land_items_1 = QCheckBox(self.f_land_items)
        self.ckb_land_items_1.setObjectName(u"ckb_land_items_1")
        self.ckb_land_items_1.setGeometry(QRect(0, 0, 71, 30))
        self.ckb_land_items_2 = QCheckBox(self.f_land_items)
        self.ckb_land_items_2.setObjectName(u"ckb_land_items_2")
        self.ckb_land_items_2.setGeometry(QRect(110, 0, 71, 30))
        self.ckb_land_items_3 = QCheckBox(self.f_land_items)
        self.ckb_land_items_3.setObjectName(u"ckb_land_items_3")
        self.ckb_land_items_3.setGeometry(QRect(220, 0, 71, 30))
        self.ckb_land_items_4 = QCheckBox(self.f_land_items)
        self.ckb_land_items_4.setObjectName(u"ckb_land_items_4")
        self.ckb_land_items_4.setGeometry(QRect(330, 0, 71, 30))
        self.f_electricity = QFrame(self.info_frame)
        self.f_electricity.setObjectName(u"f_electricity")
        self.f_electricity.setGeometry(QRect(610, 0, 241, 31))
        self.f_electricity.setFrameShape(QFrame.StyledPanel)
        self.f_electricity.setFrameShadow(QFrame.Raised)
        self.name_electricity = QLabel(self.f_electricity)
        self.name_electricity.setObjectName(u"name_electricity")
        self.name_electricity.setGeometry(QRect(0, 0, 61, 30))
        self.cbx_electricity = QComboBox(self.f_electricity)
        self.cbx_electricity.addItem("")
        self.cbx_electricity.addItem("")
        self.cbx_electricity.addItem("")
        self.cbx_electricity.addItem("")
        self.cbx_electricity.addItem("")
        self.cbx_electricity.addItem("")
        self.cbx_electricity.setObjectName(u"cbx_electricity")
        self.cbx_electricity.setGeometry(QRect(90, 0, 151, 30))
        self.f_use_area = QFrame(self.info_frame)
        self.f_use_area.setObjectName(u"f_use_area")
        self.f_use_area.setGeometry(QRect(610, 160, 241, 31))
        self.f_use_area.setFrameShape(QFrame.StyledPanel)
        self.f_use_area.setFrameShadow(QFrame.Raised)
        self.name_use_area = QLabel(self.f_use_area)
        self.name_use_area.setObjectName(u"name_use_area")
        self.name_use_area.setGeometry(QRect(0, 0, 61, 30))
        self.cbx_use_area = QComboBox(self.f_use_area)
        self.cbx_use_area.addItem("")
        self.cbx_use_area.addItem("")
        self.cbx_use_area.addItem("")
        self.cbx_use_area.addItem("")
        self.cbx_use_area.addItem("")
        self.cbx_use_area.addItem("")
        self.cbx_use_area.addItem("")
        self.cbx_use_area.addItem("")
        self.cbx_use_area.addItem("")
        self.cbx_use_area.addItem("")
        self.cbx_use_area.addItem("")
        self.cbx_use_area.addItem("")
        self.cbx_use_area.addItem("")
        self.cbx_use_area.addItem("")
        self.cbx_use_area.addItem("")
        self.cbx_use_area.addItem("")
        self.cbx_use_area.addItem("")
        self.cbx_use_area.addItem("")
        self.cbx_use_area.addItem("")
        self.cbx_use_area.addItem("")
        self.cbx_use_area.addItem("")
        self.cbx_use_area.addItem("")
        self.cbx_use_area.addItem("")
        self.cbx_use_area.addItem("")
        self.cbx_use_area.addItem("")
        self.cbx_use_area.setObjectName(u"cbx_use_area")
        self.cbx_use_area.setGeometry(QRect(90, 0, 151, 30))
        self.f_crt_purpose = QFrame(self.info_frame)
        self.f_crt_purpose.setObjectName(u"f_crt_purpose")
        self.f_crt_purpose.setGeometry(QRect(610, 40, 241, 31))
        self.f_crt_purpose.setFrameShape(QFrame.StyledPanel)
        self.f_crt_purpose.setFrameShadow(QFrame.Raised)
        self.name_crt_purpose = QLabel(self.f_crt_purpose)
        self.name_crt_purpose.setObjectName(u"name_crt_purpose")
        self.name_crt_purpose.setGeometry(QRect(0, 0, 61, 30))
        self.edt_crt_purpose = QLineEdit(self.f_crt_purpose)
        self.edt_crt_purpose.setObjectName(u"edt_crt_purpose")
        self.edt_crt_purpose.setGeometry(QRect(90, 0, 151, 30))
        self.edt_crt_purpose.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.building_frame = QFrame(self.page_2)
        self.building_frame.setObjectName(u"building_frame")
        self.building_frame.setGeometry(QRect(10, 10, 601, 191))
        self.building_frame.setFrameShape(QFrame.StyledPanel)
        self.building_frame.setFrameShadow(QFrame.Raised)
        self.f_land_share = QFrame(self.building_frame)
        self.f_land_share.setObjectName(u"f_land_share")
        self.f_land_share.setGeometry(QRect(330, 140, 241, 31))
        self.f_land_share.setFrameShape(QFrame.StyledPanel)
        self.f_land_share.setFrameShadow(QFrame.Raised)
        self.edt_land_share_1 = QLineEdit(self.f_land_share)
        self.edt_land_share_1.setObjectName(u"edt_land_share_1")
        self.edt_land_share_1.setGeometry(QRect(90, 0, 61, 30))
        self.edt_land_share_1.setStyleSheet(u"QLineEdit {\n"
"	padding-left: 0px;\n"
"	padding-right: 0px;\n"
"}")
        self.edt_land_share_1.setEchoMode(QLineEdit.Normal)
        self.edt_land_share_1.setAlignment(Qt.AlignCenter)
        self.hint_land_share = QLabel(self.f_land_share)
        self.hint_land_share.setObjectName(u"hint_land_share")
        self.hint_land_share.setGeometry(QRect(156, 0, 31, 30))
        self.hint_land_share.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.name_land_share = QLabel(self.f_land_share)
        self.name_land_share.setObjectName(u"name_land_share")
        self.name_land_share.setGeometry(QRect(0, 0, 61, 30))
        self.edt_land_share_2 = QLineEdit(self.f_land_share)
        self.edt_land_share_2.setObjectName(u"edt_land_share_2")
        self.edt_land_share_2.setGeometry(QRect(190, 0, 51, 30))
        self.edt_land_share_2.setStyleSheet(u"QLineEdit {\n"
"	padding-left: 0px;\n"
"	padding-right: 0px;\n"
"}")
        self.edt_land_share_2.setEchoMode(QLineEdit.Normal)
        self.edt_land_share_2.setAlignment(Qt.AlignCenter)
        self.f_parking = QFrame(self.building_frame)
        self.f_parking.setObjectName(u"f_parking")
        self.f_parking.setGeometry(QRect(30, 100, 241, 71))
        self.f_parking.setFrameShape(QFrame.StyledPanel)
        self.f_parking.setFrameShadow(QFrame.Raised)
        self.f_parking_1 = QFrame(self.f_parking)
        self.f_parking_1.setObjectName(u"f_parking_1")
        self.f_parking_1.setGeometry(QRect(0, 0, 241, 31))
        self.f_parking_1.setFrameShape(QFrame.StyledPanel)
        self.f_parking_1.setFrameShadow(QFrame.Raised)
        self.btn_parking_false = QPushButton(self.f_parking_1)
        self.btn_parking_false.setObjectName(u"btn_parking_false")
        self.btn_parking_false.setGeometry(QRect(170, 0, 71, 30))
        self.btn_parking_false.setStyleSheet(u"QPushButton {\n"
"    font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"    color: rgb(105,105,105);\n"
"    border: 1px solid rgb(145,145,145);\n"
"    border-radius: 2px;\n"
"    outline: none;\n"
"    padding-right: 1px;\n"
"    padding-top: 3px;\n"
"    padding-left: 2px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	color: white;\n"
"    border: 1px solid rgb(128,128,235);\n"
"    background-color: rgb(128,128,235);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(166, 168, 171);\n"
"}")
        self.btn_parking_false.setCheckable(True)
        self.btn_parking_false.setChecked(True)
        self.name_parking_1 = QLabel(self.f_parking_1)
        self.name_parking_1.setObjectName(u"name_parking_1")
        self.name_parking_1.setGeometry(QRect(0, 0, 81, 30))
        self.btn_parking_true = QPushButton(self.f_parking_1)
        self.btn_parking_true.setObjectName(u"btn_parking_true")
        self.btn_parking_true.setGeometry(QRect(90, 0, 71, 30))
        self.btn_parking_true.setStyleSheet(u"QPushButton {\n"
"    font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"    color: rgb(105,105,105);\n"
"    border: 1px solid rgb(145,145,145);\n"
"    border-radius: 2px;\n"
"    outline: none;\n"
"    padding-right: 1px;\n"
"    padding-top: 3px;\n"
"    padding-left: 2px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	color: white;\n"
"    border: 1px solid rgb(128,128,235);\n"
"    background-color: rgb(128,128,235);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(166, 168, 171);\n"
"}")
        self.btn_parking_true.setCheckable(True)
        self.f_parking_2 = QFrame(self.f_parking)
        self.f_parking_2.setObjectName(u"f_parking_2")
        self.f_parking_2.setGeometry(QRect(0, 40, 241, 31))
        self.f_parking_2.setFrameShape(QFrame.StyledPanel)
        self.f_parking_2.setFrameShadow(QFrame.Raised)
        self.edt_parking = QLineEdit(self.f_parking_2)
        self.edt_parking.setObjectName(u"edt_parking")
        self.edt_parking.setGeometry(QRect(90, 0, 151, 30))
        self.edt_parking.setEchoMode(QLineEdit.Normal)
        self.edt_parking.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.hint_parking = QLabel(self.f_parking_2)
        self.hint_parking.setObjectName(u"hint_parking")
        self.hint_parking.setGeometry(QRect(220, 0, 21, 30))
        self.hint_parking.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.name_parking_2 = QLabel(self.f_parking_2)
        self.name_parking_2.setObjectName(u"name_parking_2")
        self.name_parking_2.setGeometry(QRect(0, 0, 61, 30))
        self.f_household = QFrame(self.building_frame)
        self.f_household.setObjectName(u"f_household")
        self.f_household.setGeometry(QRect(330, 100, 241, 31))
        self.f_household.setFrameShape(QFrame.StyledPanel)
        self.f_household.setFrameShadow(QFrame.Raised)
        self.edt_household = QLineEdit(self.f_household)
        self.edt_household.setObjectName(u"edt_household")
        self.edt_household.setGeometry(QRect(90, 0, 151, 30))
        self.edt_household.setStyleSheet(u"QLineEdit {\n"
"	padding-left: 0px;\n"
"	padding-right: 0px;\n"
"}")
        self.edt_household.setEchoMode(QLineEdit.Normal)
        self.edt_household.setAlignment(Qt.AlignCenter)
        self.name_household = QLabel(self.f_household)
        self.name_household.setObjectName(u"name_household")
        self.name_household.setGeometry(QRect(0, 0, 81, 30))
        self.f_floor = QFrame(self.building_frame)
        self.f_floor.setObjectName(u"f_floor")
        self.f_floor.setGeometry(QRect(330, 20, 241, 71))
        self.f_floor.setFrameShape(QFrame.StyledPanel)
        self.f_floor.setFrameShadow(QFrame.Raised)
        self.f_crt_floor = QFrame(self.f_floor)
        self.f_crt_floor.setObjectName(u"f_crt_floor")
        self.f_crt_floor.setGeometry(QRect(0, 40, 241, 31))
        self.f_crt_floor.setFrameShape(QFrame.StyledPanel)
        self.f_crt_floor.setFrameShadow(QFrame.Raised)
        self.hint_crt_floor = QLabel(self.f_crt_floor)
        self.hint_crt_floor.setObjectName(u"hint_crt_floor")
        self.hint_crt_floor.setGeometry(QRect(220, 0, 21, 30))
        self.hint_crt_floor.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.edt_crt_floor = QLineEdit(self.f_crt_floor)
        self.edt_crt_floor.setObjectName(u"edt_crt_floor")
        self.edt_crt_floor.setGeometry(QRect(90, 0, 151, 30))
        self.edt_crt_floor.setEchoMode(QLineEdit.Normal)
        self.edt_crt_floor.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.name_crt_floor = QLabel(self.f_crt_floor)
        self.name_crt_floor.setObjectName(u"name_crt_floor")
        self.name_crt_floor.setGeometry(QRect(0, 0, 61, 30))
        self.edt_crt_floor.raise_()
        self.hint_crt_floor.raise_()
        self.name_crt_floor.raise_()
        self.f_total_floor = QFrame(self.f_floor)
        self.f_total_floor.setObjectName(u"f_total_floor")
        self.f_total_floor.setGeometry(QRect(0, 0, 241, 31))
        self.f_total_floor.setFrameShape(QFrame.StyledPanel)
        self.f_total_floor.setFrameShadow(QFrame.Raised)
        self.hint_total_floor = QLabel(self.f_total_floor)
        self.hint_total_floor.setObjectName(u"hint_total_floor")
        self.hint_total_floor.setGeometry(QRect(220, 0, 21, 30))
        self.hint_total_floor.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.name_total_floor = QLabel(self.f_total_floor)
        self.name_total_floor.setObjectName(u"name_total_floor")
        self.name_total_floor.setGeometry(QRect(0, 0, 61, 30))
        self.edt_total_floor = QLineEdit(self.f_total_floor)
        self.edt_total_floor.setObjectName(u"edt_total_floor")
        self.edt_total_floor.setGeometry(QRect(90, 0, 151, 30))
        self.edt_total_floor.setEchoMode(QLineEdit.Normal)
        self.edt_total_floor.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.edt_total_floor.raise_()
        self.hint_total_floor.raise_()
        self.name_total_floor.raise_()
        self.f_supply_area = QFrame(self.building_frame)
        self.f_supply_area.setObjectName(u"f_supply_area")
        self.f_supply_area.setGeometry(QRect(30, 20, 241, 31))
        self.f_supply_area.setFrameShape(QFrame.StyledPanel)
        self.f_supply_area.setFrameShadow(QFrame.Raised)
        self.hint_supply_area = QLabel(self.f_supply_area)
        self.hint_supply_area.setObjectName(u"hint_supply_area")
        self.hint_supply_area.setGeometry(QRect(220, 0, 21, 30))
        self.hint_supply_area.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.edt_supply_area = QLineEdit(self.f_supply_area)
        self.edt_supply_area.setObjectName(u"edt_supply_area")
        self.edt_supply_area.setGeometry(QRect(90, 0, 151, 30))
        self.edt_supply_area.setEchoMode(QLineEdit.Normal)
        self.edt_supply_area.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.name_supply_area = QLabel(self.f_supply_area)
        self.name_supply_area.setObjectName(u"name_supply_area")
        self.name_supply_area.setGeometry(QRect(0, 0, 61, 30))
        self.edt_supply_area.raise_()
        self.hint_supply_area.raise_()
        self.name_supply_area.raise_()
        self.f_area = QFrame(self.building_frame)
        self.f_area.setObjectName(u"f_area")
        self.f_area.setGeometry(QRect(30, 60, 241, 31))
        self.f_area.setFrameShape(QFrame.StyledPanel)
        self.f_area.setFrameShadow(QFrame.Raised)
        self.hint_area = QLabel(self.f_area)
        self.hint_area.setObjectName(u"hint_area")
        self.hint_area.setGeometry(QRect(220, 0, 21, 30))
        self.hint_area.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.edt_area = QLineEdit(self.f_area)
        self.edt_area.setObjectName(u"edt_area")
        self.edt_area.setGeometry(QRect(90, 0, 151, 30))
        self.edt_area.setEchoMode(QLineEdit.Normal)
        self.edt_area.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.name_area = QLabel(self.f_area)
        self.name_area.setObjectName(u"name_area")
        self.name_area.setGeometry(QRect(0, 0, 71, 30))
        self.edt_area.raise_()
        self.hint_area.raise_()
        self.name_area.raise_()
        self.building_frame_2 = QFrame(self.page_2)
        self.building_frame_2.setObjectName(u"building_frame_2")
        self.building_frame_2.setGeometry(QRect(10, 220, 601, 111))
        self.building_frame_2.setFrameShape(QFrame.StyledPanel)
        self.building_frame_2.setFrameShadow(QFrame.Raised)
        self.f_purpose_day = QFrame(self.building_frame_2)
        self.f_purpose_day.setObjectName(u"f_purpose_day")
        self.f_purpose_day.setGeometry(QRect(30, 20, 541, 71))
        self.f_purpose_day.setFrameShape(QFrame.StyledPanel)
        self.f_purpose_day.setFrameShadow(QFrame.Raised)
        self.f_day = QFrame(self.f_purpose_day)
        self.f_day.setObjectName(u"f_day")
        self.f_day.setGeometry(QRect(0, 40, 541, 31))
        self.f_day.setFrameShape(QFrame.StyledPanel)
        self.f_day.setFrameShadow(QFrame.Raised)
        self.hint_day_3 = QLabel(self.f_day)
        self.hint_day_3.setObjectName(u"hint_day_3")
        self.hint_day_3.setGeometry(QRect(500, 0, 21, 30))
        self.hint_day_3.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.edt_day_3 = QLineEdit(self.f_day)
        self.edt_day_3.setObjectName(u"edt_day_3")
        self.edt_day_3.setGeometry(QRect(448, 0, 51, 30))
        self.edt_day_3.setStyleSheet(u"QLineEdit {\n"
"	padding-left: 0px;\n"
"	padding-right: 0px;\n"
"}")
        self.edt_day_3.setEchoMode(QLineEdit.Normal)
        self.edt_day_3.setAlignment(Qt.AlignCenter)
        self.edt_day_2 = QLineEdit(self.f_day)
        self.edt_day_2.setObjectName(u"edt_day_2")
        self.edt_day_2.setGeometry(QRect(368, 0, 51, 30))
        self.edt_day_2.setStyleSheet(u"QLineEdit {\n"
"	padding-left: 0px;\n"
"	padding-right: 0px;\n"
"}")
        self.edt_day_2.setEchoMode(QLineEdit.Normal)
        self.edt_day_2.setAlignment(Qt.AlignCenter)
        self.hint_day_1 = QLabel(self.f_day)
        self.hint_day_1.setObjectName(u"hint_day_1")
        self.hint_day_1.setGeometry(QRect(340, 0, 21, 30))
        self.hint_day_1.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.cbx_day = QComboBox(self.f_day)
        self.cbx_day.addItem("")
        self.cbx_day.addItem("")
        self.cbx_day.addItem("")
        self.cbx_day.setObjectName(u"cbx_day")
        self.cbx_day.setGeometry(QRect(90, 0, 161, 30))
        self.hint_day_2 = QLabel(self.f_day)
        self.hint_day_2.setObjectName(u"hint_day_2")
        self.hint_day_2.setGeometry(QRect(420, 0, 21, 30))
        self.hint_day_2.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.edt_day_1 = QLineEdit(self.f_day)
        self.edt_day_1.setObjectName(u"edt_day_1")
        self.edt_day_1.setGeometry(QRect(268, 0, 71, 30))
        self.edt_day_1.setStyleSheet(u"QLineEdit {\n"
"	padding-left: 0px;\n"
"	padding-right: 0px;\n"
"}")
        self.edt_day_1.setEchoMode(QLineEdit.Normal)
        self.edt_day_1.setAlignment(Qt.AlignCenter)
        self.name_day = QLabel(self.f_day)
        self.name_day.setObjectName(u"name_day")
        self.name_day.setGeometry(QRect(0, 0, 71, 30))
        self.f_purpose = QFrame(self.f_purpose_day)
        self.f_purpose.setObjectName(u"f_purpose")
        self.f_purpose.setGeometry(QRect(0, 0, 541, 31))
        self.f_purpose.setFrameShape(QFrame.StyledPanel)
        self.f_purpose.setFrameShadow(QFrame.Raised)
        self.edt_purpose = QLineEdit(self.f_purpose)
        self.edt_purpose.setObjectName(u"edt_purpose")
        self.edt_purpose.setGeometry(QRect(270, 0, 151, 30))
        self.edt_purpose.setStyleSheet(u"QLineEdit {\n"
"	padding-right: 22px;\n"
"}")
        self.edt_purpose.setEchoMode(QLineEdit.Normal)
        self.edt_purpose.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.name_purpose = QLabel(self.f_purpose)
        self.name_purpose.setObjectName(u"name_purpose")
        self.name_purpose.setGeometry(QRect(2, 0, 71, 30))
        self.cbx_purpose = QComboBox(self.f_purpose)
        self.cbx_purpose.addItem("")
        self.cbx_purpose.addItem("")
        self.cbx_purpose.addItem("")
        self.cbx_purpose.addItem("")
        self.cbx_purpose.addItem("")
        self.cbx_purpose.addItem("")
        self.cbx_purpose.setObjectName(u"cbx_purpose")
        self.cbx_purpose.setGeometry(QRect(92, 0, 161, 30))
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.day_frame = QFrame(self.page_3)
        self.day_frame.setObjectName(u"day_frame")
        self.day_frame.setGeometry(QRect(10, 10, 601, 151))
        self.day_frame.setFrameShape(QFrame.StyledPanel)
        self.day_frame.setFrameShadow(QFrame.Raised)
        self.name_explanation = QLabel(self.day_frame)
        self.name_explanation.setObjectName(u"name_explanation")
        self.name_explanation.setGeometry(QRect(30, 60, 71, 30))
        self.name_in_date = QLabel(self.day_frame)
        self.name_in_date.setObjectName(u"name_in_date")
        self.name_in_date.setGeometry(QRect(30, 20, 71, 30))
        self.edt_in_date_1 = QLineEdit(self.day_frame)
        self.edt_in_date_1.setObjectName(u"edt_in_date_1")
        self.edt_in_date_1.setEnabled(False)
        self.edt_in_date_1.setGeometry(QRect(231, 20, 71, 30))
        self.edt_in_date_1.setStyleSheet(u"QLineEdit {\n"
"	padding-left: 0px;\n"
"	padding-right: 0px;\n"
"}")
        self.edt_in_date_1.setEchoMode(QLineEdit.Normal)
        self.edt_in_date_1.setAlignment(Qt.AlignCenter)
        self.edt_explanation = QLineEdit(self.day_frame)
        self.edt_explanation.setObjectName(u"edt_explanation")
        self.edt_explanation.setGeometry(QRect(120, 60, 451, 30))
        self.edt_explanation.setStyleSheet(u"QLineEdit {\n"
"	padding-right: 22px;\n"
"}")
        self.edt_explanation.setEchoMode(QLineEdit.Normal)
        self.edt_explanation.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.edt_in_date_2 = QLineEdit(self.day_frame)
        self.edt_in_date_2.setObjectName(u"edt_in_date_2")
        self.edt_in_date_2.setEnabled(False)
        self.edt_in_date_2.setGeometry(QRect(331, 20, 51, 30))
        self.edt_in_date_2.setStyleSheet(u"QLineEdit {\n"
"	padding-left: 0px;\n"
"	padding-right: 0px;\n"
"}")
        self.edt_in_date_2.setEchoMode(QLineEdit.Normal)
        self.edt_in_date_2.setAlignment(Qt.AlignCenter)
        self.edt_in_date_3 = QLineEdit(self.day_frame)
        self.edt_in_date_3.setObjectName(u"edt_in_date_3")
        self.edt_in_date_3.setEnabled(False)
        self.edt_in_date_3.setGeometry(QRect(411, 20, 51, 30))
        self.edt_in_date_3.setStyleSheet(u"QLineEdit {\n"
"	padding-left: 0px;\n"
"	padding-right: 0px;\n"
"}")
        self.edt_in_date_3.setEchoMode(QLineEdit.Normal)
        self.edt_in_date_3.setAlignment(Qt.AlignCenter)
        self.hint_in_date_1 = QLabel(self.day_frame)
        self.hint_in_date_1.setObjectName(u"hint_in_date_1")
        self.hint_in_date_1.setGeometry(QRect(303, 20, 21, 30))
        self.hint_in_date_1.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.hint_in_date_2 = QLabel(self.day_frame)
        self.hint_in_date_2.setObjectName(u"hint_in_date_2")
        self.hint_in_date_2.setGeometry(QRect(383, 20, 21, 30))
        self.hint_in_date_2.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.label_43 = QLabel(self.day_frame)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(463, 20, 21, 30))
        self.label_43.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.rbtn_in_date_1 = QRadioButton(self.day_frame)
        self.rbtn_in_date_1.setObjectName(u"rbtn_in_date_1")
        self.rbtn_in_date_1.setGeometry(QRect(120, 20, 81, 30))
        self.rbtn_in_date_1.setChecked(True)
        self.rbtn_in_date_2 = QRadioButton(self.day_frame)
        self.rbtn_in_date_2.setObjectName(u"rbtn_in_date_2")
        self.rbtn_in_date_2.setGeometry(QRect(210, 20, 21, 30))
        self.ckb_in_date = QCheckBox(self.day_frame)
        self.ckb_in_date.setObjectName(u"ckb_in_date")
        self.ckb_in_date.setGeometry(QRect(500, 20, 71, 30))
        self.ckb_in_date.setStyleSheet(u"QCheckBox { font-size: 14px; }")
        self.edt_relationship = QLineEdit(self.day_frame)
        self.edt_relationship.setObjectName(u"edt_relationship")
        self.edt_relationship.setGeometry(QRect(460, 100, 111, 30))
        self.edt_relationship.setStyleSheet(u"QLineEdit {\n"
"	padding-right: 22px;\n"
"}")
        self.edt_relationship.setEchoMode(QLineEdit.Normal)
        self.edt_relationship.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.edt_owner = QLineEdit(self.day_frame)
        self.edt_owner.setObjectName(u"edt_owner")
        self.edt_owner.setGeometry(QRect(120, 100, 121, 30))
        self.edt_owner.setStyleSheet(u"QLineEdit {\n"
"	padding-right: 22px;\n"
"}")
        self.edt_owner.setEchoMode(QLineEdit.Normal)
        self.edt_owner.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.name_relationship = QLabel(self.day_frame)
        self.name_relationship.setObjectName(u"name_relationship")
        self.name_relationship.setGeometry(QRect(280, 100, 41, 30))
        self.name_owner = QLabel(self.day_frame)
        self.name_owner.setObjectName(u"name_owner")
        self.name_owner.setGeometry(QRect(30, 100, 71, 30))
        self.cbx_relationship = QComboBox(self.day_frame)
        self.cbx_relationship.addItem("")
        self.cbx_relationship.addItem("")
        self.cbx_relationship.addItem("")
        self.cbx_relationship.addItem("")
        self.cbx_relationship.addItem("")
        self.cbx_relationship.setObjectName(u"cbx_relationship")
        self.cbx_relationship.setGeometry(QRect(350, 100, 101, 30))
        self.owner_frame = QFrame(self.page_3)
        self.owner_frame.setObjectName(u"owner_frame")
        self.owner_frame.setGeometry(QRect(10, 180, 601, 151))
        self.owner_frame.setFrameShape(QFrame.StyledPanel)
        self.owner_frame.setFrameShadow(QFrame.Raised)
        self.name_client_1 = QLabel(self.owner_frame)
        self.name_client_1.setObjectName(u"name_client_1")
        self.name_client_1.setGeometry(QRect(30, 20, 71, 30))
        self.edt_client_1 = QLineEdit(self.owner_frame)
        self.edt_client_1.setObjectName(u"edt_client_1")
        self.edt_client_1.setGeometry(QRect(210, 20, 91, 30))
        self.edt_client_1.setStyleSheet(u"QLineEdit {\n"
"	padding-right: 22px;\n"
"}")
        self.edt_client_1.setEchoMode(QLineEdit.Normal)
        self.edt_client_1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.name_client_num_1 = QLabel(self.owner_frame)
        self.name_client_num_1.setObjectName(u"name_client_num_1")
        self.name_client_num_1.setGeometry(QRect(340, 20, 71, 30))
        self.edt_client_num_1 = QLineEdit(self.owner_frame)
        self.edt_client_num_1.setObjectName(u"edt_client_num_1")
        self.edt_client_num_1.setGeometry(QRect(430, 20, 141, 30))
        self.edt_client_num_1.setStyleSheet(u"QLineEdit {\n"
"	padding-right: 22px;\n"
"}")
        self.edt_client_num_1.setEchoMode(QLineEdit.Normal)
        self.edt_client_num_1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.edt_client_num_2 = QLineEdit(self.owner_frame)
        self.edt_client_num_2.setObjectName(u"edt_client_num_2")
        self.edt_client_num_2.setGeometry(QRect(430, 60, 141, 30))
        self.edt_client_num_2.setStyleSheet(u"QLineEdit {\n"
"	padding-right: 22px;\n"
"}")
        self.edt_client_num_2.setEchoMode(QLineEdit.Normal)
        self.edt_client_num_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.edt_client_2 = QLineEdit(self.owner_frame)
        self.edt_client_2.setObjectName(u"edt_client_2")
        self.edt_client_2.setGeometry(QRect(210, 60, 91, 30))
        self.edt_client_2.setStyleSheet(u"QLineEdit {\n"
"	padding-right: 22px;\n"
"}")
        self.edt_client_2.setEchoMode(QLineEdit.Normal)
        self.edt_client_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.name_client_num_2 = QLabel(self.owner_frame)
        self.name_client_num_2.setObjectName(u"name_client_num_2")
        self.name_client_num_2.setGeometry(QRect(340, 60, 71, 30))
        self.name_client_2 = QLabel(self.owner_frame)
        self.name_client_2.setObjectName(u"name_client_2")
        self.name_client_2.setGeometry(QRect(30, 60, 71, 30))
        self.name_memo = QLabel(self.owner_frame)
        self.name_memo.setObjectName(u"name_memo")
        self.name_memo.setGeometry(QRect(30, 100, 71, 30))
        self.edt_memo = QLineEdit(self.owner_frame)
        self.edt_memo.setObjectName(u"edt_memo")
        self.edt_memo.setGeometry(QRect(120, 100, 451, 30))
        self.edt_memo.setStyleSheet(u"QLineEdit {\n"
"	padding-right: 22px;\n"
"}")
        self.edt_memo.setEchoMode(QLineEdit.Normal)
        self.edt_memo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.cbx_client_1 = QComboBox(self.owner_frame)
        self.cbx_client_1.addItem("")
        self.cbx_client_1.addItem("")
        self.cbx_client_1.addItem("")
        self.cbx_client_1.setObjectName(u"cbx_client_1")
        self.cbx_client_1.setGeometry(QRect(120, 20, 81, 30))
        self.cbx_client_2 = QComboBox(self.owner_frame)
        self.cbx_client_2.addItem("")
        self.cbx_client_2.addItem("")
        self.cbx_client_2.addItem("")
        self.cbx_client_2.setObjectName(u"cbx_client_2")
        self.cbx_client_2.setGeometry(QRect(120, 60, 81, 30))
        self.stackedWidget.addWidget(self.page_3)
        self.btn_back = QPushButton(self.centralwidget)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(380, 530, 111, 41))
        self.btn_back.setStyleSheet(u"QPushButton {\n"
"    font: 18px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"    color: rgb(88,88,255);\n"
"    border: 1px solid rgb(128,128,255);\n"
"    padding-top: 3px;\n"
"    padding-left: 2px;\n"
"    border-radius: 3px;\n"
"    background: white;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    padding-left: 4px;\n"
"    padding-top: 5px;\n"
"    background-color: rgb(245,245,245);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(166, 168, 171);\n"
"}")
        AddRoom.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.edt_address, self.cbx_type)
        QWidget.setTabOrder(self.cbx_type, self.cbx_kind_1)
        QWidget.setTabOrder(self.cbx_kind_1, self.cbx_kind_2)
        QWidget.setTabOrder(self.cbx_kind_2, self.edt_price)
        QWidget.setTabOrder(self.edt_price, self.edt_admin_cost)
        QWidget.setTabOrder(self.edt_admin_cost, self.edt_deposit_1)
        QWidget.setTabOrder(self.edt_deposit_1, self.edt_loan)
        QWidget.setTabOrder(self.edt_loan, self.ckb_cost_in_1)
        QWidget.setTabOrder(self.ckb_cost_in_1, self.ckb_cost_in_2)
        QWidget.setTabOrder(self.ckb_cost_in_2, self.ckb_cost_in_3)
        QWidget.setTabOrder(self.ckb_cost_in_3, self.ckb_cost_in_4)
        QWidget.setTabOrder(self.ckb_cost_in_4, self.ckb_cost_in_5)
        QWidget.setTabOrder(self.ckb_cost_in_5, self.edt_room_num)
        QWidget.setTabOrder(self.edt_room_num, self.edt_bathroom)
        QWidget.setTabOrder(self.edt_bathroom, self.cbx_heating)
        QWidget.setTabOrder(self.cbx_heating, self.cbx_fuel)
        QWidget.setTabOrder(self.cbx_fuel, self.cbx_direction_1)
        QWidget.setTabOrder(self.cbx_direction_1, self.cbx_direction_2)
        QWidget.setTabOrder(self.cbx_direction_2, self.btn_options)
        QWidget.setTabOrder(self.btn_options, self.edt_supply_area)
        QWidget.setTabOrder(self.edt_supply_area, self.edt_area)
        QWidget.setTabOrder(self.edt_area, self.btn_parking_true)
        QWidget.setTabOrder(self.btn_parking_true, self.btn_parking_false)
        QWidget.setTabOrder(self.btn_parking_false, self.edt_parking)
        QWidget.setTabOrder(self.edt_parking, self.edt_total_floor)
        QWidget.setTabOrder(self.edt_total_floor, self.edt_crt_floor)
        QWidget.setTabOrder(self.edt_crt_floor, self.edt_household)
        QWidget.setTabOrder(self.edt_household, self.edt_land_share_1)
        QWidget.setTabOrder(self.edt_land_share_1, self.edt_land_share_2)
        QWidget.setTabOrder(self.edt_land_share_2, self.cbx_purpose)
        QWidget.setTabOrder(self.cbx_purpose, self.edt_purpose)
        QWidget.setTabOrder(self.edt_purpose, self.cbx_day)
        QWidget.setTabOrder(self.cbx_day, self.edt_day_1)
        QWidget.setTabOrder(self.edt_day_1, self.edt_day_2)
        QWidget.setTabOrder(self.edt_day_2, self.edt_day_3)
        QWidget.setTabOrder(self.edt_day_3, self.rbtn_in_date_1)
        QWidget.setTabOrder(self.rbtn_in_date_1, self.rbtn_in_date_2)
        QWidget.setTabOrder(self.rbtn_in_date_2, self.edt_in_date_1)
        QWidget.setTabOrder(self.edt_in_date_1, self.edt_in_date_2)
        QWidget.setTabOrder(self.edt_in_date_2, self.edt_in_date_3)
        QWidget.setTabOrder(self.edt_in_date_3, self.ckb_in_date)
        QWidget.setTabOrder(self.ckb_in_date, self.edt_explanation)
        QWidget.setTabOrder(self.edt_explanation, self.edt_owner)
        QWidget.setTabOrder(self.edt_owner, self.cbx_relationship)
        QWidget.setTabOrder(self.cbx_relationship, self.edt_relationship)
        QWidget.setTabOrder(self.edt_relationship, self.cbx_client_1)
        QWidget.setTabOrder(self.cbx_client_1, self.edt_client_1)
        QWidget.setTabOrder(self.edt_client_1, self.edt_client_num_1)
        QWidget.setTabOrder(self.edt_client_num_1, self.cbx_client_2)
        QWidget.setTabOrder(self.cbx_client_2, self.edt_client_2)
        QWidget.setTabOrder(self.edt_client_2, self.edt_client_num_2)
        QWidget.setTabOrder(self.edt_client_num_2, self.edt_memo)
        QWidget.setTabOrder(self.edt_memo, self.btn_page_1)
        QWidget.setTabOrder(self.btn_page_1, self.btn_page_2)
        QWidget.setTabOrder(self.btn_page_2, self.btn_page_3)
        QWidget.setTabOrder(self.btn_page_3, self.btn_back)
        QWidget.setTabOrder(self.btn_back, self.btn_next)

        self.retranslateUi(AddRoom)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AddRoom)
    # setupUi

    def retranslateUi(self, AddRoom):
        AddRoom.setWindowTitle(QCoreApplication.translate("AddRoom", u"MainWindow", None))
        self.name_type.setText(QCoreApplication.translate("AddRoom", u"\uac70\ub798\uc720\ud615", None))
        self.cbx_type.setItemText(0, QCoreApplication.translate("AddRoom", u"\ub9e4\ub9e4", None))
        self.cbx_type.setItemText(1, QCoreApplication.translate("AddRoom", u"\uc804\uc138", None))
        self.cbx_type.setItemText(2, QCoreApplication.translate("AddRoom", u"\uc6d4\uc138", None))

        self.name_kind.setText(QCoreApplication.translate("AddRoom", u"\ub9e4\ubb3c\uc885\ub958", None))
        self.cbx_kind_1.setItemText(0, QCoreApplication.translate("AddRoom", u"\uc544\ud30c\ud2b8", None))
        self.cbx_kind_1.setItemText(1, QCoreApplication.translate("AddRoom", u"\ubd84\uc591\uad8c", None))
        self.cbx_kind_1.setItemText(2, QCoreApplication.translate("AddRoom", u"\uc624\ud53c\uc2a4\ud154", None))
        self.cbx_kind_1.setItemText(3, QCoreApplication.translate("AddRoom", u"\uc7ac\uac1c\ubc1c", None))
        self.cbx_kind_1.setItemText(4, QCoreApplication.translate("AddRoom", u"\uc8fc\ud0dd", None))
        self.cbx_kind_1.setItemText(5, QCoreApplication.translate("AddRoom", u"\uc6d0\ub8f8", None))
        self.cbx_kind_1.setItemText(6, QCoreApplication.translate("AddRoom", u"\uc0c1\uac00\uc810\ud3ec", None))
        self.cbx_kind_1.setItemText(7, QCoreApplication.translate("AddRoom", u"\uc0ac\ubb34\uc2e4", None))
        self.cbx_kind_1.setItemText(8, QCoreApplication.translate("AddRoom", u"\uacf5\uc7a5/\ucc3d\uace0", None))
        self.cbx_kind_1.setItemText(9, QCoreApplication.translate("AddRoom", u"\ube4c\ub529 \uac74\ubb3c", None))
        self.cbx_kind_1.setItemText(10, QCoreApplication.translate("AddRoom", u"\ud1a0\uc9c0", None))

        self.btn_next.setText(QCoreApplication.translate("AddRoom", u"\ub2e4 \uc74c", None))
        self.btn_page_1.setText(QCoreApplication.translate("AddRoom", u"1", None))
        self.btn_page_2.setText(QCoreApplication.translate("AddRoom", u"2", None))
        self.btn_page_3.setText(QCoreApplication.translate("AddRoom", u"3", None))
        self.name_deposit.setText(QCoreApplication.translate("AddRoom", u"\uae30\ubcf4\uc99d\uae08", None))
        self.hint_deposit_1.setText(QCoreApplication.translate("AddRoom", u"\ub9cc", None))
        self.edt_deposit_1.setText("")
        self.hint_deposit_2.setText(QCoreApplication.translate("AddRoom", u"\ub9cc", None))
        self.edt_deposit_2.setText("")
        self.name_loan.setText(QCoreApplication.translate("AddRoom", u"\uc735\uc790\uae08", None))
        self.edt_loan.setText("")
        self.hint_loan.setText(QCoreApplication.translate("AddRoom", u"\ub9cc\uc6d0", None))
        self.name_cost_in.setText(QCoreApplication.translate("AddRoom", u"\uad00\ub9ac\ube44 \ud3ec\ud568 \ud56d\ubaa9", None))
        self.ckb_cost_in_5.setText(QCoreApplication.translate("AddRoom", u"TV", None))
        self.ckb_cost_in_1.setText(QCoreApplication.translate("AddRoom", u"\uc804\uae30\uc138", None))
        self.ckb_cost_in_2.setText(QCoreApplication.translate("AddRoom", u"\uac00\uc2a4", None))
        self.ckb_cost_in_3.setText(QCoreApplication.translate("AddRoom", u"\uc218\ub3c4", None))
        self.ckb_cost_in_4.setText(QCoreApplication.translate("AddRoom", u"\uc778\ud130\ub137", None))
        self.hint_admin_cost.setText(QCoreApplication.translate("AddRoom", u"\uc6d0", None))
        self.name_admin_cost.setText(QCoreApplication.translate("AddRoom", u"\uad00\ub9ac\ube44", None))
        self.edt_admin_cost.setText("")
        self.hint_price.setText(QCoreApplication.translate("AddRoom", u"\ub9cc\uc6d0", None))
        self.name_price.setText(QCoreApplication.translate("AddRoom", u"\ub9e4\ub9e4\uac00", None))
        self.edt_price.setText("")
        self.name_rent.setText(QCoreApplication.translate("AddRoom", u"\uc6d4 \ucc28\uc784", None))
        self.edt_rent.setText("")
        self.hint_rent.setText(QCoreApplication.translate("AddRoom", u"\ub9cc\uc6d0", None))
        self.name_facility.setText(QCoreApplication.translate("AddRoom", u"\uad8c\ub9ac\uae08", None))
        self.edt_facility.setText("")
        self.hint_facility.setText(QCoreApplication.translate("AddRoom", u"\ub9cc\uc6d0", None))
        self.name_premium.setText(QCoreApplication.translate("AddRoom", u"\ud504\ub9ac\ubbf8\uc5c4", None))
        self.edt_premium.setText("")
        self.hint_premium.setText(QCoreApplication.translate("AddRoom", u"\ub9cc\uc6d0", None))
        self.name_parcel.setText(QCoreApplication.translate("AddRoom", u"\ubd84\uc591\uae08\uc561", None))
        self.edt_parcel.setText("")
        self.hint_parcel.setText(QCoreApplication.translate("AddRoom", u"\ub9cc\uc6d0", None))
        self.name_middle_pay.setText(QCoreApplication.translate("AddRoom", u"\ub0a9\uc785 \uc911\ub3c4\uae08", None))
        self.edt_middle_pay.setText("")
        self.hint_middle_pay.setText(QCoreApplication.translate("AddRoom", u"\ub9cc\uc6d0", None))
        self.hint_room_num.setText(QCoreApplication.translate("AddRoom", u"\uac1c", None))
        self.edt_room_num.setText("")
        self.name_room_num.setText(QCoreApplication.translate("AddRoom", u"\ubc29 \uac1c\uc218", None))
        self.hint_bathroom.setText(QCoreApplication.translate("AddRoom", u"\uac1c", None))
        self.name_bathroom.setText(QCoreApplication.translate("AddRoom", u"\uc695\uc2e4 \uac1c\uc218", None))
        self.edt_bathroom.setText("")
        self.cbx_direction_2.setItemText(0, QCoreApplication.translate("AddRoom", u"\ub3d9\ud5a5", None))
        self.cbx_direction_2.setItemText(1, QCoreApplication.translate("AddRoom", u"\uc11c\ud5a5", None))
        self.cbx_direction_2.setItemText(2, QCoreApplication.translate("AddRoom", u"\ub0a8\ud5a5", None))
        self.cbx_direction_2.setItemText(3, QCoreApplication.translate("AddRoom", u"\ubd81\ud5a5", None))
        self.cbx_direction_2.setItemText(4, QCoreApplication.translate("AddRoom", u"\ub0a8\ub3d9\ud5a5", None))
        self.cbx_direction_2.setItemText(5, QCoreApplication.translate("AddRoom", u"\ub0a8\uc11c\ud5a5", None))
        self.cbx_direction_2.setItemText(6, QCoreApplication.translate("AddRoom", u"\ubd81\ub3d9\ud5a5", None))
        self.cbx_direction_2.setItemText(7, QCoreApplication.translate("AddRoom", u"\ubd81\uc11c\ud5a5", None))

        self.cbx_direction_1.setItemText(0, QCoreApplication.translate("AddRoom", u"\uac70\uc2e4", None))
        self.cbx_direction_1.setItemText(1, QCoreApplication.translate("AddRoom", u"\uc548\ubc29", None))

        self.name_direction.setText(QCoreApplication.translate("AddRoom", u"\ubc29\ud5a5", None))
        self.cbx_heating.setItemText(0, QCoreApplication.translate("AddRoom", u"\uac1c\ubcc4\ub09c\ubc29", None))
        self.cbx_heating.setItemText(1, QCoreApplication.translate("AddRoom", u"\uc9c0\uc5ed\ub09c\ubc29", None))
        self.cbx_heating.setItemText(2, QCoreApplication.translate("AddRoom", u"\uc911\uc559\ub09c\ubc29", None))

        self.name_heating.setText(QCoreApplication.translate("AddRoom", u"\ub09c\ubc29\uc815\ubcf4", None))
        self.cbx_fuel.setItemText(0, QCoreApplication.translate("AddRoom", u"\ub3c4\uc2dc\uac00\uc2a4", None))
        self.cbx_fuel.setItemText(1, QCoreApplication.translate("AddRoom", u"\uc804\uae30", None))
        self.cbx_fuel.setItemText(2, QCoreApplication.translate("AddRoom", u"\uc2ec\uc57c\uc804\uae30", None))
        self.cbx_fuel.setItemText(3, QCoreApplication.translate("AddRoom", u"\uae30\ub984", None))
        self.cbx_fuel.setItemText(4, QCoreApplication.translate("AddRoom", u"LPG", None))
        self.cbx_fuel.setItemText(5, QCoreApplication.translate("AddRoom", u"\ud0dc\uc591\uc5f4", None))
        self.cbx_fuel.setItemText(6, QCoreApplication.translate("AddRoom", u"\uc9c0\uc5f4", None))
        self.cbx_fuel.setItemText(7, QCoreApplication.translate("AddRoom", u"\uc5f4\ubcd1\ud569", None))

        self.name_fuel.setText(QCoreApplication.translate("AddRoom", u"\ub09c\ubc29\uc5f0\ub8cc", None))
        self.btn_options.setText(QCoreApplication.translate("AddRoom", u"\uc635\uc158 \uc120\ud0dd", None))
        self.name_options.setText(QCoreApplication.translate("AddRoom", u"\uc2dc\uc124\uc815\ubcf4", None))
        self.rbtn_parcel_1.setText(QCoreApplication.translate("AddRoom", u"\uc77c\ubc18 \ubd84\uc591", None))
        self.rbtn_parcel_2.setText(QCoreApplication.translate("AddRoom", u"\uc870\ud569\uc6d0", None))
        self.name_rcmd_purpose.setText(QCoreApplication.translate("AddRoom", u"\ucd94\ucc9c\uc6a9\ub3c4", None))
        self.edt_rcmd_purpose.setText("")
        self.ckb_land_items_5.setText(QCoreApplication.translate("AddRoom", u"\ud1a0\uc9c0\uac70\ub798\ud5c8\uac00", None))
        self.ckb_land_items_1.setText(QCoreApplication.translate("AddRoom", u"\uad6d\ud1a0\uc774\uc6a9", None))
        self.ckb_land_items_2.setText(QCoreApplication.translate("AddRoom", u"\ub3c4\uc2dc\uacc4\ud68d", None))
        self.ckb_land_items_3.setText(QCoreApplication.translate("AddRoom", u"\uac74\ucd95\ud5c8\uac00", None))
        self.ckb_land_items_4.setText(QCoreApplication.translate("AddRoom", u"\uc9c4\uc785\ub3c4\ub85c", None))
        self.name_electricity.setText(QCoreApplication.translate("AddRoom", u"\uc0ac\uc6a9\uc804\ub825", None))
        self.cbx_electricity.setItemText(0, QCoreApplication.translate("AddRoom", u"\ub2e8\ub3c5\uc8fc\ud0dd", None))
        self.cbx_electricity.setItemText(1, QCoreApplication.translate("AddRoom", u"\uacf5\ub3d9\uc8fc\ud0dd", None))
        self.cbx_electricity.setItemText(2, QCoreApplication.translate("AddRoom", u"\uc81c1\uc885 \uadfc\ub9b0\uc0dd\ud65c\uc2dc\uc124", None))
        self.cbx_electricity.setItemText(3, QCoreApplication.translate("AddRoom", u"\uc81c2\uc885 \uadfc\ub9b0\uc0dd\ud65c\uc2dc\uc124", None))
        self.cbx_electricity.setItemText(4, QCoreApplication.translate("AddRoom", u"\uc5c5\ubb34\uc2dc\uc124", None))
        self.cbx_electricity.setItemText(5, QCoreApplication.translate("AddRoom", u"( \uc9c1\uc811\uc785\ub825 )", None))

        self.name_use_area.setText(QCoreApplication.translate("AddRoom", u"\uc6a9\ub3c4\uc9c0\uc5ed", None))
        self.cbx_use_area.setItemText(0, QCoreApplication.translate("AddRoom", u"( \uc120\ud0dd )", None))
        self.cbx_use_area.setItemText(1, QCoreApplication.translate("AddRoom", u"\uacc4\ud68d\uad00\ub9ac\uc9c0\uc5ed", None))
        self.cbx_use_area.setItemText(2, QCoreApplication.translate("AddRoom", u"\uacc4\ud68d\uad00\ub9ac", None))
        self.cbx_use_area.setItemText(3, QCoreApplication.translate("AddRoom", u"\uadfc\ub9b0\uc0c1\uc5c5", None))
        self.cbx_use_area.setItemText(4, QCoreApplication.translate("AddRoom", u"\ub18d\ub9bc\uc9c0\uc5ed", None))
        self.cbx_use_area.setItemText(5, QCoreApplication.translate("AddRoom", u"\ubcf4\uc804\uad00\ub9ac\uc9c0\uc5ed", None))
        self.cbx_use_area.setItemText(6, QCoreApplication.translate("AddRoom", u"\ubcf4\uc804\ub179\uc9c0", None))
        self.cbx_use_area.setItemText(7, QCoreApplication.translate("AddRoom", u"\uc0dd\uc0b0\uad00\ub9ac\uc9c0\uc5ed", None))
        self.cbx_use_area.setItemText(8, QCoreApplication.translate("AddRoom", u"\uc0dd\uc0b0\ub179\uc9c0", None))
        self.cbx_use_area.setItemText(9, QCoreApplication.translate("AddRoom", u"\uc720\ud1b5\uc0c1\uc5c5", None))
        self.cbx_use_area.setItemText(10, QCoreApplication.translate("AddRoom", u"\uc77c\ubc18\uacf5\uc5c5", None))
        self.cbx_use_area.setItemText(11, QCoreApplication.translate("AddRoom", u"\uc77c\ubc18\uc0c1\uc5c5", None))
        self.cbx_use_area.setItemText(12, QCoreApplication.translate("AddRoom", u"\uc790\uc5f0\ub179\uc9c0", None))
        self.cbx_use_area.setItemText(13, QCoreApplication.translate("AddRoom", u"\uc790\uc5f0\ud658\uacbd\ubcf4\uc804\uc9c0\uc5ed", None))
        self.cbx_use_area.setItemText(14, QCoreApplication.translate("AddRoom", u"\uc804\uc6a9\uacf5\uc5c5", None))
        self.cbx_use_area.setItemText(15, QCoreApplication.translate("AddRoom", u"\uc81c1\uc885\uc77c\ubc18\uc8fc\uac70", None))
        self.cbx_use_area.setItemText(16, QCoreApplication.translate("AddRoom", u"\uc81c2\uc885\uc77c\ubc18\uc8fc\uac70", None))
        self.cbx_use_area.setItemText(17, QCoreApplication.translate("AddRoom", u"\uc81c3\uc885\uc77c\ubc18\uc8fc\uac70", None))
        self.cbx_use_area.setItemText(18, QCoreApplication.translate("AddRoom", u"\uc81c1\uc885\uc804\uc6a9\uc8fc\uac70", None))
        self.cbx_use_area.setItemText(19, QCoreApplication.translate("AddRoom", u"\uc81c2\uc885\uc804\uc6a9\uc8fc\uac70", None))
        self.cbx_use_area.setItemText(20, QCoreApplication.translate("AddRoom", u"\uc900\uacf5\uc5c5", None))
        self.cbx_use_area.setItemText(21, QCoreApplication.translate("AddRoom", u"\uc900\uc8fc\uac70", None))
        self.cbx_use_area.setItemText(22, QCoreApplication.translate("AddRoom", u"\uc911\uc2ec\uc0c1\uc5c5", None))
        self.cbx_use_area.setItemText(23, QCoreApplication.translate("AddRoom", u"\uae30\ud0c0", None))
        self.cbx_use_area.setItemText(24, QCoreApplication.translate("AddRoom", u"( \uc9c1\uc811\uc785\ub825 )", None))

        self.name_crt_purpose.setText(QCoreApplication.translate("AddRoom", u"\ud604\uc7ac\uc6a9\ub3c4", None))
        self.edt_crt_purpose.setText("")
        self.edt_land_share_1.setText("")
        self.hint_land_share.setText(QCoreApplication.translate("AddRoom", u"\ubd84\uc758", None))
        self.name_land_share.setText(QCoreApplication.translate("AddRoom", u"\ub300\uc9c0 \uc9c0\ubd84", None))
        self.edt_land_share_2.setText("")
        self.btn_parking_false.setText(QCoreApplication.translate("AddRoom", u"\ubd88\uac00\ub2a5", None))
        self.name_parking_1.setText(QCoreApplication.translate("AddRoom", u"\uc8fc\ucc28 \uc5ec\ubd80", None))
        self.btn_parking_true.setText(QCoreApplication.translate("AddRoom", u"\uac00 \ub2a5", None))
        self.edt_parking.setText("")
        self.hint_parking.setText(QCoreApplication.translate("AddRoom", u"\ub300", None))
        self.name_parking_2.setText(QCoreApplication.translate("AddRoom", u"\uc8fc\ucc28 \ub300\uc218", None))
        self.edt_household.setText("")
        self.name_household.setText(QCoreApplication.translate("AddRoom", u"\uc138\ub300\uc218(\uac00\uad6c)", None))
        self.hint_crt_floor.setText(QCoreApplication.translate("AddRoom", u"\uce35", None))
        self.edt_crt_floor.setText("")
        self.name_crt_floor.setText(QCoreApplication.translate("AddRoom", u"\ud574\ub2f9 \uce35", None))
        self.hint_total_floor.setText(QCoreApplication.translate("AddRoom", u"\uce35", None))
        self.name_total_floor.setText(QCoreApplication.translate("AddRoom", u"\ucd1d \uce35", None))
        self.edt_total_floor.setText("")
        self.hint_supply_area.setText(QCoreApplication.translate("AddRoom", u"\u33a1", None))
        self.edt_supply_area.setText("")
        self.name_supply_area.setText(QCoreApplication.translate("AddRoom", u"\uacf5\uae09\uba74\uc801", None))
        self.hint_area.setText(QCoreApplication.translate("AddRoom", u"\u33a1", None))
        self.edt_area.setText("")
        self.name_area.setText(QCoreApplication.translate("AddRoom", u"\uc804\uc6a9\uba74\uc801", None))
        self.hint_day_3.setText(QCoreApplication.translate("AddRoom", u"\uc77c", None))
        self.edt_day_3.setText("")
        self.edt_day_2.setText("")
        self.hint_day_1.setText(QCoreApplication.translate("AddRoom", u"\ub144", None))
        self.cbx_day.setItemText(0, QCoreApplication.translate("AddRoom", u"\uc0ac\uc6a9\uc2b9\uc778\uc77c", None))
        self.cbx_day.setItemText(1, QCoreApplication.translate("AddRoom", u"\uc0ac\uc6a9\uac80\uc0ac\uc77c", None))
        self.cbx_day.setItemText(2, QCoreApplication.translate("AddRoom", u"\uc900\uacf5\uc778\uac00\uc77c", None))

        self.hint_day_2.setText(QCoreApplication.translate("AddRoom", u"\uc6d4", None))
        self.edt_day_1.setText("")
        self.name_day.setText(QCoreApplication.translate("AddRoom", u"\uac74\ucd95\ubb3c \uc77c\uc790", None))
        self.edt_purpose.setText("")
        self.name_purpose.setText(QCoreApplication.translate("AddRoom", u"\uac74\ucd95\ubb3c \uc6a9\ub3c4", None))
        self.cbx_purpose.setItemText(0, QCoreApplication.translate("AddRoom", u"\ub2e8\ub3c5\uc8fc\ud0dd", None))
        self.cbx_purpose.setItemText(1, QCoreApplication.translate("AddRoom", u"\uacf5\ub3d9\uc8fc\ud0dd", None))
        self.cbx_purpose.setItemText(2, QCoreApplication.translate("AddRoom", u"\uc81c1\uc885 \uadfc\ub9b0\uc0dd\ud65c\uc2dc\uc124", None))
        self.cbx_purpose.setItemText(3, QCoreApplication.translate("AddRoom", u"\uc81c2\uc885 \uadfc\ub9b0\uc0dd\ud65c\uc2dc\uc124", None))
        self.cbx_purpose.setItemText(4, QCoreApplication.translate("AddRoom", u"\uc5c5\ubb34\uc2dc\uc124", None))
        self.cbx_purpose.setItemText(5, QCoreApplication.translate("AddRoom", u"( \uc9c1\uc811\uc785\ub825 )", None))

        self.name_explanation.setText(QCoreApplication.translate("AddRoom", u"\ub9e4\ubb3c\ud2b9\uc9d5", None))
        self.name_in_date.setText(QCoreApplication.translate("AddRoom", u"\uc785\uc8fc\ub0a0\uc9dc", None))
        self.edt_in_date_1.setText("")
        self.edt_explanation.setText("")
        self.edt_in_date_2.setText("")
        self.edt_in_date_3.setText("")
        self.hint_in_date_1.setText(QCoreApplication.translate("AddRoom", u"\ub144", None))
        self.hint_in_date_2.setText(QCoreApplication.translate("AddRoom", u"\uc6d4", None))
        self.label_43.setText(QCoreApplication.translate("AddRoom", u"\uc77c", None))
        self.rbtn_in_date_1.setText(QCoreApplication.translate("AddRoom", u"\uc989\uc2dc\uc785\uc8fc", None))
        self.rbtn_in_date_2.setText("")
        self.ckb_in_date.setText(QCoreApplication.translate("AddRoom", u"\ud611\uc758\uac00\ub2a5", None))
        self.edt_relationship.setText("")
        self.edt_owner.setText("")
        self.name_relationship.setText(QCoreApplication.translate("AddRoom", u"\uad00\uacc4", None))
        self.name_owner.setText(QCoreApplication.translate("AddRoom", u"\uc18c\uc720\uc790\uba85", None))
        self.cbx_relationship.setItemText(0, QCoreApplication.translate("AddRoom", u"\ubcf8\uc778", None))
        self.cbx_relationship.setItemText(1, QCoreApplication.translate("AddRoom", u"\uc9c1\uc6d0", None))
        self.cbx_relationship.setItemText(2, QCoreApplication.translate("AddRoom", u"\ub300\ud45c", None))
        self.cbx_relationship.setItemText(3, QCoreApplication.translate("AddRoom", u"\uc138\uc785\uc790", None))
        self.cbx_relationship.setItemText(4, QCoreApplication.translate("AddRoom", u"( \uc9c1\uc811\uc785\ub825 )", None))

        self.name_client_1.setText(QCoreApplication.translate("AddRoom", u"\uc758\ub8b0\uc778 1", None))
        self.edt_client_1.setText("")
        self.name_client_num_1.setText(QCoreApplication.translate("AddRoom", u"\uc5f0\ub77d\ucc98 1", None))
        self.edt_client_num_1.setText("")
        self.edt_client_num_2.setText("")
        self.edt_client_2.setText("")
        self.name_client_num_2.setText(QCoreApplication.translate("AddRoom", u"\uc5f0\ub77d\ucc98 2", None))
        self.name_client_2.setText(QCoreApplication.translate("AddRoom", u"\uc758\ub8b0\uc778 2", None))
        self.name_memo.setText(QCoreApplication.translate("AddRoom", u"\ube44\uacf5\uac1c \uba54\ubaa8", None))
        self.edt_memo.setText("")
        self.cbx_client_1.setItemText(0, QCoreApplication.translate("AddRoom", u"\uc9d1\uc8fc\uc778", None))
        self.cbx_client_1.setItemText(1, QCoreApplication.translate("AddRoom", u"\uc138\uc785\uc790", None))
        self.cbx_client_1.setItemText(2, QCoreApplication.translate("AddRoom", u"\uae30\ud0c0", None))

        self.cbx_client_2.setItemText(0, QCoreApplication.translate("AddRoom", u"\uc9d1\uc8fc\uc778", None))
        self.cbx_client_2.setItemText(1, QCoreApplication.translate("AddRoom", u"\uc138\uc785\uc790", None))
        self.cbx_client_2.setItemText(2, QCoreApplication.translate("AddRoom", u"\uae30\ud0c0", None))

        self.btn_back.setText(QCoreApplication.translate("AddRoom", u"\uc774 \uc804", None))
    # retranslateUi

