# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'company.ui'
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
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QWidget)

class Ui_Company(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(391, 361)
        self.lb_titlebar = QLabel(Form)
        self.lb_titlebar.setObjectName(u"lb_titlebar")
        self.lb_titlebar.setGeometry(QRect(0, 0, 391, 361))
        self.lb_titlebar.setStyleSheet(u"QLabel{\n"
"	background-color: white;\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(0, 0, 0, 120);\n"
"	padding-top: 8px;\n"
"	padding-left: 8px;\n"
"	border: 1px solid #ecf0f1;\n"
"}")
        self.lb_titlebar.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 20, 371, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line1 = QFrame(Form)
        self.line1.setObjectName(u"line1")
        self.line1.setGeometry(QRect(10, 340, 371, 16))
        self.line1.setFrameShape(QFrame.HLine)
        self.line1.setFrameShadow(QFrame.Sunken)
        self.list = QListWidget(Form)
        self.list.setObjectName(u"list")
        self.list.setGeometry(QRect(11, 107, 371, 231))
        self.list.setStyleSheet(u"QListWidget {\n"
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
        self.btn_exit = QPushButton(Form)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setGeometry(QRect(360, 4, 21, 21))
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
        self.lb_notfind = QLabel(Form)
        self.lb_notfind.setObjectName(u"lb_notfind")
        self.lb_notfind.setGeometry(QRect(120, 200, 161, 21))
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
        self.cbx_choise = QComboBox(Form)
        self.cbx_choise.addItem("")
        self.cbx_choise.addItem("")
        self.cbx_choise.setObjectName(u"cbx_choise")
        self.cbx_choise.setGeometry(QRect(20, 49, 131, 30))
        self.cbx_choise.setStyleSheet(u"QComboBox {\n"
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
"    image: url(./static/img/down_arrow.png);\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:hover {\n"
"    image: url(./static/img/down_arrow"
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
        self.edt_find = QLineEdit(Form)
        self.edt_find.setObjectName(u"edt_find")
        self.edt_find.setGeometry(QRect(160, 49, 121, 30))
        self.edt_find.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(72,93,114);\n"
"    font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	border: 1px solid #34495e;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"	border: 1px solid #3498db;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid #3498db;\n"
"}\n"
"")
        self.edt_find.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.btn_find = QPushButton(Form)
        self.btn_find.setObjectName(u"btn_find")
        self.btn_find.setGeometry(QRect(290, 49, 81, 30))
        self.btn_find.setStyleSheet(u"QPushButton {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: white;\n"
"	border: 0px;\n"
"	padding-right:  2px;\n"
"	padding-top: 3px;\n"
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
        icon = QIcon()
        icon.addFile(u"E:/PyProject/Project/REI/building_info/image/bt_search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_find.setIcon(icon)
        self.btn_find.setIconSize(QSize(23, 23))
        self.line2 = QFrame(Form)
        self.line2.setObjectName(u"line2")
        self.line2.setGeometry(QRect(10, 90, 371, 16))
        self.line2.setFrameShape(QFrame.HLine)
        self.line2.setFrameShadow(QFrame.Sunken)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lb_titlebar.setText(QCoreApplication.translate("Form", u"FINDING A COMPANY (\uc0ac\ubb34\uc18c \ucc3e\uae30)", None))
        self.btn_exit.setText("")
        self.lb_notfind.setText(QCoreApplication.translate("Form", u"\uac80\uc0c9 \uacb0\uacfc\uac00 \uc5c6\uc2b5\ub2c8\ub2e4.", None))
        self.cbx_choise.setItemText(0, QCoreApplication.translate("Form", u"\uc911\uac1c\uc0ac\ubb34\uc18c\uba85", None))
        self.cbx_choise.setItemText(1, QCoreApplication.translate("Form", u"\ub300\ud45c\uc790\uba85", None))

        self.btn_find.setText(QCoreApplication.translate("Form", u"\uc870     \ud68c", None))
    # retranslateUi

