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
        AgrEditor.resize(711, 781)
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
        self.lst_title.setObjectName(u"lst_title")
        self.lst_title.setGeometry(QRect(20, 60, 341, 111))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.add_frame = QFrame(self.page_2)
        self.add_frame.setObjectName(u"add_frame")
        self.add_frame.setGeometry(QRect(30, 20, 651, 71))
        self.add_frame.setStyleSheet(u"#add_frame {\n"
"	background: white;\n"
"	border-radius: 15px;\n"
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
"    background-color: rgb(128"
                        ",128,255);\n"
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
        self.add_frame.setFrameShape(QFrame.StyledPanel)
        self.add_frame.setFrameShadow(QFrame.Raised)
        self.cbx_category = QComboBox(self.add_frame)
        self.cbx_category.setObjectName(u"cbx_category")
        self.cbx_category.setGeometry(QRect(110, 20, 121, 30))
        self.cbx_category.setStyleSheet(u"QListView {\n"
"	margin-top: 2px;\n"
"}")
        self.name_title = QLabel(self.add_frame)
        self.name_title.setObjectName(u"name_title")
        self.name_title.setGeometry(QRect(260, 20, 41, 29))
        self.name_title.setFont(font)
        self.name_title.setStyleSheet(u"")
        self.name_category_3 = QLabel(self.add_frame)
        self.name_category_3.setObjectName(u"name_category_3")
        self.name_category_3.setGeometry(QRect(30, 20, 61, 29))
        self.name_category_3.setFont(font)
        self.name_category_3.setStyleSheet(u"")
        self.edt_title = QLineEdit(self.add_frame)
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
        self.edt_agr = QTextEdit(self.text_frame)
        self.edt_agr.setObjectName(u"edt_agr")
        self.edt_agr.setGeometry(QRect(20, 60, 611, 291))
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
"    padding-top: 4px;\n"
"    padding-left: 5px;\n"
"    background: white;\n"
"    outline: none;\n"
"	border: none;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.btn_bold = QPushButton(self.frame_3)
        self.btn_bold.setObjectName(u"btn_bold")
        self.btn_bold.setGeometry(QRect(240, 0, 30, 30))
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
        self.btn_italic.setGeometry(QRect(270, 0, 30, 30))
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
        self.btn_under_line.setGeometry(QRect(300, 0, 30, 30))
        self.btn_under_line.setStyleSheet(u"#btn_under_line {\n"
"    image: url(../../data/img/button/under_icon.png);\n"
"}\n"
"\n"
"#btn_under_line:hover {\n"
"    image: url(../../data/img/button/under_hover_icon.png);\n"
"}")
        self.btn_color = QPushButton(self.frame_3)
        self.btn_color.setObjectName(u"btn_color")
        self.btn_color.setGeometry(QRect(330, 0, 30, 30))
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
        self.btn_spelling = QPushButton(self.frame_3)
        self.btn_spelling.setObjectName(u"btn_spelling")
        self.btn_spelling.setGeometry(QRect(530, 0, 81, 30))
        self.btn_spelling.setStyleSheet(u"#btn_spelling {\n"
"    font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"    color: rgb(88,88,255);\n"
"}\n"
"\n"
"#btn_spelling:hover {\n"
"    font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"    color: rgb(128,128,255);\n"
"}\n"
"\n"
"#btn_spelling:pressed {\n"
"    font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"    color: rgb(88,88,255);\n"
"	padding-left: 6px;\n"
"	padding-top: 5px;\n"
"}")
        self.category_back = QFrame(AgrEditor)
        self.category_back.setObjectName(u"category_back")
        self.category_back.setGeometry(QRect(750, 20, 341, 401))
        self.category_back.setFrameShape(QFrame.StyledPanel)
        self.category_back.setFrameShadow(QFrame.Raised)
        self.category_edit_frame = QFrame(self.category_back)
        self.category_edit_frame.setObjectName(u"category_edit_frame")
        self.category_edit_frame.setGeometry(QRect(20, 20, 301, 361))
        self.category_edit_frame.setStyleSheet(u"#category_edit_frame{\n"
"	border: 1px solid rgb(200,200,200);\n"
"	background: white;\n"
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
"#lst_edit_category {\n"
"	color: rgb(65,65,65);\n"
"    font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	border: 1px solid rgb(130,130,130);\n"
"}")
        self.category_edit_frame.setFrameShape(QFrame.StyledPanel)
        self.category_edit_frame.setFrameShadow(QFrame.Raised)
        self.lst_edit_category = QListWidget(self.category_edit_frame)
        self.lst_edit_category.setObjectName(u"lst_edit_category")
        self.lst_edit_category.setGeometry(QRect(30, 68, 241, 161))
        self.edt_category = QLineEdit(self.category_edit_frame)
        self.edt_category.setObjectName(u"edt_category")
        self.edt_category.setEnabled(True)
        self.edt_category.setGeometry(QRect(30, 240, 206, 30))
        self.edt_category.setStyleSheet(u"QLabel {\n"
"	font: 13px;\n"
"}")
        self.edt_category.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_2 = QLabel(self.category_edit_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(34, 242, 61, 25))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet(u"QLabel {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(125,125,125);\n"
"	padding-top: 3px;\n"
"	background-color: white; \n"
"}")
        self.btn_category_cancel = QPushButton(self.category_edit_frame)
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
"QPushButton:hover {\n"
"	color: rgb(118,118,255);\n"
"    border: 1px solid rgb(158,158,255);\n"
"}")
        self.btn_category_save = QPushButton(self.category_edit_frame)
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
        self.lb_category_edt = QLabel(self.category_edit_frame)
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
        self.btn_category_add = QPushButton(self.category_edit_frame)
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
        self.name_category.setText(QCoreApplication.translate("AgrEditor", u"\uce74\ud14c\uace0\ub9ac", None))
        self.btn_add_category.setText("")
        self.name_category_2.setText(QCoreApplication.translate("AgrEditor", u"\ud2b9\uc57d\uc0ac\ud56d", None))
        self.name_title.setText(QCoreApplication.translate("AgrEditor", u"\uc81c \ubaa9", None))
        self.name_category_3.setText(QCoreApplication.translate("AgrEditor", u"\uce74\ud14c\uace0\ub9ac", None))
        self.edt_title.setText("")
        self.btn_bold.setText("")
        self.btn_italic.setText("")
        self.btn_under_line.setText("")
        self.btn_color.setText("")
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

        self.btn_spelling.setText(QCoreApplication.translate("AgrEditor", u"\ub9de\ucda4\ubc95 \uac80\uc0ac", None))
        self.edt_category.setText("")
        self.label_2.setText(QCoreApplication.translate("AgrEditor", u"\uce74\ud14c\uace0\ub9ac\uba85", None))
        self.btn_category_cancel.setText(QCoreApplication.translate("AgrEditor", u"\ub2eb \uae30", None))
        self.btn_category_save.setText(QCoreApplication.translate("AgrEditor", u"\uc800 \uc7a5", None))
        self.lb_category_edt.setText(QCoreApplication.translate("AgrEditor", u"\uce74\ud14c\uace0\ub9ac \ud3b8\uc9d1", None))
        self.btn_category_add.setText("")
    # retranslateUi

