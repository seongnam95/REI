# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_agr_editor.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFontComboBox,
    QFrame, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QStackedWidget,
    QTextEdit, QWidget)

class Ui_AgrEditor(object):
    def setupUi(self, AgrEditor):
        if not AgrEditor.objectName():
            AgrEditor.setObjectName(u"AgrEditor")
        AgrEditor.resize(711, 791)
        AgrEditor.setStyleSheet(u"#AgrEditor{ background: white; }\n"
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
"QTextEdit {\n"
"	color: rgb(65,65,65);\n"
"	border: 1px solid rgb(130,130,130);\n"
"	border-radius: 2px;\n"
"	padding: 5px 5px 5px 5px;\n"
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
"QListWidget {\n"
"	border: 1px solid rgb(130,130,130);\n"
"}\n"
"\n"
"QLabel {\n"
"	font: 15px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color:  rgb(65,65,65);\n"
"	padding-top: 2px;\n"
"}")
        self.top_bar = QWidget(AgrEditor)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setGeometry(QRect(0, 0, 711, 71))
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
        self.lb_title.setGeometry(QRect(-1, 10, 711, 30))
        self.lb_title.setStyleSheet(u"")
        self.lb_title.setAlignment(Qt.AlignCenter)
        self.lb_sub_title = QLabel(self.top_bar)
        self.lb_sub_title.setObjectName(u"lb_sub_title")
        self.lb_sub_title.setGeometry(QRect(0, 35, 711, 25))
        self.lb_sub_title.setStyleSheet(u"")
        self.lb_sub_title.setAlignment(Qt.AlignCenter)
        self.lb_sub_title.raise_()
        self.lb_title.raise_()
        self.btn_save = QPushButton(AgrEditor)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(480, 710, 191, 41))
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
        self.btn_close = QPushButton(AgrEditor)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(360, 710, 111, 41))
        self.btn_close.setStyleSheet(u"QPushButton {\n"
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
"QPushButton:hover {\n"
"	color: rgb(118,118,255);\n"
"    border: 1px solid rgb(158,158,255);\n"
"}")
        self.stackedWidget = QStackedWidget(AgrEditor)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 70, 711, 221))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.category_frame = QFrame(self.page)
        self.category_frame.setObjectName(u"category_frame")
        self.category_frame.setGeometry(QRect(30, 20, 251, 191))
        self.category_frame.setStyleSheet(u"#category_frame {\n"
"	background: white;\n"
"	border-radius: 15px;\n"
"}")
        self.category_frame.setFrameShape(QFrame.StyledPanel)
        self.category_frame.setFrameShadow(QFrame.Raised)
        self.lst_category = QListWidget(self.category_frame)
        QListWidgetItem(self.lst_category)
        self.lst_category.setObjectName(u"lst_category")
        self.lst_category.setGeometry(QRect(20, 60, 211, 111))
        self.name_category = QLabel(self.category_frame)
        self.name_category.setObjectName(u"name_category")
        self.name_category.setGeometry(QRect(20, 20, 71, 30))
        font = QFont()
        font.setFamilies([u"\uc6f0\ucef4\uccb4 Regular"])
        font.setBold(False)
        font.setItalic(False)
        self.name_category.setFont(font)
        self.name_category.setStyleSheet(u"")
        self.name_category.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.btn_add_category = QPushButton(self.category_frame)
        self.btn_add_category.setObjectName(u"btn_add_category")
        self.btn_add_category.setGeometry(QRect(200, 20, 30, 30))
        self.btn_add_category.setStyleSheet(u"QPushButton {\n"
"	border-radius: 4px;\n"
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
        self.name_category.raise_()
        self.lst_category.raise_()
        self.btn_add_category.raise_()
        self.title_frame = QFrame(self.page)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setGeometry(QRect(300, 20, 381, 191))
        self.title_frame.setStyleSheet(u"#title_frame {\n"
"	background: white;\n"
"	border-radius: 15px;\n"
"}")
        self.title_frame.setFrameShape(QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.name_category_2 = QLabel(self.title_frame)
        self.name_category_2.setObjectName(u"name_category_2")
        self.name_category_2.setGeometry(QRect(20, 20, 61, 30))
        self.name_category_2.setFont(font)
        self.name_category_2.setStyleSheet(u"")
        self.name_category_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lst_title = QListWidget(self.title_frame)
        QListWidgetItem(self.lst_title)
        self.lst_title.setObjectName(u"lst_title")
        self.lst_title.setGeometry(QRect(20, 60, 341, 111))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.frame = QFrame(self.page_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 20, 651, 71))
        self.frame.setStyleSheet(u"QComboBox {\n"
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
"QComboBox::drop-down {\n"
"    width: 20px;\n"
"\n"
""
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
"QLineEdit {\n"
"	font: 13px;\n"
"	color:  rgb(85,85,85);\n"
"	border: 1px solid rgb(130,130,130);\n"
"	border-radius: 2px;\n"
"	padding-left: 5px;\n"
"	padding-top: 1px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	color:  rgb(65,65,65);\n"
"	border: 1px solid rgb(148,148,255);\n"
"	border-radius: 2px;\n"
"	padding-right: 21px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.cbx_category = QComboBox(self.frame)
        self.cbx_category.setObjectName(u"cbx_category")
        self.cbx_category.setGeometry(QRect(110, 20, 121, 30))
        self.cbx_category.setStyleSheet(u"QListView {\n"
"	margin-top: 2px;\n"
"}")
        self.name_title = QLabel(self.frame)
        self.name_title.setObjectName(u"name_title")
        self.name_title.setGeometry(QRect(260, 20, 41, 29))
        self.name_title.setFont(font)
        self.name_title.setStyleSheet(u"")
        self.name_category_3 = QLabel(self.frame)
        self.name_category_3.setObjectName(u"name_category_3")
        self.name_category_3.setGeometry(QRect(30, 20, 61, 29))
        self.name_category_3.setFont(font)
        self.name_category_3.setStyleSheet(u"")
        self.edt_title = QLineEdit(self.frame)
        self.edt_title.setObjectName(u"edt_title")
        self.edt_title.setEnabled(True)
        self.edt_title.setGeometry(QRect(320, 20, 311, 30))
        self.edt_title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.stackedWidget.addWidget(self.page_2)
        self.text_frame = QFrame(AgrEditor)
        self.text_frame.setObjectName(u"text_frame")
        self.text_frame.setGeometry(QRect(30, 300, 651, 371))
        self.text_frame.setStyleSheet(u"#text_frame {\n"
"	background: white;\n"
"	border-radius: 15px;\n"
"}")
        self.text_frame.setFrameShape(QFrame.StyledPanel)
        self.text_frame.setFrameShadow(QFrame.Raised)
        self.textEdit = QTextEdit(self.text_frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(20, 60, 611, 291))
        self.frame_3 = QFrame(self.text_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(20, 20, 611, 31))
        self.frame_3.setStyleSheet(u"QComboBox {\n"
"    border: none;\n"
"    padding-top: 4px;\n"
"    padding-left: 10px;\n"
"    min-width: 3em;\n"
"    background: rgb(255, 255, 255);\n"
"    font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"    color: rgb(65, 65, 65);\n"
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
"QComboBox::drop-down {\n"
"    width: 20px;\n"
"\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    i"
                        "mage: url(../../data/img/system/down_arrow_icon.png);\n"
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
"QPushButton {\n"
"    padding-top: 3px;\n"
"    padding-left: 2px;\n"
"    background: white;\n"
"    outline: none;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    padding-left: 4px;\n"
"    padding-top: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(118,118,255);\n"
"    border: 1px solid rgb(158,158,255);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.btn_bold = QPushButton(self.frame_3)
        self.btn_bold.setObjectName(u"btn_bold")
        self.btn_bold.setGeometry(QRect(230, 0, 30, 30))
        self.btn_bold.setStyleSheet(u"#btn_bold {\n"
"    image: url(../../data/img/button/bold_icon.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"#btn_bold:hover {\n"
"    image: url(../../data/img/button/bold_hover_icon.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}")
        self.btn_italic = QPushButton(self.frame_3)
        self.btn_italic.setObjectName(u"btn_italic")
        self.btn_italic.setGeometry(QRect(260, 0, 30, 30))
        self.btn_italic.setStyleSheet(u"#btn_italic {\n"
"    image: url(../../data/img/button/italic_icon.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"#btn_italic:hover {\n"
"    image: url(../../data/img/button/italic_hover_icon.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}")
        self.btn_under_line = QPushButton(self.frame_3)
        self.btn_under_line.setObjectName(u"btn_under_line")
        self.btn_under_line.setGeometry(QRect(290, 0, 30, 30))
        self.btn_under_line.setStyleSheet(u"#btn_under_line {\n"
"    image: url(../../data/img/button/under_icon.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"#btn_under_line:hover {\n"
"    image: url(../../data/img/button/under_hover_icon.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}")
        self.btn_color = QPushButton(self.frame_3)
        self.btn_color.setObjectName(u"btn_color")
        self.btn_color.setGeometry(QRect(320, 0, 30, 30))
        self.btn_color.setStyleSheet(u"#btn_under_line {\n"
"    image: url(../../data/img/button/color_icon.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"#btn_under_line:hover {\n"
"    image: url(../../data/img/button/color_hover_icon.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}")
        self.cbx_fontsize = QComboBox(self.frame_3)
        self.cbx_fontsize.addItem("")
        self.cbx_fontsize.addItem("")
        self.cbx_fontsize.addItem("")
        self.cbx_fontsize.addItem("")
        self.cbx_fontsize.addItem("")
        self.cbx_fontsize.addItem("")
        self.cbx_fontsize.addItem("")
        self.cbx_fontsize.addItem("")
        self.cbx_fontsize.addItem("")
        self.cbx_fontsize.addItem("")
        self.cbx_fontsize.addItem("")
        self.cbx_fontsize.addItem("")
        self.cbx_fontsize.addItem("")
        self.cbx_fontsize.setObjectName(u"cbx_fontsize")
        self.cbx_fontsize.setGeometry(QRect(160, 0, 61, 30))
        self.cbx_font = QFontComboBox(self.frame_3)
        self.cbx_font.setObjectName(u"cbx_font")
        self.cbx_font.setGeometry(QRect(0, 0, 151, 30))
        self.btn_color_2 = QPushButton(self.frame_3)
        self.btn_color_2.setObjectName(u"btn_color_2")
        self.btn_color_2.setGeometry(QRect(530, 0, 81, 30))
        self.btn_color_2.setStyleSheet(u"QPushButton {\n"
"    font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"    color: rgb(88,88,255);\n"
"}")

        self.retranslateUi(AgrEditor)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AgrEditor)
    # setupUi

    def retranslateUi(self, AgrEditor):
        AgrEditor.setWindowTitle(QCoreApplication.translate("AgrEditor", u"Dialog", None))
        self.lb_title.setText(QCoreApplication.translate("AgrEditor", u"CONTRACT", None))
        self.lb_sub_title.setText(QCoreApplication.translate("AgrEditor", u"(  \ud2b9\uc57d\uc0ac\ud56d \ucd94\uac00/\ud3b8\uc9d1  )", None))
        self.btn_save.setText(QCoreApplication.translate("AgrEditor", u"\uc800 \uc7a5", None))
        self.btn_close.setText(QCoreApplication.translate("AgrEditor", u"\ub2eb \uae30", None))

        __sortingEnabled = self.lst_category.isSortingEnabled()
        self.lst_category.setSortingEnabled(False)
        ___qlistwidgetitem = self.lst_category.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("AgrEditor", u"\ub9e4\ub9e4", None));
        self.lst_category.setSortingEnabled(__sortingEnabled)

        self.name_category.setText(QCoreApplication.translate("AgrEditor", u"\uce74\ud14c\uace0\ub9ac", None))
        self.btn_add_category.setText("")
        self.name_category_2.setText(QCoreApplication.translate("AgrEditor", u"\ud2b9\uc57d\uc0ac\ud56d", None))

        __sortingEnabled1 = self.lst_title.isSortingEnabled()
        self.lst_title.setSortingEnabled(False)
        ___qlistwidgetitem1 = self.lst_title.item(0)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("AgrEditor", u"\ub9e4\ub9e4 \uae30\ubcf8 \ud2b9\uc57d", None));
        self.lst_title.setSortingEnabled(__sortingEnabled1)

        self.name_title.setText(QCoreApplication.translate("AgrEditor", u"\uc81c \ubaa9", None))
        self.name_category_3.setText(QCoreApplication.translate("AgrEditor", u"\uce74\ud14c\uace0\ub9ac", None))
        self.edt_title.setText("")
        self.btn_bold.setText(QCoreApplication.translate("AgrEditor", u"B", None))
        self.btn_italic.setText(QCoreApplication.translate("AgrEditor", u"I", None))
        self.btn_under_line.setText(QCoreApplication.translate("AgrEditor", u"U", None))
        self.btn_color.setText(QCoreApplication.translate("AgrEditor", u"C", None))
        self.cbx_fontsize.setItemText(0, QCoreApplication.translate("AgrEditor", u"8", None))
        self.cbx_fontsize.setItemText(1, QCoreApplication.translate("AgrEditor", u"9", None))
        self.cbx_fontsize.setItemText(2, QCoreApplication.translate("AgrEditor", u"10", None))
        self.cbx_fontsize.setItemText(3, QCoreApplication.translate("AgrEditor", u"11", None))
        self.cbx_fontsize.setItemText(4, QCoreApplication.translate("AgrEditor", u"12", None))
        self.cbx_fontsize.setItemText(5, QCoreApplication.translate("AgrEditor", u"13", None))
        self.cbx_fontsize.setItemText(6, QCoreApplication.translate("AgrEditor", u"14", None))
        self.cbx_fontsize.setItemText(7, QCoreApplication.translate("AgrEditor", u"15", None))
        self.cbx_fontsize.setItemText(8, QCoreApplication.translate("AgrEditor", u"16", None))
        self.cbx_fontsize.setItemText(9, QCoreApplication.translate("AgrEditor", u"17", None))
        self.cbx_fontsize.setItemText(10, QCoreApplication.translate("AgrEditor", u"18", None))
        self.cbx_fontsize.setItemText(11, QCoreApplication.translate("AgrEditor", u"19", None))
        self.cbx_fontsize.setItemText(12, QCoreApplication.translate("AgrEditor", u"20", None))

        self.btn_color_2.setText(QCoreApplication.translate("AgrEditor", u"\ub9de\ucda4\ubc95 \uac80\uc0ac", None))
    # retranslateUi

