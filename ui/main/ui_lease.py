# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lease.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

from ui.custom.SlidingStackedWidget import SlidingStackedWidget

class Ui_MainWindow(object):
    def _setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(771, 711)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(14114, 141414))
        MainWindow.setStyleSheet(u"QMainWindow { background-color: white; }")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.top_bar = QWidget(self.centralwidget)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setGeometry(QRect(0, 0, 781, 61))
        self.top_bar.setStyleSheet(u"\n"
"#lb_title {\n"
"	font: 25px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgba(0, 0, 0, 120);\n"
"	padding-top: 8px;\n"
"	padding-left: 8px;\n"
"	border: 0px;\n"
"}\n"
"\n"
"#lb_sub_title {\n"
"	font: 15px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgba(0, 0, 0, 120);\n"
"	padding-top: 8px;\n"
"	padding-left: 8px;\n"
"	border: 0px;\n"
"}")
        self.lb_title = QLabel(self.top_bar)
        self.lb_title.setObjectName(u"lb_title")
        self.lb_title.setGeometry(QRect(270, 4, 210, 30))
        self.lb_title.setStyleSheet(u"")
        self.lb_title.setAlignment(Qt.AlignCenter)
        self.lb_sub_title = QLabel(self.top_bar)
        self.lb_sub_title.setObjectName(u"lb_sub_title")
        self.lb_sub_title.setGeometry(QRect(280, 29, 190, 25))
        self.lb_sub_title.setStyleSheet(u"")
        self.lb_sub_title.setAlignment(Qt.AlignCenter)
        self.lb_sub_title.raise_()
        self.lb_title.raise_()
        self.stackedWidget = SlidingStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 60, 781, 561))
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.info_frame = QFrame(self.page_1)
        self.info_frame.setObjectName(u"info_frame")
        self.info_frame.setGeometry(QRect(20, 20, 731, 271))
        self.info_frame.setStyleSheet(u"#info_frame {\n"
"	background-color: white;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel {\n"
"	font: 15px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(65,65,65);\n"
"}\n"
"\n"
"QLineEdit {\n"
"	font: 15px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(110,110,110);\n"
"	border: 1px solid rgb(130,130,130);\n"
"	border-radius: 2px;\n"
"	padding-top: 2px;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	color: rgb(85,85,85);\n"
"	border: 2px solid rgb(128,128,255);\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 1px solid rgb(130,130,130);\n"
"    padding-top: 4px;\n"
"    padding-left: 10px;\n"
"    min-width: 6em;\n"
"    background: rgb(255, 255, 255);\n"
"    font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"    color: rgb(65, 65, 65);\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView { \n"
"    border: 1px solid lightgray;\n"
"    outline: none;\n"
"    padding: 5px;\n"
"}      \n"
"\n"
"QComboBox QAbstractItemView::item { \n"
"    color: rgb(65, 65,"
                        " 65);\n"
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
"    image: url(../../data/img/system/down_arrow_icon.png);\n"
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
        self.info_frame.setFrameShape(QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.set_building = QWidget(self.info_frame)
        self.set_building.setObjectName(u"set_building")
        self.set_building.setGeometry(QRect(20, 180, 701, 71))
        self.label_5 = QLabel(self.set_building)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(90, 0, 71, 30))
        font = QFont()
        font.setFamilies([u"\uc6f0\ucef4\uccb4 Regular"])
        font.setBold(False)
        font.setItalic(False)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(85,85,85);\n"
"    border: 1px solid gray;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(234, 234, 234);\n"
"}")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.cbx_purposes = QComboBox(self.set_building)
        self.cbx_purposes.setObjectName(u"cbx_purposes")
        self.cbx_purposes.setGeometry(QRect(160, 40, 221, 30))
        self.cbx_purposes.setMinimumSize(QSize(108, 0))
        self.cbx_purposes.setMaximumSize(QSize(1666, 16777215))
        self.edt_area_total = QLineEdit(self.set_building)
        self.edt_area_total.setObjectName(u"edt_area_total")
        self.edt_area_total.setEnabled(True)
        self.edt_area_total.setGeometry(QRect(500, 0, 191, 30))
        self.edt_area_total.setStyleSheet(u"QLineEdit {\n"
"	padding-right: 25px;\n"
"}")
        self.edt_area_total.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lb_unit_3 = QLabel(self.set_building)
        self.lb_unit_3.setObjectName(u"lb_unit_3")
        self.lb_unit_3.setGeometry(QRect(667, 4, 20, 22))
        self.lb_unit_3.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(125,125,125);\n"
"	padding-top: 3px;\n"
"}")
        self.lb_unit_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lb_item_nm_7 = QLabel(self.set_building)
        self.lb_item_nm_7.setObjectName(u"lb_item_nm_7")
        self.lb_item_nm_7.setGeometry(QRect(420, 1, 60, 29))
        self.lb_item_nm_7.setFont(font)
        self.lb_item_nm_7.setStyleSheet(u"")
        self.cbx_structure = QComboBox(self.set_building)
        self.cbx_structure.setObjectName(u"cbx_structure")
        self.cbx_structure.setGeometry(QRect(160, 0, 221, 30))
        self.cbx_structure.setMinimumSize(QSize(108, 0))
        self.cbx_structure.setMaximumSize(QSize(1666, 16777215))
        self.label_6 = QLabel(self.set_building)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(90, 40, 71, 30))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(85,85,85);\n"
"    border: 1px solid gray;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(234, 234, 234);\n"
"}")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.lb_item_nm_25 = QLabel(self.set_building)
        self.lb_item_nm_25.setObjectName(u"lb_item_nm_25")
        self.lb_item_nm_25.setGeometry(QRect(10, 20, 71, 29))
        self.lb_item_nm_25.setFont(font)
        self.lb_item_nm_25.setStyleSheet(u"")
        self.set_land = QWidget(self.info_frame)
        self.set_land.setObjectName(u"set_land")
        self.set_land.setGeometry(QRect(20, 140, 699, 31))
        self.set_land.setMinimumSize(QSize(0, 31))
        self.set_land.setMaximumSize(QSize(16777215, 31))
        self.lb_unit_2 = QLabel(self.set_land)
        self.lb_unit_2.setObjectName(u"lb_unit_2")
        self.lb_unit_2.setGeometry(QRect(667, 4, 20, 22))
        self.lb_unit_2.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(125,125,125);\n"
"	padding-top: 3px;\n"
"}")
        self.lb_unit_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.cbx_land = QComboBox(self.set_land)
        self.cbx_land.addItem("")
        self.cbx_land.addItem("")
        self.cbx_land.setObjectName(u"cbx_land")
        self.cbx_land.setGeometry(QRect(90, 0, 110, 30))
        self.cbx_land.setMinimumSize(QSize(108, 0))
        self.cbx_land.setMaximumSize(QSize(100, 16777215))
        self.cbx_land.setIconSize(QSize(0, 0))
        self.lb_item_nm_6 = QLabel(self.set_land)
        self.lb_item_nm_6.setObjectName(u"lb_item_nm_6")
        self.lb_item_nm_6.setGeometry(QRect(420, 1, 60, 29))
        self.lb_item_nm_6.setFont(font)
        self.lb_item_nm_6.setStyleSheet(u"")
        self.cbx_land_details = QComboBox(self.set_land)
        self.cbx_land_details.setObjectName(u"cbx_land_details")
        self.cbx_land_details.setGeometry(QRect(210, 0, 171, 30))
        self.cbx_land_details.setMinimumSize(QSize(108, 0))
        self.cbx_land_details.setMaximumSize(QSize(1677, 16777215))
        self.edt_area_land = QLineEdit(self.set_land)
        self.edt_area_land.setObjectName(u"edt_area_land")
        self.edt_area_land.setEnabled(True)
        self.edt_area_land.setGeometry(QRect(500, 0, 191, 30))
        self.edt_area_land.setStyleSheet(u"QLineEdit {\n"
"	padding-right: 25px;\n"
"}")
        self.edt_area_land.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lb_item_nm_26 = QLabel(self.set_land)
        self.lb_item_nm_26.setObjectName(u"lb_item_nm_26")
        self.lb_item_nm_26.setGeometry(QRect(10, 1, 71, 29))
        self.lb_item_nm_26.setFont(font)
        self.lb_item_nm_26.setStyleSheet(u"")
        self.cbx_land.raise_()
        self.lb_item_nm_6.raise_()
        self.cbx_land_details.raise_()
        self.edt_area_land.raise_()
        self.lb_unit_2.raise_()
        self.lb_item_nm_26.raise_()
        self.set_ratio = QWidget(self.info_frame)
        self.set_ratio.setObjectName(u"set_ratio")
        self.set_ratio.setGeometry(QRect(20, 100, 699, 31))
        self.set_ratio.setMinimumSize(QSize(0, 31))
        self.set_ratio.setMaximumSize(QSize(16777215, 31))
        self.edt_ratio_1 = QLineEdit(self.set_ratio)
        self.edt_ratio_1.setObjectName(u"edt_ratio_1")
        self.edt_ratio_1.setEnabled(True)
        self.edt_ratio_1.setGeometry(QRect(90, 0, 121, 30))
        self.edt_ratio_1.setAlignment(Qt.AlignCenter)
        self.lb_item_nm_22 = QLabel(self.set_ratio)
        self.lb_item_nm_22.setObjectName(u"lb_item_nm_22")
        self.lb_item_nm_22.setGeometry(QRect(10, 1, 71, 29))
        self.lb_item_nm_22.setFont(font)
        self.lb_item_nm_22.setStyleSheet(u"")
        self.lb_item_nm_23 = QLabel(self.set_ratio)
        self.lb_item_nm_23.setObjectName(u"lb_item_nm_23")
        self.lb_item_nm_23.setGeometry(QRect(420, 1, 60, 29))
        self.lb_item_nm_23.setFont(font)
        self.lb_item_nm_23.setStyleSheet(u"")
        self.lb_item_nm_24 = QLabel(self.set_ratio)
        self.lb_item_nm_24.setObjectName(u"lb_item_nm_24")
        self.lb_item_nm_24.setGeometry(QRect(223, 0, 31, 29))
        self.lb_item_nm_24.setFont(font)
        self.lb_item_nm_24.setStyleSheet(u"")
        self.edt_ratio_2 = QLineEdit(self.set_ratio)
        self.edt_ratio_2.setObjectName(u"edt_ratio_2")
        self.edt_ratio_2.setEnabled(True)
        self.edt_ratio_2.setGeometry(QRect(260, 0, 121, 30))
        self.edt_ratio_2.setAlignment(Qt.AlignCenter)
        self.cbx_land_type = QComboBox(self.set_ratio)
        self.cbx_land_type.addItem("")
        self.cbx_land_type.addItem("")
        self.cbx_land_type.addItem("")
        self.cbx_land_type.addItem("")
        self.cbx_land_type.addItem("")
        self.cbx_land_type.addItem("")
        self.cbx_land_type.setObjectName(u"cbx_land_type")
        self.cbx_land_type.setGeometry(QRect(500, 0, 191, 30))
        self.cbx_land_type.setMinimumSize(QSize(108, 0))
        self.cbx_land_type.setMaximumSize(QSize(1677, 16777215))
        self.set_address = QWidget(self.info_frame)
        self.set_address.setObjectName(u"set_address")
        self.set_address.setGeometry(QRect(20, 20, 699, 31))
        self.set_address.setMinimumSize(QSize(0, 31))
        self.set_address.setMaximumSize(QSize(16777215, 31))
        self.edt_address = QLineEdit(self.set_address)
        self.edt_address.setObjectName(u"edt_address")
        self.edt_address.setEnabled(True)
        self.edt_address.setGeometry(QRect(90, 0, 601, 30))
        self.lb_item_nm_1 = QLabel(self.set_address)
        self.lb_item_nm_1.setObjectName(u"lb_item_nm_1")
        self.lb_item_nm_1.setGeometry(QRect(10, 1, 61, 29))
        self.lb_item_nm_1.setFont(font)
        self.lb_item_nm_1.setStyleSheet(u"")
        self.btn_search = QPushButton(self.set_address)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setGeometry(QRect(599, 2, 90, 26))
        self.btn_search.setStyleSheet(u"#btn_search {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(85,85,85);\n"
"	background-color: white;\n"
"	border: none;\n"
"	padding-top: 3px;\n"
"	\n"
"}\n"
"\n"
"#btn_search::hover {\n"
"	background-color: rgba(0,0,0,20)\n"
"}")
        self.set_rantal = QWidget(self.info_frame)
        self.set_rantal.setObjectName(u"set_rantal")
        self.set_rantal.setGeometry(QRect(20, 60, 699, 31))
        self.set_rantal.setMinimumSize(QSize(0, 31))
        self.set_rantal.setMaximumSize(QSize(16777215, 31))
        self.edt_address_details = QLineEdit(self.set_rantal)
        self.edt_address_details.setObjectName(u"edt_address_details")
        self.edt_address_details.setEnabled(True)
        self.edt_address_details.setGeometry(QRect(90, 0, 291, 30))
        self.edt_address_details.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lb_item_nm_2 = QLabel(self.set_rantal)
        self.lb_item_nm_2.setObjectName(u"lb_item_nm_2")
        self.lb_item_nm_2.setGeometry(QRect(10, 1, 60, 29))
        self.lb_item_nm_2.setFont(font)
        self.lb_item_nm_2.setStyleSheet(u"")
        self.lb_item_nm_5 = QLabel(self.set_rantal)
        self.lb_item_nm_5.setObjectName(u"lb_item_nm_5")
        self.lb_item_nm_5.setGeometry(QRect(420, 1, 60, 29))
        self.lb_item_nm_5.setFont(font)
        self.lb_item_nm_5.setStyleSheet(u"")
        self.lb_unit_1 = QLabel(self.set_rantal)
        self.lb_unit_1.setObjectName(u"lb_unit_1")
        self.lb_unit_1.setGeometry(QRect(667, 4, 20, 22))
        self.lb_unit_1.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(125,125,125);\n"
"	padding-top: 3px;\n"
"}")
        self.lb_unit_1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.edt_area_rental = QLineEdit(self.set_rantal)
        self.edt_area_rental.setObjectName(u"edt_area_rental")
        self.edt_area_rental.setEnabled(True)
        self.edt_area_rental.setGeometry(QRect(500, 0, 191, 30))
        self.edt_area_rental.setStyleSheet(u"QLineEdit {\n"
"	padding-right: 25px;\n"
"}")
        self.edt_area_rental.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.edt_address_details.raise_()
        self.lb_item_nm_2.raise_()
        self.lb_item_nm_5.raise_()
        self.edt_area_rental.raise_()
        self.lb_unit_1.raise_()
        self.money_frame = QFrame(self.page_1)
        self.money_frame.setObjectName(u"money_frame")
        self.money_frame.setGeometry(QRect(20, 310, 731, 231))
        self.money_frame.setStyleSheet(u"#money_frame {\n"
"	background-color: white;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel {\n"
"	font: 15px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(65,65,65);\n"
"}\n"
"\n"
"QLineEdit {\n"
"	font: 15px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(110,110,110);\n"
"	border: 1px solid rgb(130,130,130);\n"
"	border-radius: 2px;\n"
"	padding-top: 2px;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	color: rgb(85,85,85);\n"
"	border: 2px solid rgb(128,128,255);\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 1px solid rgb(130,130,130);\n"
"    padding-top: 4px;\n"
"    padding-left: 10px;\n"
"    min-width: 6em;\n"
"    background: rgb(255, 255, 255);\n"
"    font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"    color: rgb(65, 65, 65);\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView { \n"
"    border: 1px solid lightgray;\n"
"    outline: none;\n"
"    padding: 5px;\n"
"}      \n"
"\n"
"QComboBox QAbstractItemView::item { \n"
"    color: rgb(65, 65"
                        ", 65);\n"
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
"    image: url(../../data/img/system/down_arrow_icon.png);\n"
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
        self.money_frame.setFrameShape(QFrame.StyledPanel)
        self.money_frame.setFrameShadow(QFrame.Raised)
        self.lb_item_nm_8 = QLabel(self.money_frame)
        self.lb_item_nm_8.setObjectName(u"lb_item_nm_8")
        self.lb_item_nm_8.setGeometry(QRect(30, 20, 60, 30))
        self.lb_item_nm_8.setFont(font)
        self.lb_item_nm_8.setStyleSheet(u"")
        self.lb_price_5 = QLabel(self.money_frame)
        self.lb_price_5.setObjectName(u"lb_price_5")
        self.lb_price_5.setGeometry(QRect(366, 184, 31, 22))
        self.lb_price_5.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(125,125,125);\n"
"	padding-top: 3px;\n"
"}")
        self.lb_price_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.btn_balance_cal = QPushButton(self.money_frame)
        self.btn_balance_cal.setObjectName(u"btn_balance_cal")
        self.btn_balance_cal.setGeometry(QRect(683, 181, 28, 28))
        self.btn_balance_cal.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(0,0,0,0);\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: rgba(44,62,80,50)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(44,62,80,80)\n"
"}")
        self.lb_price_1 = QLabel(self.money_frame)
        self.lb_price_1.setObjectName(u"lb_price_1")
        self.lb_price_1.setGeometry(QRect(366, 24, 31, 22))
        self.lb_price_1.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(125,125,125);\n"
"	padding-top: 3px;\n"
"}")
        self.lb_price_1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.edt_down_pay = QLineEdit(self.money_frame)
        self.edt_down_pay.setObjectName(u"edt_down_pay")
        self.edt_down_pay.setGeometry(QRect(230, 60, 171, 30))
        self.edt_down_pay.setStyleSheet(u"QLineEdit {\n"
"	padding-right: 35px;\n"
"}")
        self.edt_down_pay.setMaxLength(15)
        self.edt_down_pay.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.edt_down_pay.setReadOnly(True)
        self.edt_balance_pay = QLineEdit(self.money_frame)
        self.edt_balance_pay.setObjectName(u"edt_balance_pay")
        self.edt_balance_pay.setGeometry(QRect(110, 180, 291, 30))
        self.edt_balance_pay.setStyleSheet(u"QLineEdit {\n"
"	padding-right: 35px;\n"
"}")
        self.edt_balance_pay.setMaxLength(15)
        self.edt_balance_pay.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.edt_balance_pay.setReadOnly(True)
        self.lb_korean_1st = QLineEdit(self.money_frame)
        self.lb_korean_1st.setObjectName(u"lb_korean_1st")
        self.lb_korean_1st.setGeometry(QRect(114, 104, 141, 22))
        self.lb_korean_1st.setStyleSheet(u"QLineEdit {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(45,45,45);\n"
"	background-color: rgba(127, 140, 141, 50);\n"
"	padding-top: 3px;\n"
"	padding-right: 8px;\n"
"	border: 0px;\n"
"}")
        self.lb_korean_1st.setReadOnly(True)
        self.lb_item_nm_14 = QLabel(self.money_frame)
        self.lb_item_nm_14.setObjectName(u"lb_item_nm_14")
        self.lb_item_nm_14.setGeometry(QRect(440, 100, 60, 30))
        self.lb_item_nm_14.setFont(font)
        self.lb_item_nm_14.setStyleSheet(u"")
        self.lb_korean_2st = QLineEdit(self.money_frame)
        self.lb_korean_2st.setObjectName(u"lb_korean_2st")
        self.lb_korean_2st.setGeometry(QRect(114, 144, 141, 22))
        self.lb_korean_2st.setStyleSheet(u"QLineEdit {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(45,45,45);\n"
"	background-color: rgba(127, 140, 141, 50);\n"
"	padding-top: 3px;\n"
"	padding-right: 8px;\n"
"	border: 0px;\n"
"}")
        self.lb_korean_2st.setReadOnly(True)
        self.edt_1st_day = QLineEdit(self.money_frame)
        self.edt_1st_day.setObjectName(u"edt_1st_day")
        self.edt_1st_day.setEnabled(True)
        self.edt_1st_day.setGeometry(QRect(520, 100, 151, 30))
        self.edt_1st_day.setStyleSheet(u"QLineEdit {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(85,85,85);\n"
"	padding-top: 3px;\n"
"}")
        self.edt_1st_day.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.edt_1st_day.setReadOnly(True)
        self.set_sub_1 = QWidget(self.money_frame)
        self.set_sub_1.setObjectName(u"set_sub_1")
        self.set_sub_1.setGeometry(QRect(440, 20, 271, 31))
        self.lb_price_sub_1 = QLabel(self.set_sub_1)
        self.lb_price_sub_1.setObjectName(u"lb_price_sub_1")
        self.lb_price_sub_1.setGeometry(QRect(236, 4, 31, 22))
        self.lb_price_sub_1.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(125,125,125);\n"
"	padding-top: 3px;\n"
"}")
        self.lb_price_sub_1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lb_item_nm_12 = QLabel(self.set_sub_1)
        self.lb_item_nm_12.setObjectName(u"lb_item_nm_12")
        self.lb_item_nm_12.setGeometry(QRect(0, 1, 60, 29))
        self.lb_item_nm_12.setFont(font)
        self.lb_item_nm_12.setStyleSheet(u"")
        self.edt_sub_1 = QLineEdit(self.set_sub_1)
        self.edt_sub_1.setObjectName(u"edt_sub_1")
        self.edt_sub_1.setGeometry(QRect(80, 0, 191, 30))
        self.edt_sub_1.setStyleSheet(u"QLineEdit {\n"
"	padding-right: 35px;\n"
"}")
        self.edt_sub_1.setMaxLength(15)
        self.edt_sub_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lb_item_nm_12.raise_()
        self.edt_sub_1.raise_()
        self.lb_price_sub_1.raise_()
        self.edt_2st_day = QLineEdit(self.money_frame)
        self.edt_2st_day.setObjectName(u"edt_2st_day")
        self.edt_2st_day.setEnabled(True)
        self.edt_2st_day.setGeometry(QRect(520, 140, 151, 30))
        self.edt_2st_day.setStyleSheet(u"QLineEdit {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(85,85,85);\n"
"	padding-top: 3px;\n"
"}")
        self.edt_2st_day.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.edt_2st_day.setReadOnly(True)
        self.lb_item_nm_10 = QLabel(self.money_frame)
        self.lb_item_nm_10.setObjectName(u"lb_item_nm_10")
        self.lb_item_nm_10.setGeometry(QRect(30, 121, 60, 30))
        self.lb_item_nm_10.setFont(font)
        self.lb_item_nm_10.setStyleSheet(u"")
        self.btn_2st_cal = QPushButton(self.money_frame)
        self.btn_2st_cal.setObjectName(u"btn_2st_cal")
        self.btn_2st_cal.setGeometry(QRect(683, 141, 28, 28))
        self.btn_2st_cal.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(0,0,0,0);\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: rgba(44,62,80,50)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(44,62,80,80)\n"
"}")
        self.set_sub_2 = QWidget(self.money_frame)
        self.set_sub_2.setObjectName(u"set_sub_2")
        self.set_sub_2.setGeometry(QRect(440, 60, 271, 31))
        self.lb_price_sub_2 = QLabel(self.set_sub_2)
        self.lb_price_sub_2.setObjectName(u"lb_price_sub_2")
        self.lb_price_sub_2.setGeometry(QRect(236, 4, 31, 22))
        self.lb_price_sub_2.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(125,125,125);\n"
"	padding-top: 3px;\n"
"}")
        self.lb_price_sub_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.edt_sub_2 = QLineEdit(self.set_sub_2)
        self.edt_sub_2.setObjectName(u"edt_sub_2")
        self.edt_sub_2.setEnabled(True)
        self.edt_sub_2.setGeometry(QRect(80, 0, 191, 30))
        self.edt_sub_2.setStyleSheet(u"QLineEdit {\n"
"	padding-right: 35px;\n"
"}")
        self.edt_sub_2.setMaxLength(15)
        self.edt_sub_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lb_item_nm_13 = QLabel(self.set_sub_2)
        self.lb_item_nm_13.setObjectName(u"lb_item_nm_13")
        self.lb_item_nm_13.setGeometry(QRect(0, 1, 71, 29))
        self.lb_item_nm_13.setFont(font)
        self.lb_item_nm_13.setStyleSheet(u"")
        self.lb_item_nm_13.raise_()
        self.edt_sub_2.raise_()
        self.lb_price_sub_2.raise_()
        self.lb_item_nm_27 = QLabel(self.money_frame)
        self.lb_item_nm_27.setObjectName(u"lb_item_nm_27")
        self.lb_item_nm_27.setGeometry(QRect(30, 181, 71, 29))
        self.lb_item_nm_27.setFont(font)
        self.lb_item_nm_27.setStyleSheet(u"")
        self.lb_korean_amount = QLineEdit(self.money_frame)
        self.lb_korean_amount.setObjectName(u"lb_korean_amount")
        self.lb_korean_amount.setGeometry(QRect(114, 24, 141, 22))
        self.lb_korean_amount.setStyleSheet(u"QLineEdit {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(45,45,45);\n"
"	background-color: rgba(127, 140, 141, 50);\n"
"	padding-top: 3px;\n"
"	padding-right: 8px;\n"
"	border: 0px;\n"
"}")
        self.lb_korean_amount.setReadOnly(True)
        self.lb_item_nm_16 = QLabel(self.money_frame)
        self.lb_item_nm_16.setObjectName(u"lb_item_nm_16")
        self.lb_item_nm_16.setGeometry(QRect(440, 180, 60, 30))
        self.lb_item_nm_16.setFont(font)
        self.lb_item_nm_16.setStyleSheet(u"")
        self.edt_mid_pay_2st = QLineEdit(self.money_frame)
        self.edt_mid_pay_2st.setObjectName(u"edt_mid_pay_2st")
        self.edt_mid_pay_2st.setGeometry(QRect(110, 140, 291, 30))
        self.edt_mid_pay_2st.setStyleSheet(u"QLineEdit {\n"
"	padding-right: 35px;\n"
"}")
        self.edt_mid_pay_2st.setMaxLength(15)
        self.edt_mid_pay_2st.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.cbx_down_pay = QComboBox(self.money_frame)
        self.cbx_down_pay.addItem("")
        self.cbx_down_pay.addItem("")
        self.cbx_down_pay.addItem("")
        self.cbx_down_pay.setObjectName(u"cbx_down_pay")
        self.cbx_down_pay.setGeometry(QRect(110, 60, 108, 30))
        self.cbx_down_pay.setMinimumSize(QSize(108, 0))
        self.cbx_down_pay.setMaximumSize(QSize(100, 16777215))
        self.lb_price_3 = QLabel(self.money_frame)
        self.lb_price_3.setObjectName(u"lb_price_3")
        self.lb_price_3.setGeometry(QRect(366, 104, 31, 22))
        self.lb_price_3.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(125,125,125);\n"
"	padding-top: 3px;\n"
"}")
        self.lb_price_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.btn_1st_cal = QPushButton(self.money_frame)
        self.btn_1st_cal.setObjectName(u"btn_1st_cal")
        self.btn_1st_cal.setGeometry(QRect(683, 101, 28, 28))
        self.btn_1st_cal.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(0,0,0,0);\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: rgba(44,62,80,50)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(44,62,80,80)\n"
"}")
        self.lb_item_nm_9 = QLabel(self.money_frame)
        self.lb_item_nm_9.setObjectName(u"lb_item_nm_9")
        self.lb_item_nm_9.setGeometry(QRect(30, 60, 81, 30))
        self.lb_item_nm_9.setFont(font)
        self.lb_item_nm_9.setStyleSheet(u"")
        self.edt_amount = QLineEdit(self.money_frame)
        self.edt_amount.setObjectName(u"edt_amount")
        self.edt_amount.setGeometry(QRect(110, 20, 291, 30))
        self.edt_amount.setStyleSheet(u"QLineEdit {\n"
"	padding-right: 35px;\n"
"}")
        self.edt_amount.setMaxLength(15)
        self.edt_amount.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.edt_balance_day = QLineEdit(self.money_frame)
        self.edt_balance_day.setObjectName(u"edt_balance_day")
        self.edt_balance_day.setEnabled(True)
        self.edt_balance_day.setGeometry(QRect(520, 180, 151, 30))
        self.edt_balance_day.setStyleSheet(u"QLineEdit {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(85,85,85);\n"
"	padding-top: 3px;\n"
"}")
        self.edt_balance_day.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.edt_balance_day.setReadOnly(True)
        self.lb_item_nm_15 = QLabel(self.money_frame)
        self.lb_item_nm_15.setObjectName(u"lb_item_nm_15")
        self.lb_item_nm_15.setGeometry(QRect(440, 140, 60, 30))
        self.lb_item_nm_15.setFont(font)
        self.lb_item_nm_15.setStyleSheet(u"")
        self.edt_mid_pay_1st = QLineEdit(self.money_frame)
        self.edt_mid_pay_1st.setObjectName(u"edt_mid_pay_1st")
        self.edt_mid_pay_1st.setGeometry(QRect(110, 100, 291, 30))
        self.edt_mid_pay_1st.setStyleSheet(u"QLineEdit {\n"
"	padding-right: 35px;\n"
"}")
        self.edt_mid_pay_1st.setMaxLength(15)
        self.edt_mid_pay_1st.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lb_korean_balance = QLineEdit(self.money_frame)
        self.lb_korean_balance.setObjectName(u"lb_korean_balance")
        self.lb_korean_balance.setGeometry(QRect(114, 184, 141, 22))
        self.lb_korean_balance.setStyleSheet(u"QLineEdit {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(45,45,45);\n"
"	background-color: rgba(127, 140, 141, 50);\n"
"	padding-top: 3px;\n"
"	padding-right: 8px;\n"
"	border: 0px;\n"
"}")
        self.lb_korean_balance.setReadOnly(True)
        self.lb_price_2 = QLabel(self.money_frame)
        self.lb_price_2.setObjectName(u"lb_price_2")
        self.lb_price_2.setGeometry(QRect(366, 64, 31, 22))
        self.lb_price_2.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(125,125,125);\n"
"	padding-top: 3px;\n"
"}")
        self.lb_price_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lb_price_4 = QLabel(self.money_frame)
        self.lb_price_4.setObjectName(u"lb_price_4")
        self.lb_price_4.setGeometry(QRect(366, 144, 31, 22))
        self.lb_price_4.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(125,125,125);\n"
"	padding-top: 3px;\n"
"}")
        self.lb_price_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.edt_balance_pay.raise_()
        self.edt_mid_pay_2st.raise_()
        self.edt_mid_pay_1st.raise_()
        self.edt_amount.raise_()
        self.lb_item_nm_8.raise_()
        self.lb_price_5.raise_()
        self.btn_balance_cal.raise_()
        self.lb_price_1.raise_()
        self.edt_down_pay.raise_()
        self.lb_korean_1st.raise_()
        self.lb_item_nm_14.raise_()
        self.lb_korean_2st.raise_()
        self.edt_1st_day.raise_()
        self.set_sub_1.raise_()
        self.edt_2st_day.raise_()
        self.lb_item_nm_10.raise_()
        self.btn_2st_cal.raise_()
        self.set_sub_2.raise_()
        self.lb_item_nm_27.raise_()
        self.lb_korean_amount.raise_()
        self.lb_item_nm_16.raise_()
        self.cbx_down_pay.raise_()
        self.lb_price_3.raise_()
        self.btn_1st_cal.raise_()
        self.lb_item_nm_9.raise_()
        self.edt_balance_day.raise_()
        self.lb_item_nm_15.raise_()
        self.lb_korean_balance.raise_()
        self.lb_price_2.raise_()
        self.lb_price_4.raise_()
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.frame_2 = QFrame(self.page_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 20, 731, 201))
        self.frame_2.setStyleSheet(u"QPushButton {\n"
"    font: 15px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"    color: white;\n"
"    border: none;\n"
"    padding-top: 3px;\n"
"    padding-left: 2px;\n"
"    background: rgb(128,128,255);\n"
"    border-radius: 15px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(148,148,255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 6px;\n"
"    background-color: rgb(108,108,235);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(166, 168, 171);\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.lst_keyword = QListWidget(self.frame_2)
        self.lst_keyword.setObjectName(u"lst_keyword")
        self.lst_keyword.setGeometry(QRect(100, 50, 141, 131))
        self.lst_keyword.setStyleSheet(u"QListWidget:hover {\n"
"    border: 1px solid #3498db;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	width: 5px;\n"
"	border-radius: 2px;\n"
"	background: rgb(220,220,220);\n"
"}\n"
"\n"
"QScrollBar::handle:vertical  {\n"
"	border-radius: 2px;\n"
"	background: rgba(84,102,120, 120);\n"
"	min-height: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover  {\n"
"	border-radius: 2px;\n"
"	background: rgba(134,152,170, 120);\n"
"	min-height: 0px;\n"
"}")
        self.lst_keyword.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.lst_keyword.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.lb_item_nm_20 = QLabel(self.frame_2)
        self.lb_item_nm_20.setObjectName(u"lb_item_nm_20")
        self.lb_item_nm_20.setGeometry(QRect(250, 21, 341, 30))
        self.lb_item_nm_20.setFont(font)
        self.lb_item_nm_20.setStyleSheet(u"#lb_item_nm_20 {\n"
"	font: 15px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(65,65,65);\n"
"    border: 1px solid gray;\n"
"	padding-top: 3px;\n"
"	padding-left: 8px;\n"
"	background-color: rgb(234, 234, 234);\n"
"}")
        self.lst_title = QListWidget(self.frame_2)
        self.lst_title.setObjectName(u"lst_title")
        self.lst_title.setGeometry(QRect(250, 50, 341, 131))
        self.lst_title.setStyleSheet(u"QListWidget:hover {\n"
"    border: 1px solid #3498db;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	width: 5px;\n"
"	border-radius: 2px;\n"
"	background: rgb(220,220,220);\n"
"}\n"
"\n"
"QScrollBar::handle:vertical  {\n"
"	border-radius: 2px;\n"
"	background: rgba(84,102,120, 120);\n"
"	min-height: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover  {\n"
"	border-radius: 2px;\n"
"	background: rgba(134,152,170, 120);\n"
"	min-height: 0px;\n"
"}")
        self.lst_title.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.lst_title.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.lb_item_nm_17 = QLabel(self.frame_2)
        self.lb_item_nm_17.setObjectName(u"lb_item_nm_17")
        self.lb_item_nm_17.setGeometry(QRect(20, 21, 60, 30))
        self.lb_item_nm_17.setFont(font)
        self.lb_item_nm_17.setStyleSheet(u"QLabel {\n"
"	font: 15px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(65,65,65);\n"
"}")
        self.btn_edit = QPushButton(self.frame_2)
        self.btn_edit.setObjectName(u"btn_edit")
        self.btn_edit.setGeometry(QRect(610, 113, 101, 30))
        self.btn_edit.setStyleSheet(u"")
        self.lb_item_nm_19 = QLabel(self.frame_2)
        self.lb_item_nm_19.setObjectName(u"lb_item_nm_19")
        self.lb_item_nm_19.setGeometry(QRect(100, 21, 141, 30))
        self.lb_item_nm_19.setFont(font)
        self.lb_item_nm_19.setStyleSheet(u"#lb_item_nm_19 {\n"
"	font: 15px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(65,65,65);\n"
"    border: 1px solid gray;\n"
"	padding-top: 3px;\n"
"	padding-left: 8px;\n"
"	background-color: rgb(234, 234, 234);\n"
"}")
        self.btn_add = QPushButton(self.frame_2)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setGeometry(QRect(610, 76, 101, 30))
        self.btn_add.setStyleSheet(u"")
        self.btn_del = QPushButton(self.frame_2)
        self.btn_del.setObjectName(u"btn_del")
        self.btn_del.setGeometry(QRect(610, 150, 101, 30))
        self.btn_del.setStyleSheet(u"")
        self.frame_3 = QFrame(self.page_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(20, 240, 731, 321))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.lb_item_nm_18 = QLabel(self.frame_3)
        self.lb_item_nm_18.setObjectName(u"lb_item_nm_18")
        self.lb_item_nm_18.setGeometry(QRect(20, 130, 60, 30))
        self.lb_item_nm_18.setFont(font)
        self.lb_item_nm_18.setStyleSheet(u"QLabel {\n"
"	font: 15px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(65,65,65);\n"
"}")
        self.edt_agreement = QTextEdit(self.frame_3)
        self.edt_agreement.setObjectName(u"edt_agreement")
        self.edt_agreement.setGeometry(QRect(100, 20, 611, 281))
        self.edt_agreement.setStyleSheet(u"QTextEdit {\n"
"	font: 15px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	border: 1px solid rgb(130,130,130);\n"
"	border-radius: 3px;\n"
"	padding-top: 5px;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(128,128,255);\n"
"	border-radius: 3px;\n"
"}")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.part_3 = QFrame(self.page_4)
        self.part_3.setObjectName(u"part_3")
        self.part_3.setGeometry(QRect(0, 0, 701, 501))
        self.part_3.setStyleSheet(u"#part_3 { background-color: white; }\n"
"\n"
"QLabel {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(127, 140, 141);\n"
"}\n"
"\n"
"QPushButton {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: white;\n"
"	border: 0px;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(84,102,120);\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 0px;\n"
"	background-color: rgb(104,122,140);\n"
"	border-style: inset;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 0px;\n"
"	background-color: rgb(64,82,100);\n"
"	border-style: inset;\n"
"}\n"
"\n"
"QListWidget {\n"
"	outline: none;\n"
"	border: none;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	width: 5px;\n"
"	border-radius: 2px;\n"
"	background: rgb(220,220,220);\n"
"}\n"
"\n"
"QScrollBar::handle:vertical  {\n"
"	border-radius: 2px;\n"
"	background: rgba(84,102,120, 120);\n"
"	min-height: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover  {\n"
"	border-radius: 2px;\n"
""
                        "	background: rgba(134,152,170, 120);\n"
"	min-height: 0px;\n"
"}\n"
"")
        self.line_7 = QFrame(self.part_3)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(0, 10, 691, 20))
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.lb_sub_title_6 = QLabel(self.part_3)
        self.lb_sub_title_6.setObjectName(u"lb_sub_title_6")
        self.lb_sub_title_6.setGeometry(QRect(0, 0, 91, 16))
        self.lb_sub_title_6.setStyleSheet(u"")
        self.btn_add_c = QPushButton(self.part_3)
        self.btn_add_c.setObjectName(u"btn_add_c")
        self.btn_add_c.setGeometry(QRect(580, 30, 111, 30))
        self.btn_add_c.setStyleSheet(u"")
        self.lst_contractor = QListWidget(self.part_3)
        self.lst_contractor.setObjectName(u"lst_contractor")
        self.lst_contractor.setGeometry(QRect(10, 80, 681, 381))
        self.lst_contractor.setStyleSheet(u"")
        self.lst_contractor.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.lst_contractor.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.line_2 = QFrame(self.part_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 460, 691, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.lb_hint_3 = QLabel(self.part_3)
        self.lb_hint_3.setObjectName(u"lb_hint_3")
        self.lb_hint_3.setGeometry(QRect(480, 476, 211, 16))
        self.lb_hint_3.setStyleSheet(u"")
        self.lb_hint_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.btn_add_b = QPushButton(self.part_3)
        self.btn_add_b.setObjectName(u"btn_add_b")
        self.btn_add_b.setGeometry(QRect(464, 30, 111, 30))
        self.btn_add_b.setStyleSheet(u"")
        self.btn_add_a = QPushButton(self.part_3)
        self.btn_add_a.setObjectName(u"btn_add_a")
        self.btn_add_a.setGeometry(QRect(348, 30, 111, 30))
        self.btn_add_a.setStyleSheet(u"")
        self.line_8 = QFrame(self.part_3)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(0, 60, 691, 20))
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)
        self.lb_hint_2 = QLabel(self.part_3)
        self.lb_hint_2.setObjectName(u"lb_hint_2")
        self.lb_hint_2.setGeometry(QRect(0, 50, 211, 16))
        self.lb_hint_2.setStyleSheet(u"")
        self.lb_hint_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lb_icon = QLabel(self.part_3)
        self.lb_icon.setObjectName(u"lb_icon")
        self.lb_icon.setGeometry(QRect(13, 45, 23, 23))
        self.line_7.raise_()
        self.lb_sub_title_6.raise_()
        self.lst_contractor.raise_()
        self.line_2.raise_()
        self.lb_hint_3.raise_()
        self.btn_add_c.raise_()
        self.btn_add_b.raise_()
        self.btn_add_a.raise_()
        self.line_8.raise_()
        self.lb_hint_2.raise_()
        self.lb_icon.raise_()
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.stackedWidget.addWidget(self.page_5)
        self.btn_back = QPushButton(self.centralwidget)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(450, 640, 141, 40))
        self.btn_back.setStyleSheet(u"QPushButton {\n"
"    font: 16px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"    color: rgb(88,88,255);\n"
"    border: 3px solid rgb(128,128,255);\n"
"    padding-top: 3px;\n"
"    padding-left: 2px;\n"
"    background: white;\n"
"    border-radius: 20px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(148,148,255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 6px;\n"
"    background-color: rgb(108,108,235);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(166, 168, 171);\n"
"}")
        self.btn_next = QPushButton(self.centralwidget)
        self.btn_next.setObjectName(u"btn_next")
        self.btn_next.setGeometry(QRect(610, 640, 141, 40))
        self.btn_next.setStyleSheet(u"QPushButton {\n"
"    font: 16px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"    color: white;\n"
"    border: none;\n"
"    padding-top: 3px;\n"
"    padding-left: 2px;\n"
"    background: rgb(128,128,255);\n"
"    border-radius: 20px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(148,148,255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 6px;\n"
"    background-color: rgb(108,108,235);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(166, 168, 171);\n"
"}")
        self.btn_provisions = QPushButton(self.centralwidget)
        self.btn_provisions.setObjectName(u"btn_provisions")
        self.btn_provisions.setGeometry(QRect(30, 650, 111, 31))
        self.btn_provisions.setStyleSheet(u"QPushButton {\n"
"    font: 15px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"    color: rgb(88,88,255);\n"
"    border: 2px solid rgb(128,128,255);\n"
"    padding-top: 3px;\n"
"    padding-left: 2px;\n"
"    background: white;\n"
"    border-radius: 8px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(148,148,255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 6px;\n"
"    background-color: rgb(108,108,235);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(166, 168, 171);\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_add_a, self.btn_add_b)
        QWidget.setTabOrder(self.btn_add_b, self.btn_add_c)
        QWidget.setTabOrder(self.btn_add_c, self.lst_contractor)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\ub808\uc774 - Real estate Information", None))
        self.lb_title.setText(QCoreApplication.translate("MainWindow", u"CONTRACT", None))
        self.lb_sub_title.setText(QCoreApplication.translate("MainWindow", u"(  \uacc4\uc57d\uc11c \uc791\uc131  )", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\uad6c    \uc870", None))
        self.lb_unit_3.setText(QCoreApplication.translate("MainWindow", u"\u33a1", None))
        self.lb_item_nm_7.setText(QCoreApplication.translate("MainWindow", u"\uc5f0 \uba74 \uc801", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\uc6a9    \ub3c4", None))
        self.lb_item_nm_25.setText(QCoreApplication.translate("MainWindow", u"\uac74 \ubb3c", None))
        self.lb_unit_2.setText(QCoreApplication.translate("MainWindow", u"\u33a1", None))
        self.cbx_land.setItemText(0, QCoreApplication.translate("MainWindow", u"\uc9c0\ubaa9", None))
        self.cbx_land.setItemText(1, QCoreApplication.translate("MainWindow", u"\ub300\ud45c\uc9c0\ubaa9", None))

        self.lb_item_nm_6.setText(QCoreApplication.translate("MainWindow", u"\ub300 \uc9c0 \uba74 \uc801", None))
        self.lb_item_nm_26.setText(QCoreApplication.translate("MainWindow", u"\ud1a0 \uc9c0", None))
        self.edt_ratio_1.setText("")
        self.lb_item_nm_22.setText(QCoreApplication.translate("MainWindow", u"\ub300\uc9c0\uad8c\ube44\uc728", None))
        self.lb_item_nm_23.setText(QCoreApplication.translate("MainWindow", u"\ub300\uc9c0\uad8c\uc885\ub958", None))
        self.lb_item_nm_24.setText(QCoreApplication.translate("MainWindow", u"\ubd84\uc758", None))
        self.edt_ratio_2.setText("")
        self.cbx_land_type.setItemText(0, QCoreApplication.translate("MainWindow", u"\uc18c\uc720\uad8c", None))
        self.cbx_land_type.setItemText(1, QCoreApplication.translate("MainWindow", u"\uc784\ucc28\uad8c", None))
        self.cbx_land_type.setItemText(2, QCoreApplication.translate("MainWindow", u"\uc804\uc138\uad8c", None))
        self.cbx_land_type.setItemText(3, QCoreApplication.translate("MainWindow", u"\uc9c0\uc0c1\uad8c", None))
        self.cbx_land_type.setItemText(4, QCoreApplication.translate("MainWindow", u"\uc0ac\uc6a9\ucc28\uad8c", None))
        self.cbx_land_type.setItemText(5, QCoreApplication.translate("MainWindow", u"( \uc9c1\uc811\uc785\ub825 )", None))

        self.lb_item_nm_1.setText(QCoreApplication.translate("MainWindow", u"\uc18c \uc7ac \uc9c0", None))
        self.btn_search.setText(QCoreApplication.translate("MainWindow", u"\uc18c\uc7ac\uc9c0 \uac80\uc0c9", None))
        self.edt_address_details.setText("")
        self.lb_item_nm_2.setText(QCoreApplication.translate("MainWindow", u"\uc784 \ub300 \ubd80 \ubd84", None))
        self.lb_item_nm_5.setText(QCoreApplication.translate("MainWindow", u"\uc784 \ub300 \uba74 \uc801", None))
        self.lb_unit_1.setText(QCoreApplication.translate("MainWindow", u"\u33a1", None))
        self.edt_area_rental.setText("")
        self.lb_item_nm_8.setText(QCoreApplication.translate("MainWindow", u"\ubcf4 \uc99d \uae08", None))
        self.lb_price_5.setText(QCoreApplication.translate("MainWindow", u"\ub9cc\uc6d0", None))
        self.btn_balance_cal.setText("")
        self.lb_price_1.setText(QCoreApplication.translate("MainWindow", u"\ub9cc\uc6d0", None))
        self.edt_down_pay.setText("")
        self.edt_balance_pay.setText("")
        self.lb_korean_1st.setText("")
        self.lb_item_nm_14.setText(QCoreApplication.translate("MainWindow", u"1\ucc28 \uc9c0\ubd88\uc77c", None))
        self.lb_korean_2st.setText("")
        self.lb_price_sub_1.setText(QCoreApplication.translate("MainWindow", u"\ub9cc\uc6d0", None))
        self.lb_item_nm_12.setText(QCoreApplication.translate("MainWindow", u"\uc735 \uc790 \uae08", None))
        self.edt_sub_1.setText("")
        self.lb_item_nm_10.setText(QCoreApplication.translate("MainWindow", u"\uc911 \ub3c4 \uae08", None))
        self.btn_2st_cal.setText("")
        self.lb_price_sub_2.setText(QCoreApplication.translate("MainWindow", u"\ub9cc\uc6d0", None))
        self.edt_sub_2.setText("")
        self.lb_item_nm_13.setText(QCoreApplication.translate("MainWindow", u"\uae30 \ubcf4 \uc99d \uae08", None))
        self.lb_item_nm_27.setText(QCoreApplication.translate("MainWindow", u"\uc794 \uae08", None))
        self.lb_korean_amount.setText("")
        self.lb_item_nm_16.setText(QCoreApplication.translate("MainWindow", u"\uc794 \uae08 \uc77c", None))
        self.edt_mid_pay_2st.setText("")
        self.cbx_down_pay.setItemText(0, QCoreApplication.translate("MainWindow", u"10 %", None))
        self.cbx_down_pay.setItemText(1, QCoreApplication.translate("MainWindow", u"5 %", None))
        self.cbx_down_pay.setItemText(2, QCoreApplication.translate("MainWindow", u"(\uc9c1\uc811\uc785\ub825)", None))

        self.lb_price_3.setText(QCoreApplication.translate("MainWindow", u"\ub9cc\uc6d0", None))
        self.btn_1st_cal.setText("")
        self.lb_item_nm_9.setText(QCoreApplication.translate("MainWindow", u"\uacc4 \uc57d \uae08", None))
        self.edt_amount.setText("")
        self.lb_item_nm_15.setText(QCoreApplication.translate("MainWindow", u"2\ucc28 \uc9c0\ubd88\uc77c", None))
        self.edt_mid_pay_1st.setText("")
        self.lb_korean_balance.setText("")
        self.lb_price_2.setText(QCoreApplication.translate("MainWindow", u"\ub9cc\uc6d0", None))
        self.lb_price_4.setText(QCoreApplication.translate("MainWindow", u"\ub9cc\uc6d0", None))
        self.lb_item_nm_20.setText(QCoreApplication.translate("MainWindow", u"My \ud2b9\uc57d \ub9ac\uc2a4\ud2b8", None))
        self.lb_item_nm_17.setText(QCoreApplication.translate("MainWindow", u"My \ud2b9 \uc57d", None))
        self.btn_edit.setText(QCoreApplication.translate("MainWindow", u"\ud3b8      \uc9d1", None))
        self.lb_item_nm_19.setText(QCoreApplication.translate("MainWindow", u"\ud0a4 \uc6cc \ub4dc", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"\ucd94      \uac00", None))
        self.btn_del.setText(QCoreApplication.translate("MainWindow", u"\uc0ad      \uc81c", None))
        self.lb_item_nm_18.setText(QCoreApplication.translate("MainWindow", u"\ud2b9 \uc57d \uc0ac \ud56d", None))
        self.edt_agreement.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\uc6f0\ucef4\uccb4 Regular'; font-size:15px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.lb_sub_title_6.setText(QCoreApplication.translate("MainWindow", u"4. \uacc4\uc57d\uc790 \uc815\ubcf4", None))
        self.btn_add_c.setText(QCoreApplication.translate("MainWindow", u"\uc911 \uac1c \uc0ac   \ucd94 \uac00", None))
        self.lb_hint_3.setText(QCoreApplication.translate("MainWindow", u"* \ub9c8\uc6b0\uc2a4 \uc6b0\uce21 \ud074\ub9ad \uc2dc \ud56d\ubaa9 \uc0ad\uc81c \uac00\ub2a5", None))
        self.btn_add_b.setText(QCoreApplication.translate("MainWindow", u"\ub9e4 \uc218 \uc778   \ucd94 \uac00", None))
        self.btn_add_a.setText(QCoreApplication.translate("MainWindow", u"\ub9e4 \ub3c4 \uc778   \ucd94 \uac00", None))
        self.lb_hint_2.setText(QCoreApplication.translate("MainWindow", u"*           \uc544\uc774\ucf58 \ud074\ub9ad \uc2dc \uc774\ub984 \ubcc0\uacbd \uac00\ub2a5", None))
        self.lb_icon.setText("")
        self.btn_back.setText(QCoreApplication.translate("MainWindow", u"\uc774   \uc804", None))
        self.btn_next.setText(QCoreApplication.translate("MainWindow", u"\ub2e4   \uc74c", None))
        self.btn_provisions.setText(QCoreApplication.translate("MainWindow", u"\uacc4\uc57d \uc870\ud56d \uc218\uc815", None))
    # retranslateUi

