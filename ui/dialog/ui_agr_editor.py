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
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_AgreementEditor(object):
    def _setupUi(self, AgreementEditor):
        if not AgreementEditor.objectName():
            AgreementEditor.setObjectName(u"AgreementEditor")
        AgreementEditor.resize(551, 516)
        AgreementEditor.setMinimumSize(QSize(551, 516))
        AgreementEditor.setMaximumSize(QSize(551, 516))
        AgreementEditor.setStyleSheet(u"QDialog {\n"
"	background-color: white;\n"
"}")
        self.top_bar = QWidget(AgreementEditor)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setGeometry(QRect(0, 0, 551, 61))
        self.top_bar.setStyleSheet(u"#top_bar {\n"
"	background-color: rgb(245, 245, 245);\n"
"	border-bottom: 1px solid;\n"
"	border-top: 1px solid;\n"
"	border-color: rgb(230, 230, 230);\n"
"}")
        self.lb_title = QLabel(self.top_bar)
        self.lb_title.setObjectName(u"lb_title")
        self.lb_title.setGeometry(QRect(170, 4, 210, 30))
        self.lb_title.setStyleSheet(u"QLabel{\n"
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
        self.lb_sub_title.setGeometry(QRect(180, 29, 190, 25))
        self.lb_sub_title.setStyleSheet(u"QLabel{\n"
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
        self.widget_3 = QWidget(AgreementEditor)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(10, 75, 531, 351))
        self.widget_3.setStyleSheet(u"\n"
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
"")
        self.cbx_keyword = QComboBox(self.widget_3)
        self.cbx_keyword.setObjectName(u"cbx_keyword")
        self.cbx_keyword.setEnabled(False)
        self.cbx_keyword.setGeometry(QRect(10, 6, 111, 30))
        self.cbx_keyword.setStyleSheet(u"QComboBox {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"    color: rgb(44, 62, 80);\n"
"	padding-top: 3px;\n"
"	padding-left: 5px;\n"
"    border: 1px solid gray;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    color: rgb(127, 140, 141);\n"
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
"QComboBox::setView {\n"
"    color: rgb(44, 62"
                        ", 80);\n"
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
        self.edt_title = QLineEdit(self.widget_3)
        self.edt_title.setObjectName(u"edt_title")
        self.edt_title.setGeometry(QRect(130, 6, 391, 30))
        self.edt_title.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(72,93,114);\n"
"    font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	border: 1px solid #34495e;\n"
"	padding-left: 58px;\n"
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
        self.lb_agr_title = QLabel(self.widget_3)
        self.lb_agr_title.setObjectName(u"lb_agr_title")
        self.lb_agr_title.setGeometry(QRect(134, 10, 51, 22))
        self.lb_agr_title.setStyleSheet(u"#lb_agr_title {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: white;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(149, 165, 166);\n"
"}")
        self.lb_agr_title.setAlignment(Qt.AlignCenter)
        self.lst_content = QListWidget(self.widget_3)
        self.lst_content.setObjectName(u"lst_content")
        self.lst_content.setGeometry(QRect(10, 50, 511, 211))
        self.lst_content.setStyleSheet(u"QListView {\n"
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
        self.lst_content.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.lst_content.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.lb_info = QLabel(self.widget_3)
        self.lb_info.setObjectName(u"lb_info")
        self.lb_info.setGeometry(QRect(300, 264, 221, 20))
        self.lb_info.setStyleSheet(u"QLabel {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(127, 140, 141);\n"
"}")
        self.lb_info.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lb_number = QLabel(self.widget_3)
        self.lb_number.setObjectName(u"lb_number")
        self.lb_number.setGeometry(QRect(20, 311, 20, 20))
        self.lb_number.setStyleSheet(u"QLabel {\n"
"	font: 11px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: white;\n"
"	background-color: rgb(82, 103, 124);\n"
"	padding-top: 2px;\n"
"	border-radius: 2px;\n"
"}")
        self.lb_number.setAlignment(Qt.AlignCenter)
        self.edt_add = QTextEdit(self.widget_3)
        self.edt_add.setObjectName(u"edt_add")
        self.edt_add.setGeometry(QRect(9, 295, 511, 50))
        self.edt_add.setStyleSheet(u"QTextEdit {\n"
"    font: 12px;\n"
"	border: 1px solid #34495e;\n"
"	padding-left: 35px;\n"
"	padding-top: 3px;\n"
"	padding-right: 80px;\n"
"}\n"
"\n"
"QTextEdit::hover {\n"
"	border: 1px solid #3498db;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"	border: 1px solid #3498db;\n"
"}")
        self.btn_add = QPushButton(self.widget_3)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setGeometry(QRect(449, 295, 71, 50))
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
        self.edt_add.raise_()
        self.cbx_keyword.raise_()
        self.edt_title.raise_()
        self.lb_agr_title.raise_()
        self.lst_content.raise_()
        self.lb_info.raise_()
        self.lb_number.raise_()
        self.btn_add.raise_()
        self.bottm_bar = QWidget(AgreementEditor)
        self.bottm_bar.setObjectName(u"bottm_bar")
        self.bottm_bar.setGeometry(QRect(0, 445, 551, 71))
        self.bottm_bar.setStyleSheet(u"#bottm_bar {\n"
"	background-color: rgb(245, 245, 245);\n"
"	border-top: 1px solid;\n"
"	border-color: rgb(230, 230, 230);\n"
"}\n"
"\n"
"#btn_save {\n"
"	font: 17px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: white;\n"
"	border: 0px;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(44,62,80);\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"#btn_save::hover {\n"
"	border: 0px;\n"
"	background-color: rgb(64,82,100);\n"
"	border-style: inset;\n"
"}\n"
"\n"
"#btn_save:pressed {\n"
"	border: 0px;\n"
"	background-color: rgb(24,42,60);\n"
"	border-style: inset;\n"
"}\n"
"")
        self.btn_save = QPushButton(self.bottm_bar)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(110, 15, 321, 41))
        self.btn_save.setStyleSheet(u"")
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
        self.lb_title.setText(QCoreApplication.translate("AgreementEditor", u"AGREEMENT", None))
        self.lb_sub_title.setText(QCoreApplication.translate("AgreementEditor", u"(  \ud2b9\uc57d\uc0ac\ud56d \ud3b8\uc9d1  )", None))
        self.lb_agr_title.setText(QCoreApplication.translate("AgreementEditor", u"\uc81c \u3000 \ubaa9", None))
        self.lb_info.setText(QCoreApplication.translate("AgreementEditor", u"* \uc6b0\uce21 \ub9c8\uc6b0\uc2a4 \ud074\ub9ad \uc2dc, \ud56d\ubaa9 \ud3b8\uc9d1 / \uc0ad\uc81c \uac00\ub2a5", None))
        self.lb_number.setText(QCoreApplication.translate("AgreementEditor", u"1", None))
        self.edt_add.setHtml(QCoreApplication.translate("AgreementEditor", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Gulim'; font-size:12px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.btn_add.setText(QCoreApplication.translate("AgreementEditor", u"\uc791  \uc131", None))
        self.btn_save.setText(QCoreApplication.translate("AgreementEditor", u"M y \ud2b9 \uc57d   \uc800 \uc7a5", None))
    # retranslateUi

