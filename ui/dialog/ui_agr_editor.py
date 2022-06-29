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
    QListWidgetItem, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_AgrEditor(object):
    def setupUi(self, AgrEditor):
        if not AgrEditor.objectName():
            AgrEditor.setObjectName(u"AgrEditor")
        AgrEditor.resize(711, 831)
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
        self.btn_save.setGeometry(QRect(480, 750, 191, 41))
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
        self.btn_close.setGeometry(QRect(360, 750, 111, 41))
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
        self.text_frame = QFrame(AgrEditor)
        self.text_frame.setObjectName(u"text_frame")
        self.text_frame.setGeometry(QRect(30, 330, 651, 381))
        self.text_frame.setStyleSheet(u"#text_frame {\n"
"	background: white;\n"
"	border-radius: 15px;\n"
"}")
        self.text_frame.setFrameShape(QFrame.StyledPanel)
        self.text_frame.setFrameShadow(QFrame.Raised)
        self.edt_agr = QTextEdit(self.text_frame)
        self.edt_agr.setObjectName(u"edt_agr")
        self.edt_agr.setGeometry(QRect(20, 60, 611, 301))
        self.frame_3 = QFrame(self.text_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(20, 20, 611, 30))
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
                        "mage: url(../../static/img/system/down_arrow_icon.png);\n"
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
"    image: url(../../static/img/button/bold_icon.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"#btn_bold:hover {\n"
"    image: url(../../static/img/button/bold_hover_icon.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}")
        self.btn_italic = QPushButton(self.frame_3)
        self.btn_italic.setObjectName(u"btn_italic")
        self.btn_italic.setGeometry(QRect(270, 0, 30, 30))
        self.btn_italic.setStyleSheet(u"#btn_italic {\n"
"    image: url(../../static/img/button/italic_icon.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"#btn_italic:hover {\n"
"    image: url(../../static/img/button/italic_hover_icon.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}")
        self.btn_italic.setCheckable(True)
        self.btn_under_line = QPushButton(self.frame_3)
        self.btn_under_line.setObjectName(u"btn_under_line")
        self.btn_under_line.setGeometry(QRect(300, 0, 30, 30))
        self.btn_under_line.setStyleSheet(u"#btn_under_line {\n"
"    image: url(../../static/img/button/under_icon.png);\n"
"}\n"
"\n"
"#btn_under_line:hover {\n"
"    image: url(../../static/img/button/under_hover_icon.png);\n"
"}")
        self.btn_color = QPushButton(self.frame_3)
        self.btn_color.setObjectName(u"btn_color")
        self.btn_color.setGeometry(QRect(330, 0, 30, 30))
        self.btn_color.setStyleSheet(u"#btn_under_line {\n"
"    image: url(../../static/img/button/color_icon.png);\n"
"}\n"
"\n"
"#btn_under_line:hover {\n"
"    image: url(../../static/img/button/color_hover_icon.png);\n"
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
        self.editor_back = QFrame(AgrEditor)
        self.editor_back.setObjectName(u"editor_back")
        self.editor_back.setGeometry(QRect(750, 20, 341, 231))
        self.editor_back.setStyleSheet(u"#editor_back { background: rgba(0,0,0,150) }")
        self.editor_back.setFrameShape(QFrame.StyledPanel)
        self.editor_back.setFrameShadow(QFrame.Raised)
        self.editor_frame = QFrame(self.editor_back)
        self.editor_frame.setObjectName(u"editor_frame")
        self.editor_frame.setGeometry(QRect(20, 20, 301, 191))
        self.editor_frame.setStyleSheet(u"#editor_frame{\n"
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
        self.editor_frame.setFrameShape(QFrame.StyledPanel)
        self.editor_frame.setFrameShadow(QFrame.Raised)
        self.edt_name = QLineEdit(self.editor_frame)
        self.edt_name.setObjectName(u"edt_name")
        self.edt_name.setEnabled(True)
        self.edt_name.setGeometry(QRect(30, 68, 241, 30))
        self.edt_name.setStyleSheet(u"QLabel {\n"
"	font: 13px;\n"
"}")
        self.edt_name.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.hint = QLabel(self.editor_frame)
        self.hint.setObjectName(u"hint")
        self.hint.setGeometry(QRect(34, 70, 61, 25))
        self.hint.setAutoFillBackground(False)
        self.hint.setStyleSheet(u"QLabel {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(125,125,125);\n"
"	padding-top: 3px;\n"
"	background-color: white; \n"
"}")
        self.btn_editor_cancel = QPushButton(self.editor_frame)
        self.btn_editor_cancel.setObjectName(u"btn_editor_cancel")
        self.btn_editor_cancel.setGeometry(QRect(70, 130, 71, 31))
        self.btn_editor_cancel.setStyleSheet(u"QPushButton {\n"
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
        self.btn_editor_save = QPushButton(self.editor_frame)
        self.btn_editor_save.setObjectName(u"btn_editor_save")
        self.btn_editor_save.setGeometry(QRect(150, 130, 81, 31))
        self.btn_editor_save.setStyleSheet(u"QPushButton {\n"
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
        self.editor_title = QLabel(self.editor_frame)
        self.editor_title.setObjectName(u"editor_title")
        self.editor_title.setGeometry(QRect(0, 20, 300, 25))
        self.editor_title.setStyleSheet(u"#lb_category_edt {\n"
"	font: 15px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgba(0, 0, 0, 120);\n"
"	padding-top: 8px;\n"
"	padding-left: 8px;\n"
"	border: 0px;\n"
"}")
        self.editor_title.setAlignment(Qt.AlignCenter)
        self.title_frame = QFrame(AgrEditor)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setGeometry(QRect(300, 90, 381, 221))
        self.title_frame.setStyleSheet(u"#title_frame {\n"
"	background: white;\n"
"	border-radius: 15px;\n"
"}")
        self.title_frame.setFrameShape(QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.name_category_2 = QLabel(self.title_frame)
        self.name_category_2.setObjectName(u"name_category_2")
        self.name_category_2.setGeometry(QRect(20, 20, 61, 30))
        font = QFont()
        font.setFamilies([u"\uc6f0\ucef4\uccb4 Regular"])
        font.setBold(False)
        font.setItalic(False)
        self.name_category_2.setFont(font)
        self.name_category_2.setStyleSheet(u"")
        self.name_category_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lst_title = QListWidget(self.title_frame)
        self.lst_title.setObjectName(u"lst_title")
        self.lst_title.setGeometry(QRect(20, 60, 341, 141))
        self.btn_add_title = QPushButton(self.title_frame)
        self.btn_add_title.setObjectName(u"btn_add_title")
        self.btn_add_title.setGeometry(QRect(300, 20, 30, 30))
        self.btn_add_title.setStyleSheet(u"QPushButton {\n"
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
        self.btn_del_title = QPushButton(self.title_frame)
        self.btn_del_title.setObjectName(u"btn_del_title")
        self.btn_del_title.setGeometry(QRect(330, 20, 30, 30))
        self.btn_del_title.setStyleSheet(u"QPushButton {\n"
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
        self.category_frame = QFrame(AgrEditor)
        self.category_frame.setObjectName(u"category_frame")
        self.category_frame.setGeometry(QRect(30, 90, 251, 221))
        self.category_frame.setStyleSheet(u"#category_frame {\n"
"	background: white;\n"
"	border-radius: 15px;\n"
"}")
        self.category_frame.setFrameShape(QFrame.StyledPanel)
        self.category_frame.setFrameShadow(QFrame.Raised)
        self.lst_category = QListWidget(self.category_frame)
        self.lst_category.setObjectName(u"lst_category")
        self.lst_category.setGeometry(QRect(20, 60, 211, 141))
        self.name_category = QLabel(self.category_frame)
        self.name_category.setObjectName(u"name_category")
        self.name_category.setGeometry(QRect(20, 20, 71, 30))
        self.name_category.setFont(font)
        self.name_category.setStyleSheet(u"")
        self.name_category.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.btn_add_category = QPushButton(self.category_frame)
        self.btn_add_category.setObjectName(u"btn_add_category")
        self.btn_add_category.setGeometry(QRect(170, 20, 30, 30))
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
        self.btn_del_category = QPushButton(self.category_frame)
        self.btn_del_category.setObjectName(u"btn_del_category")
        self.btn_del_category.setGeometry(QRect(200, 20, 30, 30))
        self.btn_del_category.setStyleSheet(u"QPushButton {\n"
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
        self.btn_del_category.raise_()
        self.top_bar.raise_()
        self.btn_save.raise_()
        self.btn_close.raise_()
        self.text_frame.raise_()
        self.title_frame.raise_()
        self.category_frame.raise_()
        self.editor_back.raise_()

        self.retranslateUi(AgrEditor)

        QMetaObject.connectSlotsByName(AgrEditor)
    # setupUi

    def retranslateUi(self, AgrEditor):
        AgrEditor.setWindowTitle(QCoreApplication.translate("AgrEditor", u"Dialog", None))
        self.lb_title.setText(QCoreApplication.translate("AgrEditor", u"CONTRACT", None))
        self.lb_sub_title.setText(QCoreApplication.translate("AgrEditor", u"(  \ud2b9\uc57d\uc0ac\ud56d \ucd94\uac00/\ud3b8\uc9d1  )", None))
        self.btn_save.setText(QCoreApplication.translate("AgrEditor", u"\uc800 \uc7a5", None))
        self.btn_close.setText(QCoreApplication.translate("AgrEditor", u"\ub2eb \uae30", None))
        self.edt_agr.setHtml(QCoreApplication.translate("AgrEditor", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Gulim'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
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
        self.edt_name.setText("")
        self.hint.setText(QCoreApplication.translate("AgrEditor", u"\uce74\ud14c\uace0\ub9ac\uba85", None))
        self.btn_editor_cancel.setText(QCoreApplication.translate("AgrEditor", u"\ub2eb \uae30", None))
        self.btn_editor_save.setText(QCoreApplication.translate("AgrEditor", u"\uc800 \uc7a5", None))
        self.editor_title.setText(QCoreApplication.translate("AgrEditor", u"\uce74\ud14c\uace0\ub9ac \ud3b8\uc9d1", None))
        self.name_category_2.setText(QCoreApplication.translate("AgrEditor", u"\ud2b9\uc57d\uc0ac\ud56d", None))
        self.btn_add_title.setText("")
        self.btn_del_title.setText("")
        self.name_category.setText(QCoreApplication.translate("AgrEditor", u"\uce74\ud14c\uace0\ub9ac", None))
        self.btn_add_category.setText("")
        self.btn_del_category.setText("")
    # retranslateUi

