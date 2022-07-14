# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_register.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QRadioButton, QSizePolicy, QWidget)

class UiRegister(object):
    def setupUi(self, Register):
        if not Register.objectName():
            Register.setObjectName(u"Register")
        Register.resize(521, 381)
        Register.setMinimumSize(QSize(521, 381))
        Register.setMaximumSize(QSize(521, 381))
        Register.setStyleSheet(u"QDialog {\n"
"	background-color: rgb(253,253,253);\n"
"}")
        self.address_frame = QFrame(Register)
        self.address_frame.setObjectName(u"address_frame")
        self.address_frame.setGeometry(QRect(20, 20, 481, 151))
        self.address_frame.setStyleSheet(u"#address_frame {\n"
"	background-color: white;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(120,120,120);\n"
"}")
        self.address_frame.setFrameShape(QFrame.StyledPanel)
        self.address_frame.setFrameShadow(QFrame.Raised)
        self.cbx_buildings = QComboBox(self.address_frame)
        self.cbx_buildings.addItem("")
        self.cbx_buildings.setObjectName(u"cbx_buildings")
        self.cbx_buildings.setGeometry(QRect(20, 95, 216, 40))
        self.cbx_buildings.setStyleSheet(u"        QComboBox {\n"
"            border: 2px solid rgb(235,235,235);\n"
"            padding-top: 4px;\n"
"            padding-left: 10px;\n"
"            min-width: 6em;\n"
"            background: rgb(255, 255, 255);\n"
"            font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"            color: rgb(65, 65, 65);\n"
"            border-radius: 5px;\n"
"        }\n"
"        \n"
"        QComboBox QAbstractItemView { \n"
"            border: 1px solid lightgray;\n"
"            outline: none;\n"
"            padding: 5px;\n"
"        }      \n"
"\n"
"        QComboBox QAbstractItemView::item { \n"
"            color: rgb(65, 65, 65);\n"
"            border-radius: 5px;\n"
"            padding-left: 10px;\n"
"            padding-top: 3px;\n"
"            min-height: 30px; \n"
"        }    \n"
"        \n"
"        QComboBox QAbstractItemView::item:hover { \n"
"            selection-color: white;\n"
"            background-color: rgb(128,128,255);\n"
"        }\n"
"\n"
"        QComboBox::drop-down {\n"
" "
                        "           width: 30px;\n"
"\n"
"            border-top-right-radius: 3px;\n"
"            border-bottom-right-radius: 3px;\n"
"        }\n"
"\n"
"        QComboBox::down-arrow {\n"
"            image: url(../../static/img/system/down_arrow_icon.png);\n"
"            width: 8px;\n"
"            height: 8px;\n"
"        }\n"
"\n"
"        QScrollBar:vertical {\n"
"            width: 5px;\n"
"            border: none;\n"
"        }\n"
"        \n"
"        QScrollBar::handle {\n"
"            background: rgb(235,235,235);\n"
"            border: none;\n"
"        }\n"
"        \n"
"        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"            border: none;\n"
"            background: none;\n"
"        }")
        self.edt_address = QLineEdit(self.address_frame)
        self.edt_address.setObjectName(u"edt_address")
        self.edt_address.setGeometry(QRect(20, 40, 441, 45))
        self.edt_address.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(125,125,125);\n"
"	font: 16px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"    border: 2px solid rgb(128,128,255);\n"
"    border-radius: 5px;\n"
"    padding-top: 3px;\n"
"    padding-left: 10px;\n"
"    padding-right: 40px;\n"
"}\n"
"    \n"
"QLineEdit:focus {\n"
"	color: rgb(65,65,65);\n"
"}")
        self.lb_sub_title_1 = QLabel(self.address_frame)
        self.lb_sub_title_1.setObjectName(u"lb_sub_title_1")
        self.lb_sub_title_1.setGeometry(QRect(20, 20, 91, 16))
        self.lb_sub_title_1.setStyleSheet(u"")
        self.cbx_rooms = QComboBox(self.address_frame)
        self.cbx_rooms.addItem("")
        self.cbx_rooms.setObjectName(u"cbx_rooms")
        self.cbx_rooms.setGeometry(QRect(245, 95, 216, 40))
        self.cbx_rooms.setStyleSheet(u"        QComboBox {\n"
"            border: 2px solid rgb(235,235,235);\n"
"            padding-top: 4px;\n"
"            padding-left: 10px;\n"
"            min-width: 6em;\n"
"            background: rgb(255, 255, 255);\n"
"            font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"            color: rgb(65, 65, 65);\n"
"            border-radius: 5px;\n"
"        }\n"
"        \n"
"        QComboBox QAbstractItemView { \n"
"            border: 1px solid lightgray;\n"
"            outline: none;\n"
"            padding: 5px;\n"
"        }      \n"
"\n"
"        QComboBox QAbstractItemView::item { \n"
"            color: rgb(65, 65, 65);\n"
"            border-radius: 5px;\n"
"            padding-left: 10px;\n"
"            padding-top: 3px;\n"
"            min-height: 30px; \n"
"        }    \n"
"        \n"
"        QComboBox QAbstractItemView::item:hover { \n"
"            selection-color: white;\n"
"            background-color: rgb(128,128,255);\n"
"        }\n"
"\n"
"        QComboBox::drop-down {\n"
" "
                        "           width: 30px;\n"
"\n"
"            border-top-right-radius: 3px;\n"
"            border-bottom-right-radius: 3px;\n"
"        }\n"
"\n"
"        QComboBox::down-arrow {\n"
"            image: url(../../static/img/system/down_arrow_icon.png);\n"
"            width: 8px;\n"
"            height: 8px;\n"
"        }\n"
"\n"
"        QScrollBar:vertical {\n"
"            width: 5px;\n"
"            border: none;\n"
"        }\n"
"        \n"
"        QScrollBar::handle {\n"
"            background: rgb(235,235,235);\n"
"            border: none;\n"
"        }\n"
"        \n"
"        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"            border: none;\n"
"            background: none;\n"
"        }")
        self.btn_search = QPushButton(self.address_frame)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setGeometry(QRect(418, 42, 41, 41))
        self.btn_search.setStyleSheet(u"#btn_search {\n"
"	background: white;\n"
"	border-radius: 5px;\n"
"}")
        self.type_frame = QFrame(Register)
        self.type_frame.setObjectName(u"type_frame")
        self.type_frame.setGeometry(QRect(20, 190, 481, 81))
        self.type_frame.setStyleSheet(u"#type_frame {\n"
"	background-color: white;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QRadioButton {\n"
"	font: 15px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(85,85,85);\n"
"	outline: none;\n"
"	border: none;\n"
"}\n"
"\n"
"QRadioButton:checked {\n"
"	color: rgb(108,108,255);\n"
"}")
        self.type_frame.setFrameShape(QFrame.StyledPanel)
        self.type_frame.setFrameShadow(QFrame.Raised)
        self.rbtn_set = QRadioButton(self.type_frame)
        self.rbtn_set.setObjectName(u"rbtn_set")
        self.rbtn_set.setGeometry(QRect(240, 34, 90, 16))
        self.rbtn_building = QRadioButton(self.type_frame)
        self.rbtn_building.setObjectName(u"rbtn_building")
        self.rbtn_building.setGeometry(QRect(330, 34, 51, 16))
        self.rbtn_land = QRadioButton(self.type_frame)
        self.rbtn_land.setObjectName(u"rbtn_land")
        self.rbtn_land.setGeometry(QRect(400, 34, 61, 16))
        self.cbx_flag = QComboBox(self.type_frame)
        self.cbx_flag.addItem("")
        self.cbx_flag.addItem("")
        self.cbx_flag.addItem("")
        self.cbx_flag.setObjectName(u"cbx_flag")
        self.cbx_flag.setGeometry(QRect(120, 20, 91, 40))
        self.cbx_flag.setStyleSheet(u"QComboBox {\n"
"    border: 2px solid rgb(235,235,235);\n"
"    padding-top: 4px;\n"
"    padding-left: 10px;\n"
"    min-width: 4em;\n"
"    background: rgb(255, 255, 255);\n"
"    font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"    color: rgb(65, 65, 65);\n"
"    border-radius: 5px;\n"
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
"QComboBox QAbstractItemView::item:hover { \n"
"    selection-color: white;\n"
"    background-color: rgb(128,128,255);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    width: 30px;\n"
"\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(../../static/img/system/down_arrow_icon.png);\n"
"    width: 8px;\n"
"    he"
                        "ight: 8px;\n"
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
"}")
        self.label = QLabel(self.type_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(25, 35, 81, 16))
        self.label.setStyleSheet(u"QLabel {\n"
"	font: 15px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(85,85,85);\n"
"}")
        self.list_frame = QFrame(Register)
        self.list_frame.setObjectName(u"list_frame")
        self.list_frame.setGeometry(QRect(20, 290, 481, 241))
        self.list_frame.setStyleSheet(u"#list_frame {\n"
"	background-color: white;\n"
"	border-radius: 15px;\n"
"}")
        self.list_frame.setFrameShape(QFrame.StyledPanel)
        self.list_frame.setFrameShadow(QFrame.Raised)
        self.list_item = QListWidget(self.list_frame)
        self.list_item.setObjectName(u"list_item")
        self.list_item.setGeometry(QRect(20, 20, 441, 201))
        self.list_item.setStyleSheet(u"QScrollBar:vertical {\n"
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
"QListWidget {\n"
"	border: none;\n"
"	outline: none;\n"
"}")
        self.btn_issuance = QPushButton(Register)
        self.btn_issuance.setObjectName(u"btn_issuance")
        self.btn_issuance.setGeometry(QRect(140, 300, 241, 45))
        self.btn_issuance.setStyleSheet(u"QPushButton {\n"
"    font: 16px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"    color: white;\n"
"    border: none;\n"
"    padding-top: 3px;\n"
"    padding-left: 2px;\n"
"    background: rgb(128,128,255);\n"
"    border-radius: 22px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(148,148,255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 6px;\n"
"    background-color: rgb(108,108,235);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(166, 168, 171);\n"
"}")

        self.retranslateUi(Register)

        QMetaObject.connectSlotsByName(Register)
    # setupUi

    def retranslateUi(self, Register):
        Register.setWindowTitle(QCoreApplication.translate("Register", u"\ub4f1\uae30\ubd80\ub4f1\ubcf8 PDF \ubc1c\uae09", None))
        self.cbx_buildings.setItemText(0, QCoreApplication.translate("Register", u"( \uac74\ubb3c\uba85\uce6d / \ub3d9)", None))

        self.lb_sub_title_1.setText(QCoreApplication.translate("Register", u"\uc18c\uc7ac\uc9c0 \uac80\uc0c9", None))
        self.cbx_rooms.setItemText(0, QCoreApplication.translate("Register", u"( \uc0c1\uc138\uc8fc\uc18c / \ud638 )", None))

        self.btn_search.setText("")
        self.rbtn_set.setText(QCoreApplication.translate("Register", u"\uc9d1\ud569\uac74\ubb3c", None))
        self.rbtn_building.setText(QCoreApplication.translate("Register", u"\uac74 \ubb3c", None))
        self.rbtn_land.setText(QCoreApplication.translate("Register", u"\ud1a0 \uc9c0", None))
        self.cbx_flag.setItemText(0, QCoreApplication.translate("Register", u"\ud604\ud589", None))
        self.cbx_flag.setItemText(1, QCoreApplication.translate("Register", u"\ud604\ud589+\ud3d0\uc1c4", None))
        self.cbx_flag.setItemText(2, QCoreApplication.translate("Register", u"\ud3d0\uc1c4", None))

        self.label.setText(QCoreApplication.translate("Register", u"\ub4f1\uae30\uae30\ub85d\uc0c1\ud0dc", None))
        self.btn_issuance.setText(QCoreApplication.translate("Register", u"\ub4f1\uae30\ubd80\ub4f1\ubcf8 PDF \uc800\uc7a5", None))
    # retranslateUi

