# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Login(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(270, 290)
        self.lb_form = QLabel(Form)
        self.lb_form.setObjectName(u"label_1")
        self.lb_form.setGeometry(QRect(0, 0, 270, 290))
        self.lb_form.setStyleSheet(u"QLabel{\n"
"	background-color: white;\n"
"	font: 12px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgba(0, 0, 0, 120);\n"
"	padding-top: 8px;\n"
"	padding-left: 10px;\n"
"	border: 1px solid #ecf0f1;\n"
"}")
        self.lb_form.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 50, 41, 16))
        self.label_2.setStyleSheet(u"QLabel {\n"
"	font: 12px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: #2c3e50;\n"
"}")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 120, 51, 16))
        self.label_3.setStyleSheet(u"QLabel {\n"
"	font: 12px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: #2c3e50;\n"
"}")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 260, 121, 16))
        self.label_4.setStyleSheet(u"QLabel {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(87,100,101);\n"
"	background-color: rgb(0,0,0,0);\n"
"}")
        self.edt_id = QLineEdit(Form)
        self.edt_id.setObjectName(u"edt_id")
        self.edt_id.setGeometry(QRect(20, 70, 230, 30))
        self.edt_id.setStyleSheet(u"QLineEdit {\n"
"    font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	border: 1px solid #34495e;\n"
"	padding-left: 8px;\n"
"	padding-top: 3px;\n"
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
        self.edt_pw = QLineEdit(Form)
        self.edt_pw.setObjectName(u"edt_pw")
        self.edt_pw.setGeometry(QRect(20, 140, 230, 30))
        self.edt_pw.setEchoMode(QLineEdit.Password)
        self.edt_pw.setStyleSheet(u"QLineEdit {\n"
"    font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	border: 1px solid #34495e;\n"
"	padding-left: 8px;\n"
"	padding-top: 3px;\n"
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
        self.btn_find = QPushButton(Form)
        self.btn_find.setObjectName(u"btn_find")
        self.btn_find.setGeometry(QRect(180, 175, 70, 25))
        self.btn_find.setStyleSheet(u"QPushButton {\n"
"	font: 12px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(44,62,80);\n"
"	border: 0px;\n"
"	padding-top: 1px;\n"
"	padding-left: 1px;\n"
"	background-color: rgb(0,0,0,0);\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 0px;\n"
"	color: white;\n"
"	background-color: rgb(84,102,120);\n"
"	border-style: inset;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 0px;\n"
"	background-color: rgb(44,62,80);\n"
"	border-style: inset;\n"
"}\n"
"")
        self.btn_register = QPushButton(Form)
        self.btn_register.setObjectName(u"btn_register")
        self.btn_register.setGeometry(QRect(160, 255, 80, 25))
        self.btn_register.setStyleSheet(u"QPushButton {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(44,62,80);\n"
"	border: 0px;\n"
"	padding-top: 3px;\n"
"	padding-left: 1px;\n"
"	background-color: rgb(0,0,0,0);\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 0px;\n"
"	color: white;\n"
"	background-color: rgb(84,102,120);\n"
"	border-style: inset;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 0px;\n"
"	background-color: rgb(44,62,80);\n"
"	border-style: inset;\n"
"}\n"
"")
        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 20, 251, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(20, 180, 81, 16))
        self.checkBox.setStyleSheet(u"QCheckBox {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(87,100,101);\n"
"	background-color: rgb(0,0,0,0);\n"
"}\n"
"\n"
"")
        self.checkBox.setChecked(True)
        self.btn_login = QPushButton(Form)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(20, 210, 231, 41))
        self.btn_login.setStyleSheet(u"QPushButton {\n"
"	font: 18px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: white;\n"
"	border: 0px;\n"
"	padding-top: 5px;\n"
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
        QWidget.setTabOrder(self.edt_id, self.edt_pw)
        QWidget.setTabOrder(self.edt_pw, self.btn_login)
        QWidget.setTabOrder(self.btn_login, self.checkBox)
        QWidget.setTabOrder(self.checkBox, self.btn_find)
        QWidget.setTabOrder(self.btn_find, self.btn_register)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lb_form.setText(QCoreApplication.translate("Form", u"LOGIN (\ub85c\uadf8\uc778)", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\uc544 \uc774 \ub514", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\ud328 \uc2a4 \uc6cc \ub4dc", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\uc544\uc9c1 \ud68c\uc6d0\uc774 \uc544\ub2c8\uc2e0\uac00\uc694?", None))
        self.btn_find.setText(QCoreApplication.translate("Form", u"ID/PW \ucc3e\uae30", None))
        self.btn_register.setText(QCoreApplication.translate("Form", u"\ud68c\uc6d0\uac00\uc785 \ud558\uae30", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"\uc790\ub3d9 \ub85c\uadf8\uc778", None))
        self.btn_login.setText(QCoreApplication.translate("Form", u"\ub85c  \uadf8  \uc778", None))
    # retranslateUi

