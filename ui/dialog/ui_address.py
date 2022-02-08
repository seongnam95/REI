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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFrame, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QRadioButton, QSizePolicy,
    QWidget)

class Ui_FindAddress(object):
    def _setupUi(self, FindAddress):
        if not FindAddress.objectName():
            FindAddress.setObjectName(u"FindAddress")
        FindAddress.resize(460, 600)
        FindAddress.setMinimumSize(QSize(460, 600))
        FindAddress.setMaximumSize(QSize(460, 600))
        FindAddress.setStyleSheet(u"#FindAddress {\n"
"	background-color: white;\n"
"}\n"
"\n"
"QRadioButton {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: #2c3e50;\n"
"}\n"
"\n"
"QCheckBox {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(87,100,101);\n"
"	background-color: rgb(0,0,0,0);\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: 0px solid #999999;\n"
"	background: white;\n"
"	width: 4px;    \n"
"	margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {         \n"
"	min-height: 0px;\n"
"	border: 0px solid red;\n"
"	border-radius: 2px;\n"
"	background-color: rgb(72,93,114,180);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {       \n"
"	height: 0px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}")
        self.rbt_set = QRadioButton(FindAddress)
        self.rbt_set.setObjectName(u"rbt_set")
        self.rbt_set.setGeometry(QRect(20, 406, 181, 16))
        self.rbt_set.setStyleSheet(u"")
        self.rbt_set.setChecked(True)
        self.cbx_buildings = QComboBox(FindAddress)
        self.cbx_buildings.addItem("")
        self.cbx_buildings.setObjectName(u"cbx_buildings")
        self.cbx_buildings.setGeometry(QRect(20, 433, 211, 30))
        self.cbx_buildings.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid gray;\n"
"    padding: 4px 1px 1px 5px;\n"
"    min-width: 6em;\n"
"    background: rgb(255, 255, 255);\n"
"    font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"    color: rgb(44, 62, 80);\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    padding: 4px 1px 1px 5px;\n"
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
        self.rbt_solo = QRadioButton(FindAddress)
        self.rbt_solo.setObjectName(u"rbt_solo")
        self.rbt_solo.setGeometry(QRect(210, 406, 191, 16))
        self.rbt_solo.setStyleSheet(u"")
        self.cbx_rooms = QComboBox(FindAddress)
        self.cbx_rooms.addItem("")
        self.cbx_rooms.setObjectName(u"cbx_rooms")
        self.cbx_rooms.setGeometry(QRect(240, 433, 201, 30))
        self.cbx_rooms.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid gray;\n"
"    padding: 4px 1px 1px 5px;\n"
"    min-width: 6em;\n"
"    background: rgb(255, 255, 255);\n"
"    font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"    color: rgb(44, 62, 80);\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    padding: 4px 1px 1px 5px;\n"
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
        self.line_3 = QFrame(FindAddress)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(10, 157, 441, 20))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.edt_address = QLineEdit(FindAddress)
        self.edt_address.setObjectName(u"edt_address")
        self.edt_address.setEnabled(True)
        self.edt_address.setGeometry(QRect(20, 82, 421, 45))
        self.edt_address.setStyleSheet(u"#edt_address {\n"
"	color: rgb(72,93,114);\n"
"    font: 16px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	border: 2px solid #34495e;\n"
"	padding-top: 3px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"#edt_address::hover {\n"
"	border: 2px solid #3498db;\n"
"}\n"
"\n"
"#edt_address:focus {\n"
"	border: 2px solid #3498db;\n"
"}\n"
"")
        self.edt_address.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.list_address = QListWidget(FindAddress)
        self.list_address.setObjectName(u"list_address")
        self.list_address.setGeometry(QRect(15, 174, 431, 201))
        self.list_address.setStyleSheet(u"QListWidget {\n"
"	border: 0px;\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: #2c3e50;\n"
"	padding-top: 2px;\n"
"}\n"
"")
        self.lb_hint_1 = QLabel(FindAddress)
        self.lb_hint_1.setObjectName(u"lb_hint_1")
        self.lb_hint_1.setGeometry(QRect(25, 131, 371, 20))
        font = QFont()
        font.setFamilies([u"\uc6f0\ucef4\uccb4 Regular"])
        font.setBold(False)
        font.setItalic(False)
        self.lb_hint_1.setFont(font)
        self.lb_hint_1.setStyleSheet(u"QLabel {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(127, 140, 141);\n"
"}")
        self.lb_hint_1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.line_6 = QFrame(FindAddress)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(10, 375, 441, 16))
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.edt_result_address = QLineEdit(FindAddress)
        self.edt_result_address.setObjectName(u"edt_result_address")
        self.edt_result_address.setEnabled(True)
        self.edt_result_address.setGeometry(QRect(20, 472, 371, 35))
        self.edt_result_address.setStyleSheet(u"#edt_result_address {\n"
"	color: rgb(72,93,114);\n"
"    font: 16px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	border: 1px solid #34495e;\n"
"	padding-top: 3px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"#edt_result_address::hover {\n"
"	border: 2px solid #3498db;\n"
"}")
        self.edt_result_address.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.edt_result_address.setReadOnly(True)
        self.ckb_part = QCheckBox(FindAddress)
        self.ckb_part.setObjectName(u"ckb_part")
        self.ckb_part.setGeometry(QRect(400, 484, 41, 16))
        self.ckb_part.setStyleSheet(u"")
        self.ckb_part.setCheckable(True)
        self.ckb_part.setChecked(False)
        self.ckb_part.setTristate(False)
        self.btn_search = QPushButton(FindAddress)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setGeometry(QRect(389, 84, 50, 41))
        self.btn_search.setStyleSheet(u"#btn_search {\n"
"	background-color: white;\n"
"	border: none;\n"
"}")
        self.top_bar = QWidget(FindAddress)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setGeometry(QRect(0, 0, 460, 61))
        self.top_bar.setStyleSheet(u"#top_bar {\n"
"	background-color: rgb(245, 245, 245);\n"
"	border-bottom: 1px solid;\n"
"	border-top: 1px solid;\n"
"	border-color: rgb(230, 230, 230);\n"
"}")
        self.lb_title = QLabel(self.top_bar)
        self.lb_title.setObjectName(u"lb_title")
        self.lb_title.setGeometry(QRect(120, 4, 211, 30))
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
        self.lb_sub_title.setGeometry(QRect(130, 29, 190, 25))
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
        self.bot_bar = QWidget(FindAddress)
        self.bot_bar.setObjectName(u"bot_bar")
        self.bot_bar.setGeometry(QRect(0, 530, 460, 71))
        self.bot_bar.setStyleSheet(u"#bot_bar {\n"
"	background-color: rgb(245, 245, 245);\n"
"	border-top: 1px solid;\n"
"	border-color: rgb(230, 230, 230);\n"
"}")
        self.btn_input = QPushButton(self.bot_bar)
        self.btn_input.setObjectName(u"btn_input")
        self.btn_input.setGeometry(QRect(110, 18, 241, 35))
        self.btn_input.setStyleSheet(u"#btn_input {\n"
"	font: 16px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: white;\n"
"	border: 0px;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(84,102,120);\n"
"	border-radius: 17px;\n"
"}\n"
"\n"
"#btn_input::hover {\n"
"	border: 0px;\n"
"	background-color: rgb(64,82,100);\n"
"	border-style: inset;\n"
"}\n"
"\n"
"#btn_input:pressed {\n"
"	border: 0px;\n"
"	background-color: rgb(24,42,60);\n"
"	border-style: inset;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"E:/PyProject/Project/REI/building_info/image/bt_search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_input.setIcon(icon)
        self.btn_input.setIconSize(QSize(23, 23))
        self.lb_hint_2 = QLabel(FindAddress)
        self.lb_hint_2.setObjectName(u"lb_hint_2")
        self.lb_hint_2.setGeometry(QRect(35, 242, 391, 61))
        self.lb_hint_2.setStyleSheet(u"#lb_hint_2 {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	padding-top: 3px;\n"
"	color: rgb(80, 80, 80);\n"
"}")
        self.lb_hint_2.setAlignment(Qt.AlignCenter)
        self.list_address.raise_()
        self.rbt_set.raise_()
        self.cbx_buildings.raise_()
        self.rbt_solo.raise_()
        self.cbx_rooms.raise_()
        self.line_3.raise_()
        self.edt_address.raise_()
        self.lb_hint_1.raise_()
        self.line_6.raise_()
        self.edt_result_address.raise_()
        self.ckb_part.raise_()
        self.btn_search.raise_()
        self.top_bar.raise_()
        self.bot_bar.raise_()
        self.lb_hint_2.raise_()
        QWidget.setTabOrder(self.edt_address, self.list_address)
        QWidget.setTabOrder(self.list_address, self.rbt_set)
        QWidget.setTabOrder(self.rbt_set, self.rbt_solo)
        QWidget.setTabOrder(self.rbt_solo, self.cbx_buildings)
        QWidget.setTabOrder(self.cbx_buildings, self.cbx_rooms)
        QWidget.setTabOrder(self.cbx_rooms, self.edt_result_address)
        QWidget.setTabOrder(self.edt_result_address, self.ckb_part)

        self.retranslateUi(FindAddress)

        QMetaObject.connectSlotsByName(FindAddress)
    # setupUi

    def retranslateUi(self, FindAddress):
        FindAddress.setWindowTitle(QCoreApplication.translate("FindAddress", u"\ub808\uc774 - Real estate Information", None))
        self.rbt_set.setText(QCoreApplication.translate("FindAddress", u"\uc9d1\ud569 (\uc544\ud30c\ud2b8, \ub2e4\uc138\ub300, \uc5f0\ub9bd \ub4f1)", None))
        self.cbx_buildings.setItemText(0, QCoreApplication.translate("FindAddress", u"( \uac74\ubb3c\uba85\uce6d / \ub3d9 \uc120\ud0dd )", None))

        self.rbt_solo.setText(QCoreApplication.translate("FindAddress", u"\uc77c\ubc18 (\ub2e8\ub3c5, \ub2e4\uac00\uad6c, \uc0c1\uac00\uc8fc\ud0dd \ub4f1)", None))
        self.cbx_rooms.setItemText(0, QCoreApplication.translate("FindAddress", u"( \uc0c1\uc138\uc8fc\uc18c / \ud638 \uc120\ud0dd )", None))

        self.edt_address.setText("")
        self.lb_hint_1.setText(QCoreApplication.translate("FindAddress", u"\uc608\uc2dc) \ub3c4\ub85c\uba85 \uac80\uc0c9: (\ub3d9\uc77c\ub85c112\uae38 45), \uc9c0\ubc88 \uac80\uc0c9: (\uc0c1\ubd09\ub3d9 122-76)", None))
        self.edt_result_address.setText("")
        self.ckb_part.setText(QCoreApplication.translate("FindAddress", u"\uc77c\ubd80", None))
        self.btn_search.setText("")
        self.lb_title.setText(QCoreApplication.translate("FindAddress", u"ADDRESS", None))
        self.lb_sub_title.setText(QCoreApplication.translate("FindAddress", u"(  \uc18c\uc7ac\uc9c0 \uac80\uc0c9  )", None))
        self.btn_input.setText(QCoreApplication.translate("FindAddress", u"\uc18c\uc7ac\uc9c0 \uc785\ub825", None))
        self.lb_hint_2.setText(QCoreApplication.translate("FindAddress", u"\uac80\uc0c9 \ub41c \uacb0\uacfc\ub294 \uac01\uc885 \uacf5\uacf5\ub370\uc774\ud130 \ud3ec\ud138\uc5d0\uc11c \uc81c\uacf5\ud558\ub294 API \ub370\uc774\ud130\ub85c\n"
"\uc2e4\uc81c \uac74\ucd95\ubb3c\ub300\uc7a5 \uc815\ubcf4\uc640 \uc0c1\uc774 \ud560 \uc218 \uc788\uc73c\ub2c8 \ucc38\uace0\uc6a9\uc73c\ub85c\ub9cc \uc0ac\uc6a9\ud574\uc8fc\uc138\uc694.\n"
"(\ubcf8 \ud504\ub85c\uadf8\ub7a8\uc740 \uc870\ud68c\ub41c \uc815\ubcf4\uc5d0 \ub300\ud55c \ucc45\uc784\uc744 \uc9c0\uc9c0 \uc54a\uc2b5\ub2c8\ub2e4.)", None))
    # retranslateUi

