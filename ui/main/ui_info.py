# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info_ui.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_BuildingInfo(object):
    def _setupUi(self, BuildingInfo):
        if not BuildingInfo.objectName():
            BuildingInfo.setObjectName(u"BuildingInfo")
        BuildingInfo.resize(470, 801)
        BuildingInfo.setMinimumSize(QSize(470, 801))
        BuildingInfo.setMaximumSize(QSize(470, 801))
        BuildingInfo.setStyleSheet(u"#BuildingInfo {\n"
"	background-color: white;\n"
"}\n"
"\n"
"QLabel {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(127, 140, 141);\n"
"}")
        self.lb_hint_2 = QLabel(BuildingInfo)
        self.lb_hint_2.setObjectName(u"lb_hint_2")
        self.lb_hint_2.setGeometry(QRect(20, 650, 431, 61))
        self.lb_hint_2.setStyleSheet(u"#lb_hint_2 {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	border-radius: 10px;\n"
"	padding-top: 3px;\n"
"	background-color: rgba(0, 0, 0, 40);\n"
"	color: rgb(80, 80, 80);\n"
"}")
        self.lb_hint_2.setAlignment(Qt.AlignCenter)
        self.top_bar = QWidget(BuildingInfo)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setGeometry(QRect(0, 0, 921, 61))
        self.top_bar.setStyleSheet(u"#top_bar {\n"
"	background-color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"	border-radius: 10px;\n"
"	padding-top: 2px;\n"
"	padding-left: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(245, 245, 245);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   padding-left: 4px;\n"
"   padding-top: 4px;\n"
"	background-color: rgb(225, 225, 225);\n"
"}")
        self.lb_title = QLabel(self.top_bar)
        self.lb_title.setObjectName(u"lb_title")
        self.lb_title.setGeometry(QRect(120, 5, 211, 30))
        self.lb_title.setStyleSheet(u"#lb_title {\n"
"	background-color: rgba(0,0,0,0);\n"
"	font: 25px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(125, 125, 125);\n"
"	padding-top: 8px;\n"
"	padding-left: 4px;\n"
"	border: 0px;\n"
"}")
        self.lb_title.setAlignment(Qt.AlignCenter)
        self.lb_sub_title = QLabel(self.top_bar)
        self.lb_sub_title.setObjectName(u"lb_sub_title")
        self.lb_sub_title.setGeometry(QRect(130, 30, 191, 24))
        self.lb_sub_title.setStyleSheet(u"#lb_sub_title {\n"
"	background-color: rgb(0,0,0,0);\n"
"	font: 15px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(125, 125, 125);\n"
"	padding-top: 8px;\n"
"	padding-left: 8px;\n"
"	border: 0px;\n"
"}")
        self.lb_sub_title.setAlignment(Qt.AlignCenter)
        self.btn_menu = QPushButton(self.top_bar)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setGeometry(QRect(410, 12, 40, 40))
        self.btn_menu.setStyleSheet(u"")
        self.btn_menu.raise_()

        self.lb_sub_title.raise_()
        self.lb_title.raise_()
        self.bot_bar = QWidget(BuildingInfo)
        self.bot_bar.setObjectName(u"bot_bar")
        self.bot_bar.setGeometry(QRect(0, 730, 921, 71))
        self.bot_bar.setStyleSheet(u"#bot_bar {\n"
"	background-color: rgb(245, 245, 245);\n"
"	border-top: 1px solid;\n"
"	border-color: rgb(230, 230, 230);\n"
"}")
        self.btn_viol = QPushButton(self.bot_bar)
        self.btn_viol.setObjectName(u"btn_viol")
        self.btn_viol.setGeometry(QRect(760, 20, 141, 31))
        self.btn_viol.setStyleSheet(u"QPushButton {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 15px;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(255, 120, 90);\n"
"	outline: noen;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(225, 64, 44);\n"
"	border-style: inset;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: rgb(166, 168, 171);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"E:/PyProject/Project/REI/building_info/image/bt_search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_viol.setIcon(icon1)
        self.btn_viol.setIconSize(QSize(23, 23))
        self.lb_viol = QLabel(self.bot_bar)
        self.lb_viol.setObjectName(u"lb_viol")
        self.lb_viol.setGeometry(QRect(650, 20, 91, 31))
        self.lb_viol.setStyleSheet(u"#lb_viol { background-color: rgb(245, 245, 245); }")
        self.lb_viol.setAlignment(Qt.AlignCenter)
        self.btn_details = QPushButton(self.bot_bar)
        self.btn_details.setObjectName(u"btn_details")
        self.btn_details.setGeometry(QRect(370, 20, 81, 31))
        self.btn_details.setStyleSheet(u"#btn_details {\n"
"	font: 15px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(125, 125, 125);\n"
"	border: none;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(245, 245, 245);\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"#btn_details::hover {\n"
"	color: rgb(155, 155, 155);\n"
"	border-style: inset;\n"
"}\n"
"\n"
"#btn_details:pressed {\n"
"	color: rgb(125, 125, 125);\n"
"   padding-left: 2px;\n"
"   padding-top: 4px;\n"
"	border-style: inset;\n"
"}\n"
"")
        self.btn_issuance = QPushButton(self.bot_bar)
        self.btn_issuance.setObjectName(u"btn_issuance")
        self.btn_issuance.setEnabled(True)
        self.btn_issuance.setGeometry(QRect(20, 16, 40, 40))
        self.btn_issuance.setStyleSheet(u"QPushButton {\n"
"	border-radius: 10px;\n"
"	padding-top: 2px;\n"
"	padding-left: 1px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(235, 235, 235);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"                  
"   padding-left: 3px;\n"
"   padding-top: 3px;\n"
"	background-color: rgb(215, 215, 215);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../../print.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_issuance.setIcon(icon2)
        self.btn_issuance.setIconSize(QSize(23, 23))
        self.address_frame = QFrame(BuildingInfo)
        self.address_frame.setObjectName(u"address_frame")
        self.address_frame.setGeometry(QRect(20, 80, 431, 141))
        self.address_frame.setStyleSheet(u"#address_frame {\n"
"	background-color: white;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 2px solid rgb(235,235,235);\n"
"    padding-top: 3px;\n"
"    padding-left: 10px;\n"
"    min-width: 6em;\n"
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
"    width: 30px;\n"
"\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
" "
                        "   image: url(../../data/img/system/down_arrow_icon.png);\n"
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
"}")
        self.address_frame.setFrameShape(QFrame.StyledPanel)
        self.address_frame.setFrameShadow(QFrame.Raised)
        self.lb_sub_title_1 = QLabel(self.address_frame)
        self.lb_sub_title_1.setObjectName(u"lb_sub_title_1")
        self.lb_sub_title_1.setGeometry(QRect(20, 15, 91, 16))
        self.lb_sub_title_1.setStyleSheet(u"#lb_sub_title_1 {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(123,123,123);\n"
"	border: none;\n"
"}")
        self.edt_address = QLineEdit(self.address_frame)
        self.edt_address.setObjectName(u"edt_address")
        self.edt_address.setEnabled(True)
        self.edt_address.setGeometry(QRect(20, 35, 391, 45))
        self.edt_address.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(125,125,125);\n"
"	font: 16px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"    border: 2px solid rgb(128,128,255);\n"
"    border-radius: 5px;\n"
"    padding-top: 3px;\n"
"    padding-left: 10px;\n"
"    padding-right: 55px;\n"
"}\n"
"    \n"
"QLineEdit:focus {\n"
"	color: rgb(65,65,65);\n"
"}")
        self.edt_address.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.cbx_rooms = QComboBox(self.address_frame)
        self.cbx_rooms.addItem("")
        self.cbx_rooms.setObjectName(u"cbx_rooms")
        self.cbx_rooms.setGeometry(QRect(20, 90, 391, 35))
        self.btn_search = QPushButton(self.address_frame)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setGeometry(QRect(359, 37, 50, 41))
        self.btn_search.setStyleSheet(u"#btn_search {\n"
"	background-color: white;\n"
"	border: none;\n"
"	outline: none;\n"
"	border-radius: 5px;\n"
"}")
        self.info_frame = QFrame(BuildingInfo)
        self.info_frame.setObjectName(u"info_frame")
        self.info_frame.setGeometry(QRect(20, 240, 431, 391))
        self.info_frame.setStyleSheet(u"#info_frame {\n"
"	background-color: white;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(67,67,67);\n"
"	padding-top: 4px;\n"
"}")
        self.info_frame.setFrameShape(QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.lb_hint_3 = QLabel(self.info_frame)
        self.lb_hint_3.setObjectName(u"lb_hint_3")
        self.lb_hint_3.setGeometry(QRect(81, 360, 261, 18))
        self.lb_hint_3.setStyleSheet(u"#lb_hint_3 {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(123,123,123);\n"
"	border: none;\n"
"}")
        self.lb_hint_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.base_name_7 = QLabel(self.info_frame)
        self.base_name_7.setObjectName(u"base_name_7")
        self.base_name_7.setGeometry(QRect(20, 221, 60, 26))
        self.base_name_7.setStyleSheet(u"")
        self.base_name_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.base_name_2 = QLabel(self.info_frame)
        self.base_name_2.setObjectName(u"base_name_2")
        self.base_name_2.setGeometry(QRect(20, 56, 60, 26))
        font = QFont()
        font.setFamilies([u"\uc6f0\ucef4\uccb4 Regular"])
        font.setBold(False)
        font.setItalic(False)
        self.base_name_2.setFont(font)
        self.base_name_2.setStyleSheet(u"")
        self.base_name_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.base_name_4 = QLabel(self.info_frame)
        self.base_name_4.setObjectName(u"base_name_4")
        self.base_name_4.setGeometry(QRect(20, 122, 60, 26))
        self.base_name_4.setFont(font)
        self.base_name_4.setStyleSheet(u"")
        self.base_name_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.base_name_1 = QLabel(self.info_frame)
        self.base_name_1.setObjectName(u"base_name_1")
        self.base_name_1.setGeometry(QRect(20, 23, 80, 26))
        self.base_name_1.setFont(font)
        self.base_name_1.setStyleSheet(u"")
        self.base_name_1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.base_name_5 = QLabel(self.info_frame)
        self.base_name_5.setObjectName(u"base_name_5")
        self.base_name_5.setGeometry(QRect(20, 155, 60, 26))
        self.base_name_5.setStyleSheet(u"")
        self.base_name_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.base_name_3 = QLabel(self.info_frame)
        self.base_name_3.setObjectName(u"base_name_3")
        self.base_name_3.setGeometry(QRect(20, 89, 60, 26))
        self.base_name_3.setFont(font)
        self.base_name_3.setStyleSheet(u"")
        self.base_name_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.base_name_6 = QLabel(self.info_frame)
        self.base_name_6.setObjectName(u"base_name_6")
        self.base_name_6.setGeometry(QRect(20, 188, 60, 26))
        self.base_name_6.setStyleSheet(u"")
        self.base_name_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.base_name_13 = QLabel(self.info_frame)
        self.base_name_13.setObjectName(u"base_name_13")
        self.base_name_13.setGeometry(QRect(20, 320, 90, 26))
        self.base_name_13.setStyleSheet(u"")
        self.base_name_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.base_name_12 = QLabel(self.info_frame)
        self.base_name_12.setObjectName(u"base_name_12")
        self.base_name_12.setGeometry(QRect(20, 287, 90, 26))
        self.base_name_12.setStyleSheet(u"")
        self.base_name_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.base_name_11 = QLabel(self.info_frame)
        self.base_name_11.setObjectName(u"base_name_11")
        self.base_name_11.setGeometry(QRect(20, 254, 90, 26))
        self.base_name_11.setStyleSheet(u"")
        self.base_name_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.base_item_7 = QLabel(self.info_frame)
        self.base_item_7.setObjectName(u"base_item_7")
        self.base_item_7.setGeometry(QRect(110, 220, 101, 28))
        self.base_item_7.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(240, 240, 240); \n"
"	border-radius: 5px;\n"
"}")
        self.base_item_7.setAlignment(Qt.AlignCenter)
        self.base_item_3 = QLabel(self.info_frame)
        self.base_item_3.setObjectName(u"base_item_3")
        self.base_item_3.setGeometry(QRect(110, 88, 301, 28))
        self.base_item_3.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(240, 240, 240); \n"
"	border-radius: 5px;\n"
"}")
        self.base_item_3.setAlignment(Qt.AlignCenter)
        self.base_item_4 = QLabel(self.info_frame)
        self.base_item_4.setObjectName(u"base_item_4")
        self.base_item_4.setGeometry(QRect(110, 121, 301, 28))
        self.base_item_4.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(240, 240, 240); \n"
"	border-radius: 5px;\n"
"}")
        self.base_item_4.setAlignment(Qt.AlignCenter)
        self.base_item_2 = QLabel(self.info_frame)
        self.base_item_2.setObjectName(u"base_item_2")
        self.base_item_2.setGeometry(QRect(110, 55, 301, 28))
        self.base_item_2.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(240, 240, 240); \n"
"	border-radius: 5px;\n"
"}")
        self.base_item_2.setAlignment(Qt.AlignCenter)
        self.base_item_6 = QLabel(self.info_frame)
        self.base_item_6.setObjectName(u"base_item_6")
        self.base_item_6.setGeometry(QRect(110, 187, 101, 28))
        self.base_item_6.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(240, 240, 240); \n"
"	border-radius: 5px;\n"
"}")
        self.base_item_6.setAlignment(Qt.AlignCenter)
        self.base_item_5 = QLabel(self.info_frame)
        self.base_item_5.setObjectName(u"base_item_5")
        self.base_item_5.setGeometry(QRect(110, 154, 101, 28))
        self.base_item_5.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(240, 240, 240); \n"
"	border-radius: 5px;\n"
"}")
        self.base_item_5.setAlignment(Qt.AlignCenter)
        self.base_item_1 = QLabel(self.info_frame)
        self.base_item_1.setObjectName(u"base_item_1")
        self.base_item_1.setGeometry(QRect(110, 22, 301, 28))
        self.base_item_1.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(240, 240, 240); \n"
"	border-radius: 5px;\n"
"}")
        self.base_item_1.setAlignment(Qt.AlignCenter)
        self.base_name_10 = QLabel(self.info_frame)
        self.base_name_10.setObjectName(u"base_name_10")
        self.base_name_10.setGeometry(QRect(235, 221, 60, 26))
        self.base_name_10.setStyleSheet(u"")
        self.base_name_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.base_name_9 = QLabel(self.info_frame)
        self.base_name_9.setObjectName(u"base_name_9")
        self.base_name_9.setGeometry(QRect(235, 188, 60, 26))
        self.base_name_9.setStyleSheet(u"")
        self.base_name_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.base_name_8 = QLabel(self.info_frame)
        self.base_name_8.setObjectName(u"base_name_8")
        self.base_name_8.setGeometry(QRect(235, 155, 60, 26))
        self.base_name_8.setStyleSheet(u"")
        self.base_name_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.base_item_10 = QLabel(self.info_frame)
        self.base_item_10.setObjectName(u"base_item_10")
        self.base_item_10.setGeometry(QRect(310, 220, 101, 28))
        self.base_item_10.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(240, 240, 240); \n"
"	border-radius: 5px;\n"
"}")
        self.base_item_10.setAlignment(Qt.AlignCenter)
        self.base_item_8 = QLabel(self.info_frame)
        self.base_item_8.setObjectName(u"base_item_8")
        self.base_item_8.setGeometry(QRect(310, 154, 101, 28))
        self.base_item_8.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(240, 240, 240); \n"
"	border-radius: 5px;\n"
"}")
        self.base_item_8.setAlignment(Qt.AlignCenter)
        self.base_item_9 = QLabel(self.info_frame)
        self.base_item_9.setObjectName(u"base_item_9")
        self.base_item_9.setGeometry(QRect(310, 187, 101, 28))
        self.base_item_9.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(240, 240, 240); \n"
"	border-radius: 5px;\n"
"}")
        self.base_item_9.setAlignment(Qt.AlignCenter)
        self.base_item_13 = QLabel(self.info_frame)
        self.base_item_13.setObjectName(u"base_item_13")
        self.base_item_13.setGeometry(QRect(110, 319, 301, 28))
        self.base_item_13.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(240, 240, 240); \n"
"	border-radius: 5px;\n"
"}")
        self.base_item_13.setAlignment(Qt.AlignCenter)
        self.base_item_11 = QLabel(self.info_frame)
        self.base_item_11.setObjectName(u"base_item_11")
        self.base_item_11.setGeometry(QRect(110, 253, 301, 28))
        self.base_item_11.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(240, 240, 240); \n"
"	border-radius: 5px;\n"
"}")
        self.base_item_11.setAlignment(Qt.AlignCenter)
        self.base_item_12 = QLabel(self.info_frame)
        self.base_item_12.setObjectName(u"base_item_12")
        self.base_item_12.setGeometry(QRect(110, 286, 301, 28))
        self.base_item_12.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(240, 240, 240); \n"
"	border-radius: 5px;\n"
"}")
        self.base_item_12.setAlignment(Qt.AlignCenter)
        self.detail_frame = QFrame(BuildingInfo)
        self.detail_frame.setObjectName(u"detail_frame")
        self.detail_frame.setGeometry(QRect(470, 80, 431, 261))
        self.detail_frame.setStyleSheet(u"#detail_frame {\n"
"	background-color: white;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(67,67,67);\n"
"	padding-top: 4px;\n"
"}")
        self.detail_frame.setFrameShape(QFrame.StyledPanel)
        self.detail_frame.setFrameShadow(QFrame.Raised)
        self.detail_name_7 = QLabel(self.detail_frame)
        self.detail_name_7.setObjectName(u"detail_name_7")
        self.detail_name_7.setGeometry(QRect(230, 150, 60, 26))
        self.detail_name_7.setStyleSheet(u"")
        self.detail_name_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.detail_name_9 = QLabel(self.detail_frame)
        self.detail_name_9.setObjectName(u"detail_name_9")
        self.detail_name_9.setGeometry(QRect(230, 216, 60, 26))
        self.detail_name_9.setStyleSheet(u"")
        self.detail_name_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.detail_item_1 = QLabel(self.detail_frame)
        self.detail_item_1.setObjectName(u"detail_item_1")
        self.detail_item_1.setGeometry(QRect(110, 22, 301, 28))
        self.detail_item_1.setStyleSheet(u"QLabel { \n"
"	background-color: rgb(240, 240, 240); \n"
"	border-radius: 5px;\n"
"}")
        self.detail_item_1.setAlignment(Qt.AlignCenter)
        self.detail_item_8 = QLabel(self.detail_frame)
        self.detail_item_8.setObjectName(u"detail_item_8")
        self.detail_item_8.setGeometry(QRect(310, 182, 101, 28))
        self.detail_item_8.setStyleSheet(u"QLabel { \n"
"	background-color: rgb(240, 240, 240); \n"
"	border-radius: 5px;\n"
"}")
        self.detail_item_8.setAlignment(Qt.AlignCenter)
        self.detail_name_2 = QLabel(self.detail_frame)
        self.detail_name_2.setObjectName(u"detail_name_2")
        self.detail_name_2.setGeometry(QRect(20, 71, 80, 26))
        self.detail_name_2.setFont(font)
        self.detail_name_2.setStyleSheet(u"")
        self.detail_name_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.detail_item_7 = QLabel(self.detail_frame)
        self.detail_item_7.setObjectName(u"detail_item_7")
        self.detail_item_7.setGeometry(QRect(310, 149, 101, 28))
        self.detail_item_7.setStyleSheet(u"QLabel { \n"
"	background-color: rgb(240, 240, 240); \n"
"	border-radius: 5px;\n"
"}")
        self.detail_item_7.setAlignment(Qt.AlignCenter)
        self.detail_name_6 = QLabel(self.detail_frame)
        self.detail_name_6.setObjectName(u"detail_name_6")
        self.detail_name_6.setGeometry(QRect(20, 216, 80, 26))
        self.detail_name_6.setStyleSheet(u"")
        self.detail_name_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.detail_name_4 = QLabel(self.detail_frame)
        self.detail_name_4.setObjectName(u"detail_name_4")
        self.detail_name_4.setGeometry(QRect(20, 150, 80, 26))
        self.detail_name_4.setStyleSheet(u"")
        self.detail_name_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.detail_name_1 = QLabel(self.detail_frame)
        self.detail_name_1.setObjectName(u"detail_name_1")
        self.detail_name_1.setGeometry(QRect(20, 23, 80, 26))
        self.detail_name_1.setFont(font)
        self.detail_name_1.setStyleSheet(u"")
        self.detail_name_1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.detail_item_5 = QLabel(self.detail_frame)
        self.detail_item_5.setObjectName(u"detail_item_5")
        self.detail_item_5.setGeometry(QRect(110, 182, 101, 28))
        self.detail_item_5.setStyleSheet(u"QLabel { \n"
"	background-color: rgb(240, 240, 240); \n"
"	border-radius: 5px;\n"
"}")
        self.detail_item_5.setAlignment(Qt.AlignCenter)
        self.detail_item_3 = QLabel(self.detail_frame)
        self.detail_item_3.setObjectName(u"detail_item_3")
        self.detail_item_3.setGeometry(QRect(110, 116, 301, 28))
        self.detail_item_3.setStyleSheet(u"QLabel { \n"
"	background-color: rgb(240, 240, 240); \n"
"	border-radius: 5px;\n"
"}")
        self.detail_item_3.setAlignment(Qt.AlignCenter)
        self.detail_name_5 = QLabel(self.detail_frame)
        self.detail_name_5.setObjectName(u"detail_name_5")
        self.detail_name_5.setGeometry(QRect(20, 183, 80, 26))
        self.detail_name_5.setStyleSheet(u"")
        self.detail_name_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.detail_item_2 = QLabel(self.detail_frame)
        self.detail_item_2.setObjectName(u"detail_item_2")
        self.detail_item_2.setGeometry(QRect(110, 55, 301, 56))
        self.detail_item_2.setMinimumSize(QSize(0, 30))
        self.detail_item_2.setMaximumSize(QSize(16777215, 16777215))
        self.detail_item_2.setStyleSheet(u"QLabel { \n"
"	background-color: rgb(240, 240, 240); \n"
"	border-radius: 5px;\n"
"	padding-right: 7px;\n"
"	padding-left: 7px;\n"
"}")
        self.detail_item_2.setAlignment(Qt.AlignCenter)
        self.detail_item_2.setWordWrap(True)
        self.detail_name_3 = QLabel(self.detail_frame)
        self.detail_name_3.setObjectName(u"detail_name_3")
        self.detail_name_3.setGeometry(QRect(20, 118, 80, 26))
        self.detail_name_3.setFont(font)
        self.detail_name_3.setStyleSheet(u"")
        self.detail_name_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.detail_item_4 = QLabel(self.detail_frame)
        self.detail_item_4.setObjectName(u"detail_item_4")
        self.detail_item_4.setGeometry(QRect(110, 149, 101, 28))
        self.detail_item_4.setStyleSheet(u"QLabel { \n"
"	background-color: rgb(240, 240, 240); \n"
"	border-radius: 5px;\n"
"}")
        self.detail_item_4.setAlignment(Qt.AlignCenter)
        self.detail_item_6 = QLabel(self.detail_frame)
        self.detail_item_6.setObjectName(u"detail_item_6")
        self.detail_item_6.setGeometry(QRect(110, 215, 101, 28))
        self.detail_item_6.setStyleSheet(u"QLabel { \n"
"	background-color: rgb(240, 240, 240); \n"
"	border-radius: 5px;\n"
"}")
        self.detail_item_6.setAlignment(Qt.AlignCenter)
        self.detail_item_9 = QLabel(self.detail_frame)
        self.detail_item_9.setObjectName(u"detail_item_9")
        self.detail_item_9.setGeometry(QRect(310, 215, 101, 28))
        self.detail_item_9.setStyleSheet(u"QLabel { \n"
"	background-color: rgb(240, 240, 240); \n"
"	border-radius: 5px;\n"
"}")
        self.detail_item_9.setAlignment(Qt.AlignCenter)
        self.detail_name_8 = QLabel(self.detail_frame)
        self.detail_name_8.setObjectName(u"detail_name_8")
        self.detail_name_8.setGeometry(QRect(230, 183, 60, 26))
        self.detail_name_8.setStyleSheet(u"")
        self.detail_name_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.parking_frame = QFrame(BuildingInfo)
        self.parking_frame.setObjectName(u"parking_frame")
        self.parking_frame.setGeometry(QRect(470, 360, 431, 101))
        self.parking_frame.setStyleSheet(u"#parking_frame {\n"
"	background-color: white;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(67,67,67);\n"
"	padding-top: 4px;\n"
"}")
        self.parking_frame.setFrameShape(QFrame.StyledPanel)
        self.parking_frame.setFrameShadow(QFrame.Raised)
        self.park_name_1 = QLabel(self.parking_frame)
        self.park_name_1.setObjectName(u"park_name_1")
        self.park_name_1.setGeometry(QRect(20, 23, 80, 26))
        self.park_name_1.setStyleSheet(u"=")
        self.park_name_1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.park_name_4 = QLabel(self.parking_frame)
        self.park_name_4.setObjectName(u"park_name_4")
        self.park_name_4.setGeometry(QRect(226, 56, 80, 26))
        self.park_name_4.setStyleSheet(u"=")
        self.park_name_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.park_name_2 = QLabel(self.parking_frame)
        self.park_name_2.setObjectName(u"park_name_2")
        self.park_name_2.setGeometry(QRect(20, 56, 80, 26))
        self.park_name_2.setStyleSheet(u"=")
        self.park_name_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.park_item_1 = QLabel(self.parking_frame)
        self.park_item_1.setObjectName(u"park_item_1")
        self.park_item_1.setGeometry(QRect(108, 22, 101, 28))
        self.park_item_1.setStyleSheet(u"QLabel { \n"
"	background-color: rgb(240, 240, 240); \n"
"	border-radius: 5px;\n"
"}")
        self.park_item_1.setAlignment(Qt.AlignCenter)
        self.park_item_2 = QLabel(self.parking_frame)
        self.park_item_2.setObjectName(u"park_item_2")
        self.park_item_2.setGeometry(QRect(108, 55, 101, 28))
        self.park_item_2.setStyleSheet(u"QLabel { \n"
"	background-color: rgb(240, 240, 240); \n"
"	border-radius: 5px;\n"
"}")
        self.park_item_2.setAlignment(Qt.AlignCenter)
        self.park_item_3 = QLabel(self.parking_frame)
        self.park_item_3.setObjectName(u"park_item_3")
        self.park_item_3.setGeometry(QRect(310, 22, 101, 28))
        self.park_item_3.setStyleSheet(u"QLabel { \n"
"	background-color: rgb(240, 240, 240); \n"
"	border-radius: 5px;\n"
"}")
        self.park_item_3.setAlignment(Qt.AlignCenter)
        self.park_name_3 = QLabel(self.parking_frame)
        self.park_name_3.setObjectName(u"park_name_3")
        self.park_name_3.setGeometry(QRect(226, 23, 80, 26))
        self.park_name_3.setStyleSheet(u"=")
        self.park_name_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.park_item_4 = QLabel(self.parking_frame)
        self.park_item_4.setObjectName(u"park_item_4")
        self.park_item_4.setGeometry(QRect(310, 55, 101, 28))
        self.park_item_4.setStyleSheet(u"QLabel { \n"
"	background-color: rgb(240, 240, 240); \n"
"	border-radius: 5px;\n"
"}")
        self.park_item_4.setAlignment(Qt.AlignCenter)
        self.land_frame = QFrame(BuildingInfo)
        self.land_frame.setObjectName(u"land_frame")
        self.land_frame.setGeometry(QRect(470, 480, 431, 201))
        self.land_frame.setStyleSheet(u"#land_frame {\n"
"	background-color: white;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(67,67,67);\n"
"	padding-top: 4px;\n"
"}")
        self.land_frame.setFrameShape(QFrame.StyledPanel)
        self.land_frame.setFrameShadow(QFrame.Raised)
        self.land_item_2 = QLabel(self.land_frame)
        self.land_item_2.setObjectName(u"land_item_2")
        self.land_item_2.setGeometry(QRect(110, 55, 301, 63))
        self.land_item_2.setStyleSheet(u"QLabel { \n"
"	background-color: rgb(240, 240, 240); \n"
"	border-radius: 5px;\n"
"	padding-right: 7px;\n"
"	padding-left: 7px;\n"
"}")
        self.land_item_2.setAlignment(Qt.AlignCenter)
        self.land_item_2.setWordWrap(True)
        self.land_name_3 = QLabel(self.land_frame)
        self.land_name_3.setObjectName(u"land_name_3")
        self.land_name_3.setGeometry(QRect(20, 125, 80, 61))
        self.land_name_3.setStyleSheet(u"")
        self.land_name_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.land_name_1 = QLabel(self.land_frame)
        self.land_name_1.setObjectName(u"land_name_1")
        self.land_name_1.setGeometry(QRect(20, 23, 80, 30))
        self.land_name_1.setStyleSheet(u"")
        self.land_name_1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.land_item_1 = QLabel(self.land_frame)
        self.land_item_1.setObjectName(u"land_item_1")
        self.land_item_1.setGeometry(QRect(110, 22, 301, 28))
        self.land_item_1.setStyleSheet(u"QLabel { \n"
"	background-color: rgb(240, 240, 240); \n"
"	border-radius: 5px;\n"
"}")
        self.land_item_1.setAlignment(Qt.AlignCenter)
        self.land_item_3 = QLabel(self.land_frame)
        self.land_item_3.setObjectName(u"land_item_3")
        self.land_item_3.setGeometry(QRect(110, 123, 301, 63))
        self.land_item_3.setStyleSheet(u"QLabel { \n"
"	background-color: rgb(240, 240, 240); \n"
"	border-radius: 5px;\n"
"	padding-right: 7px;\n"
"	padding-left: 7px;\n"
"}")
        self.land_item_3.setAlignment(Qt.AlignCenter)
        self.land_item_3.setWordWrap(True)
        self.land_name_2 = QLabel(self.land_frame)
        self.land_name_2.setObjectName(u"land_name_2")
        self.land_name_2.setGeometry(QRect(20, 56, 80, 62))
        self.land_name_2.setStyleSheet(u"")
        self.land_name_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.top_bar.raise_()
        self.bot_bar.raise_()
        self.lb_hint_2.raise_()
        self.address_frame.raise_()
        self.info_frame.raise_()
        self.detail_frame.raise_()
        self.parking_frame.raise_()
        self.land_frame.raise_()
        QWidget.setTabOrder(self.edt_address, self.btn_viol)
        QWidget.setTabOrder(self.btn_viol, self.btn_details)

        self.retranslateUi(BuildingInfo)

        QMetaObject.connectSlotsByName(BuildingInfo)
    # setupUi

    def retranslateUi(self, BuildingInfo):
        self.lb_hint_2.setText(QCoreApplication.translate("BuildingInfo", u"\uac80\uc0c9 \ub41c \uacb0\uacfc\ub294 \uac01\uc885 \uacf5\uacf5\ub370\uc774\ud130 \ud3ec\ud138\uc5d0\uc11c \uc81c\uacf5\ud558\ub294 API \ub370\uc774\ud130\ub85c\n"
"\uc2e4\uc81c \uac74\ucd95\ubb3c\ub300\uc7a5 \uc815\ubcf4\uc640 \uc0c1\uc774 \ud560 \uc218 \uc788\uc73c\ub2c8 \ucc38\uace0\uc6a9\uc73c\ub85c\ub9cc \uc0ac\uc6a9\ud574\uc8fc\uc138\uc694.\n"
"(\ubcf8 \ud504\ub85c\uadf8\ub7a8\uc740 \uc870\ud68c\ub41c \uc815\ubcf4\uc5d0 \ub300\ud55c \ucc45\uc784\uc744 \uc9c0\uc9c0 \uc54a\uc2b5\ub2c8\ub2e4.)", None))
        self.lb_title.setText(QCoreApplication.translate("BuildingInfo", u"INFORMATION", None))
        self.lb_sub_title.setText(QCoreApplication.translate("BuildingInfo", u"(  \uac74\ucd95\ubb3c \uc870\ud68c  )", None))
        self.btn_menu.setText("")
        self.btn_viol.setText(QCoreApplication.translate("BuildingInfo", u"\uc704\ubc18 \uac74\ucd95\ubb3c \uc870\ud68c", None))
        self.lb_viol.setText("")
        self.btn_details.setText(QCoreApplication.translate("BuildingInfo", u"\uc0c1\uc138\uc815\ubcf4  >", None))
        self.btn_issuance.setText("")
        self.lb_sub_title_1.setText(QCoreApplication.translate("BuildingInfo", u"\uc18c\uc7ac\uc9c0 \uac80\uc0c9", None))
        self.edt_address.setText("")
        self.cbx_rooms.setItemText(0, QCoreApplication.translate("BuildingInfo", u"( \uc0c1\uc138\uc8fc\uc18c / \ud638 \uc120\ud0dd )", None))

        self.btn_search.setText("")
        self.lb_hint_3.setText(QCoreApplication.translate("BuildingInfo", u"* \ud56d\ubaa9 \ub354\ube14 \ud074\ub9ad \uc2dc, \ub0b4\uc6a9\uc774 \ud074\ub9bd\ubcf4\ub4dc\uc5d0 \ubcf5\uc0ac \ub429\ub2c8\ub2e4.", None))
        self.base_name_7.setText(QCoreApplication.translate("BuildingInfo", u"\uc8fc \ucc28 \uc7a5", None))
        self.base_name_2.setText(QCoreApplication.translate("BuildingInfo", u"\ub3c4 \ub85c \uba85", None))
        self.base_name_4.setText(QCoreApplication.translate("BuildingInfo", u"\uc8fc \uc6a9 \ub3c4", None))
        self.base_name_1.setText(QCoreApplication.translate("BuildingInfo", u"\uc18c \uc7ac \uc9c0", None))
        self.base_name_5.setText(QCoreApplication.translate("BuildingInfo", u"\uacf5\uc6a9\uba74\uc801", None))
        self.base_name_3.setText(QCoreApplication.translate("BuildingInfo", u"\uc0c1\uc138\uc8fc\uc18c", None))
        self.base_name_6.setText(QCoreApplication.translate("BuildingInfo", u"\uc2b9 \uac15 \uae30", None))
        self.base_name_13.setText(QCoreApplication.translate("BuildingInfo", u"\uacf5 \uc2dc \uac00 \uaca9", None))
        self.base_name_12.setText(QCoreApplication.translate("BuildingInfo", u"\uc0ac \uc6a9 \uc2b9 \uc778 \uc77c", None))
        self.base_name_11.setText(QCoreApplication.translate("BuildingInfo", u"\ud638/\uac00\uad6c/\uc138\ub300", None))
        self.base_item_7.setText("")
        self.base_item_3.setText("")
        self.base_item_4.setText("")
        self.base_item_2.setText("")
        self.base_item_6.setText("")
        self.base_item_5.setText("")
        self.base_item_1.setText("")
        self.base_name_10.setText(QCoreApplication.translate("BuildingInfo", u"\uc18c \uc720 \uc790", None))
        self.base_name_9.setText(QCoreApplication.translate("BuildingInfo", u"\ucd1d \uce35 \uc218", None))
        self.base_name_8.setText(QCoreApplication.translate("BuildingInfo", u"\uc804\uc6a9\uba74\uc801", None))
        self.base_item_10.setText("")
        self.base_item_8.setText("")
        self.base_item_9.setText("")
        self.base_item_13.setText("")
        self.base_item_11.setText("")
        self.base_item_12.setText("")
        self.detail_name_7.setText(QCoreApplication.translate("BuildingInfo", u"\uc5f0 \uba74 \uc801", None))
        self.detail_name_9.setText(QCoreApplication.translate("BuildingInfo", u"\uc6a9 \uc801 \ub960", None))
        self.detail_item_1.setText("")
        self.detail_item_8.setText("")
        self.detail_name_2.setText(QCoreApplication.translate("BuildingInfo", u"\uc9c0\uc5ed\u318d\uc9c0\uad6c", None))
        self.detail_item_7.setText("")
        self.detail_name_6.setText(QCoreApplication.translate("BuildingInfo", u"\uac74 \ud3d0 \uc728", None))
        self.detail_name_4.setText(QCoreApplication.translate("BuildingInfo", u"\ub300\uc9c0\uba74\uc801", None))
        self.detail_name_1.setText(QCoreApplication.translate("BuildingInfo", u"\uc8fc \uad6c \uc870", None))
        self.detail_item_5.setText("")
        self.detail_item_3.setText("")
        self.detail_name_5.setText(QCoreApplication.translate("BuildingInfo", u"\uac74\ucd95\uba74\uc801", None))
        self.detail_item_2.setText("")
        self.detail_name_3.setText(QCoreApplication.translate("BuildingInfo", u"\uc8fc \uc6a9 \ub3c4", None))
        self.detail_item_4.setText("")
        self.detail_item_6.setText("")
        self.detail_item_9.setText("")
        self.detail_name_8.setText(QCoreApplication.translate("BuildingInfo", u"\ub192 \uc774", None))
        self.park_name_1.setText(QCoreApplication.translate("BuildingInfo", u"\uc625\ub0b4\uc790\uc8fc\uc2dd", None))
        self.park_name_4.setText(QCoreApplication.translate("BuildingInfo", u"\uc625\uc678\uae30\uacc4\uc2dd", None))
        self.park_name_2.setText(QCoreApplication.translate("BuildingInfo", u"\uc625\ub0b4\uae30\uacc4\uc2dd", None))
        self.park_item_1.setText("")
        self.park_item_2.setText("")
        self.park_item_3.setText("")
        self.park_name_3.setText(QCoreApplication.translate("BuildingInfo", u"\uc625\uc678\uc790\uc8fc\uc2dd", None))
        self.park_item_4.setText("")
        self.land_item_2.setText("")
        self.land_name_3.setText(QCoreApplication.translate("BuildingInfo", u" \uae30 \ud0c0 \n"
" \uc9c0\uc5ed\u318d\uc9c0\uad6c", None))
        self.land_name_1.setText(QCoreApplication.translate("BuildingInfo", u"\uac1c\ubcc4\uacf5\uc2dc\uc9c0\uac00", None))
        self.land_item_1.setText("")
        self.land_item_3.setText("")
        self.land_name_2.setText(QCoreApplication.translate("BuildingInfo", u"\uc9c0\uc5ed\u318d\uc9c0\uad6c", None))
        pass
    # retranslateUi

