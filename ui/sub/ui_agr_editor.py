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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDialog,
    QFrame, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_AgreementEditor(object):
    def setupUi(self, AgreementEditor):
        if not AgreementEditor.objectName():
            AgreementEditor.setObjectName(u"AgreementEditor")
        AgreementEditor.resize(611, 602)
        AgreementEditor.setStyleSheet(u"QDialog {\n"
"	background-color: white;\n"
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
"    background-color: rgb(128,128,255);\n"
"}\n"
"\n"
""
                        "QComboBox::drop-down {\n"
"    width: 20px;\n"
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
"}\n"
"\n"
"QLineEdit {\n"
"	font: 13;\n"
"	color:  rgb(85,85,85);\n"
"	border: 1px solid rgb(130,130,130);\n"
"	border-radius: 2px;\n"
"	padding-left: 55px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	color:  rgb(65,65,65);\n"
"	border: 1px solid rgb(148,148,255);\n"
"	border-radius: 2px;\n"
"	padding-right: 21px;\n"
"}\n"
"\n"
"QListView {\n"
"	color: rgb(72,93,114);\n"
"    font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	border: 1px solid rgb(130,130"
                        ",130);\n"
"}\n"
"\n"
"QListView::hover {\n"
"	border: 1px solid rgb(148,148,255);\n"
"}\n"
"\n"
"QListView:focus {\n"
"	border: 1px solid rgb(148,148,255);\n"
"}\n"
"\n"
"QTextEdit {\n"
"	color: rgb(65,65,65);\n"
"	border: 1px solid rgb(130,130,130);\n"
"	border-radius: 2px;\n"
"	padding-left: 35px;\n"
"}\n"
"\n"
"QTextEdit:focus{\n"
"	color:  rgb(65,65,65);\n"
"	border: 1px solid rgb(148,148,255);\n"
"	border-radius: 2px;\n"
"	padding-right: 21px;\n"
"}")
        self.con_frame = QFrame(AgreementEditor)
        self.con_frame.setObjectName(u"con_frame")
        self.con_frame.setGeometry(QRect(30, 90, 551, 391))
        self.con_frame.setStyleSheet(u"#con_frame {\n"
"	background-color: white;\n"
"	border-radius: 15px;\n"
"}")
        self.cbx_keyword = QComboBox(self.con_frame)
        self.cbx_keyword.addItem("")
        self.cbx_keyword.setObjectName(u"cbx_keyword")
        self.cbx_keyword.setEnabled(False)
        self.cbx_keyword.setGeometry(QRect(20, 20, 111, 30))
        self.cbx_keyword.setStyleSheet(u"")
        self.edt_title = QLineEdit(self.con_frame)
        self.edt_title.setObjectName(u"edt_title")
        self.edt_title.setGeometry(QRect(140, 20, 391, 30))
        self.edt_title.setStyleSheet(u"")
        self.lb_agr_title = QLabel(self.con_frame)
        self.lb_agr_title.setObjectName(u"lb_agr_title")
        self.lb_agr_title.setGeometry(QRect(144, 24, 51, 22))
        self.lb_agr_title.setStyleSheet(u"#lb_agr_title {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(125,125,125);\n"
"	padding-top: 3px;\n"
"	background-color: white;\n"
"}")
        self.lb_agr_title.setAlignment(Qt.AlignCenter)
        self.lst_content = QListWidget(self.con_frame)
        self.lst_content.setObjectName(u"lst_content")
        self.lst_content.setGeometry(QRect(20, 70, 511, 211))
        self.lst_content.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.lst_content.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.lb_info = QLabel(self.con_frame)
        self.lb_info.setObjectName(u"lb_info")
        self.lb_info.setGeometry(QRect(310, 284, 221, 20))
        self.lb_info.setStyleSheet(u"QLabel {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(125,125,125);\n"
"}")
        self.lb_info.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lb_number = QLabel(self.con_frame)
        self.lb_number.setObjectName(u"lb_number")
        self.lb_number.setGeometry(QRect(30, 335, 20, 20))
        self.lb_number.setStyleSheet(u"QLabel {\n"
"	font: 11px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: white;\n"
"	background-color: rgb(125,125,255);\n"
"	padding-top: 2px;\n"
"	border-radius: 2px;\n"
"}")
        self.lb_number.setAlignment(Qt.AlignCenter)
        self.edt_add = QTextEdit(self.con_frame)
        self.edt_add.setObjectName(u"edt_add")
        self.edt_add.setGeometry(QRect(20, 320, 441, 50))
        self.btn_add = QPushButton(self.con_frame)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setGeometry(QRect(460, 320, 71, 50))
        self.btn_add.setStyleSheet(u"QPushButton {\n"
"    font: 16px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"    color: rgb(88,88,255);\n"
"    border: 1px solid rgb(128,128,255);\n"
"    padding-top: 3px;\n"
"    padding-left: 2px;\n"
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
        self.edt_add.raise_()
        self.cbx_keyword.raise_()
        self.edt_title.raise_()
        self.lb_agr_title.raise_()
        self.lst_content.raise_()
        self.lb_info.raise_()
        self.lb_number.raise_()
        self.btn_add.raise_()
        self.top_bar = QWidget(AgreementEditor)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setGeometry(QRect(0, 0, 611, 71))
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
        self.lb_title.setGeometry(QRect(-1, 10, 611, 30))
        self.lb_title.setStyleSheet(u"")
        self.lb_title.setAlignment(Qt.AlignCenter)
        self.lb_sub_title = QLabel(self.top_bar)
        self.lb_sub_title.setObjectName(u"lb_sub_title")
        self.lb_sub_title.setGeometry(QRect(0, 35, 611, 25))
        self.lb_sub_title.setStyleSheet(u"")
        self.lb_sub_title.setAlignment(Qt.AlignCenter)
        self.lb_sub_title.raise_()
        self.lb_title.raise_()
        self.btn_save = QPushButton(AgreementEditor)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(210, 520, 181, 41))
        self.btn_save.setStyleSheet(u"QPushButton {\n"
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
        QWidget.setTabOrder(self.cbx_keyword, self.edt_title)
        QWidget.setTabOrder(self.edt_title, self.lst_content)
        QWidget.setTabOrder(self.lst_content, self.edt_add)
        QWidget.setTabOrder(self.edt_add, self.btn_add)
        QWidget.setTabOrder(self.btn_add, self.btn_save)

        self.retranslateUi(AgreementEditor)

        QMetaObject.connectSlotsByName(AgreementEditor)
    # setupUi

    def retranslateUi(self, AgreementEditor):
        AgreementEditor.setWindowTitle(QCoreApplication.translate("AgreementEditor", u"\ub808\uc774 - Real estate Information", None))
        self.cbx_keyword.setItemText(0, QCoreApplication.translate("AgreementEditor", u"\ub9e4\ub9e4", None))

        self.lb_agr_title.setText(QCoreApplication.translate("AgreementEditor", u"\uc81c \u3000 \ubaa9", None))
        self.lb_info.setText(QCoreApplication.translate("AgreementEditor", u"* \uc6b0\uce21 \ub9c8\uc6b0\uc2a4 \ud074\ub9ad \uc2dc, \ud56d\ubaa9 \ud3b8\uc9d1 / \uc0ad\uc81c \uac00\ub2a5", None))
        self.lb_number.setText(QCoreApplication.translate("AgreementEditor", u"1", None))
        self.edt_add.setHtml(QCoreApplication.translate("AgreementEditor", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Gulim'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12px;\"><br /></p></body></html>", None))
        self.btn_add.setText(QCoreApplication.translate("AgreementEditor", u"\uc791  \uc131", None))
        self.lb_title.setText(QCoreApplication.translate("AgreementEditor", u"CONTRACT", None))
        self.lb_sub_title.setText(QCoreApplication.translate("AgreementEditor", u"(  \ud2b9\uc57d\uc0ac\ud56d \ud3b8\uc9d1  )", None))
        self.btn_save.setText(QCoreApplication.translate("AgreementEditor", u"\uc800 \uc7a5", None))
    # retranslateUi

