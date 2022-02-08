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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_BuildingInfo(object):
    def _setupUi(self, BuildingInfo):
        if not BuildingInfo.objectName():
            BuildingInfo.setObjectName(u"BuildingInfo")
        BuildingInfo.resize(430, 760)
        BuildingInfo.setMinimumSize(QSize(430, 760))
        BuildingInfo.setMaximumSize(QSize(430, 760))
        BuildingInfo.setStyleSheet(u"#BuildingInfo {\n"
"	background-color: white;\n"
"}\n"
"\n"
"QLabel {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(127, 140, 141);\n"
"}")
        self.cbx_rooms = QComboBox(BuildingInfo)
        self.cbx_rooms.addItem("")
        self.cbx_rooms.setObjectName(u"cbx_rooms")
        self.cbx_rooms.setGeometry(QRect(20, 169, 391, 35))
        self.cbx_rooms.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid gray;\n"
"    padding: 3px 1px 1px 5px;\n"
"    min-width: 6em;\n"
"    background: rgb(255, 255, 255);\n"
"    font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"    color: rgb(44, 62, 80);\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    padding: 3px 1px 1px 5px;\n"
"    color: rgb(127, 140, 141);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #3498db;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item { \n"
"	min-height: 30px; \n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 30px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-style: solid;\n"
"    border-left-color: darkgray;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(../../data/img/system/down_arrow_icon.png);\n"
"    width: 22px;\n"
"    height: 22px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:on {\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
""
                        "QComboBox::setView {\n"
"    color: rgb(44, 62, 80);\n"
"    background-color: lightblue\n"
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
"}\n"
"\n"
"comboBox->setView(view);\n"
"QListView::item:selected {\n"
"    color: rgb(44, 62, 80);\n"
"    background-color: lightblue\n"
"}")
        self.line_sub_title_2 = QFrame(BuildingInfo)
        self.line_sub_title_2.setObjectName(u"line_sub_title_2")
        self.line_sub_title_2.setGeometry(QRect(20, 235, 391, 20))
        self.line_sub_title_2.setFrameShape(QFrame.HLine)
        self.line_sub_title_2.setFrameShadow(QFrame.Sunken)
        self.lb_sub_title_2 = QLabel(BuildingInfo)
        self.lb_sub_title_2.setObjectName(u"lb_sub_title_2")
        self.lb_sub_title_2.setGeometry(QRect(25, 225, 91, 16))
        self.lb_sub_title_2.setStyleSheet(u"")
        self.edt_address = QLineEdit(BuildingInfo)
        self.edt_address.setObjectName(u"edt_address")
        self.edt_address.setEnabled(True)
        self.edt_address.setGeometry(QRect(20, 117, 391, 45))
        self.edt_address.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(72,93,114);\n"
"    font: 16px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	border: 2px solid #34495e;\n"
"	padding-top: 3px;\n"
"	padding-left: 10px;\n"
"	padding-right: 70px;\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"	border: 2px solid #3498db;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid #3498db;\n"
"}\n"
"")
        self.edt_address.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lb_sub_title_1 = QLabel(BuildingInfo)
        self.lb_sub_title_1.setObjectName(u"lb_sub_title_1")
        self.lb_sub_title_1.setGeometry(QRect(25, 87, 91, 16))
        self.lb_sub_title_1.setStyleSheet(u"")
        self.line_sub_title_1 = QFrame(BuildingInfo)
        self.line_sub_title_1.setObjectName(u"line_sub_title_1")
        self.line_sub_title_1.setGeometry(QRect(20, 97, 391, 20))
        self.line_sub_title_1.setFrameShape(QFrame.HLine)
        self.line_sub_title_1.setFrameShadow(QFrame.Sunken)
        self.lb_detail_name_2 = QFrame(BuildingInfo)
        self.lb_detail_name_2.setObjectName(u"lb_detail_name_2")
        self.lb_detail_name_2.setGeometry(QRect(20, 583, 391, 20))
        self.lb_detail_name_2.setFrameShape(QFrame.HLine)
        self.lb_detail_name_2.setFrameShadow(QFrame.Sunken)
        self.line_sub_title_3 = QFrame(BuildingInfo)
        self.line_sub_title_3.setObjectName(u"line_sub_title_3")
        self.line_sub_title_3.setGeometry(QRect(440, 97, 381, 20))
        self.line_sub_title_3.setFrameShape(QFrame.HLine)
        self.line_sub_title_3.setFrameShadow(QFrame.Sunken)
        self.lb_sub_title_3 = QLabel(BuildingInfo)
        self.lb_sub_title_3.setObjectName(u"lb_sub_title_3")
        self.lb_sub_title_3.setGeometry(QRect(445, 87, 91, 16))
        self.lb_sub_title_3.setStyleSheet(u"")
        self.lb_sub_title_4 = QLabel(BuildingInfo)
        self.lb_sub_title_4.setObjectName(u"lb_sub_title_4")
        self.lb_sub_title_4.setGeometry(QRect(445, 361, 91, 16))
        self.lb_sub_title_4.setStyleSheet(u"")
        self.line_sub_title_4 = QFrame(BuildingInfo)
        self.line_sub_title_4.setObjectName(u"line_sub_title_4")
        self.line_sub_title_4.setGeometry(QRect(440, 371, 381, 20))
        self.line_sub_title_4.setFrameShape(QFrame.HLine)
        self.line_sub_title_4.setFrameShadow(QFrame.Sunken)
        self.line_sub_title_5 = QFrame(BuildingInfo)
        self.line_sub_title_5.setObjectName(u"line_sub_title_5")
        self.line_sub_title_5.setGeometry(QRect(440, 488, 381, 20))
        self.line_sub_title_5.setFrameShape(QFrame.HLine)
        self.line_sub_title_5.setFrameShadow(QFrame.Sunken)
        self.lb_sub_title_5 = QLabel(BuildingInfo)
        self.lb_sub_title_5.setObjectName(u"lb_sub_title_5")
        self.lb_sub_title_5.setGeometry(QRect(445, 478, 91, 16))
        self.lb_sub_title_5.setStyleSheet(u"")
        self.lb_hint_2 = QLabel(BuildingInfo)
        self.lb_hint_2.setObjectName(u"lb_hint_2")
        self.lb_hint_2.setGeometry(QRect(20, 607, 391, 61))
        self.lb_hint_2.setStyleSheet(u"#lb_hint_2 {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	padding-top: 3px;\n"
"	background-color: rgba(0, 0, 0, 50);\n"
"	color: rgb(80, 80, 80);\n"
"}")
        self.lb_hint_2.setAlignment(Qt.AlignCenter)
        self.top_bar = QWidget(BuildingInfo)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setGeometry(QRect(0, 0, 840, 61))
        self.top_bar.setStyleSheet(u"#top_bar {\n"
"	background-color: rgb(245, 245, 245);\n"
"	border-bottom: 1px solid;\n"
"	border-top: 1px solid;\n"
"	border-color: rgb(230, 230, 230);\n"
"}")
        self.lb_title = QLabel(self.top_bar)
        self.lb_title.setObjectName(u"lb_title")
        self.lb_title.setGeometry(QRect(112, 4, 211, 30))
        self.lb_title.setStyleSheet(u"#lb_title {\n"
"	background-color: rgb(245, 245, 245);\n"
"	font: 25px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgba(0, 0, 0, 120);\n"
"	padding-top: 8px;\n"
"	padding-left: 8px;\n"
"	border: 0px;\n"
"}")
        self.lb_title.setAlignment(Qt.AlignCenter)
        self.lb_sub_title = QLabel(self.top_bar)
        self.lb_sub_title.setObjectName(u"lb_sub_title")
        self.lb_sub_title.setGeometry(QRect(122, 29, 190, 25))
        self.lb_sub_title.setStyleSheet(u"#lb_sub_title {\n"
"	background-color: rgb(245, 245, 245);\n"
"	font: 15px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgba(0, 0, 0, 120);\n"
"	padding-top: 8px;\n"
"	padding-left: 8px;\n"
"	border: 0px;\n"
"}")
        self.lb_sub_title.setAlignment(Qt.AlignCenter)
        self.lb_sub_title.raise_()
        self.lb_title.raise_()
        self.bot_bar = QWidget(BuildingInfo)
        self.bot_bar.setObjectName(u"bot_bar")
        self.bot_bar.setGeometry(QRect(0, 690, 840, 71))
        self.bot_bar.setStyleSheet(u"#bot_bar {\n"
"	background-color: rgb(245, 245, 245);\n"
"	border-top: 1px solid;\n"
"	border-color: rgb(230, 230, 230);\n"
"}")
        self.btn_viol = QPushButton(self.bot_bar)
        self.btn_viol.setObjectName(u"btn_viol")
        self.btn_viol.setGeometry(QRect(20, 20, 141, 31))
        self.btn_viol.setStyleSheet(u"#btn_viol {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: white;\n"
"	border: 0px;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(84,102,120);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"#btn_viol::hover {\n"
"	border: 0px;\n"
"	background-color: rgb(104,122,140);\n"
"	border-style: inset;\n"
"}\n"
"\n"
"#btn_viol:pressed {\n"
"	border: 0px;\n"
"	background-color: rgb(64,82,100);\n"
"	border-style: inset;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"E:/PyProject/Project/REI/building_info/image/bt_search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_viol.setIcon(icon)
        self.btn_viol.setIconSize(QSize(23, 23))
        self.btn_details = QPushButton(self.bot_bar)
        self.btn_details.setObjectName(u"btn_details")
        self.btn_details.setGeometry(QRect(340, 20, 81, 31))
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
"	padding-left: 1px;\n"
"	padding-top: 1px;\n"
"	color: rgb(155, 155, 155);\n"
"	border-style: inset;\n"
"}\n"
"\n"
"#btn_details:pressed {\n"
"	color: rgb(125, 125, 125);\n"
"	border-style: inset;\n"
"}\n"
"")
        self.lb_viol = QLabel(self.bot_bar)
        self.lb_viol.setObjectName(u"lb_viol")
        self.lb_viol.setGeometry(QRect(170, 20, 91, 31))
        self.lb_viol.setStyleSheet(u"#lb_viol { background-color: rgb(245, 245, 245); }")
        self.lb_viol.setAlignment(Qt.AlignCenter)
        self.widget_3 = QWidget(BuildingInfo)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(20, 255, 391, 331))
        self.widget_3.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(44,62,80);\n"
"	padding-top: 4px;\n"
"	border-right: 1px solid;\n"
"	border-bottom: 1px solid;\n"
"	border-color: rgb(210, 210, 210);\n"
"	border-radius: 5px;\n"
"}")
        self.gridLayoutWidget = QWidget(self.widget_3)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 391, 329))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.base_item_11 = QLabel(self.gridLayoutWidget)
        self.base_item_11.setObjectName(u"base_item_11")
        self.base_item_11.setMinimumSize(QSize(0, 30))
        self.base_item_11.setMaximumSize(QSize(16777215, 30))
        self.base_item_11.setStyleSheet(u"QLabel { \n"
"	padding-left: 5px;\n"
"	background-color: rgb(240, 240, 240); \n"
"}")
        self.base_item_11.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.base_item_11, 7, 2, 1, 2)

        self.base_name_12 = QLabel(self.gridLayoutWidget)
        self.base_name_12.setObjectName(u"base_name_12")
        self.base_name_12.setMinimumSize(QSize(0, 30))
        self.base_name_12.setMaximumSize(QSize(16777215, 30))
        self.base_name_12.setStyleSheet(u"")
        self.base_name_12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.base_name_12, 8, 0, 1, 2)

        self.base_name_11 = QLabel(self.gridLayoutWidget)
        self.base_name_11.setObjectName(u"base_name_11")
        self.base_name_11.setMinimumSize(QSize(0, 30))
        self.base_name_11.setMaximumSize(QSize(16777215, 30))
        self.base_name_11.setStyleSheet(u"")
        self.base_name_11.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.base_name_11, 7, 0, 1, 2)

        self.base_name_4 = QLabel(self.gridLayoutWidget)
        self.base_name_4.setObjectName(u"base_name_4")
        self.base_name_4.setMinimumSize(QSize(0, 30))
        self.base_name_4.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamilies([u"\uc6f0\ucef4\uccb4 Regular"])
        font.setBold(False)
        font.setItalic(False)
        self.base_name_4.setFont(font)
        self.base_name_4.setStyleSheet(u"")
        self.base_name_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.base_name_4, 3, 0, 1, 1)

        self.base_name_2 = QLabel(self.gridLayoutWidget)
        self.base_name_2.setObjectName(u"base_name_2")
        self.base_name_2.setMinimumSize(QSize(0, 30))
        self.base_name_2.setMaximumSize(QSize(16777215, 30))
        self.base_name_2.setFont(font)
        self.base_name_2.setStyleSheet(u"")
        self.base_name_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.base_name_2, 1, 0, 1, 1)

        self.base_item_4 = QLabel(self.gridLayoutWidget)
        self.base_item_4.setObjectName(u"base_item_4")
        self.base_item_4.setMinimumSize(QSize(0, 30))
        self.base_item_4.setMaximumSize(QSize(16777215, 30))
        self.base_item_4.setStyleSheet(u"QLabel { \n"
"	padding-left: 5px;\n"
"	background-color: rgb(240, 240, 240); \n"
"}")
        self.base_item_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.base_item_4, 3, 1, 1, 3)

        self.base_name_6 = QLabel(self.gridLayoutWidget)
        self.base_name_6.setObjectName(u"base_name_6")
        self.base_name_6.setMinimumSize(QSize(0, 30))
        self.base_name_6.setMaximumSize(QSize(16777215, 30))
        self.base_name_6.setStyleSheet(u"")
        self.base_name_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.base_name_6, 5, 0, 1, 1)

        self.base_name_13 = QLabel(self.gridLayoutWidget)
        self.base_name_13.setObjectName(u"base_name_13")
        self.base_name_13.setMinimumSize(QSize(0, 30))
        self.base_name_13.setMaximumSize(QSize(16777215, 30))
        self.base_name_13.setStyleSheet(u"")
        self.base_name_13.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.base_name_13, 9, 0, 1, 2)

        self.base_item_12 = QLabel(self.gridLayoutWidget)
        self.base_item_12.setObjectName(u"base_item_12")
        self.base_item_12.setMinimumSize(QSize(0, 30))
        self.base_item_12.setMaximumSize(QSize(16777215, 30))
        self.base_item_12.setStyleSheet(u"QLabel { \n"
"	padding-left: 5px;\n"
"	background-color: rgb(240, 240, 240); \n"
"}")
        self.base_item_12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.base_item_12, 8, 2, 1, 2)

        self.base_name_8 = QLabel(self.gridLayoutWidget)
        self.base_name_8.setObjectName(u"base_name_8")
        self.base_name_8.setMinimumSize(QSize(80, 30))
        self.base_name_8.setMaximumSize(QSize(80, 30))
        self.base_name_8.setStyleSheet(u"")
        self.base_name_8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.base_name_8, 4, 2, 1, 1)

        self.base_item_13 = QLabel(self.gridLayoutWidget)
        self.base_item_13.setObjectName(u"base_item_13")
        self.base_item_13.setMinimumSize(QSize(0, 30))
        self.base_item_13.setMaximumSize(QSize(16777215, 30))
        self.base_item_13.setStyleSheet(u"QLabel { \n"
"	padding-left: 5px;\n"
"	background-color: rgb(240, 240, 240); \n"
"}")
        self.base_item_13.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.base_item_13, 9, 2, 1, 2)

        self.base_name_5 = QLabel(self.gridLayoutWidget)
        self.base_name_5.setObjectName(u"base_name_5")
        self.base_name_5.setMinimumSize(QSize(0, 30))
        self.base_name_5.setMaximumSize(QSize(16777215, 30))
        self.base_name_5.setStyleSheet(u"")
        self.base_name_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.base_name_5, 4, 0, 1, 1)

        self.base_name_10 = QLabel(self.gridLayoutWidget)
        self.base_name_10.setObjectName(u"base_name_10")
        self.base_name_10.setMinimumSize(QSize(0, 30))
        self.base_name_10.setMaximumSize(QSize(16777215, 30))
        self.base_name_10.setStyleSheet(u"")
        self.base_name_10.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.base_name_10, 6, 2, 1, 1)

        self.base_item_9 = QLabel(self.gridLayoutWidget)
        self.base_item_9.setObjectName(u"base_item_9")
        self.base_item_9.setMinimumSize(QSize(0, 30))
        self.base_item_9.setMaximumSize(QSize(16777215, 30))
        self.base_item_9.setStyleSheet(u"QLabel { \n"
"	padding-left: 5px;\n"
"	background-color: rgb(240, 240, 240); \n"
"}")
        self.base_item_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.base_item_9, 5, 3, 1, 1)

        self.base_item_5 = QLabel(self.gridLayoutWidget)
        self.base_item_5.setObjectName(u"base_item_5")
        self.base_item_5.setMinimumSize(QSize(0, 30))
        self.base_item_5.setMaximumSize(QSize(16777215, 30))
        self.base_item_5.setStyleSheet(u"QLabel { \n"
"	padding-left: 5px;\n"
"	background-color: rgb(240, 240, 240); \n"
"}")
        self.base_item_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.base_item_5, 4, 1, 1, 1)

        self.base_name_9 = QLabel(self.gridLayoutWidget)
        self.base_name_9.setObjectName(u"base_name_9")
        self.base_name_9.setMinimumSize(QSize(0, 30))
        self.base_name_9.setMaximumSize(QSize(16777215, 30))
        self.base_name_9.setStyleSheet(u"")
        self.base_name_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.base_name_9, 5, 2, 1, 1)

        self.base_item_7 = QLabel(self.gridLayoutWidget)
        self.base_item_7.setObjectName(u"base_item_7")
        self.base_item_7.setMinimumSize(QSize(0, 30))
        self.base_item_7.setMaximumSize(QSize(16777215, 30))
        self.base_item_7.setStyleSheet(u"QLabel { \n"
"	padding-left: 5px;\n"
"	background-color: rgb(240, 240, 240); \n"
"}")
        self.base_item_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.base_item_7, 6, 1, 1, 1)

        self.base_name_7 = QLabel(self.gridLayoutWidget)
        self.base_name_7.setObjectName(u"base_name_7")
        self.base_name_7.setMinimumSize(QSize(0, 30))
        self.base_name_7.setMaximumSize(QSize(16777215, 30))
        self.base_name_7.setStyleSheet(u"")
        self.base_name_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.base_name_7, 6, 0, 1, 1)

        self.base_item_6 = QLabel(self.gridLayoutWidget)
        self.base_item_6.setObjectName(u"base_item_6")
        self.base_item_6.setMinimumSize(QSize(0, 30))
        self.base_item_6.setMaximumSize(QSize(16777215, 30))
        self.base_item_6.setStyleSheet(u"QLabel { \n"
"	padding-left: 5px;\n"
"	background-color: rgb(240, 240, 240); \n"
"}")
        self.base_item_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.base_item_6, 5, 1, 1, 1)

        self.base_item_8 = QLabel(self.gridLayoutWidget)
        self.base_item_8.setObjectName(u"base_item_8")
        self.base_item_8.setMinimumSize(QSize(0, 30))
        self.base_item_8.setMaximumSize(QSize(16777215, 30))
        self.base_item_8.setStyleSheet(u"QLabel { \n"
"	padding-left: 5px;\n"
"	background-color: rgb(240, 240, 240); \n"
"}")
        self.base_item_8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.base_item_8, 4, 3, 1, 1)

        self.base_name_1 = QLabel(self.gridLayoutWidget)
        self.base_name_1.setObjectName(u"base_name_1")
        self.base_name_1.setMinimumSize(QSize(80, 30))
        self.base_name_1.setMaximumSize(QSize(80, 30))
        self.base_name_1.setFont(font)
        self.base_name_1.setStyleSheet(u"")
        self.base_name_1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.base_name_1, 0, 0, 1, 1)

        self.base_item_2 = QLabel(self.gridLayoutWidget)
        self.base_item_2.setObjectName(u"base_item_2")
        self.base_item_2.setMinimumSize(QSize(0, 30))
        self.base_item_2.setMaximumSize(QSize(16777215, 30))
        self.base_item_2.setStyleSheet(u"QLabel { \n"
"	padding-left: 5px;\n"
"	background-color: rgb(240, 240, 240); \n"
"}")
        self.base_item_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.base_item_2, 1, 1, 1, 3)

        self.base_item_1 = QLabel(self.gridLayoutWidget)
        self.base_item_1.setObjectName(u"base_item_1")
        self.base_item_1.setMinimumSize(QSize(0, 30))
        self.base_item_1.setMaximumSize(QSize(16777215, 30))
        self.base_item_1.setStyleSheet(u"QLabel { \n"
"	padding-left: 5px;\n"
"	background-color: rgb(240, 240, 240); \n"
"}")
        self.base_item_1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.base_item_1, 0, 1, 1, 3)

        self.base_name_3 = QLabel(self.gridLayoutWidget)
        self.base_name_3.setObjectName(u"base_name_3")
        self.base_name_3.setMinimumSize(QSize(0, 30))
        self.base_name_3.setMaximumSize(QSize(16777215, 30))
        self.base_name_3.setFont(font)
        self.base_name_3.setStyleSheet(u"")
        self.base_name_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.base_name_3, 2, 0, 1, 1)

        self.base_item_3 = QLabel(self.gridLayoutWidget)
        self.base_item_3.setObjectName(u"base_item_3")
        self.base_item_3.setMinimumSize(QSize(0, 30))
        self.base_item_3.setMaximumSize(QSize(16777215, 30))
        self.base_item_3.setStyleSheet(u"QLabel { \n"
"	padding-left: 5px;\n"
"	background-color: rgb(240, 240, 240); \n"
"}")
        self.base_item_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.base_item_3, 2, 1, 1, 3)

        self.base_item_10 = QLabel(self.gridLayoutWidget)
        self.base_item_10.setObjectName(u"base_item_10")
        self.base_item_10.setMinimumSize(QSize(0, 30))
        self.base_item_10.setMaximumSize(QSize(16777215, 30))
        self.base_item_10.setStyleSheet(u"QLabel { \n"
"	padding-left: 5px;\n"
"	background-color: rgb(240, 240, 240); \n"
"}")
        self.base_item_10.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.base_item_10, 6, 3, 1, 1)

        self.widget_4 = QWidget(BuildingInfo)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(440, 116, 381, 231))
        self.widget_4.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(44,62,80);\n"
"	padding-top: 4px;\n"
"	border-right: 1px solid;\n"
"	border-bottom: 1px solid;\n"
"	border-color: rgb(210, 210, 210);\n"
"	border-radius: 5px;\n"
"}")
        self.gridLayoutWidget_5 = QWidget(self.widget_4)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(0, 0, 381, 221))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(3)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.detail_name_7 = QLabel(self.gridLayoutWidget_5)
        self.detail_name_7.setObjectName(u"detail_name_7")
        self.detail_name_7.setMinimumSize(QSize(0, 30))
        self.detail_name_7.setMaximumSize(QSize(16777215, 30))
        self.detail_name_7.setStyleSheet(u"")
        self.detail_name_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.detail_name_7, 4, 2, 1, 1)

        self.detail_name_4 = QLabel(self.gridLayoutWidget_5)
        self.detail_name_4.setObjectName(u"detail_name_4")
        self.detail_name_4.setMinimumSize(QSize(0, 30))
        self.detail_name_4.setMaximumSize(QSize(16777215, 30))
        self.detail_name_4.setStyleSheet(u"")
        self.detail_name_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.detail_name_4, 4, 0, 1, 1)

        self.detail_item_6 = QLabel(self.gridLayoutWidget_5)
        self.detail_item_6.setObjectName(u"detail_item_6")
        self.detail_item_6.setMinimumSize(QSize(0, 30))
        self.detail_item_6.setMaximumSize(QSize(16777215, 30))
        self.detail_item_6.setStyleSheet(u"QLabel { \n"
"	padding-left: 5px;\n"
"	background-color: rgb(240, 240, 240); \n"
"}")
        self.detail_item_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.detail_item_6, 6, 1, 1, 1)

        self.detail_name_6 = QLabel(self.gridLayoutWidget_5)
        self.detail_name_6.setObjectName(u"detail_name_6")
        self.detail_name_6.setMinimumSize(QSize(0, 30))
        self.detail_name_6.setMaximumSize(QSize(16777215, 30))
        self.detail_name_6.setStyleSheet(u"")
        self.detail_name_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.detail_name_6, 6, 0, 1, 1)

        self.detail_name_9 = QLabel(self.gridLayoutWidget_5)
        self.detail_name_9.setObjectName(u"detail_name_9")
        self.detail_name_9.setMinimumSize(QSize(0, 30))
        self.detail_name_9.setMaximumSize(QSize(16777215, 30))
        self.detail_name_9.setStyleSheet(u"")
        self.detail_name_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.detail_name_9, 6, 2, 1, 1)

        self.detail_item_9 = QLabel(self.gridLayoutWidget_5)
        self.detail_item_9.setObjectName(u"detail_item_9")
        self.detail_item_9.setMinimumSize(QSize(0, 30))
        self.detail_item_9.setMaximumSize(QSize(16777215, 30))
        self.detail_item_9.setStyleSheet(u"QLabel { \n"
"	padding-left: 5px;\n"
"	background-color: rgb(240, 240, 240); \n"
"}")
        self.detail_item_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.detail_item_9, 6, 3, 1, 1)

        self.detail_name_3 = QLabel(self.gridLayoutWidget_5)
        self.detail_name_3.setObjectName(u"detail_name_3")
        self.detail_name_3.setMinimumSize(QSize(0, 30))
        self.detail_name_3.setMaximumSize(QSize(16777215, 30))
        self.detail_name_3.setFont(font)
        self.detail_name_3.setStyleSheet(u"")
        self.detail_name_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.detail_name_3, 3, 0, 1, 1)

        self.detail_name_5 = QLabel(self.gridLayoutWidget_5)
        self.detail_name_5.setObjectName(u"detail_name_5")
        self.detail_name_5.setMinimumSize(QSize(0, 30))
        self.detail_name_5.setMaximumSize(QSize(16777215, 30))
        self.detail_name_5.setStyleSheet(u"")
        self.detail_name_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.detail_name_5, 5, 0, 1, 1)

        self.detail_item_7 = QLabel(self.gridLayoutWidget_5)
        self.detail_item_7.setObjectName(u"detail_item_7")
        self.detail_item_7.setMinimumSize(QSize(0, 30))
        self.detail_item_7.setMaximumSize(QSize(16777215, 30))
        self.detail_item_7.setStyleSheet(u"QLabel { \n"
"	padding-left: 5px;\n"
"	background-color: rgb(240, 240, 240); \n"
"}")
        self.detail_item_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.detail_item_7, 4, 3, 1, 1)

        self.detail_item_1 = QLabel(self.gridLayoutWidget_5)
        self.detail_item_1.setObjectName(u"detail_item_1")
        self.detail_item_1.setMinimumSize(QSize(0, 30))
        self.detail_item_1.setMaximumSize(QSize(16777215, 30))
        self.detail_item_1.setStyleSheet(u"QLabel { \n"
"	padding-left: 5px;\n"
"	background-color: rgb(240, 240, 240); \n"
"}")
        self.detail_item_1.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.detail_item_1, 0, 1, 1, 3)

        self.detail_item_3 = QLabel(self.gridLayoutWidget_5)
        self.detail_item_3.setObjectName(u"detail_item_3")
        self.detail_item_3.setMinimumSize(QSize(0, 30))
        self.detail_item_3.setMaximumSize(QSize(16777215, 30))
        self.detail_item_3.setStyleSheet(u"QLabel { \n"
"	padding-left: 5px;\n"
"	background-color: rgb(240, 240, 240); \n"
"}")
        self.detail_item_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.detail_item_3, 3, 1, 1, 3)

        self.detail_name_1 = QLabel(self.gridLayoutWidget_5)
        self.detail_name_1.setObjectName(u"detail_name_1")
        self.detail_name_1.setMinimumSize(QSize(0, 30))
        self.detail_name_1.setMaximumSize(QSize(16777215, 30))
        self.detail_name_1.setFont(font)
        self.detail_name_1.setStyleSheet(u"")
        self.detail_name_1.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.detail_name_1, 0, 0, 1, 1)

        self.detail_item_8 = QLabel(self.gridLayoutWidget_5)
        self.detail_item_8.setObjectName(u"detail_item_8")
        self.detail_item_8.setMinimumSize(QSize(0, 30))
        self.detail_item_8.setMaximumSize(QSize(16777215, 30))
        self.detail_item_8.setStyleSheet(u"QLabel { \n"
"	padding-left: 5px;\n"
"	background-color: rgb(240, 240, 240); \n"
"}")
        self.detail_item_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.detail_item_8, 5, 3, 1, 1)

        self.detail_name_8 = QLabel(self.gridLayoutWidget_5)
        self.detail_name_8.setObjectName(u"detail_name_8")
        self.detail_name_8.setMinimumSize(QSize(0, 30))
        self.detail_name_8.setMaximumSize(QSize(16777215, 30))
        self.detail_name_8.setStyleSheet(u"")
        self.detail_name_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.detail_name_8, 5, 2, 1, 1)

        self.detail_item_4 = QLabel(self.gridLayoutWidget_5)
        self.detail_item_4.setObjectName(u"detail_item_4")
        self.detail_item_4.setMinimumSize(QSize(0, 30))
        self.detail_item_4.setMaximumSize(QSize(16777215, 30))
        self.detail_item_4.setStyleSheet(u"QLabel { \n"
"	padding-left: 5px;\n"
"	background-color: rgb(240, 240, 240); \n"
"}")
        self.detail_item_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.detail_item_4, 4, 1, 1, 1)

        self.detail_item_5 = QLabel(self.gridLayoutWidget_5)
        self.detail_item_5.setObjectName(u"detail_item_5")
        self.detail_item_5.setMinimumSize(QSize(0, 30))
        self.detail_item_5.setMaximumSize(QSize(16777215, 30))
        self.detail_item_5.setStyleSheet(u"QLabel { \n"
"	padding-left: 5px;\n"
"	background-color: rgb(240, 240, 240); \n"
"}")
        self.detail_item_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.detail_item_5, 5, 1, 1, 1)

        self.detail_item_2 = QLabel(self.gridLayoutWidget_5)
        self.detail_item_2.setObjectName(u"detail_item_2")
        self.detail_item_2.setMinimumSize(QSize(0, 30))
        self.detail_item_2.setMaximumSize(QSize(16777215, 16777215))
        self.detail_item_2.setStyleSheet(u"QLabel { \n"
"	padding-left: 5px;\n"
"	background-color: rgb(240, 240, 240); \n"
"}")
        self.detail_item_2.setAlignment(Qt.AlignCenter)
        self.detail_item_2.setWordWrap(True)

        self.gridLayout_2.addWidget(self.detail_item_2, 1, 1, 2, 3)

        self.detail_name_2 = QLabel(self.gridLayoutWidget_5)
        self.detail_name_2.setObjectName(u"detail_name_2")
        self.detail_name_2.setMinimumSize(QSize(0, 30))
        self.detail_name_2.setMaximumSize(QSize(16777215, 16777215))
        self.detail_name_2.setFont(font)
        self.detail_name_2.setStyleSheet(u"")
        self.detail_name_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.detail_name_2, 1, 0, 2, 1)

        self.widget_5 = QWidget(BuildingInfo)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(440, 390, 381, 71))
        self.widget_5.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(44,62,80);\n"
"	padding-top: 4px;\n"
"	border-right: 1px solid;\n"
"	border-bottom: 1px solid;\n"
"	border-color: rgb(210, 210, 210);\n"
"	border-radius: 5px;\n"
"}")
        self.gridLayoutWidget_6 = QWidget(self.widget_5)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(0, 0, 381, 65))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_3.setHorizontalSpacing(5)
        self.gridLayout_3.setVerticalSpacing(3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.park_name_1 = QLabel(self.gridLayoutWidget_6)
        self.park_name_1.setObjectName(u"park_name_1")
        self.park_name_1.setMinimumSize(QSize(0, 30))
        self.park_name_1.setMaximumSize(QSize(16777215, 30))
        self.park_name_1.setStyleSheet(u"=")
        self.park_name_1.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.park_name_1, 0, 0, 1, 1)

        self.park_name_3 = QLabel(self.gridLayoutWidget_6)
        self.park_name_3.setObjectName(u"park_name_3")
        self.park_name_3.setMinimumSize(QSize(0, 30))
        self.park_name_3.setMaximumSize(QSize(16777215, 30))
        self.park_name_3.setStyleSheet(u"=")
        self.park_name_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.park_name_3, 0, 2, 1, 1)

        self.park_name_4 = QLabel(self.gridLayoutWidget_6)
        self.park_name_4.setObjectName(u"park_name_4")
        self.park_name_4.setMinimumSize(QSize(0, 30))
        self.park_name_4.setMaximumSize(QSize(16777215, 30))
        self.park_name_4.setStyleSheet(u"=")
        self.park_name_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.park_name_4, 1, 2, 1, 1)

        self.park_item_1 = QLabel(self.gridLayoutWidget_6)
        self.park_item_1.setObjectName(u"park_item_1")
        self.park_item_1.setMinimumSize(QSize(0, 30))
        self.park_item_1.setMaximumSize(QSize(16777215, 30))
        self.park_item_1.setStyleSheet(u"QLabel { \n"
"	padding-left: 5px;\n"
"	background-color: rgb(240, 240, 240); \n"
"}")
        self.park_item_1.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.park_item_1, 0, 1, 1, 1)

        self.park_item_3 = QLabel(self.gridLayoutWidget_6)
        self.park_item_3.setObjectName(u"park_item_3")
        self.park_item_3.setMinimumSize(QSize(0, 30))
        self.park_item_3.setMaximumSize(QSize(16777215, 30))
        self.park_item_3.setStyleSheet(u"QLabel { \n"
"	padding-left: 5px;\n"
"	background-color: rgb(240, 240, 240); \n"
"}")
        self.park_item_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.park_item_3, 0, 3, 1, 1)

        self.park_item_2 = QLabel(self.gridLayoutWidget_6)
        self.park_item_2.setObjectName(u"park_item_2")
        self.park_item_2.setMinimumSize(QSize(0, 30))
        self.park_item_2.setMaximumSize(QSize(16777215, 30))
        self.park_item_2.setStyleSheet(u"QLabel { \n"
"	padding-left: 5px;\n"
"	background-color: rgb(240, 240, 240); \n"
"}")
        self.park_item_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.park_item_2, 1, 1, 1, 1)

        self.park_item_4 = QLabel(self.gridLayoutWidget_6)
        self.park_item_4.setObjectName(u"park_item_4")
        self.park_item_4.setMinimumSize(QSize(0, 30))
        self.park_item_4.setMaximumSize(QSize(16777215, 30))
        self.park_item_4.setStyleSheet(u"QLabel { \n"
"	padding-left: 5px;\n"
"	background-color: rgb(240, 240, 240); \n"
"}")
        self.park_item_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.park_item_4, 1, 3, 1, 1)

        self.park_name_2 = QLabel(self.gridLayoutWidget_6)
        self.park_name_2.setObjectName(u"park_name_2")
        self.park_name_2.setMinimumSize(QSize(0, 30))
        self.park_name_2.setMaximumSize(QSize(16777215, 30))
        self.park_name_2.setStyleSheet(u"=")
        self.park_name_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.park_name_2, 1, 0, 1, 1)

        self.widget_6 = QWidget(BuildingInfo)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(440, 507, 381, 171))
        self.widget_6.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(44,62,80);\n"
"	padding-top: 4px;\n"
"	border-right: 1px solid;\n"
"	border-bottom: 1px solid;\n"
"	border-color: rgb(210, 210, 210);\n"
"	border-radius: 5px;\n"
"}")
        self.gridLayoutWidget_7 = QWidget(self.widget_6)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(0, 0, 381, 161))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_4.setHorizontalSpacing(5)
        self.gridLayout_4.setVerticalSpacing(3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.land_item_2 = QLabel(self.gridLayoutWidget_7)
        self.land_item_2.setObjectName(u"land_item_2")
        self.land_item_2.setMinimumSize(QSize(0, 30))
        self.land_item_2.setMaximumSize(QSize(16777215, 16777215))
        self.land_item_2.setStyleSheet(u"QLabel { \n"
"	padding-left: 5px;\n"
"	background-color: rgb(240, 240, 240); \n"
"}")
        self.land_item_2.setAlignment(Qt.AlignCenter)
        self.land_item_2.setWordWrap(True)

        self.gridLayout_4.addWidget(self.land_item_2, 1, 1, 2, 1)

        self.land_name_2 = QLabel(self.gridLayoutWidget_7)
        self.land_name_2.setObjectName(u"land_name_2")
        self.land_name_2.setMinimumSize(QSize(91, 25))
        self.land_name_2.setMaximumSize(QSize(91, 16777215))
        self.land_name_2.setStyleSheet(u"")
        self.land_name_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.land_name_2, 1, 0, 2, 1)

        self.land_name_1 = QLabel(self.gridLayoutWidget_7)
        self.land_name_1.setObjectName(u"land_name_1")
        self.land_name_1.setMinimumSize(QSize(91, 30))
        self.land_name_1.setMaximumSize(QSize(91, 30))
        self.land_name_1.setStyleSheet(u"")
        self.land_name_1.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.land_name_1, 0, 0, 1, 1)

        self.land_item_1 = QLabel(self.gridLayoutWidget_7)
        self.land_item_1.setObjectName(u"land_item_1")
        self.land_item_1.setMinimumSize(QSize(0, 30))
        self.land_item_1.setMaximumSize(QSize(16777215, 30))
        self.land_item_1.setStyleSheet(u"QLabel { \n"
"	padding-left: 5px;\n"
"	background-color: rgb(240, 240, 240); \n"
"}")
        self.land_item_1.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.land_item_1, 0, 1, 1, 1)

        self.land_item_3 = QLabel(self.gridLayoutWidget_7)
        self.land_item_3.setObjectName(u"land_item_3")
        self.land_item_3.setMinimumSize(QSize(0, 30))
        self.land_item_3.setMaximumSize(QSize(16777215, 16777215))
        self.land_item_3.setStyleSheet(u"QLabel { \n"
"	padding-left: 5px;\n"
"	background-color: rgb(240, 240, 240); \n"
"}")
        self.land_item_3.setAlignment(Qt.AlignCenter)
        self.land_item_3.setWordWrap(True)

        self.gridLayout_4.addWidget(self.land_item_3, 3, 1, 2, 1)

        self.land_name_3 = QLabel(self.gridLayoutWidget_7)
        self.land_name_3.setObjectName(u"land_name_3")
        self.land_name_3.setMinimumSize(QSize(91, 0))
        self.land_name_3.setMaximumSize(QSize(91, 16777215))
        self.land_name_3.setStyleSheet(u"")
        self.land_name_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.land_name_3, 3, 0, 2, 1)

        self.lb_hint_3 = QLabel(BuildingInfo)
        self.lb_hint_3.setObjectName(u"lb_hint_3")
        self.lb_hint_3.setGeometry(QRect(150, 225, 261, 16))
        self.lb_hint_3.setStyleSheet(u"")
        self.lb_hint_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.btn_search = QPushButton(BuildingInfo)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setGeometry(QRect(359, 119, 50, 41))
        self.btn_search.setStyleSheet(u"#btn_search {\n"
"	background-color: white;\n"
"	padding-top: 3px;\n"
"	border: none;\n"
"}")
        self.widget_3.raise_()
        self.line_sub_title_5.raise_()
        self.lb_detail_name_2.raise_()
        self.cbx_rooms.raise_()
        self.edt_address.raise_()
        self.line_sub_title_1.raise_()
        self.lb_sub_title_1.raise_()
        self.line_sub_title_3.raise_()
        self.lb_sub_title_3.raise_()
        self.line_sub_title_4.raise_()
        self.lb_sub_title_4.raise_()
        self.lb_sub_title_5.raise_()
        self.top_bar.raise_()
        self.bot_bar.raise_()
        self.widget_4.raise_()
        self.widget_5.raise_()
        self.widget_6.raise_()
        self.lb_hint_2.raise_()
        self.line_sub_title_2.raise_()
        self.lb_hint_3.raise_()
        self.lb_sub_title_2.raise_()
        self.btn_search.raise_()
        QWidget.setTabOrder(self.edt_address, self.cbx_rooms)
        QWidget.setTabOrder(self.cbx_rooms, self.btn_viol)
        QWidget.setTabOrder(self.btn_viol, self.btn_details)

        self.retranslateUi(BuildingInfo)

        QMetaObject.connectSlotsByName(BuildingInfo)
    # setupUi

    def retranslateUi(self, BuildingInfo):
        BuildingInfo.setWindowTitle(QCoreApplication.translate("BuildingInfo", u"\ub808\uc774 - Real estate Information", None))
        self.cbx_rooms.setItemText(0, QCoreApplication.translate("BuildingInfo", u"( \uc0c1\uc138\uc8fc\uc18c / \ud638 \uc120\ud0dd )", None))

        self.lb_sub_title_2.setText(QCoreApplication.translate("BuildingInfo", u"\uac74\ubb3c \uc815\ubcf4", None))
        self.edt_address.setText("")
        self.lb_sub_title_1.setText(QCoreApplication.translate("BuildingInfo", u"\uc18c\uc7ac\uc9c0 \uac80\uc0c9", None))
        self.lb_sub_title_3.setText(QCoreApplication.translate("BuildingInfo", u"\uac74\ubb3c \uc0c1\uc138\uc815\ubcf4", None))
        self.lb_sub_title_4.setText(QCoreApplication.translate("BuildingInfo", u"\uc8fc\ucc28\uc7a5 \uc815\ubcf4", None))
        self.lb_sub_title_5.setText(QCoreApplication.translate("BuildingInfo", u"\ud1a0\uc9c0 \uc815\ubcf4", None))
        self.lb_hint_2.setText(QCoreApplication.translate("BuildingInfo", u"\uac80\uc0c9 \ub41c \uacb0\uacfc\ub294 \uac01\uc885 \uacf5\uacf5\ub370\uc774\ud130 \ud3ec\ud138\uc5d0\uc11c \uc81c\uacf5\ud558\ub294 API \ub370\uc774\ud130\ub85c\n"
"\uc2e4\uc81c \uac74\ucd95\ubb3c\ub300\uc7a5 \uc815\ubcf4\uc640 \uc0c1\uc774 \ud560 \uc218 \uc788\uc73c\ub2c8 \ucc38\uace0\uc6a9\uc73c\ub85c\ub9cc \uc0ac\uc6a9\ud574\uc8fc\uc138\uc694.\n"
"(\ubcf8 \ud504\ub85c\uadf8\ub7a8\uc740 \uc870\ud68c\ub41c \uc815\ubcf4\uc5d0 \ub300\ud55c \ucc45\uc784\uc744 \uc9c0\uc9c0 \uc54a\uc2b5\ub2c8\ub2e4.)", None))
        self.lb_title.setText(QCoreApplication.translate("BuildingInfo", u"INFORMATION", None))
        self.lb_sub_title.setText(QCoreApplication.translate("BuildingInfo", u"(  \uac74\ucd95\ubb3c \uc870\ud68c  )", None))
        self.btn_viol.setText(QCoreApplication.translate("BuildingInfo", u"\uc704\ubc18 \uac74\ucd95\ubb3c \uc870\ud68c", None))
        self.btn_details.setText(QCoreApplication.translate("BuildingInfo", u"\uc0c1\uc138\uc815\ubcf4  >", None))
        self.lb_viol.setText("")
        self.base_item_11.setText("")
        self.base_name_12.setText(QCoreApplication.translate("BuildingInfo", u"\uc0ac \uc6a9 \uc2b9 \uc778 \uc77c", None))
        self.base_name_11.setText(QCoreApplication.translate("BuildingInfo", u"\ud638 / \uac00 \uad6c / \uc138 \ub300 \uc218", None))
        self.base_name_4.setText(QCoreApplication.translate("BuildingInfo", u"\uc8fc \uc6a9 \ub3c4", None))
        self.base_name_2.setText(QCoreApplication.translate("BuildingInfo", u"\ub3c4 \ub85c \uba85", None))
        self.base_item_4.setText("")
        self.base_name_6.setText(QCoreApplication.translate("BuildingInfo", u"\uc2b9 \uac15 \uae30", None))
        self.base_name_13.setText(QCoreApplication.translate("BuildingInfo", u"\uacf5 \uc2dc \uac00 \uaca9", None))
        self.base_item_12.setText("")
        self.base_name_8.setText(QCoreApplication.translate("BuildingInfo", u"\uc804\uc6a9\uba74\uc801", None))
        self.base_item_13.setText("")
        self.base_name_5.setText(QCoreApplication.translate("BuildingInfo", u"\uacf5\uc6a9\uba74\uc801", None))
        self.base_name_10.setText(QCoreApplication.translate("BuildingInfo", u"\uc18c \uc720 \uc790", None))
        self.base_item_9.setText("")
        self.base_item_5.setText("")
        self.base_name_9.setText(QCoreApplication.translate("BuildingInfo", u"\ucd1d \uce35 \uc218", None))
        self.base_item_7.setText("")
        self.base_name_7.setText(QCoreApplication.translate("BuildingInfo", u"\uc8fc \ucc28 \uc7a5", None))
        self.base_item_6.setText("")
        self.base_item_8.setText("")
        self.base_name_1.setText(QCoreApplication.translate("BuildingInfo", u"\uc18c \uc7ac \uc9c0", None))
        self.base_item_2.setText("")
        self.base_item_1.setText("")
        self.base_name_3.setText(QCoreApplication.translate("BuildingInfo", u"\uc0c1\uc138\uc8fc\uc18c", None))
        self.base_item_3.setText("")
        self.base_item_10.setText("")
        self.detail_name_7.setText(QCoreApplication.translate("BuildingInfo", u"\uc5f0 \uba74 \uc801", None))
        self.detail_name_4.setText(QCoreApplication.translate("BuildingInfo", u"\ub300\uc9c0\uba74\uc801", None))
        self.detail_item_6.setText("")
        self.detail_name_6.setText(QCoreApplication.translate("BuildingInfo", u"\uac74 \ud3d0 \uc728", None))
        self.detail_name_9.setText(QCoreApplication.translate("BuildingInfo", u"\uc6a9 \uc801 \ub960", None))
        self.detail_item_9.setText("")
        self.detail_name_3.setText(QCoreApplication.translate("BuildingInfo", u"\uc8fc \uc6a9 \ub3c4", None))
        self.detail_name_5.setText(QCoreApplication.translate("BuildingInfo", u"\uac74\ucd95\uba74\uc801", None))
        self.detail_item_7.setText("")
        self.detail_item_1.setText("")
        self.detail_item_3.setText("")
        self.detail_name_1.setText(QCoreApplication.translate("BuildingInfo", u"\uc8fc \uad6c \uc870", None))
        self.detail_item_8.setText("")
        self.detail_name_8.setText(QCoreApplication.translate("BuildingInfo", u"\ub192 \uc774", None))
        self.detail_item_4.setText("")
        self.detail_item_5.setText("")
        self.detail_item_2.setText("")
        self.detail_name_2.setText(QCoreApplication.translate("BuildingInfo", u"\uc9c0\uc5ed\u318d\uc9c0\uad6c", None))
        self.park_name_1.setText(QCoreApplication.translate("BuildingInfo", u"\uc625\ub0b4\uc790\uc8fc\uc2dd", None))
        self.park_name_3.setText(QCoreApplication.translate("BuildingInfo", u"\uc625\uc678\uc790\uc8fc\uc2dd", None))
        self.park_name_4.setText(QCoreApplication.translate("BuildingInfo", u"\uc625\uc678\uae30\uacc4\uc2dd", None))
        self.park_item_1.setText("")
        self.park_item_3.setText("")
        self.park_item_2.setText("")
        self.park_item_4.setText("")
        self.park_name_2.setText(QCoreApplication.translate("BuildingInfo", u"\uc625\ub0b4\uae30\uacc4\uc2dd", None))
        self.land_item_2.setText("")
        self.land_name_2.setText(QCoreApplication.translate("BuildingInfo", u"\uc9c0\uc5ed\u318d\uc9c0\uad6c", None))
        self.land_name_1.setText(QCoreApplication.translate("BuildingInfo", u"\uac1c\ubcc4\uacf5\uc2dc\uc9c0\uac00", None))
        self.land_item_1.setText("")
        self.land_item_3.setText("")
        self.land_name_3.setText(QCoreApplication.translate("BuildingInfo", u" \uae30 \ud0c0 \n"
" \uc9c0\uc5ed\u318d\uc9c0\uad6c", None))
        self.lb_hint_3.setText(QCoreApplication.translate("BuildingInfo", u"* \ud56d\ubaa9 \ub354\ube14 \ud074\ub9ad \uc2dc \ub0b4\uc6a9\uc774 \ud074\ub9bd\ubcf4\ub4dc\uc5d0 \ubcf5\uc0ac \ub429\ub2c8\ub2e4.", None))
        self.btn_search.setText("")
    # retranslateUi

