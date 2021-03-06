# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'address_details.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QWidget)

class Ui_FindAddress(object):
    def setupUi(self, FindAddress):
        if not FindAddress.objectName():
            FindAddress.setObjectName(u"FindAddress")
        FindAddress.resize(471, 621)
        FindAddress.setMinimumSize(QSize(471, 621))
        FindAddress.setMaximumSize(QSize(471, 621))
        FindAddress.setStyleSheet(u"#FindAddress {\n"
"	background-color: white;\n"
"}")
        self.address_frame = QFrame(FindAddress)
        self.address_frame.setObjectName(u"address_frame")
        self.address_frame.setGeometry(QRect(20, 20, 431, 101))
        self.address_frame.setStyleSheet(u"#address_frame {\n"
"	background-color: white;\n"
"	border-radius: 15px;\n"
"}")
        self.address_frame.setFrameShape(QFrame.StyledPanel)
        self.address_frame.setFrameShadow(QFrame.Raised)
        self.btn_search = QPushButton(self.address_frame)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setGeometry(QRect(360, 22, 50, 41))
        self.btn_search.setStyleSheet(u"#btn_search {\n"
"	background-color: white;\n"
"	border: none;\n"
"	outline: none;\n"
"	border-radius: 5px;\n"
"}")
        self.edt_address = QLineEdit(self.address_frame)
        self.edt_address.setObjectName(u"edt_address")
        self.edt_address.setEnabled(True)
        self.edt_address.setGeometry(QRect(21, 20, 391, 45))
        self.edt_address.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(125,125,125);\n"
"	font: 16px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"    border: 2px solid rgb(128,128,255);\n"
"    border-radius: 5px;\n"
"    padding-top: 3px;\n"
"    padding-left: 10px;\n"
"    padding-right: 40px;\n"
"}\n"
"    \n"
"QLineEdit:focus {\n"
"	color: rgb(65,65,65);\n"
"}")
        self.edt_address.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lb_hint_1 = QLabel(self.address_frame)
        self.lb_hint_1.setObjectName(u"lb_hint_1")
        self.lb_hint_1.setGeometry(QRect(25, 69, 351, 20))
        font = QFont()
        font.setFamilies([u"\uc6f0\ucef4\uccb4 Regular"])
        font.setBold(False)
        font.setItalic(False)
        self.lb_hint_1.setFont(font)
        self.lb_hint_1.setStyleSheet(u"QLabel {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(120,120,120);\n"
"}")
        self.lb_hint_1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.edt_address.raise_()
        self.lb_hint_1.raise_()
        self.btn_search.raise_()
        self.list_frame = QFrame(FindAddress)
        self.list_frame.setObjectName(u"list_frame")
        self.list_frame.setGeometry(QRect(20, 140, 431, 221))
        self.list_frame.setStyleSheet(u"QScrollBar:vertical {\n"
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
"#list_frame {\n"
"	background-color: white;\n"
"	border-radius: 15px;\n"
"}")
        self.list_frame.setFrameShape(QFrame.StyledPanel)
        self.list_frame.setFrameShadow(QFrame.Raised)
        self.list_address = QListWidget(self.list_frame)
        self.list_address.setObjectName(u"list_address")
        self.list_address.setGeometry(QRect(10, 10, 411, 201))
        self.list_address.setStyleSheet(u"QListWidget {\n"
"	border: none;\n"
"	outline: none;\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: #2c3e50;\n"
"}")
        self.lb_hint_2 = QLabel(self.list_frame)
        self.lb_hint_2.setObjectName(u"lb_hint_2")
        self.lb_hint_2.setGeometry(QRect(20, 80, 391, 61))
        self.lb_hint_2.setStyleSheet(u"#lb_hint_2 {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	padding-top: 3px;\n"
"	color: rgb(80, 80, 80);\n"
"}")
        self.lb_hint_2.setAlignment(Qt.AlignCenter)
        self.detail_frame = QFrame(FindAddress)
        self.detail_frame.setObjectName(u"detail_frame")
        self.detail_frame.setGeometry(QRect(20, 380, 431, 121))
        self.detail_frame.setStyleSheet(u"#detail_frame {\n"
"	background-color: white;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QCheckBox {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(85,85,85);\n"
"	background-color: rgb(0,0,0,0);\n"
"}\n"
"\n"
"QRadioButton {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(85,85,85);\n"
"	border: none;\n"
"	outline: none;\n"
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
"QComboBox QAbstractItemV"
                        "iew::item:hover { \n"
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
"}")
        self.detail_frame.setFrameShape(QFrame.StyledPanel)
        self.detail_frame.setFrameShadow(QFrame.Raised)
        self.edt_result_address = QLineEdit(self.detail_frame)
        self.edt_result_address.setObjectName(u"edt_result_address")
        self.edt_result_address.setEnabled(True)
        self.edt_result_address.setGeometry(QRect(20, 65, 391, 35))
        self.edt_result_address.setStyleSheet(u"#edt_result_address {\n"
"	color: rgb(65,65,65);\n"
"    font: 15px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	border: 1px solid rgb(120,120,120);\n"
"	padding-top: 3px;\n"
"	padding-left: 10px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#edt_result_address::hover {\n"
"	border: 2px solid rgb(128,128,255);\n"
"}")
        self.edt_result_address.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.edt_result_address.setReadOnly(True)
        self.cbx_rooms = QComboBox(self.detail_frame)
        self.cbx_rooms.addItem("")
        self.cbx_rooms.setObjectName(u"cbx_rooms")
        self.cbx_rooms.setGeometry(QRect(220, 20, 191, 35))
        self.cbx_buildings = QComboBox(self.detail_frame)
        self.cbx_buildings.addItem("")
        self.cbx_buildings.setObjectName(u"cbx_buildings")
        self.cbx_buildings.setGeometry(QRect(20, 20, 191, 35))
        self.btn_input = QPushButton(FindAddress)
        self.btn_input.setObjectName(u"btn_input")
        self.btn_input.setGeometry(QRect(110, 530, 241, 45))
        self.btn_input.setStyleSheet(u"QPushButton {\n"
"    font: 18px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"    color: white;\n"
"    border: none;\n"
"    padding-top: 3px;\n"
"    padding-left: 2px;\n"
"    background: rgb(128,128,255);\n"
"    border-radius: 22px;\n"
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
        QWidget.setTabOrder(self.edt_address, self.list_address)
        QWidget.setTabOrder(self.list_address, self.cbx_buildings)
        QWidget.setTabOrder(self.cbx_buildings, self.cbx_rooms)
        QWidget.setTabOrder(self.cbx_rooms, self.edt_result_address)

        self.retranslateUi(FindAddress)

        QMetaObject.connectSlotsByName(FindAddress)
    # setupUi

    def retranslateUi(self, FindAddress):
        FindAddress.setWindowTitle(QCoreApplication.translate("FindAddress", u"\ub808\uc774 - Real estate Information", None))
        self.btn_search.setText("")
        self.edt_address.setText("")
        self.lb_hint_1.setText(QCoreApplication.translate("FindAddress", u"\uc608\uc2dc) \ub3c4\ub85c\uba85 \uac80\uc0c9: (\ub3d9\uc77c\ub85c112\uae38 45), \uc9c0\ubc88 \uac80\uc0c9: (\uc0c1\ubd09\ub3d9 122-76)", None))
        self.lb_hint_2.setText(QCoreApplication.translate("FindAddress", u"\uac80\uc0c9 \ub41c \uacb0\uacfc\ub294 \uac01\uc885 \uacf5\uacf5\ub370\uc774\ud130 \ud3ec\ud138\uc5d0\uc11c \uc81c\uacf5\ud558\ub294 API \ub370\uc774\ud130\ub85c\n"
"\uc2e4\uc81c \uac74\ucd95\ubb3c\ub300\uc7a5 \uc815\ubcf4\uc640 \uc0c1\uc774 \ud560 \uc218 \uc788\uc73c\ub2c8 \ucc38\uace0\uc6a9\uc73c\ub85c\ub9cc \uc0ac\uc6a9\ud574\uc8fc\uc138\uc694.\n"
"(\ubcf8 \ud504\ub85c\uadf8\ub7a8\uc740 \uc870\ud68c\ub41c \uc815\ubcf4\uc5d0 \ub300\ud55c \ucc45\uc784\uc744 \uc9c0\uc9c0 \uc54a\uc2b5\ub2c8\ub2e4.)", None))
        self.edt_result_address.setText("")
        self.cbx_rooms.setItemText(0, QCoreApplication.translate("FindAddress", u"( \uc0c1\uc138\uc8fc\uc18c / \ud638 \uc120\ud0dd )", None))

        self.cbx_buildings.setItemText(0, QCoreApplication.translate("FindAddress", u"( \uac74\ubb3c\uba85\uce6d / \ub3d9 \uc120\ud0dd )", None))

        self.btn_input.setText(QCoreApplication.translate("FindAddress", u"\uac74\ucd95\ubb3c \ud604\ud669 \uc5f4\ub78c", None))
    # retranslateUi

