# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'doc_setting.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QStackedWidget, QWidget)

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(671, 471)
        main.setStyleSheet(u"#main {background-color: white;}")
        self.label_3 = QLabel(main)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(160, 0, 511, 51))
        self.label_3.setStyleSheet(u"QLabel {\n"
"	font: 20px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(44,62,80);\n"
"	padding-left: 10px;\n"
"}")
        self.listWidget = QListWidget(main)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(0, 0, 161, 471))
        self.listWidget.setStyleSheet(u"QListWidget {\n"
"	border: 0px;\n"
"	outline: none;\n"
"	font: 15px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: #2c3e50;\n"
"	background-color: rgb(245,245,245);\n"
"}\n"
"\n"
"QListWidget::item {\n"
"	border: 0px;\n"
"	padding-left: 5px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"}\n"
"\n"
"QListWidget::item:hover\n"
"{\n"
"    background: rgba(0,0,0,20); \n"
"}\n"
"\n"
"QListWidget::item:selected\n"
"{\n"
"	color: white;\n"
"    background: rgb(128,128,255);\n"
"}")
        self.stackedWidget = QStackedWidget(main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(160, 50, 511, 421))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page_1 = QFrame(self.page)
        self.page_1.setObjectName(u"page_1")
        self.page_1.setGeometry(QRect(0, 0, 511, 421))
        self.page_1.setStyleSheet(u"QFrame {\n"
"	background-color: white;\n"
"}\n"
"\n"
"QLabel {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(44,62,80);\n"
"}\n"
"\n"
"/* -------------------------------------------- */\n"
"\n"
"QLineEdit {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(44,62,80);\n"
"	padding-top: 2px;\n"
"	padding-left: 2px;\n"
"	border: 0px;\n"
"	border-bottom: 1px solid lightgray;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	border-bottom: 1px solid #3498db;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom: 1px solid #3498db;\n"
"}\n"
"\n"
"/* -------------------------------------------- */\n"
"\n"
"QPushButton{\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: white;\n"
"	padding-top: 3px;\n"
"	border-radius: 2px;\n"
"	background-color: rgb(128,128,255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(108,108,235);\n"
"}")
        self.page_1.setFrameShape(QFrame.StyledPanel)
        self.page_1.setFrameShadow(QFrame.Raised)
        self.edt_24_id = QLineEdit(self.page_1)
        self.edt_24_id.setObjectName(u"edt_24_id")
        self.edt_24_id.setGeometry(QRect(90, 55, 151, 30))
        self.btn_24_login = QPushButton(self.page_1)
        self.btn_24_login.setObjectName(u"btn_24_login")
        self.btn_24_login.setGeometry(QRect(415, 54, 61, 31))
        self.btn_24_login.setStyleSheet(u"")
        self.line = QFrame(self.page_1)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(25, 30, 461, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.hint_1 = QLabel(self.page_1)
        self.hint_1.setObjectName(u"hint_1")
        self.hint_1.setGeometry(QRect(25, 20, 171, 16))
        self.hint_1.setStyleSheet(u"color: rgb(127, 140, 141);")
        self.label_8 = QLabel(self.page_1)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 145, 61, 16))
        self.edt_cash_1 = QLineEdit(self.page_1)
        self.edt_cash_1.setObjectName(u"edt_cash_1")
        self.edt_cash_1.setGeometry(QRect(90, 135, 91, 30))
        self.edt_cash_1.setMaxLength(8)
        self.edt_cash_1.setAlignment(Qt.AlignCenter)
        self.edt_cash_pw = QLineEdit(self.page_1)
        self.edt_cash_pw.setObjectName(u"edt_cash_pw")
        self.edt_cash_pw.setGeometry(QRect(270, 135, 131, 30))
        self.edt_cash_pw.setEchoMode(QLineEdit.Password)
        self.line_3 = QFrame(self.page_1)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(25, 206, 461, 16))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.hint_3 = QLabel(self.page_1)
        self.hint_3.setObjectName(u"hint_3")
        self.hint_3.setGeometry(QRect(25, 196, 101, 16))
        self.hint_3.setStyleSheet(u"color: rgb(127, 140, 141);")
        self.btn_cash_login = QPushButton(self.page_1)
        self.btn_cash_login.setObjectName(u"btn_cash_login")
        self.btn_cash_login.setGeometry(QRect(415, 135, 61, 31))
        self.edt_cash_2 = QLineEdit(self.page_1)
        self.edt_cash_2.setObjectName(u"edt_cash_2")
        self.edt_cash_2.setGeometry(QRect(195, 135, 66, 30))
        self.edt_cash_2.setMaxLength(4)
        self.edt_cash_2.setAlignment(Qt.AlignCenter)
        self.edt_24_pw = QLineEdit(self.page_1)
        self.edt_24_pw.setObjectName(u"edt_24_pw")
        self.edt_24_pw.setGeometry(QRect(250, 55, 151, 30))
        self.label_10 = QLabel(self.page_1)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(30, 65, 61, 16))
        self.edt_iros_id = QLineEdit(self.page_1)
        self.edt_iros_id.setObjectName(u"edt_iros_id")
        self.edt_iros_id.setGeometry(QRect(90, 95, 151, 30))
        self.btn_iros_login = QPushButton(self.page_1)
        self.btn_iros_login.setObjectName(u"btn_iros_login")
        self.btn_iros_login.setGeometry(QRect(415, 94, 61, 31))
        self.btn_iros_login.setStyleSheet(u"")
        self.label_11 = QLabel(self.page_1)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(30, 105, 61, 16))
        self.edt_iros_pw = QLineEdit(self.page_1)
        self.edt_iros_pw.setObjectName(u"edt_iros_pw")
        self.edt_iros_pw.setGeometry(QRect(250, 95, 151, 30))
        self.label_9 = QLabel(self.page_1)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 239, 81, 16))
        self.edt_pdf_path = QLineEdit(self.page_1)
        self.edt_pdf_path.setObjectName(u"edt_pdf_path")
        self.edt_pdf_path.setGeometry(QRect(120, 231, 311, 30))
        self.edt_pdf_path.setStyleSheet(u"#edt_pdf_path {\n"
"	border: 1px solid rgb(170,170,170);\n"
"}")
        self.edt_pdf_path.setReadOnly(True)
        self.btn_path = QPushButton(self.page_1)
        self.btn_path.setObjectName(u"btn_path")
        self.btn_path.setGeometry(QRect(440, 230, 31, 31))
        self.btn_path.setStyleSheet(u"#btn_path {\n"
"	background-color: rgba(0,0,0,0);\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"#btn_path::hover {\n"
"	background-color: rgba(44,62,80,50)\n"
"}\n"
"\n"
"#btn_path:pressed {\n"
"	background-color: rgba(44,62,80,80)\n"
"}")
        self.label_12 = QLabel(self.page_1)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(185, 145, 16, 16))
        self.edt_24_id.raise_()
        self.line.raise_()
        self.hint_1.raise_()
        self.label_8.raise_()
        self.edt_cash_1.raise_()
        self.edt_cash_pw.raise_()
        self.line_3.raise_()
        self.hint_3.raise_()
        self.btn_cash_login.raise_()
        self.edt_cash_2.raise_()
        self.edt_24_pw.raise_()
        self.btn_24_login.raise_()
        self.label_10.raise_()
        self.edt_iros_id.raise_()
        self.btn_iros_login.raise_()
        self.label_11.raise_()
        self.edt_iros_pw.raise_()
        self.label_9.raise_()
        self.edt_pdf_path.raise_()
        self.btn_path.raise_()
        self.label_12.raise_()
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)
        QWidget.setTabOrder(self.edt_24_id, self.edt_24_pw)
        QWidget.setTabOrder(self.edt_24_pw, self.btn_24_login)
        QWidget.setTabOrder(self.btn_24_login, self.edt_iros_id)
        QWidget.setTabOrder(self.edt_iros_id, self.edt_iros_pw)
        QWidget.setTabOrder(self.edt_iros_pw, self.btn_iros_login)
        QWidget.setTabOrder(self.btn_iros_login, self.edt_cash_1)
        QWidget.setTabOrder(self.edt_cash_1, self.edt_cash_2)
        QWidget.setTabOrder(self.edt_cash_2, self.edt_cash_pw)
        QWidget.setTabOrder(self.edt_cash_pw, self.btn_cash_login)
        QWidget.setTabOrder(self.btn_cash_login, self.edt_pdf_path)
        QWidget.setTabOrder(self.edt_pdf_path, self.btn_path)
        QWidget.setTabOrder(self.btn_path, self.listWidget)

        self.retranslateUi(main)

        self.listWidget.setCurrentRow(0)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"\ub808\uc774 - Real estate Information", None))
        self.label_3.setText(QCoreApplication.translate("main", u"\ubb38\uc11c \ubc1c\uae09 \uacc4\uc815 \uc124\uc815", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("main", u"\ubb38\uc11c \ubc1c\uae09 \uacc4\uc815 \uc124\uc815", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.edt_24_id.setText("")
        self.btn_24_login.setText(QCoreApplication.translate("main", u"\uc778 \uc99d", None))
        self.hint_1.setText(QCoreApplication.translate("main", u"\uacc4\uc815 \uc778\uc99d / \uc804\uc790\uc9c0\ubd88 \uc120\ubd88\uce74\ub4dc", None))
        self.label_8.setText(QCoreApplication.translate("main", u"\uce74\ub4dc\ubc88\ud638", None))
        self.edt_cash_1.setText("")
        self.hint_3.setText(QCoreApplication.translate("main", u"\ub4f1\uae30\ubd80\ub4f1\ubcf8 \uc124\uc815", None))
        self.btn_cash_login.setText(QCoreApplication.translate("main", u"\uc800 \uc7a5", None))
        self.edt_cash_2.setText("")
        self.edt_24_pw.setText("")
        self.label_10.setText(QCoreApplication.translate("main", u"\uc815\ubd8024", None))
        self.edt_iros_id.setText("")
        self.btn_iros_login.setText(QCoreApplication.translate("main", u"\uc778 \uc99d", None))
        self.label_11.setText(QCoreApplication.translate("main", u"\ub4f1 \uae30 \uc18c", None))
        self.edt_iros_pw.setText("")
        self.label_9.setText(QCoreApplication.translate("main", u"PDF \uc800\uc7a5 \uacbd\ub85c", None))
        self.btn_path.setText("")
        self.label_12.setText(QCoreApplication.translate("main", u"-", None))
    # retranslateUi

