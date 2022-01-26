# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_lease_sub.ui'
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
    QListWidgetItem, QPushButton, QSizePolicy, QTextEdit,
    QWidget)
from ui.custom.TitleBarWidget import TitleBarWidget

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(551, 677)
        Dialog.setMinimumSize(QSize(551, 677))
        Dialog.setMaximumSize(QSize(551, 677))
        self.lb_titlebar = QLabel(Dialog)
        self.lb_titlebar.setObjectName(u"lb_titlebar")
        self.lb_titlebar.setGeometry(QRect(0, 0, 551, 677))
        self.lb_titlebar.setStyleSheet(u"QLabel{\n"
"	background-color: white;\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"    min-width: 4em;\n"
"	color: rgba(0, 0, 0, 120);\n"
"	padding-top: 8px;\n"
"	padding-left: 8px;\n"
"	border: 1px solid #ecf0f1;\n"
"}")
        self.lb_titlebar.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 20, 531, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.lb_name_1 = QLabel(Dialog)
        self.lb_name_1.setObjectName(u"lb_name_1")
        self.lb_name_1.setGeometry(QRect(20, 50, 61, 30))
        font = QFont()
        font.setFamilies([u"\uc6f0\ucef4\uccb4 Regular"])
        font.setBold(False)
        font.setItalic(False)
        self.lb_name_1.setFont(font)
        self.lb_name_1.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: #2c3e50;\n"
"	padding-top: 2px;\n"
"}")
        self.btn_add = QPushButton(Dialog)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setGeometry(QRect(460, 537, 71, 50))
        self.btn_add.setStyleSheet(u"QPushButton {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: white;\n"
"	border: 0px;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(64,82,100);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	border: 0px;\n"
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
        self.edt_add = QTextEdit(Dialog)
        self.edt_add.setObjectName(u"edt_add")
        self.edt_add.setGeometry(QRect(20, 537, 511, 50))
        self.edt_add.setStyleSheet(u"QTextEdit {\n"
"    font: 12px;\n"
"	border: 1px solid #34495e;\n"
"	padding-left: 35px;\n"
"	padding-top: 3px;\n"
"	padding-right: 40px;\n"
"}\n"
"\n"
"QTextEdit::hover {\n"
"	border: 1px solid #3498db;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"	border: 1px solid #3498db;\n"
"}\n"
"")
        self.line_6 = QFrame(Dialog)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(10, 220, 531, 20))
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.edt_title = QLineEdit(Dialog)
        self.edt_title.setObjectName(u"edt_title")
        self.edt_title.setGeometry(QRect(140, 247, 391, 30))
        self.edt_title.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(72,93,114);\n"
"    font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	border: 1px solid #34495e;\n"
"	padding-left: 55px;\n"
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
        self.lb_name_5 = QLabel(Dialog)
        self.lb_name_5.setObjectName(u"lb_name_5")
        self.lb_name_5.setGeometry(QRect(144, 251, 51, 22))
        self.lb_name_5.setStyleSheet(u"QLabel {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: white;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(149, 165, 166);\n"
"}")
        self.lb_name_5.setAlignment(Qt.AlignCenter)
        self.btn_save = QPushButton(Dialog)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(120, 610, 321, 41))
        self.btn_save.setStyleSheet(u"QPushButton {\n"
"	font: 17px \"\uc6f0\ucef4\uccb4 Regular\";\n"
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
        self.lst_agreement = QListWidget(Dialog)
        self.lst_agreement.setObjectName(u"lst_agreement")
        self.lst_agreement.setGeometry(QRect(20, 287, 511, 211))
        self.lst_agreement.setStyleSheet(u"QListView {\n"
"	color: rgb(72,93,114);\n"
"    font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	border: 1px solid #34495e;\n"
"}\n"
"\n"
"QListView::hover {\n"
"	border: 1px solid #3498db;\n"
"}\n"
"\n"
"QListView:focus {\n"
"	border: 1px solid #3498db;\n"
"}\n"
"")
        self.lb_number = QLabel(Dialog)
        self.lb_number.setObjectName(u"lb_number")
        self.lb_number.setGeometry(QRect(30, 553, 20, 20))
        self.lb_number.setStyleSheet(u"QLabel {\n"
"	font: 11px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: white;\n"
"	background-color: rgb(82, 103, 124);\n"
"	padding-top: 2px;\n"
"	border-radius: 2px;\n"
"}")
        self.lb_number.setAlignment(Qt.AlignCenter)
        self.cbx_keyword = QComboBox(Dialog)
        self.cbx_keyword.addItem("")
        self.cbx_keyword.addItem("")
        self.cbx_keyword.addItem("")
        self.cbx_keyword.addItem("")
        self.cbx_keyword.setObjectName(u"cbx_keyword")
        self.cbx_keyword.setGeometry(QRect(20, 247, 111, 30))
        self.cbx_keyword.setStyleSheet(u"QComboBox {\n"
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
"    image: url(./data/img/system/down_arrow.png);\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:hover {\n"
"    image: url(./data/img/sys"
                        "tem/down_arrow.png);\n"
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
        self.lb_sub_title_1 = QLabel(Dialog)
        self.lb_sub_title_1.setObjectName(u"lb_sub_title_1")
        self.lb_sub_title_1.setGeometry(QRect(20, 210, 111, 16))
        self.lb_sub_title_1.setStyleSheet(u"QLabel {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(127, 140, 141);\n"
"}")
        self.lst_agrs = QListWidget(Dialog)
        self.lst_agrs.setObjectName(u"lst_agrs")
        self.lst_agrs.setGeometry(QRect(210, 80, 321, 111))
        self.lst_agrs.setStyleSheet(u"QListView {\n"
"	color: rgb(72,93,114);\n"
"    font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	border: 1px solid #34495e;\n"
"}\n"
"\n"
"QListView::hover {\n"
"	border: 1px solid #3498db;\n"
"}\n"
"\n"
"QListView:focus {\n"
"	border: 1px solid #3498db;\n"
"}\n"
"")
        self.lb_info = QLabel(Dialog)
        self.lb_info.setObjectName(u"lb_info")
        self.lb_info.setGeometry(QRect(310, 501, 221, 20))
        self.lb_info.setStyleSheet(u"QLabel {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(127, 140, 141);\n"
"}")
        self.lb_info.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ckb_check = QCheckBox(Dialog)
        self.ckb_check.setObjectName(u"ckb_check")
        self.ckb_check.setGeometry(QRect(20, 517, 161, 16))
        self.ckb_check.setStyleSheet(u"QCheckBox {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(87,100,101);\n"
"	background-color: rgb(0,0,0,0);\n"
"}\n"
"\n"
"")
        self.lst_keyword = QListWidget(Dialog)
        self.lst_keyword.setObjectName(u"lst_keyword")
        self.lst_keyword.setGeometry(QRect(90, 80, 111, 111))
        self.lst_keyword.setStyleSheet(u"QListView {\n"
"	color: rgb(72,93,114);\n"
"    font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	border: 1px solid #34495e;\n"
"}\n"
"\n"
"QListView::hover {\n"
"	border: 1px solid #3498db;\n"
"}\n"
"\n"
"QListView:focus {\n"
"	border: 1px solid #3498db;\n"
"}\n"
"")
        self.lb_name_2 = QLabel(Dialog)
        self.lb_name_2.setObjectName(u"lb_name_2")
        self.lb_name_2.setGeometry(QRect(90, 51, 111, 30))
        self.lb_name_2.setFont(font)
        self.lb_name_2.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: #2c3e50;\n"
"    border: 1px solid gray;\n"
"	padding-top: 3px;\n"
"	padding-left: 10px;\n"
"	background-color: rgb(234, 234, 234);\n"
"}")
        self.lb_name_3 = QLabel(Dialog)
        self.lb_name_3.setObjectName(u"lb_name_3")
        self.lb_name_3.setGeometry(QRect(210, 51, 321, 30))
        self.lb_name_3.setFont(font)
        self.lb_name_3.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: #2c3e50;\n"
"    border: 1px solid gray;\n"
"	padding-top: 3px;\n"
"	padding-left: 10px;\n"
"	background-color: rgb(234, 234, 234);\n"
"}")
        self.lb_titlebar.raise_()
        self.line.raise_()
        self.lb_name_1.raise_()
        self.line_6.raise_()
        self.edt_title.raise_()
        self.lb_name_5.raise_()
        self.edt_add.raise_()
        self.btn_add.raise_()
        self.btn_save.raise_()
        self.lst_agreement.raise_()
        self.lb_number.raise_()
        self.cbx_keyword.raise_()
        self.lb_sub_title_1.raise_()
        self.lb_info.raise_()
        self.ckb_check.raise_()
        self.lb_name_2.raise_()
        self.lb_name_3.raise_()
        self.lst_keyword.raise_()
        self.lst_agrs.raise_()
        QWidget.setTabOrder(self.edt_title, self.lst_agreement)
        QWidget.setTabOrder(self.lst_agreement, self.edt_add)
        QWidget.setTabOrder(self.edt_add, self.btn_add)
        QWidget.setTabOrder(self.btn_add, self.btn_save)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"레이 - Real estate Information", None))
        self.lb_titlebar.setText(QCoreApplication.translate("Dialog", u"AGREEMENT - \ud2b9\uc57d\uc0ac\ud56d", None))
        self.lb_name_1.setText(QCoreApplication.translate("Dialog", u"My \ud2b9 \uc57d", None))
        self.btn_add.setText(QCoreApplication.translate("Dialog", u"\uc791  \uc131", None))
        self.edt_add.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Gulim'; font-size:12px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.lb_name_5.setText(QCoreApplication.translate("Dialog", u"\uc81c \u3000 \ubaa9", None))
        self.btn_save.setText(QCoreApplication.translate("Dialog", u"M y \ud2b9 \uc57d   \ucd94 \uac00", None))
        self.lb_number.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.cbx_keyword.setItemText(0, QCoreApplication.translate("Dialog", u"\ub9e4\ub9e4", None))
        self.cbx_keyword.setItemText(1, QCoreApplication.translate("Dialog", u"\uc804\uc138", None))
        self.cbx_keyword.setItemText(2, QCoreApplication.translate("Dialog", u"\uc6d4\uc138", None))
        self.cbx_keyword.setItemText(3, QCoreApplication.translate("Dialog", u"( \uc9c1\uc811\uc785\ub825 )", None))

        self.lb_sub_title_1.setText(QCoreApplication.translate("Dialog", u"\ud2b9\uc57d\uc0ac\ud56d \ucd94\uac00 & \ud3b8\uc9d1", None))
        self.lb_info.setText(QCoreApplication.translate("Dialog", u"* \uc6b0\uce21 \ub9c8\uc6b0\uc2a4 \ud074\ub9ad \uc2dc, \ud56d\ubaa9 \ud3b8\uc9d1 / \uc0ad\uc81c \uac00\ub2a5", None))
        self.ckb_check.setText(QCoreApplication.translate("Dialog", u"\ub9de\ucda4\ubc95, \ub744\uc5b4\uc4f0\uae30 \uc790\ub3d9 \uad50\uc815", None))
        self.lb_name_2.setText(QCoreApplication.translate("Dialog", u"\ud0a4 \uc6cc \ub4dc", None))
        self.lb_name_3.setText(QCoreApplication.translate("Dialog", u"My  \ud2b9\uc57d \ub9ac\uc2a4\ud2b8", None))
    # retranslateUi

