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
        AgreementEditor.resize(591, 682)
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
"	font: 13px;\n"
"	color:  rgb(85,85,85);\n"
"	border: 1px solid rgb(130,130,130);\n"
"	border-radius: 2px;\n"
"	padding-left: 70px;\n"
"	padding-top: 1px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	color:  rgb(65,65,65);\n"
"	border: 1px solid rgb(148,148,255);\n"
"	border-radius: 2px;\n"
"	padding-right: 21px;\n"
"}\n"
"\n"
"#lst_content {\n"
"	color: rgb(72,93,114);\n"
"    font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	b"
                        "order: 1px solid rgb(130,130,130);\n"
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
"	padding-top: 3px;\n"
"}\n"
"\n"
"QLabel {\n"
"	font: 15px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color:  rgb(65,65,65);\n"
"	padding-top: 2px;\n"
"}")
        self.top_bar = QWidget(AgreementEditor)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setGeometry(QRect(0, 0, 591, 71))
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
        self.lb_title.setGeometry(QRect(-1, 10, 591, 30))
        self.lb_title.setStyleSheet(u"")
        self.lb_title.setAlignment(Qt.AlignCenter)
        self.lb_sub_title = QLabel(self.top_bar)
        self.lb_sub_title.setObjectName(u"lb_sub_title")
        self.lb_sub_title.setGeometry(QRect(0, 35, 591, 25))
        self.lb_sub_title.setStyleSheet(u"")
        self.lb_sub_title.setAlignment(Qt.AlignCenter)
        self.lb_sub_title.raise_()
        self.lb_title.raise_()
        self.btn_save = QPushButton(AgreementEditor)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(200, 600, 191, 41))
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
        self.edt_frame = QFrame(AgreementEditor)
        self.edt_frame.setObjectName(u"edt_frame")
        self.edt_frame.setGeometry(QRect(20, 90, 551, 471))
        self.edt_frame.setStyleSheet(u"#edt_frame {\n"
"	background-color: white;\n"
"	border-radius: 15px;\n"
"}")
        self.lst_content = QListWidget(self.edt_frame)
        self.lst_content.setObjectName(u"lst_content")
        self.lst_content.setGeometry(QRect(20, 110, 511, 251))
        self.lst_content.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.lst_content.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.lb_info = QLabel(self.edt_frame)
        self.lb_info.setObjectName(u"lb_info")
        self.lb_info.setGeometry(QRect(310, 365, 221, 20))
        self.lb_info.setStyleSheet(u"QLabel {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(125,125,125);\n"
"}")
        self.lb_info.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.cbx_category = QComboBox(self.edt_frame)
        self.cbx_category.setObjectName(u"cbx_category")
        self.cbx_category.setGeometry(QRect(120, 20, 101, 30))
        self.cbx_category.setStyleSheet(u"QListView {\n"
"	margin-top: 2px;\n"
"}")
        self.cbx_title = QComboBox(self.edt_frame)
        self.cbx_title.setObjectName(u"cbx_title")
        self.cbx_title.setGeometry(QRect(290, 20, 241, 30))
        self.cbx_title.setStyleSheet(u"QListView {\n"
"	margin-top: 2px;\n"
"}")
        self.frame = QFrame(self.edt_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 400, 521, 51))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btn_add = QPushButton(self.frame)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setGeometry(QRect(440, 0, 71, 50))
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
        self.lb_number = QLabel(self.frame)
        self.lb_number.setObjectName(u"lb_number")
        self.lb_number.setGeometry(QRect(10, 15, 20, 20))
        self.lb_number.setStyleSheet(u"QLabel {\n"
"	font: 11px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: white;\n"
"	background-color: rgb(125,125,255);\n"
"	padding-top: 2px;\n"
"	border-radius: 2px;\n"
"}")
        self.lb_number.setAlignment(Qt.AlignCenter)
        self.edt_add = QTextEdit(self.frame)
        self.edt_add.setObjectName(u"edt_add")
        self.edt_add.setGeometry(QRect(0, 0, 441, 50))
        self.edt_add.raise_()
        self.btn_add.raise_()
        self.lb_number.raise_()
        self.edt_title = QLineEdit(self.edt_frame)
        self.edt_title.setObjectName(u"edt_title")
        self.edt_title.setEnabled(True)
        self.edt_title.setGeometry(QRect(20, 70, 511, 30))
        self.edt_title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label = QLabel(self.edt_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(25, 72, 61, 25))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"QLabel {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(125,125,125);\n"
"	padding-top: 3px;\n"
"	background-color: white; \n"
"}")
        self.name_title = QLabel(self.edt_frame)
        self.name_title.setObjectName(u"name_title")
        self.name_title.setGeometry(QRect(240, 20, 41, 29))
        font = QFont()
        font.setFamilies([u"\uc6f0\ucef4\uccb4 Regular"])
        font.setBold(False)
        font.setItalic(False)
        self.name_title.setFont(font)
        self.name_title.setStyleSheet(u"")
        self.name_category = QLabel(self.edt_frame)
        self.name_category.setObjectName(u"name_category")
        self.name_category.setGeometry(QRect(20, 20, 61, 29))
        self.name_category.setFont(font)
        self.name_category.setStyleSheet(u"")
        self.btn_add_category = QPushButton(self.edt_frame)
        self.btn_add_category.setObjectName(u"btn_add_category")
        self.btn_add_category.setGeometry(QRect(80, 20, 30, 30))
        self.btn_add_category.setStyleSheet(u"QPushButton {\n"
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
        self.category_back = QFrame(AgreementEditor)
        self.category_back.setObjectName(u"category_back")
        self.category_back.setGeometry(QRect(610, 30, 341, 401))
        self.category_back.setFrameShape(QFrame.StyledPanel)
        self.category_back.setFrameShadow(QFrame.Raised)
        self.category_frame = QFrame(self.category_back)
        self.category_frame.setObjectName(u"category_frame")
        self.category_frame.setGeometry(QRect(20, 20, 301, 361))
        self.category_frame.setStyleSheet(u"#category_frame{\n"
"	border: 1px solid rgb(200,200,200);\n"
"	background: white;\n"
"}")
        self.category_frame.setFrameShape(QFrame.StyledPanel)
        self.category_frame.setFrameShadow(QFrame.Raised)
        self.lst_category = QListWidget(self.category_frame)
        self.lst_category.setObjectName(u"lst_category")
        self.lst_category.setGeometry(QRect(30, 68, 241, 161))
        self.edt_category = QLineEdit(self.category_frame)
        self.edt_category.setObjectName(u"edt_category")
        self.edt_category.setEnabled(True)
        self.edt_category.setGeometry(QRect(30, 240, 201, 30))
        self.edt_category.setStyleSheet(u"QLabel {\n"
"	font: 13px;\n"
"}")
        self.edt_category.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_2 = QLabel(self.category_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(34, 242, 61, 25))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet(u"QLabel {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(125,125,125);\n"
"	padding-top: 3px;\n"
"	background-color: white; \n"
"}")
        self.btn_category_cancel = QPushButton(self.category_frame)
        self.btn_category_cancel.setObjectName(u"btn_category_cancel")
        self.btn_category_cancel.setGeometry(QRect(70, 300, 71, 31))
        self.btn_category_cancel.setStyleSheet(u"QPushButton {\n"
"    font: 15px \"\uc6f0\ucef4\uccb4 Regular\";\n"
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
        self.btn_category_save = QPushButton(self.category_frame)
        self.btn_category_save.setObjectName(u"btn_category_save")
        self.btn_category_save.setGeometry(QRect(150, 300, 81, 31))
        self.btn_category_save.setStyleSheet(u"QPushButton {\n"
"    font: 15px \"\uc6f0\ucef4\uccb4 Regular\";\n"
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
        self.lb_category_edt = QLabel(self.category_frame)
        self.lb_category_edt.setObjectName(u"lb_category_edt")
        self.lb_category_edt.setGeometry(QRect(0, 20, 300, 25))
        self.lb_category_edt.setStyleSheet(u"#lb_category_edt {\n"
"	font: 15px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgba(0, 0, 0, 120);\n"
"	padding-top: 8px;\n"
"	padding-left: 8px;\n"
"	border: 0px;\n"
"}")
        self.lb_category_edt.setAlignment(Qt.AlignCenter)
        self.btn_category_add = QPushButton(self.category_frame)
        self.btn_category_add.setObjectName(u"btn_category_add")
        self.btn_category_add.setGeometry(QRect(240, 240, 30, 30))
        self.btn_category_add.setStyleSheet(u"QPushButton {\n"
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

        self.retranslateUi(AgreementEditor)

        QMetaObject.connectSlotsByName(AgreementEditor)
    # setupUi

    def retranslateUi(self, AgreementEditor):
        AgreementEditor.setWindowTitle(QCoreApplication.translate("AgreementEditor", u"\ub808\uc774 - Real estate Information", None))
        self.lb_title.setText(QCoreApplication.translate("AgreementEditor", u"CONTRACT", None))
        self.lb_sub_title.setText(QCoreApplication.translate("AgreementEditor", u"(  \ud2b9\uc57d\uc0ac\ud56d \ucd94\uac00/\ud3b8\uc9d1  )", None))
        self.btn_save.setText(QCoreApplication.translate("AgreementEditor", u"\uc800 \uc7a5", None))
        self.lb_info.setText(QCoreApplication.translate("AgreementEditor", u"* \ub9c8\uc6b0\uc2a4 \uc6b0\uce21 \ud074\ub9ad \uc2dc, \ud56d\ubaa9 \ud3b8\uc9d1 / \uc0ad\uc81c \uac00\ub2a5", None))
        self.btn_add.setText(QCoreApplication.translate("AgreementEditor", u"\uc791  \uc131", None))
        self.lb_number.setText(QCoreApplication.translate("AgreementEditor", u"1", None))
        self.edt_add.setHtml(QCoreApplication.translate("AgreementEditor", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Gulim'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12px;\"><br /></p></body></html>", None))
        self.edt_title.setText("")
        self.label.setText(QCoreApplication.translate("AgreementEditor", u"\ud2b9 \uc57d \uc81c \ubaa9", None))
        self.name_title.setText(QCoreApplication.translate("AgreementEditor", u"\uc81c \ubaa9", None))
        self.name_category.setText(QCoreApplication.translate("AgreementEditor", u"\uce74\ud14c\uace0\ub9ac", None))
        self.btn_add_category.setText("")
        self.edt_category.setText("")
        self.label_2.setText(QCoreApplication.translate("AgreementEditor", u"\uce74\ud14c\uace0\ub9ac\uba85", None))
        self.btn_category_cancel.setText(QCoreApplication.translate("AgreementEditor", u"\ub2eb \uae30", None))
        self.btn_category_save.setText(QCoreApplication.translate("AgreementEditor", u"\uc800 \uc7a5", None))
        self.lb_category_edt.setText(QCoreApplication.translate("AgreementEditor", u"\uce74\ud14c\uace0\ub9ac \ud3b8\uc9d1", None))
        self.btn_category_add.setText("")
    # retranslateUi

