# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_lease.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(791, 771)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(14114, 141414))
        MainWindow.setStyleSheet(u"QMainWindow { background-color: white; }\n"
"\n"
"#AddRoom {\n"
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
"QComboBox:focus {\n"
"	border: 2px solid rgb(148,148,255);\n"
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
"QComboBox QAbstractItemView::item:focus { \n"
"    selection-color: white;\n"
"    background-color: rgb(128,128,255);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover { \n"
"    selection-color: white;\n"
"    bac"
                        "kground-color: rgb(128,128,255);\n"
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
"    image: url(../../static/img/system/down_arrow_icon.png);\n"
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
"	border: "
                        "1px solid rgb(148,148,255);\n"
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.top_bar = QWidget(self.centralwidget)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setGeometry(QRect(0, 0, 791, 71))
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
        self.lb_title.setGeometry(QRect(-1, 10, 791, 30))
        self.lb_title.setStyleSheet(u"")
        self.lb_title.setAlignment(Qt.AlignCenter)
        self.lb_sub_title = QLabel(self.top_bar)
        self.lb_sub_title.setObjectName(u"lb_sub_title")
        self.lb_sub_title.setGeometry(QRect(0, 35, 791, 25))
        self.lb_sub_title.setStyleSheet(u"")
        self.lb_sub_title.setAlignment(Qt.AlignCenter)
        self.lb_sub_title.raise_()
        self.lb_title.raise_()
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(20, 80, 751, 581))
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.info_frame = QFrame(self.page_1)
        self.info_frame.setObjectName(u"info_frame")
        self.info_frame.setGeometry(QRect(10, 10, 731, 291))
        self.info_frame.setStyleSheet(u"#info_frame {\n"
"	background-color: white;\n"
"	border-radius: 15px;\n"
"}")
        self.info_frame.setFrameShape(QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.set_building = QWidget(self.info_frame)
        self.set_building.setObjectName(u"set_building")
        self.set_building.setGeometry(QRect(20, 190, 681, 71))
        self.hint_1 = QLabel(self.set_building)
        self.hint_1.setObjectName(u"hint_1")
        self.hint_1.setGeometry(QRect(100, 0, 41, 30))
        font = QFont()
        font.setFamilies([u"\uc6f0\ucef4\uccb4 Regular"])
        font.setBold(False)
        font.setItalic(False)
        self.hint_1.setFont(font)
        self.hint_1.setStyleSheet(u"QLabel { color: rgb(125,125,125) }")
        self.hint_1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.cbx_purposes = QComboBox(self.set_building)
        self.cbx_purposes.setObjectName(u"cbx_purposes")
        self.cbx_purposes.setGeometry(QRect(160, 40, 231, 30))
        self.cbx_purposes.setMinimumSize(QSize(62, 0))
        self.cbx_purposes.setMaximumSize(QSize(1666, 16777215))
        self.cbx_purposes.setStyleSheet(u"QListView {\n"
"	margin-top: 2px;\n"
"}")
        self.cbx_structure = QComboBox(self.set_building)
        self.cbx_structure.setObjectName(u"cbx_structure")
        self.cbx_structure.setGeometry(QRect(160, 0, 231, 30))
        self.cbx_structure.setMinimumSize(QSize(62, 0))
        self.cbx_structure.setMaximumSize(QSize(1666, 16777215))
        self.cbx_structure.setStyleSheet(u"QListView {\n"
"	margin-top: 2px;\n"
"}")
        self.hint_2 = QLabel(self.set_building)
        self.hint_2.setObjectName(u"hint_2")
        self.hint_2.setGeometry(QRect(100, 40, 41, 30))
        self.hint_2.setFont(font)
        self.hint_2.setStyleSheet(u"QLabel { color: rgb(125,125,125) }")
        self.hint_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.name_bld = QLabel(self.set_building)
        self.name_bld.setObjectName(u"name_bld")
        self.name_bld.setGeometry(QRect(10, 20, 71, 29))
        self.name_bld.setFont(font)
        self.name_bld.setStyleSheet(u"")
        self.f_area_total = QFrame(self.set_building)
        self.f_area_total.setObjectName(u"f_area_total")
        self.f_area_total.setGeometry(QRect(430, 0, 251, 31))
        self.f_area_total.setFrameShape(QFrame.StyledPanel)
        self.f_area_total.setFrameShadow(QFrame.Raised)
        self.lb_unit_3 = QLabel(self.f_area_total)
        self.lb_unit_3.setObjectName(u"lb_unit_3")
        self.lb_unit_3.setGeometry(QRect(227, 4, 20, 22))
        self.lb_unit_3.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(125,125,125);\n"
"	padding-top: 3px;\n"
"}")
        self.lb_unit_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.name_area_total = QLabel(self.f_area_total)
        self.name_area_total.setObjectName(u"name_area_total")
        self.name_area_total.setGeometry(QRect(3, 1, 60, 29))
        self.name_area_total.setFont(font)
        self.name_area_total.setStyleSheet(u"")
        self.edt_area_total = QLineEdit(self.f_area_total)
        self.edt_area_total.setObjectName(u"edt_area_total")
        self.edt_area_total.setEnabled(True)
        self.edt_area_total.setGeometry(QRect(120, 0, 131, 30))
        self.edt_area_total.setStyleSheet(u"QLineEdit {\n"
"	padding-right: 25px;\n"
"}")
        self.edt_area_total.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.edt_area_total.raise_()
        self.lb_unit_3.raise_()
        self.name_area_total.raise_()
        self.set_land = QWidget(self.info_frame)
        self.set_land.setObjectName(u"set_land")
        self.set_land.setGeometry(QRect(20, 150, 691, 31))
        self.set_land.setMinimumSize(QSize(0, 31))
        self.set_land.setMaximumSize(QSize(16777215, 31))
        self.cbx_land = QComboBox(self.set_land)
        self.cbx_land.addItem("")
        self.cbx_land.addItem("")
        self.cbx_land.setObjectName(u"cbx_land")
        self.cbx_land.setGeometry(QRect(100, 0, 100, 30))
        self.cbx_land.setMinimumSize(QSize(62, 0))
        self.cbx_land.setMaximumSize(QSize(100, 16777215))
        self.cbx_land.setStyleSheet(u"QListView {\n"
"	margin-top: 2px;\n"
"}")
        self.cbx_land.setIconSize(QSize(0, 0))
        self.cbx_land_details = QComboBox(self.set_land)
        self.cbx_land_details.setObjectName(u"cbx_land_details")
        self.cbx_land_details.setGeometry(QRect(210, 0, 181, 30))
        self.cbx_land_details.setMinimumSize(QSize(62, 0))
        self.cbx_land_details.setMaximumSize(QSize(1677, 16777215))
        self.cbx_land_details.setStyleSheet(u"QListView {\n"
"	margin-top: 2px;\n"
"}")
        self.name_land = QLabel(self.set_land)
        self.name_land.setObjectName(u"name_land")
        self.name_land.setGeometry(QRect(10, 1, 71, 29))
        self.name_land.setFont(font)
        self.name_land.setStyleSheet(u"")
        self.f_area_land = QFrame(self.set_land)
        self.f_area_land.setObjectName(u"f_area_land")
        self.f_area_land.setGeometry(QRect(430, 0, 251, 31))
        self.f_area_land.setFrameShape(QFrame.StyledPanel)
        self.f_area_land.setFrameShadow(QFrame.Raised)
        self.hint_area_land = QLabel(self.f_area_land)
        self.hint_area_land.setObjectName(u"hint_area_land")
        self.hint_area_land.setGeometry(QRect(227, 4, 20, 22))
        self.hint_area_land.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(125,125,125);\n"
"	padding-top: 3px;\n"
"}")
        self.hint_area_land.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.name_area_land = QLabel(self.f_area_land)
        self.name_area_land.setObjectName(u"name_area_land")
        self.name_area_land.setGeometry(QRect(3, 1, 60, 29))
        self.name_area_land.setFont(font)
        self.name_area_land.setStyleSheet(u"")
        self.edt_area_land = QLineEdit(self.f_area_land)
        self.edt_area_land.setObjectName(u"edt_area_land")
        self.edt_area_land.setEnabled(True)
        self.edt_area_land.setGeometry(QRect(120, 0, 131, 30))
        self.edt_area_land.setStyleSheet(u"QLineEdit {\n"
"	padding-right: 25px;\n"
"}")
        self.edt_area_land.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.edt_area_land.raise_()
        self.hint_area_land.raise_()
        self.name_area_land.raise_()
        self.f_ratio = QWidget(self.info_frame)
        self.f_ratio.setObjectName(u"f_ratio")
        self.f_ratio.setGeometry(QRect(20, 110, 691, 31))
        self.f_ratio.setMinimumSize(QSize(0, 31))
        self.f_ratio.setMaximumSize(QSize(16777215, 31))
        self.edt_ratio_1 = QLineEdit(self.f_ratio)
        self.edt_ratio_1.setObjectName(u"edt_ratio_1")
        self.edt_ratio_1.setEnabled(True)
        self.edt_ratio_1.setGeometry(QRect(100, 0, 121, 30))
        self.edt_ratio_1.setStyleSheet(u"QLineEdit { padding-right: 0px;}")
        self.edt_ratio_1.setAlignment(Qt.AlignCenter)
        self.name_ratio = QLabel(self.f_ratio)
        self.name_ratio.setObjectName(u"name_ratio")
        self.name_ratio.setGeometry(QRect(10, 1, 71, 29))
        self.name_ratio.setFont(font)
        self.name_ratio.setStyleSheet(u"")
        self.name_ratio_2 = QLabel(self.f_ratio)
        self.name_ratio_2.setObjectName(u"name_ratio_2")
        self.name_ratio_2.setGeometry(QRect(230, 0, 31, 29))
        self.name_ratio_2.setFont(font)
        self.name_ratio_2.setStyleSheet(u"")
        self.edt_ratio_2 = QLineEdit(self.f_ratio)
        self.edt_ratio_2.setObjectName(u"edt_ratio_2")
        self.edt_ratio_2.setEnabled(True)
        self.edt_ratio_2.setGeometry(QRect(270, 0, 121, 30))
        self.edt_ratio_2.setStyleSheet(u"QLineEdit { padding-right: 0px;}")
        self.edt_ratio_2.setAlignment(Qt.AlignCenter)
        self.f_land_type = QFrame(self.f_ratio)
        self.f_land_type.setObjectName(u"f_land_type")
        self.f_land_type.setGeometry(QRect(430, 0, 251, 31))
        self.f_land_type.setFrameShape(QFrame.StyledPanel)
        self.f_land_type.setFrameShadow(QFrame.Raised)
        self.name_land_type = QLabel(self.f_land_type)
        self.name_land_type.setObjectName(u"name_land_type")
        self.name_land_type.setGeometry(QRect(3, 1, 71, 29))
        self.name_land_type.setFont(font)
        self.name_land_type.setStyleSheet(u"")
        self.cbx_land_type = QComboBox(self.f_land_type)
        self.cbx_land_type.addItem("")
        self.cbx_land_type.addItem("")
        self.cbx_land_type.addItem("")
        self.cbx_land_type.addItem("")
        self.cbx_land_type.addItem("")
        self.cbx_land_type.addItem("")
        self.cbx_land_type.setObjectName(u"cbx_land_type")
        self.cbx_land_type.setGeometry(QRect(120, 0, 131, 30))
        self.cbx_land_type.setMinimumSize(QSize(62, 0))
        self.cbx_land_type.setMaximumSize(QSize(1677, 16777215))
        self.cbx_land_type.setStyleSheet(u"QListView {\n"
"	margin-top: 2px;\n"
"}")
        self.f_address = QWidget(self.info_frame)
        self.f_address.setObjectName(u"f_address")
        self.f_address.setGeometry(QRect(20, 30, 681, 31))
        self.f_address.setMinimumSize(QSize(0, 31))
        self.f_address.setMaximumSize(QSize(16777215, 31))
        self.edt_address = QLineEdit(self.f_address)
        self.edt_address.setObjectName(u"edt_address")
        self.edt_address.setEnabled(True)
        self.edt_address.setGeometry(QRect(100, 0, 581, 30))
        self.name_address = QLabel(self.f_address)
        self.name_address.setObjectName(u"name_address")
        self.name_address.setGeometry(QRect(10, 1, 61, 29))
        self.name_address.setFont(font)
        self.name_address.setStyleSheet(u"")
        self.f_rantal = QWidget(self.info_frame)
        self.f_rantal.setObjectName(u"f_rantal")
        self.f_rantal.setGeometry(QRect(20, 70, 681, 31))
        self.f_rantal.setMinimumSize(QSize(0, 31))
        self.f_rantal.setMaximumSize(QSize(16777215, 31))
        self.edt_address_details = QLineEdit(self.f_rantal)
        self.edt_address_details.setObjectName(u"edt_address_details")
        self.edt_address_details.setEnabled(True)
        self.edt_address_details.setGeometry(QRect(100, 0, 291, 30))
        self.edt_address_details.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.name_address_details = QLabel(self.f_rantal)
        self.name_address_details.setObjectName(u"name_address_details")
        self.name_address_details.setGeometry(QRect(10, 1, 71, 29))
        self.name_address_details.setFont(font)
        self.name_address_details.setStyleSheet(u"")
        self.f_area_rental = QFrame(self.f_rantal)
        self.f_area_rental.setObjectName(u"f_area_rental")
        self.f_area_rental.setGeometry(QRect(430, 0, 251, 31))
        self.f_area_rental.setFrameShape(QFrame.StyledPanel)
        self.f_area_rental.setFrameShadow(QFrame.Raised)
        self.hint_area_rental = QLabel(self.f_area_rental)
        self.hint_area_rental.setObjectName(u"hint_area_rental")
        self.hint_area_rental.setGeometry(QRect(227, 4, 20, 22))
        self.hint_area_rental.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(125,125,125);\n"
"	padding-top: 3px;\n"
"}")
        self.hint_area_rental.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.name_area_rental = QLabel(self.f_area_rental)
        self.name_area_rental.setObjectName(u"name_area_rental")
        self.name_area_rental.setGeometry(QRect(3, 1, 60, 29))
        self.name_area_rental.setFont(font)
        self.name_area_rental.setStyleSheet(u"")
        self.edt_area_rental = QLineEdit(self.f_area_rental)
        self.edt_area_rental.setObjectName(u"edt_area_rental")
        self.edt_area_rental.setEnabled(True)
        self.edt_area_rental.setGeometry(QRect(120, 0, 131, 30))
        self.edt_area_rental.setStyleSheet(u"QLineEdit {\n"
"	padding-right: 25px;\n"
"}")
        self.edt_area_rental.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.edt_area_rental.raise_()
        self.hint_area_rental.raise_()
        self.name_area_rental.raise_()
        self.money_frame = QFrame(self.page_1)
        self.money_frame.setObjectName(u"money_frame")
        self.money_frame.setGeometry(QRect(10, 320, 731, 251))
        self.money_frame.setStyleSheet(u"#money_frame {\n"
"	background-color: white;\n"
"	border-radius: 15px;\n"
"}")
        self.money_frame.setFrameShape(QFrame.StyledPanel)
        self.money_frame.setFrameShadow(QFrame.Raised)
        self.name_price = QLabel(self.money_frame)
        self.name_price.setObjectName(u"name_price")
        self.name_price.setGeometry(QRect(30, 30, 60, 30))
        self.name_price.setFont(font)
        self.name_price.setStyleSheet(u"")
        self.lb_price_5 = QLabel(self.money_frame)
        self.lb_price_5.setObjectName(u"lb_price_5")
        self.lb_price_5.setGeometry(QRect(376, 194, 31, 22))
        self.lb_price_5.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(125,125,125);\n"
"	padding-top: 3px;\n"
"}")
        self.lb_price_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.btn_balance_cal = QPushButton(self.money_frame)
        self.btn_balance_cal.setObjectName(u"btn_balance_cal")
        self.btn_balance_cal.setGeometry(QRect(670, 191, 28, 28))
        self.btn_balance_cal.setStyleSheet(u"QPushButton {\n"
"	border-radius: 4px;\n"
"	padding-top: 2px;\n"
"	padding-left: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(235, 235, 235);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(215, 215, 215);\n"
"	padding-top: 3px;\n"
"	padding-left: 3px;\n"
"}")
        self.lb_price_1 = QLabel(self.money_frame)
        self.lb_price_1.setObjectName(u"lb_price_1")
        self.lb_price_1.setGeometry(QRect(376, 34, 31, 22))
        self.lb_price_1.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(125,125,125);\n"
"	padding-top: 3px;\n"
"}")
        self.lb_price_1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.edt_down_pay = QLineEdit(self.money_frame)
        self.edt_down_pay.setObjectName(u"edt_down_pay")
        self.edt_down_pay.setGeometry(QRect(240, 70, 171, 30))
        self.edt_down_pay.setStyleSheet(u"QLineEdit {\n"
"	padding-right: 35px;\n"
"}")
        self.edt_down_pay.setMaxLength(15)
        self.edt_down_pay.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.edt_down_pay.setReadOnly(True)
        self.edt_balance_pay = QLineEdit(self.money_frame)
        self.edt_balance_pay.setObjectName(u"edt_balance_pay")
        self.edt_balance_pay.setGeometry(QRect(120, 190, 291, 30))
        self.edt_balance_pay.setStyleSheet(u"QLineEdit {\n"
"	padding-right: 35px;\n"
"}")
        self.edt_balance_pay.setMaxLength(15)
        self.edt_balance_pay.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.edt_balance_pay.setReadOnly(True)
        self.lb_korean_1st = QLineEdit(self.money_frame)
        self.lb_korean_1st.setObjectName(u"lb_korean_1st")
        self.lb_korean_1st.setGeometry(QRect(124, 114, 171, 22))
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
        self.lb_item_nm_14.setGeometry(QRect(450, 110, 71, 30))
        self.lb_item_nm_14.setFont(font)
        self.lb_item_nm_14.setStyleSheet(u"")
        self.lb_korean_2st = QLineEdit(self.money_frame)
        self.lb_korean_2st.setObjectName(u"lb_korean_2st")
        self.lb_korean_2st.setGeometry(QRect(124, 154, 171, 22))
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
        self.edt_1st_day.setGeometry(QRect(540, 110, 121, 30))
        self.edt_1st_day.setStyleSheet(u"QLineEdit {\n"
"	padding-right: 0px;\n"
"}")
        self.edt_1st_day.setAlignment(Qt.AlignCenter)
        self.edt_1st_day.setReadOnly(True)
        self.set_sub_1 = QWidget(self.money_frame)
        self.set_sub_1.setObjectName(u"set_sub_1")
        self.set_sub_1.setGeometry(QRect(450, 30, 251, 31))
        self.lb_price_sub_1 = QLabel(self.set_sub_1)
        self.lb_price_sub_1.setObjectName(u"lb_price_sub_1")
        self.lb_price_sub_1.setGeometry(QRect(217, 4, 31, 22))
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
        self.edt_sub_1.setGeometry(QRect(90, 0, 161, 30))
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
        self.edt_2st_day.setGeometry(QRect(540, 150, 121, 30))
        self.edt_2st_day.setStyleSheet(u"QLineEdit {\n"
"	padding-right: 0px;\n"
"}")
        self.edt_2st_day.setAlignment(Qt.AlignCenter)
        self.edt_2st_day.setReadOnly(True)
        self.lb_item_nm_10 = QLabel(self.money_frame)
        self.lb_item_nm_10.setObjectName(u"lb_item_nm_10")
        self.lb_item_nm_10.setGeometry(QRect(30, 131, 60, 30))
        self.lb_item_nm_10.setFont(font)
        self.lb_item_nm_10.setStyleSheet(u"")
        self.btn_2st_cal = QPushButton(self.money_frame)
        self.btn_2st_cal.setObjectName(u"btn_2st_cal")
        self.btn_2st_cal.setGeometry(QRect(670, 151, 28, 28))
        self.btn_2st_cal.setStyleSheet(u"QPushButton {\n"
"	border-radius: 4px;\n"
"	padding-top: 2px;\n"
"	padding-left: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(235, 235, 235);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(215, 215, 215);\n"
"	padding-top: 3px;\n"
"	padding-left: 3px;\n"
"}")
        self.set_sub_2 = QWidget(self.money_frame)
        self.set_sub_2.setObjectName(u"set_sub_2")
        self.set_sub_2.setGeometry(QRect(450, 70, 251, 31))
        self.lb_price_sub_2 = QLabel(self.set_sub_2)
        self.lb_price_sub_2.setObjectName(u"lb_price_sub_2")
        self.lb_price_sub_2.setGeometry(QRect(217, 4, 31, 22))
        self.lb_price_sub_2.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(125,125,125);\n"
"	padding-top: 3px;\n"
"}")
        self.lb_price_sub_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.edt_sub_2 = QLineEdit(self.set_sub_2)
        self.edt_sub_2.setObjectName(u"edt_sub_2")
        self.edt_sub_2.setEnabled(True)
        self.edt_sub_2.setGeometry(QRect(90, 0, 161, 30))
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
        self.lb_item_nm_27.setGeometry(QRect(30, 191, 71, 29))
        self.lb_item_nm_27.setFont(font)
        self.lb_item_nm_27.setStyleSheet(u"")
        self.lb_korean_amount = QLineEdit(self.money_frame)
        self.lb_korean_amount.setObjectName(u"lb_korean_amount")
        self.lb_korean_amount.setGeometry(QRect(124, 34, 171, 22))
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
        self.lb_item_nm_16.setGeometry(QRect(450, 190, 60, 30))
        self.lb_item_nm_16.setFont(font)
        self.lb_item_nm_16.setStyleSheet(u"")
        self.edt_mid_pay_2st = QLineEdit(self.money_frame)
        self.edt_mid_pay_2st.setObjectName(u"edt_mid_pay_2st")
        self.edt_mid_pay_2st.setGeometry(QRect(120, 150, 291, 30))
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
        self.cbx_down_pay.setGeometry(QRect(120, 70, 100, 30))
        self.cbx_down_pay.setMinimumSize(QSize(62, 0))
        self.cbx_down_pay.setMaximumSize(QSize(100, 16777215))
        self.cbx_down_pay.setStyleSheet(u"QListView {\n"
"	margin-top: 2px;\n"
"}")
        self.lb_price_3 = QLabel(self.money_frame)
        self.lb_price_3.setObjectName(u"lb_price_3")
        self.lb_price_3.setGeometry(QRect(376, 114, 31, 22))
        self.lb_price_3.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(125,125,125);\n"
"	padding-top: 3px;\n"
"}")
        self.lb_price_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.btn_1st_cal = QPushButton(self.money_frame)
        self.btn_1st_cal.setObjectName(u"btn_1st_cal")
        self.btn_1st_cal.setGeometry(QRect(670, 111, 28, 28))
        self.btn_1st_cal.setStyleSheet(u"QPushButton {\n"
"	border-radius: 4px;\n"
"	padding-top: 2px;\n"
"	padding-left: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(235, 235, 235);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(215, 215, 215);\n"
"	padding-top: 3px;\n"
"	padding-left: 3px;\n"
"}")
        self.lb_item_nm_9 = QLabel(self.money_frame)
        self.lb_item_nm_9.setObjectName(u"lb_item_nm_9")
        self.lb_item_nm_9.setGeometry(QRect(30, 70, 81, 30))
        self.lb_item_nm_9.setFont(font)
        self.lb_item_nm_9.setStyleSheet(u"")
        self.edt_price = QLineEdit(self.money_frame)
        self.edt_price.setObjectName(u"edt_price")
        self.edt_price.setGeometry(QRect(120, 30, 291, 30))
        self.edt_price.setStyleSheet(u"QLineEdit {\n"
"	padding-right: 35px;\n"
"}")
        self.edt_price.setMaxLength(15)
        self.edt_price.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.edt_balance_day = QLineEdit(self.money_frame)
        self.edt_balance_day.setObjectName(u"edt_balance_day")
        self.edt_balance_day.setEnabled(True)
        self.edt_balance_day.setGeometry(QRect(540, 190, 121, 30))
        self.edt_balance_day.setStyleSheet(u"QLineEdit {\n"
"	padding-right: 0px;\n"
"}")
        self.edt_balance_day.setAlignment(Qt.AlignCenter)
        self.edt_balance_day.setReadOnly(True)
        self.lb_item_nm_15 = QLabel(self.money_frame)
        self.lb_item_nm_15.setObjectName(u"lb_item_nm_15")
        self.lb_item_nm_15.setGeometry(QRect(450, 150, 71, 30))
        self.lb_item_nm_15.setFont(font)
        self.lb_item_nm_15.setStyleSheet(u"")
        self.edt_mid_pay_1st = QLineEdit(self.money_frame)
        self.edt_mid_pay_1st.setObjectName(u"edt_mid_pay_1st")
        self.edt_mid_pay_1st.setGeometry(QRect(120, 110, 291, 30))
        self.edt_mid_pay_1st.setStyleSheet(u"QLineEdit {\n"
"	padding-right: 35px;\n"
"}")
        self.edt_mid_pay_1st.setMaxLength(15)
        self.edt_mid_pay_1st.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lb_korean_balance = QLineEdit(self.money_frame)
        self.lb_korean_balance.setObjectName(u"lb_korean_balance")
        self.lb_korean_balance.setGeometry(QRect(124, 194, 171, 22))
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
        self.lb_price_2.setGeometry(QRect(376, 74, 31, 22))
        self.lb_price_2.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(125,125,125);\n"
"	padding-top: 3px;\n"
"}")
        self.lb_price_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lb_price_4 = QLabel(self.money_frame)
        self.lb_price_4.setObjectName(u"lb_price_4")
        self.lb_price_4.setGeometry(QRect(376, 154, 31, 22))
        self.lb_price_4.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(125,125,125);\n"
"	padding-top: 3px;\n"
"}")
        self.lb_price_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.edt_balance_pay.raise_()
        self.edt_mid_pay_2st.raise_()
        self.edt_mid_pay_1st.raise_()
        self.edt_price.raise_()
        self.name_price.raise_()
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
        self.my_sc_frame = QFrame(self.page_2)
        self.my_sc_frame.setObjectName(u"my_sc_frame")
        self.my_sc_frame.setGeometry(QRect(10, 10, 731, 91))
        self.my_sc_frame.setStyleSheet(u"#my_sc_frame {\n"
"	background-color: white;\n"
"	border-radius: 15px;\n"
"}")
        self.my_sc_frame.setFrameShape(QFrame.StyledPanel)
        self.my_sc_frame.setFrameShadow(QFrame.Raised)
        self.lb_item_nm_11 = QLabel(self.my_sc_frame)
        self.lb_item_nm_11.setObjectName(u"lb_item_nm_11")
        self.lb_item_nm_11.setGeometry(QRect(30, 30, 60, 30))
        self.lb_item_nm_11.setFont(font)
        self.lb_item_nm_11.setStyleSheet(u"")
        self.cbx_title = QComboBox(self.my_sc_frame)
        self.cbx_title.addItem("")
        self.cbx_title.setObjectName(u"cbx_title")
        self.cbx_title.setGeometry(QRect(300, 30, 311, 30))
        self.cbx_title.setStyleSheet(u"QListView {\n"
"	margin-top: 2px;\n"
"}")
        self.cbx_category = QComboBox(self.my_sc_frame)
        self.cbx_category.addItem("")
        self.cbx_category.setObjectName(u"cbx_category")
        self.cbx_category.setGeometry(QRect(120, 30, 171, 30))
        self.cbx_category.setStyleSheet(u"QListView {\n"
"	margin-top: 2px;\n"
"}")
        self.cbx_category.setIconSize(QSize(0, 0))
        self.btn_agr_edit = QPushButton(self.my_sc_frame)
        self.btn_agr_edit.setObjectName(u"btn_agr_edit")
        self.btn_agr_edit.setGeometry(QRect(630, 30, 81, 30))
        self.btn_agr_edit.setStyleSheet(u"QPushButton {\n"
"    font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
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
"    background-color: rgb(250,250,250);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(166, 168, 171);\n"
"}")
        self.sc_frame = QFrame(self.page_2)
        self.sc_frame.setObjectName(u"sc_frame")
        self.sc_frame.setGeometry(QRect(10, 120, 731, 451))
        self.sc_frame.setStyleSheet(u"#sc_frame {\n"
"	background-color: white;\n"
"	border-radius: 15px;\n"
"}")
        self.sc_frame.setFrameShape(QFrame.StyledPanel)
        self.sc_frame.setFrameShadow(QFrame.Raised)
        self.edt_agrs = QTextEdit(self.sc_frame)
        self.edt_agrs.setObjectName(u"edt_agrs")
        self.edt_agrs.setGeometry(QRect(20, 20, 691, 411))
        self.edt_agrs.setStyleSheet(u"QTextEdit {\n"
"	font: bold 15px;\n"
"	color: rgb(65,65,65);\n"
"	border: 1px solid rgb(130,130,130);\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QTextEdit:focus{\n"
"	color:  rgb(65,65,65);\n"
"	border: 1px solid rgb(148,148,255);\n"
"	border-radius: 2px;\n"
"	padding-right: 21px;\n"
"}")
        self.stackedWidget.addWidget(self.page_2)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.agrs_frame = QFrame(self.page_4)
        self.agrs_frame.setObjectName(u"agrs_frame")
        self.agrs_frame.setGeometry(QRect(10, 10, 731, 561))
        self.agrs_frame.setStyleSheet(u"#agrs_frame {\n"
"	background-color: white;\n"
"	border-radius: 15px;\n"
"}")
        self.btn_add_c = QPushButton(self.agrs_frame)
        self.btn_add_c.setObjectName(u"btn_add_c")
        self.btn_add_c.setGeometry(QRect(600, 30, 111, 30))
        self.btn_add_c.setStyleSheet(u"QPushButton {\n"
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
"    font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
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
"    background-color: rgb(250,250,250);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(166, 168, 171);\n"
"}")
        self.lst_contractor = QListWidget(self.agrs_frame)
        self.lst_contractor.setObjectName(u"lst_contractor")
        self.lst_contractor.setGeometry(QRect(20, 80, 691, 461))
        self.lst_contractor.setStyleSheet(u"QListWidget {\n"
"	outline: none;\n"
"	border: none;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"	border: none;\n"
"}\n"
"")
        self.lst_contractor.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.lst_contractor.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.btn_add_b = QPushButton(self.agrs_frame)
        self.btn_add_b.setObjectName(u"btn_add_b")
        self.btn_add_b.setGeometry(QRect(484, 30, 111, 30))
        self.btn_add_b.setStyleSheet(u"QPushButton {\n"
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
"    font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
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
"    background-color: rgb(250,250,250);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(166, 168, 171);\n"
"}")
        self.btn_add_a = QPushButton(self.agrs_frame)
        self.btn_add_a.setObjectName(u"btn_add_a")
        self.btn_add_a.setGeometry(QRect(368, 30, 111, 30))
        self.btn_add_a.setStyleSheet(u"QPushButton {\n"
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
"    font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
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
"    background-color: rgb(250,250,250);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(166, 168, 171);\n"
"}")
        self.lst_contractor.raise_()
        self.btn_add_c.raise_()
        self.btn_add_b.raise_()
        self.btn_add_a.raise_()
        self.stackedWidget.addWidget(self.page_4)
        self.btn_provisions = QPushButton(self.centralwidget)
        self.btn_provisions.setObjectName(u"btn_provisions")
        self.btn_provisions.setGeometry(QRect(40, 695, 111, 31))
        self.btn_provisions.setStyleSheet(u"QPushButton {\n"
"    font: 15px \"\uc6f0\ucef4\uccb4 Regular\";\n"
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
        self.btn_next = QPushButton(self.centralwidget)
        self.btn_next.setObjectName(u"btn_next")
        self.btn_next.setGeometry(QRect(640, 690, 111, 41))
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
        self.btn_back = QPushButton(self.centralwidget)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(520, 690, 111, 41))
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
"    background-color: rgb(250,250,250);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(166, 168, 171);\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.edt_address, self.edt_address_details)
        QWidget.setTabOrder(self.edt_address_details, self.edt_ratio_1)
        QWidget.setTabOrder(self.edt_ratio_1, self.edt_ratio_2)
        QWidget.setTabOrder(self.edt_ratio_2, self.cbx_land)
        QWidget.setTabOrder(self.cbx_land, self.cbx_land_details)
        QWidget.setTabOrder(self.cbx_land_details, self.cbx_structure)
        QWidget.setTabOrder(self.cbx_structure, self.cbx_purposes)
        QWidget.setTabOrder(self.cbx_purposes, self.edt_area_rental)
        QWidget.setTabOrder(self.edt_area_rental, self.cbx_land_type)
        QWidget.setTabOrder(self.cbx_land_type, self.edt_area_land)
        QWidget.setTabOrder(self.edt_area_land, self.edt_area_total)
        QWidget.setTabOrder(self.edt_area_total, self.edt_price)
        QWidget.setTabOrder(self.edt_price, self.cbx_down_pay)
        QWidget.setTabOrder(self.cbx_down_pay, self.edt_down_pay)
        QWidget.setTabOrder(self.edt_down_pay, self.edt_mid_pay_1st)
        QWidget.setTabOrder(self.edt_mid_pay_1st, self.edt_mid_pay_2st)
        QWidget.setTabOrder(self.edt_mid_pay_2st, self.edt_balance_pay)
        QWidget.setTabOrder(self.edt_balance_pay, self.edt_sub_1)
        QWidget.setTabOrder(self.edt_sub_1, self.edt_sub_2)
        QWidget.setTabOrder(self.edt_sub_2, self.edt_1st_day)
        QWidget.setTabOrder(self.edt_1st_day, self.edt_2st_day)
        QWidget.setTabOrder(self.edt_2st_day, self.edt_balance_day)
        QWidget.setTabOrder(self.edt_balance_day, self.btn_1st_cal)
        QWidget.setTabOrder(self.btn_1st_cal, self.btn_2st_cal)
        QWidget.setTabOrder(self.btn_2st_cal, self.btn_balance_cal)
        QWidget.setTabOrder(self.btn_balance_cal, self.lb_korean_amount)
        QWidget.setTabOrder(self.lb_korean_amount, self.lb_korean_1st)
        QWidget.setTabOrder(self.lb_korean_1st, self.lb_korean_2st)
        QWidget.setTabOrder(self.lb_korean_2st, self.lb_korean_balance)
        QWidget.setTabOrder(self.lb_korean_balance, self.btn_provisions)
        QWidget.setTabOrder(self.btn_provisions, self.btn_back)
        QWidget.setTabOrder(self.btn_back, self.btn_next)
        QWidget.setTabOrder(self.btn_next, self.cbx_category)
        QWidget.setTabOrder(self.cbx_category, self.cbx_title)
        QWidget.setTabOrder(self.cbx_title, self.btn_agr_edit)
        QWidget.setTabOrder(self.btn_agr_edit, self.edt_agrs)
        QWidget.setTabOrder(self.edt_agrs, self.btn_add_a)
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
        self.hint_1.setText(QCoreApplication.translate("MainWindow", u"\uad6c    \uc870", None))
        self.hint_2.setText(QCoreApplication.translate("MainWindow", u"\uc6a9    \ub3c4", None))
        self.name_bld.setText(QCoreApplication.translate("MainWindow", u"\uac74 \ubb3c", None))
        self.lb_unit_3.setText(QCoreApplication.translate("MainWindow", u"\u33a1", None))
        self.name_area_total.setText(QCoreApplication.translate("MainWindow", u"\uc5f0 \uba74\uc801", None))
        self.cbx_land.setItemText(0, QCoreApplication.translate("MainWindow", u"\uc9c0\ubaa9", None))
        self.cbx_land.setItemText(1, QCoreApplication.translate("MainWindow", u"\ub300\ud45c\uc9c0\ubaa9", None))

        self.name_land.setText(QCoreApplication.translate("MainWindow", u"\ud1a0 \uc9c0", None))
        self.hint_area_land.setText(QCoreApplication.translate("MainWindow", u"\u33a1", None))
        self.name_area_land.setText(QCoreApplication.translate("MainWindow", u"\ub300\uc9c0 \uba74\uc801", None))
        self.edt_ratio_1.setText("")
        self.name_ratio.setText(QCoreApplication.translate("MainWindow", u"\ub300\uc9c0\uad8c \ube44\uc728", None))
        self.name_ratio_2.setText(QCoreApplication.translate("MainWindow", u"\ubd84\uc758", None))
        self.edt_ratio_2.setText("")
        self.name_land_type.setText(QCoreApplication.translate("MainWindow", u"\ub300\uc9c0\uad8c \uc885\ub958", None))
        self.cbx_land_type.setItemText(0, QCoreApplication.translate("MainWindow", u"\uc18c\uc720\uad8c", None))
        self.cbx_land_type.setItemText(1, QCoreApplication.translate("MainWindow", u"\uc784\ucc28\uad8c", None))
        self.cbx_land_type.setItemText(2, QCoreApplication.translate("MainWindow", u"\uc804\uc138\uad8c", None))
        self.cbx_land_type.setItemText(3, QCoreApplication.translate("MainWindow", u"\uc9c0\uc0c1\uad8c", None))
        self.cbx_land_type.setItemText(4, QCoreApplication.translate("MainWindow", u"\uc0ac\uc6a9\ucc28\uad8c", None))
        self.cbx_land_type.setItemText(5, QCoreApplication.translate("MainWindow", u"( \uc9c1\uc811\uc785\ub825 )", None))

        self.name_address.setText(QCoreApplication.translate("MainWindow", u"\uc18c \uc7ac \uc9c0", None))
        self.edt_address_details.setText("")
        self.name_address_details.setText(QCoreApplication.translate("MainWindow", u"\uc784\ub300\ubd80\ubd84", None))
        self.hint_area_rental.setText(QCoreApplication.translate("MainWindow", u"\u33a1", None))
        self.name_area_rental.setText(QCoreApplication.translate("MainWindow", u"\uc784\ub300 \uba74\uc801", None))
        self.name_price.setText(QCoreApplication.translate("MainWindow", u"\ubcf4 \uc99d \uae08", None))
        self.lb_price_5.setText(QCoreApplication.translate("MainWindow", u"\ub9cc\uc6d0", None))
        self.btn_balance_cal.setText("")
        self.lb_price_1.setText(QCoreApplication.translate("MainWindow", u"\ub9cc\uc6d0", None))
        self.edt_down_pay.setText("")
        self.edt_balance_pay.setText("")
        self.lb_korean_1st.setText("")
        self.lb_item_nm_14.setText(QCoreApplication.translate("MainWindow", u"1\ucc28 \uc9c0\ubd88\uc77c", None))
        self.lb_korean_2st.setText("")
        self.edt_1st_day.setText("")
        self.lb_price_sub_1.setText(QCoreApplication.translate("MainWindow", u"\ub9cc\uc6d0", None))
        self.lb_item_nm_12.setText(QCoreApplication.translate("MainWindow", u"\uc735 \uc790 \uae08", None))
        self.edt_sub_1.setText("")
        self.edt_2st_day.setText("")
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
        self.edt_price.setText("")
        self.edt_balance_day.setText("")
        self.lb_item_nm_15.setText(QCoreApplication.translate("MainWindow", u"2\ucc28 \uc9c0\ubd88\uc77c", None))
        self.edt_mid_pay_1st.setText("")
        self.lb_korean_balance.setText("")
        self.lb_price_2.setText(QCoreApplication.translate("MainWindow", u"\ub9cc\uc6d0", None))
        self.lb_price_4.setText(QCoreApplication.translate("MainWindow", u"\ub9cc\uc6d0", None))
        self.lb_item_nm_11.setText(QCoreApplication.translate("MainWindow", u"\ud2b9\uc57d\uc0ac\ud56d", None))
        self.cbx_title.setItemText(0, QCoreApplication.translate("MainWindow", u"( \ud2b9\uc57d\uc0ac\ud56d \uc120\ud0dd )", None))

        self.cbx_category.setItemText(0, QCoreApplication.translate("MainWindow", u"( \uce74\ud14c\uace0\ub9ac \uc120\ud0dd )", None))

        self.btn_agr_edit.setText(QCoreApplication.translate("MainWindow", u"\ucd94\uac00/\ud3b8\uc9d1", None))
        self.btn_add_c.setText(QCoreApplication.translate("MainWindow", u"\uc911 \uac1c \uc0ac   \ucd94 \uac00", None))
        self.btn_add_b.setText(QCoreApplication.translate("MainWindow", u"\ub9e4 \uc218 \uc778   \ucd94 \uac00", None))
        self.btn_add_a.setText(QCoreApplication.translate("MainWindow", u"\ub9e4 \ub3c4 \uc778   \ucd94 \uac00", None))
        self.btn_provisions.setText(QCoreApplication.translate("MainWindow", u"\uacc4\uc57d \uc870\ud56d \uc218\uc815", None))
        self.btn_next.setText(QCoreApplication.translate("MainWindow", u"\ub2e4 \uc74c", None))
        self.btn_back.setText(QCoreApplication.translate("MainWindow", u"\uc774 \uc804", None))
    # retranslateUi

