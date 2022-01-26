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

class Ui_Address_Detaile(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(460, 581)
        self.rbt_set = QRadioButton(Dialog)
        self.rbt_set.setObjectName(u"rbt_set")
        self.rbt_set.setGeometry(QRect(20, 376, 181, 16))
        self.rbt_set.setStyleSheet(u"QRadioButton {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: #2c3e50;\n"
"}")
        self.rbt_set.setChecked(True)
        self.cbx_buildings = QComboBox(Dialog)
        self.cbx_buildings.addItem("")
        self.cbx_buildings.setObjectName(u"cbx_buildings")
        self.cbx_buildings.setGeometry(QRect(20, 403, 211, 30))
        self.cbx_buildings.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid gray;\n"
"    padding-top: 3px;\n"
"	padding-left: 6px;\n"
"    min-width: 6em;\n"
"    background: rgb(255, 255, 255);\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(104,122,140);\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    color: rgb(44,62,80);\n"
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
"    width: 25px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(./data/img/data/down_arrow.png);\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:hover {\n"
"    image: url(./data/img/down_arrow.png);\n"
"}\n"
"\n"
""
                        "QComboBox::down-arrow:on {\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    color: #2c3e50;\n"
"    background-color: lightblue\n"
"}")
        self.rbt_solo = QRadioButton(Dialog)
        self.rbt_solo.setObjectName(u"rbt_solo")
        self.rbt_solo.setGeometry(QRect(210, 376, 191, 16))
        self.rbt_solo.setStyleSheet(u"QRadioButton {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: #2c3e50;\n"
"}")
        self.cbx_rooms = QComboBox(Dialog)
        self.cbx_rooms.addItem("")
        self.cbx_rooms.setObjectName(u"cbx_rooms")
        self.cbx_rooms.setGeometry(QRect(240, 403, 201, 30))
        self.cbx_rooms.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid gray;\n"
"    padding-top: 3px;\n"
"	padding-left: 6px;\n"
"    min-width: 6em;\n"
"    background: rgb(255, 255, 255);\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(104,122,140);\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    color: rgb(44,62,80);\n"
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
"    width: 25px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(./data/img/data/down_arrow.png);\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:hover {\n"
"    image: url(./data/img/down_arrow.png);\n"
"}\n"
"\n"
""
                        "QComboBox::down-arrow:on {\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    color: #2c3e50;\n"
"    background-color: lightblue\n"
"}")
        self.btn_input = QPushButton(Dialog)
        self.btn_input.setObjectName(u"btn_input")
        self.btn_input.setGeometry(QRect(20, 518, 421, 41))
        self.btn_input.setStyleSheet(u"QPushButton {\n"
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
        self.btn_input.setIconSize(QSize(0, 0))
        self.line_3 = QFrame(Dialog)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(10, 127, 441, 20))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.lb_titlebar = QLabel(Dialog)
        self.lb_titlebar.setObjectName(u"lb_titlebar")
        self.lb_titlebar.setGeometry(QRect(0, 0, 461, 581))
        self.lb_titlebar.setStyleSheet(u"QLabel{\n"
"	background-color: white;\n"
"	font: 12px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgba(0, 0, 0, 120);\n"
"	padding-top: 8px;\n"
"	padding-left: 10px;\n"
"	border: 1px solid #ecf0f1;\n"
"}")
        self.lb_titlebar.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lb_notfind = QLabel(Dialog)
        self.lb_notfind.setObjectName(u"lb_notfind")
        self.lb_notfind.setGeometry(QRect(150, 230, 161, 21))
        font = QFont()
        font.setFamilies([u"\uc6f0\ucef4\uccb4 Regular"])
        font.setBold(False)
        font.setItalic(False)
        self.lb_notfind.setFont(font)
        self.lb_notfind.setStyleSheet(u"QLabel {\n"
"	font: 20px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: #353b48;\n"
"}")
        self.lb_notfind.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.edt_address = QLineEdit(Dialog)
        self.edt_address.setObjectName(u"edt_address")
        self.edt_address.setEnabled(True)
        self.edt_address.setGeometry(QRect(20, 52, 421, 45))
        self.edt_address.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(72,93,114);\n"
"    font: 16px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	border: 2px solid #34495e;\n"
"	padding-top: 3px;\n"
"	padding-left: 10px;\n"
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
        self.list_address = QListWidget(Dialog)
        self.list_address.setObjectName(u"list_address")
        self.list_address.setGeometry(QRect(15, 144, 431, 201))
        self.list_address.setStyleSheet(u"QListWidget {\n"
"	border: 0px;\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: #2c3e50;\n"
"	padding-top: 2px;\n"
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
        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 20, 441, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_12 = QLabel(Dialog)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(25, 101, 371, 20))
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"QLabel {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(127, 140, 141);\n"
"}")
        self.label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.btn_search = QPushButton(Dialog)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setGeometry(QRect(398, 54, 41, 41))
        self.btn_search.setStyleSheet(u"QPushButton{\n"
"	color: rgba(0,0,0,0);\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.btn_exit = QPushButton(Dialog)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setGeometry(QRect(430, 4, 21, 21))
        self.btn_exit.setStyleSheet(u"QPushButton {\n"
"	border: 0px solid;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: rgb(239, 111, 108, 170);\n"
"	border-style: inset;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(239, 111, 108);\n"
"	border-style: inset;\n"
"}\n"
"")
        self.line_6 = QFrame(Dialog)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(10, 345, 441, 16))
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.line_7 = QFrame(Dialog)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(10, 490, 441, 16))
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.edt_result_address = QLineEdit(Dialog)
        self.edt_result_address.setObjectName(u"edt_result_address")
        self.edt_result_address.setEnabled(True)
        self.edt_result_address.setGeometry(QRect(20, 442, 371, 35))
        self.edt_result_address.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(72,93,114);\n"
"    font: 16px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	border: 1px solid #34495e;\n"
"	padding-top: 3px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"	border: 2px solid #3498db;\n"
"}")
        self.edt_result_address.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.edt_result_address.setReadOnly(True)
        self.ckb_part = QCheckBox(Dialog)
        self.ckb_part.setObjectName(u"ckb_part")
        self.ckb_part.setGeometry(QRect(400, 454, 41, 16))
        self.ckb_part.setStyleSheet(u"QCheckBox {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(87,100,101);\n"
"	background-color: rgb(0,0,0,0);\n"
"}\n"
"\n"
"")
        self.ckb_part.setChecked(False)
        self.lb_titlebar.raise_()
        self.list_address.raise_()
        self.rbt_set.raise_()
        self.cbx_buildings.raise_()
        self.rbt_solo.raise_()
        self.cbx_rooms.raise_()
        self.btn_input.raise_()
        self.line_3.raise_()
        self.lb_notfind.raise_()
        self.edt_address.raise_()
        self.line.raise_()
        self.label_12.raise_()
        self.btn_search.raise_()
        self.btn_exit.raise_()
        self.line_6.raise_()
        self.line_7.raise_()
        self.edt_result_address.raise_()
        self.ckb_part.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.rbt_set.setText(QCoreApplication.translate("Dialog", u"\uc9d1\ud569 (\uc544\ud30c\ud2b8, \ub2e4\uc138\ub300, \uc5f0\ub9bd \ub4f1)", None))
        self.cbx_buildings.setItemText(0, QCoreApplication.translate("Dialog", u"( \uac74\ubb3c\uba85\uce6d / \ub3d9 \uc120\ud0dd )", None))

        self.rbt_solo.setText(QCoreApplication.translate("Dialog", u"\uc77c\ubc18 (\ub2e8\ub3c5, \ub2e4\uac00\uad6c, \uc0c1\uac00\uc8fc\ud0dd \ub4f1)", None))
        self.cbx_rooms.setItemText(0, QCoreApplication.translate("Dialog", u"( \uc0c1\uc138\uc8fc\uc18c / \ud638 \uc120\ud0dd )", None))

        self.btn_input.setText(QCoreApplication.translate("Dialog", u"\uc8fc \uc18c   \uc785 \ub825", None))
        self.lb_titlebar.setText(QCoreApplication.translate("Dialog", u"REI - ADDRESS (\uc0c1\uc138\uc8fc\uc18c \ucc3e\uae30)", None))
        self.lb_notfind.setText(QCoreApplication.translate("Dialog", u"\uac80\uc0c9 \uacb0\uacfc\uac00 \uc5c6\uc2b5\ub2c8\ub2e4.", None))
        self.edt_address.setText("")
        self.label_12.setText(QCoreApplication.translate("Dialog", u"\uc608\uc2dc) \ub3c4\ub85c\uba85 \uac80\uc0c9: (\ub3d9\uc77c\ub85c112\uae38 45), \uc9c0\ubc88 \uac80\uc0c9: (\uc0c1\ubd09\ub3d9 122-76)", None))
        self.btn_search.setText(QCoreApplication.translate("Dialog", u"PushButton", None))
        self.btn_exit.setText("")
        self.edt_result_address.setText("")
        self.ckb_part.setText(QCoreApplication.translate("Dialog", u"\uc77c\ubd80", None))
    # retranslateUi

