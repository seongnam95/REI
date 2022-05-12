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
        AddRoom.resize(641, 611)
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
"}\n"
"\n"
"QCheckBox:c"
                        "hecked {\n"
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
        self.name_1 = QLabel(self.address_frame)
        self.name_1.setObjectName(u"name_1")
        self.name_1.setGeometry(QRect(30, 80, 61, 30))
        self.cbx_type = QComboBox(self.address_frame)
        self.cbx_type.addItem("")
        self.cbx_type.addItem("")
        self.cbx_type.addItem("")
        self.cbx_type.setObjectName(u"cbx_type")
        self.cbx_type.setGeometry(QRect(110, 80, 81, 30))
        self.name_3 = QLabel(self.address_frame)
        self.name_3.setObjectName(u"name_3")
        self.name_3.setGeometry(QRect(230, 80, 61, 30))
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
        self.stackedWidget.setGeometry(QRect(10, 160, 621, 341))
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
        self.name_price = QLabel(self.money_frame)
        self.name_price.setObjectName(u"name_price")
        self.name_price.setGeometry(QRect(30, 20, 61, 30))
        self.edt_price = QLineEdit(self.money_frame)
        self.edt_price.setObjectName(u"edt_price")
        self.edt_price.setGeometry(QRect(120, 20, 151, 30))
        self.edt_price.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.name_admin_cost = QLabel(self.money_frame)
        self.name_admin_cost.setObjectName(u"name_admin_cost")
        self.name_admin_cost.setGeometry(QRect(30, 60, 61, 30))
        self.edt_admin_cost = QLineEdit(self.money_frame)
        self.edt_admin_cost.setObjectName(u"edt_admin_cost")
        self.edt_admin_cost.setGeometry(QRect(120, 60, 151, 30))
        self.edt_admin_cost.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ckb_cost_in_1 = QCheckBox(self.money_frame)
        self.ckb_cost_in_1.setObjectName(u"ckb_cost_in_1")
        self.ckb_cost_in_1.setGeometry(QRect(170, 110, 61, 30))
        self.ckb_cost_in_2 = QCheckBox(self.money_frame)
        self.ckb_cost_in_2.setObjectName(u"ckb_cost_in_2")
        self.ckb_cost_in_2.setGeometry(QRect(260, 110, 61, 30))
        self.ckb_cost_in_3 = QCheckBox(self.money_frame)
        self.ckb_cost_in_3.setObjectName(u"ckb_cost_in_3")
        self.ckb_cost_in_3.setGeometry(QRect(340, 110, 61, 30))
        self.ckb_cost_in_4 = QCheckBox(self.money_frame)
        self.ckb_cost_in_4.setObjectName(u"ckb_cost_in_4")
        self.ckb_cost_in_4.setGeometry(QRect(420, 110, 61, 30))
        self.ckb_cost_in_5 = QCheckBox(self.money_frame)
        self.ckb_cost_in_5.setObjectName(u"ckb_cost_in_5")
        self.ckb_cost_in_5.setGeometry(QRect(510, 110, 41, 30))
        self.name_cost_in = QLabel(self.money_frame)
        self.name_cost_in.setObjectName(u"name_cost_in")
        self.name_cost_in.setGeometry(QRect(30, 110, 101, 30))
        self.hint = QLabel(self.money_frame)
        self.hint.setObjectName(u"hint")
        self.hint.setGeometry(QRect(238, 20, 31, 30))
        self.hint.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.label_14 = QLabel(self.money_frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(250, 60, 21, 30))
        self.label_14.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.frame = QFrame(self.money_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(330, 20, 241, 31))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.name_edt_deposit = QLabel(self.frame)
        self.name_edt_deposit.setObjectName(u"name_edt_deposit")
        self.name_edt_deposit.setGeometry(QRect(0, 0, 61, 30))
        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(208, 0, 31, 30))
        self.label_15.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.edt_deposit = QLineEdit(self.frame)
        self.edt_deposit.setObjectName(u"edt_deposit")
        self.edt_deposit.setGeometry(QRect(90, 0, 151, 30))
        self.edt_deposit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.edt_deposit.raise_()
        self.name_edt_deposit.raise_()
        self.label_15.raise_()
        self.frame_2 = QFrame(self.money_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(330, 60, 241, 31))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.name_loan = QLabel(self.frame_2)
        self.name_loan.setObjectName(u"name_loan")
        self.name_loan.setGeometry(QRect(0, 0, 61, 30))
        self.edt_loan = QLineEdit(self.frame_2)
        self.edt_loan.setObjectName(u"edt_loan")
        self.edt_loan.setGeometry(QRect(90, 0, 151, 30))
        self.edt_loan.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_16 = QLabel(self.frame_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(208, 0, 31, 30))
        self.label_16.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.info_frame = QFrame(self.page_1)
        self.info_frame.setObjectName(u"info_frame")
        self.info_frame.setGeometry(QRect(10, 180, 601, 151))
        self.info_frame.setFrameShape(QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.name_room_num = QLabel(self.info_frame)
        self.name_room_num.setObjectName(u"name_room_num")
        self.name_room_num.setGeometry(QRect(30, 20, 61, 30))
        self.edt_room_num = QLineEdit(self.info_frame)
        self.edt_room_num.setObjectName(u"edt_room_num")
        self.edt_room_num.setGeometry(QRect(120, 20, 151, 30))
        self.edt_room_num.setEchoMode(QLineEdit.Normal)
        self.edt_room_num.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.name_bathroom = QLabel(self.info_frame)
        self.name_bathroom.setObjectName(u"name_bathroom")
        self.name_bathroom.setGeometry(QRect(330, 20, 61, 30))
        self.edt_bathroom = QLineEdit(self.info_frame)
        self.edt_bathroom.setObjectName(u"edt_bathroom")
        self.edt_bathroom.setGeometry(QRect(420, 20, 151, 30))
        self.edt_bathroom.setEchoMode(QLineEdit.Normal)
        self.edt_bathroom.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.name_heating = QLabel(self.info_frame)
        self.name_heating.setObjectName(u"name_heating")
        self.name_heating.setGeometry(QRect(30, 60, 61, 30))
        self.name_fuel = QLabel(self.info_frame)
        self.name_fuel.setObjectName(u"name_fuel")
        self.name_fuel.setGeometry(QRect(30, 100, 61, 30))
        self.name_direction = QLabel(self.info_frame)
        self.name_direction.setObjectName(u"name_direction")
        self.name_direction.setGeometry(QRect(330, 60, 61, 30))
        self.cbx_direction_1 = QComboBox(self.info_frame)
        self.cbx_direction_1.addItem("")
        self.cbx_direction_1.addItem("")
        self.cbx_direction_1.setObjectName(u"cbx_direction_1")
        self.cbx_direction_1.setGeometry(QRect(420, 60, 62, 30))
        self.cbx_direction_2 = QComboBox(self.info_frame)
        self.cbx_direction_2.addItem("")
        self.cbx_direction_2.addItem("")
        self.cbx_direction_2.addItem("")
        self.cbx_direction_2.addItem("")
        self.cbx_direction_2.addItem("")
        self.cbx_direction_2.addItem("")
        self.cbx_direction_2.addItem("")
        self.cbx_direction_2.addItem("")
        self.cbx_direction_2.setObjectName(u"cbx_direction_2")
        self.cbx_direction_2.setGeometry(QRect(490, 60, 81, 30))
        self.cbx_heating = QComboBox(self.info_frame)
        self.cbx_heating.addItem("")
        self.cbx_heating.addItem("")
        self.cbx_heating.addItem("")
        self.cbx_heating.setObjectName(u"cbx_heating")
        self.cbx_heating.setGeometry(QRect(120, 60, 151, 30))
        self.cbx_fuel = QComboBox(self.info_frame)
        self.cbx_fuel.addItem("")
        self.cbx_fuel.addItem("")
        self.cbx_fuel.addItem("")
        self.cbx_fuel.addItem("")
        self.cbx_fuel.addItem("")
        self.cbx_fuel.addItem("")
        self.cbx_fuel.addItem("")
        self.cbx_fuel.addItem("")
        self.cbx_fuel.setObjectName(u"cbx_fuel")
        self.cbx_fuel.setGeometry(QRect(120, 100, 151, 30))
        self.label_17 = QLabel(self.info_frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(250, 20, 21, 30))
        self.label_17.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.label_18 = QLabel(self.info_frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(550, 20, 21, 30))
        self.label_18.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.name_options = QLabel(self.info_frame)
        self.name_options.setObjectName(u"name_options")
        self.name_options.setGeometry(QRect(330, 100, 61, 30))
        self.btn_options = QPushButton(self.info_frame)
        self.btn_options.setObjectName(u"btn_options")
        self.btn_options.setGeometry(QRect(420, 100, 151, 31))
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
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.building_frame = QFrame(self.page_2)
        self.building_frame.setObjectName(u"building_frame")
        self.building_frame.setGeometry(QRect(10, 10, 601, 191))
        self.building_frame.setFrameShape(QFrame.StyledPanel)
        self.building_frame.setFrameShadow(QFrame.Raised)
        self.name_supply_area = QLabel(self.building_frame)
        self.name_supply_area.setObjectName(u"name_supply_area")
        self.name_supply_area.setGeometry(QRect(30, 20, 61, 30))
        self.edt_supply_area = QLineEdit(self.building_frame)
        self.edt_supply_area.setObjectName(u"edt_supply_area")
        self.edt_supply_area.setGeometry(QRect(120, 20, 151, 30))
        self.edt_supply_area.setEchoMode(QLineEdit.Normal)
        self.edt_supply_area.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_20 = QLabel(self.building_frame)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(330, 20, 61, 30))
        self.lineEdit_10 = QLineEdit(self.building_frame)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(420, 20, 151, 30))
        self.lineEdit_10.setEchoMode(QLineEdit.Normal)
        self.lineEdit_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.name_area = QLabel(self.building_frame)
        self.name_area.setObjectName(u"name_area")
        self.name_area.setGeometry(QRect(30, 60, 71, 30))
        self.label_24 = QLabel(self.building_frame)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(250, 20, 21, 30))
        self.label_24.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.label_25 = QLabel(self.building_frame)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(550, 20, 21, 30))
        self.label_25.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.label_26 = QLabel(self.building_frame)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(250, 60, 21, 30))
        self.label_26.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.edt_area = QLineEdit(self.building_frame)
        self.edt_area.setObjectName(u"edt_area")
        self.edt_area.setGeometry(QRect(120, 60, 151, 30))
        self.edt_area.setEchoMode(QLineEdit.Normal)
        self.edt_area.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_28 = QLabel(self.building_frame)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(550, 60, 21, 30))
        self.label_28.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.lineEdit_12 = QLineEdit(self.building_frame)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setGeometry(QRect(420, 60, 151, 30))
        self.lineEdit_12.setEchoMode(QLineEdit.Normal)
        self.lineEdit_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_23 = QLabel(self.building_frame)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(330, 60, 61, 30))
        self.label_31 = QLabel(self.building_frame)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(30, 100, 81, 30))
        self.parking_frame = QFrame(self.building_frame)
        self.parking_frame.setObjectName(u"parking_frame")
        self.parking_frame.setGeometry(QRect(30, 140, 241, 31))
        self.parking_frame.setFrameShape(QFrame.StyledPanel)
        self.parking_frame.setFrameShadow(QFrame.Raised)
        self.edt_parking = QLineEdit(self.parking_frame)
        self.edt_parking.setObjectName(u"edt_parking")
        self.edt_parking.setGeometry(QRect(90, 0, 151, 30))
        self.edt_parking.setEchoMode(QLineEdit.Normal)
        self.edt_parking.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_30 = QLabel(self.parking_frame)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(220, 0, 21, 30))
        self.label_30.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.name_parking = QLabel(self.parking_frame)
        self.name_parking.setObjectName(u"name_parking")
        self.name_parking.setGeometry(QRect(0, 0, 61, 30))
        self.pushButton_6 = QPushButton(self.building_frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(120, 100, 71, 30))
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton_6.setCheckable(True)
        self.pushButton_7 = QPushButton(self.building_frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(200, 100, 71, 30))
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setChecked(True)
        self.name_household = QLabel(self.building_frame)
        self.name_household.setObjectName(u"name_household")
        self.name_household.setGeometry(QRect(330, 100, 81, 30))
        self.edt_household = QLineEdit(self.building_frame)
        self.edt_household.setObjectName(u"edt_household")
        self.edt_household.setGeometry(QRect(420, 100, 151, 30))
        self.edt_household.setStyleSheet(u"QLineEdit {\n"
"	padding-left: 0px;\n"
"	padding-right: 0px;\n"
"}")
        self.edt_household.setEchoMode(QLineEdit.Normal)
        self.edt_household.setAlignment(Qt.AlignCenter)
        self.land_frame = QFrame(self.building_frame)
        self.land_frame.setObjectName(u"land_frame")
        self.land_frame.setGeometry(QRect(330, 140, 241, 31))
        self.land_frame.setFrameShape(QFrame.StyledPanel)
        self.land_frame.setFrameShadow(QFrame.Raised)
        self.edt_land_share_1 = QLineEdit(self.land_frame)
        self.edt_land_share_1.setObjectName(u"edt_land_share_1")
        self.edt_land_share_1.setGeometry(QRect(90, 0, 61, 30))
        self.edt_land_share_1.setStyleSheet(u"QLineEdit {\n"
"	padding-left: 0px;\n"
"	padding-right: 0px;\n"
"}")
        self.edt_land_share_1.setEchoMode(QLineEdit.Normal)
        self.edt_land_share_1.setAlignment(Qt.AlignCenter)
        self.label_32 = QLabel(self.land_frame)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(156, 0, 31, 30))
        self.label_32.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.name_land_share = QLabel(self.land_frame)
        self.name_land_share.setObjectName(u"name_land_share")
        self.name_land_share.setGeometry(QRect(0, 0, 61, 30))
        self.edt_land_share_2 = QLineEdit(self.land_frame)
        self.edt_land_share_2.setObjectName(u"edt_land_share_2")
        self.edt_land_share_2.setGeometry(QRect(190, 0, 51, 30))
        self.edt_land_share_2.setStyleSheet(u"QLineEdit {\n"
"	padding-left: 0px;\n"
"	padding-right: 0px;\n"
"}")
        self.edt_land_share_2.setEchoMode(QLineEdit.Normal)
        self.edt_land_share_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_12.raise_()
        self.edt_area.raise_()
        self.name_supply_area.raise_()
        self.edt_supply_area.raise_()
        self.label_20.raise_()
        self.lineEdit_10.raise_()
        self.name_area.raise_()
        self.label_24.raise_()
        self.label_25.raise_()
        self.label_26.raise_()
        self.label_28.raise_()
        self.label_23.raise_()
        self.label_31.raise_()
        self.parking_frame.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.name_household.raise_()
        self.edt_household.raise_()
        self.land_frame.raise_()
        self.building_frame_2 = QFrame(self.page_2)
        self.building_frame_2.setObjectName(u"building_frame_2")
        self.building_frame_2.setGeometry(QRect(10, 220, 601, 111))
        self.building_frame_2.setFrameShape(QFrame.StyledPanel)
        self.building_frame_2.setFrameShadow(QFrame.Raised)
        self.name_day = QLabel(self.building_frame_2)
        self.name_day.setObjectName(u"name_day")
        self.name_day.setGeometry(QRect(30, 60, 71, 30))
        self.cbx_purpose = QComboBox(self.building_frame_2)
        self.cbx_purpose.addItem("")
        self.cbx_purpose.addItem("")
        self.cbx_purpose.addItem("")
        self.cbx_purpose.addItem("")
        self.cbx_purpose.addItem("")
        self.cbx_purpose.addItem("")
        self.cbx_purpose.setObjectName(u"cbx_purpose")
        self.cbx_purpose.setGeometry(QRect(120, 20, 161, 30))
        self.name_purpose = QLabel(self.building_frame_2)
        self.name_purpose.setObjectName(u"name_purpose")
        self.name_purpose.setGeometry(QRect(30, 20, 71, 30))
        self.cbx_day = QComboBox(self.building_frame_2)
        self.cbx_day.addItem("")
        self.cbx_day.addItem("")
        self.cbx_day.addItem("")
        self.cbx_day.setObjectName(u"cbx_day")
        self.cbx_day.setGeometry(QRect(120, 60, 161, 30))
        self.edt_day_1 = QLineEdit(self.building_frame_2)
        self.edt_day_1.setObjectName(u"edt_day_1")
        self.edt_day_1.setGeometry(QRect(298, 60, 71, 30))
        self.edt_day_1.setStyleSheet(u"QLineEdit {\n"
"	padding-left: 0px;\n"
"	padding-right: 0px;\n"
"}")
        self.edt_day_1.setEchoMode(QLineEdit.Normal)
        self.edt_day_1.setAlignment(Qt.AlignCenter)
        self.edt_purpose = QLineEdit(self.building_frame_2)
        self.edt_purpose.setObjectName(u"edt_purpose")
        self.edt_purpose.setGeometry(QRect(298, 20, 151, 30))
        self.edt_purpose.setStyleSheet(u"QLineEdit {\n"
"	padding-right: 22px;\n"
"}")
        self.edt_purpose.setEchoMode(QLineEdit.Normal)
        self.edt_purpose.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.edt_day_2 = QLineEdit(self.building_frame_2)
        self.edt_day_2.setObjectName(u"edt_day_2")
        self.edt_day_2.setGeometry(QRect(398, 60, 51, 30))
        self.edt_day_2.setStyleSheet(u"QLineEdit {\n"
"	padding-left: 0px;\n"
"	padding-right: 0px;\n"
"}")
        self.edt_day_2.setEchoMode(QLineEdit.Normal)
        self.edt_day_2.setAlignment(Qt.AlignCenter)
        self.edt_day_3 = QLineEdit(self.building_frame_2)
        self.edt_day_3.setObjectName(u"edt_day_3")
        self.edt_day_3.setGeometry(QRect(478, 60, 51, 30))
        self.edt_day_3.setStyleSheet(u"QLineEdit {\n"
"	padding-left: 0px;\n"
"	padding-right: 0px;\n"
"}")
        self.edt_day_3.setEchoMode(QLineEdit.Normal)
        self.edt_day_3.setAlignment(Qt.AlignCenter)
        self.label_34 = QLabel(self.building_frame_2)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(370, 60, 21, 30))
        self.label_34.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.label_37 = QLabel(self.building_frame_2)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(450, 60, 21, 30))
        self.label_37.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.label_38 = QLabel(self.building_frame_2)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(530, 60, 21, 30))
        self.label_38.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
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
        self.label_41 = QLabel(self.day_frame)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(303, 20, 21, 30))
        self.label_41.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(128,128,128);\n"
"	padding-top: 3px;\n"
"}")
        self.label_42 = QLabel(self.day_frame)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(383, 20, 21, 30))
        self.label_42.setStyleSheet(u"QLabel {\n"
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
        QWidget.setTabOrder(self.edt_admin_cost, self.edt_deposit)
        QWidget.setTabOrder(self.edt_deposit, self.edt_loan)
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
        QWidget.setTabOrder(self.edt_area, self.pushButton_6)
        QWidget.setTabOrder(self.pushButton_6, self.pushButton_7)
        QWidget.setTabOrder(self.pushButton_7, self.edt_parking)
        QWidget.setTabOrder(self.edt_parking, self.lineEdit_10)
        QWidget.setTabOrder(self.lineEdit_10, self.lineEdit_12)
        QWidget.setTabOrder(self.lineEdit_12, self.edt_household)
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
        self.name_1.setText(QCoreApplication.translate("AddRoom", u"\uac70\ub798\uc720\ud615", None))
        self.cbx_type.setItemText(0, QCoreApplication.translate("AddRoom", u"\ub9e4\ub9e4", None))
        self.cbx_type.setItemText(1, QCoreApplication.translate("AddRoom", u"\uc804\uc138", None))
        self.cbx_type.setItemText(2, QCoreApplication.translate("AddRoom", u"\uc6d4\uc138", None))

        self.name_3.setText(QCoreApplication.translate("AddRoom", u"\ub9e4\ubb3c\uc885\ub958", None))
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
        self.name_price.setText(QCoreApplication.translate("AddRoom", u"\ub9e4\ub9e4\uac00", None))
        self.edt_price.setText("")
        self.name_admin_cost.setText(QCoreApplication.translate("AddRoom", u"\uad00\ub9ac\ube44", None))
        self.edt_admin_cost.setText("")
        self.ckb_cost_in_1.setText(QCoreApplication.translate("AddRoom", u"\uc804\uae30\uc138", None))
        self.ckb_cost_in_2.setText(QCoreApplication.translate("AddRoom", u"\uac00\uc2a4", None))
        self.ckb_cost_in_3.setText(QCoreApplication.translate("AddRoom", u"\uc218\ub3c4", None))
        self.ckb_cost_in_4.setText(QCoreApplication.translate("AddRoom", u"\uc778\ud130\ub137", None))
        self.ckb_cost_in_5.setText(QCoreApplication.translate("AddRoom", u"TV", None))
        self.name_cost_in.setText(QCoreApplication.translate("AddRoom", u"\uad00\ub9ac\ube44 \ud3ec\ud568 \ud56d\ubaa9", None))
        self.hint.setText(QCoreApplication.translate("AddRoom", u"\ub9cc\uc6d0", None))
        self.label_14.setText(QCoreApplication.translate("AddRoom", u"\uc6d0", None))
        self.name_edt_deposit.setText(QCoreApplication.translate("AddRoom", u"\uae30\ubcf4\uc99d\uae08", None))
        self.label_15.setText(QCoreApplication.translate("AddRoom", u"\ub9cc\uc6d0", None))
        self.edt_deposit.setText("")
        self.name_loan.setText(QCoreApplication.translate("AddRoom", u"\uc735\uc790\uae08", None))
        self.edt_loan.setText("")
        self.label_16.setText(QCoreApplication.translate("AddRoom", u"\ub9cc\uc6d0", None))
        self.name_room_num.setText(QCoreApplication.translate("AddRoom", u"\ubc29 \uac1c\uc218", None))
        self.edt_room_num.setText("")
        self.name_bathroom.setText(QCoreApplication.translate("AddRoom", u"\uc695\uc2e4 \uac1c\uc218", None))
        self.edt_bathroom.setText("")
        self.name_heating.setText(QCoreApplication.translate("AddRoom", u"\ub09c\ubc29\uc815\ubcf4", None))
        self.name_fuel.setText(QCoreApplication.translate("AddRoom", u"\ub09c\ubc29\uc5f0\ub8cc", None))
        self.name_direction.setText(QCoreApplication.translate("AddRoom", u"\ubc29\ud5a5", None))
        self.cbx_direction_1.setItemText(0, QCoreApplication.translate("AddRoom", u"\uac70\uc2e4", None))
        self.cbx_direction_1.setItemText(1, QCoreApplication.translate("AddRoom", u"\uc548\ubc29", None))

        self.cbx_direction_2.setItemText(0, QCoreApplication.translate("AddRoom", u"\ub3d9\ud5a5", None))
        self.cbx_direction_2.setItemText(1, QCoreApplication.translate("AddRoom", u"\uc11c\ud5a5", None))
        self.cbx_direction_2.setItemText(2, QCoreApplication.translate("AddRoom", u"\ub0a8\ud5a5", None))
        self.cbx_direction_2.setItemText(3, QCoreApplication.translate("AddRoom", u"\ubd81\ud5a5", None))
        self.cbx_direction_2.setItemText(4, QCoreApplication.translate("AddRoom", u"\ub0a8\ub3d9\ud5a5", None))
        self.cbx_direction_2.setItemText(5, QCoreApplication.translate("AddRoom", u"\ub0a8\uc11c\ud5a5", None))
        self.cbx_direction_2.setItemText(6, QCoreApplication.translate("AddRoom", u"\ubd81\ub3d9\ud5a5", None))
        self.cbx_direction_2.setItemText(7, QCoreApplication.translate("AddRoom", u"\ubd81\uc11c\ud5a5", None))

        self.cbx_heating.setItemText(0, QCoreApplication.translate("AddRoom", u"\uac1c\ubcc4\ub09c\ubc29", None))
        self.cbx_heating.setItemText(1, QCoreApplication.translate("AddRoom", u"\uc9c0\uc5ed\ub09c\ubc29", None))
        self.cbx_heating.setItemText(2, QCoreApplication.translate("AddRoom", u"\uc911\uc559\ub09c\ubc29", None))

        self.cbx_fuel.setItemText(0, QCoreApplication.translate("AddRoom", u"\ub3c4\uc2dc\uac00\uc2a4", None))
        self.cbx_fuel.setItemText(1, QCoreApplication.translate("AddRoom", u"\uc804\uae30", None))
        self.cbx_fuel.setItemText(2, QCoreApplication.translate("AddRoom", u"\uc2ec\uc57c\uc804\uae30", None))
        self.cbx_fuel.setItemText(3, QCoreApplication.translate("AddRoom", u"\uae30\ub984", None))
        self.cbx_fuel.setItemText(4, QCoreApplication.translate("AddRoom", u"LPG", None))
        self.cbx_fuel.setItemText(5, QCoreApplication.translate("AddRoom", u"\ud0dc\uc591\uc5f4", None))
        self.cbx_fuel.setItemText(6, QCoreApplication.translate("AddRoom", u"\uc9c0\uc5f4", None))
        self.cbx_fuel.setItemText(7, QCoreApplication.translate("AddRoom", u"\uc5f4\ubcd1\ud569", None))

        self.label_17.setText(QCoreApplication.translate("AddRoom", u"\uac1c", None))
        self.label_18.setText(QCoreApplication.translate("AddRoom", u"\uac1c", None))
        self.name_options.setText(QCoreApplication.translate("AddRoom", u"\uc2dc\uc124\uc815\ubcf4", None))
        self.btn_options.setText(QCoreApplication.translate("AddRoom", u"\uc635\uc158 \uc120\ud0dd", None))
        self.name_supply_area.setText(QCoreApplication.translate("AddRoom", u"\uacf5\uae09\uba74\uc801", None))
        self.edt_supply_area.setText("")
        self.label_20.setText(QCoreApplication.translate("AddRoom", u"\ucd1d \uce35", None))
        self.lineEdit_10.setText("")
        self.name_area.setText(QCoreApplication.translate("AddRoom", u"\uc804\uc6a9\uba74\uc801", None))
        self.label_24.setText(QCoreApplication.translate("AddRoom", u"\u33a1", None))
        self.label_25.setText(QCoreApplication.translate("AddRoom", u"\uce35", None))
        self.label_26.setText(QCoreApplication.translate("AddRoom", u"\u33a1", None))
        self.edt_area.setText("")
        self.label_28.setText(QCoreApplication.translate("AddRoom", u"\uce35", None))
        self.lineEdit_12.setText("")
        self.label_23.setText(QCoreApplication.translate("AddRoom", u"\ud574\ub2f9 \uce35", None))
        self.label_31.setText(QCoreApplication.translate("AddRoom", u"\uc8fc\ucc28 \uc5ec\ubd80", None))
        self.edt_parking.setText("")
        self.label_30.setText(QCoreApplication.translate("AddRoom", u"\ub300", None))
        self.name_parking.setText(QCoreApplication.translate("AddRoom", u"\uc8fc\ucc28 \ub300\uc218", None))
        self.pushButton_6.setText(QCoreApplication.translate("AddRoom", u"\uac00 \ub2a5", None))
        self.pushButton_7.setText(QCoreApplication.translate("AddRoom", u"\ubd88\uac00\ub2a5", None))
        self.name_household.setText(QCoreApplication.translate("AddRoom", u"\uc138\ub300\uc218(\uac00\uad6c)", None))
        self.edt_household.setText("")
        self.edt_land_share_1.setText("")
        self.label_32.setText(QCoreApplication.translate("AddRoom", u"\ubd84\uc758", None))
        self.name_land_share.setText(QCoreApplication.translate("AddRoom", u"\ub300\uc9c0 \uc9c0\ubd84", None))
        self.edt_land_share_2.setText("")
        self.name_day.setText(QCoreApplication.translate("AddRoom", u"\uac74\ucd95\ubb3c \uc77c\uc790", None))
        self.cbx_purpose.setItemText(0, QCoreApplication.translate("AddRoom", u"\ub2e8\ub3c5\uc8fc\ud0dd", None))
        self.cbx_purpose.setItemText(1, QCoreApplication.translate("AddRoom", u"\uacf5\ub3d9\uc8fc\ud0dd", None))
        self.cbx_purpose.setItemText(2, QCoreApplication.translate("AddRoom", u"\uc81c1\uc885 \uadfc\ub9b0\uc0dd\ud65c\uc2dc\uc124", None))
        self.cbx_purpose.setItemText(3, QCoreApplication.translate("AddRoom", u"\uc81c2\uc885 \uadfc\ub9b0\uc0dd\ud65c\uc2dc\uc124", None))
        self.cbx_purpose.setItemText(4, QCoreApplication.translate("AddRoom", u"\uc5c5\ubb34\uc2dc\uc124", None))
        self.cbx_purpose.setItemText(5, QCoreApplication.translate("AddRoom", u"( \uc9c1\uc811\uc785\ub825 )", None))

        self.name_purpose.setText(QCoreApplication.translate("AddRoom", u"\uac74\ucd95\ubb3c \uc6a9\ub3c4", None))
        self.cbx_day.setItemText(0, QCoreApplication.translate("AddRoom", u"\uc0ac\uc6a9\uc2b9\uc778\uc77c", None))
        self.cbx_day.setItemText(1, QCoreApplication.translate("AddRoom", u"\uc0ac\uc6a9\uac80\uc0ac\uc77c", None))
        self.cbx_day.setItemText(2, QCoreApplication.translate("AddRoom", u"\uc900\uacf5\uc778\uac00\uc77c", None))

        self.edt_day_1.setText("")
        self.edt_purpose.setText("")
        self.edt_day_2.setText("")
        self.edt_day_3.setText("")
        self.label_34.setText(QCoreApplication.translate("AddRoom", u"\ub144", None))
        self.label_37.setText(QCoreApplication.translate("AddRoom", u"\uc6d4", None))
        self.label_38.setText(QCoreApplication.translate("AddRoom", u"\uc77c", None))
        self.name_explanation.setText(QCoreApplication.translate("AddRoom", u"\ub9e4\ubb3c\ud2b9\uc9d5", None))
        self.name_in_date.setText(QCoreApplication.translate("AddRoom", u"\uc785\uc8fc\ub0a0\uc9dc", None))
        self.edt_in_date_1.setText("")
        self.edt_explanation.setText("")
        self.edt_in_date_2.setText("")
        self.edt_in_date_3.setText("")
        self.label_41.setText(QCoreApplication.translate("AddRoom", u"\ub144", None))
        self.label_42.setText(QCoreApplication.translate("AddRoom", u"\uc6d4", None))
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

