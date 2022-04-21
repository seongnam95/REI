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
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(401, 342)
        Dialog.setStyleSheet(u"QDialog {\n"
"	background-color: rgb(253,253,253);\n"
"}")
        self.type_frame = QFrame(Dialog)
        self.type_frame.setObjectName(u"type_frame")
        self.type_frame.setGeometry(QRect(20, 190, 361, 61))
        self.type_frame.setStyleSheet(u"#type_frame {\n"
"	background-color: white;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QRadioButton {\n"
"	font: 15px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: #2c3e50;\n"
"}")
        self.type_frame.setFrameShape(QFrame.StyledPanel)
        self.type_frame.setFrameShadow(QFrame.Raised)
        self.rbtn_total = QRadioButton(self.type_frame)
        self.rbtn_total.setObjectName(u"rbtn_total")
        self.rbtn_total.setGeometry(QRect(20, 25, 90, 16))
        self.rbtn_building = QRadioButton(self.type_frame)
        self.rbtn_building.setObjectName(u"rbtn_building")
        self.rbtn_building.setGeometry(QRect(120, 25, 131, 16))
        self.rbtn_room = QRadioButton(self.type_frame)
        self.rbtn_room.setObjectName(u"rbtn_room")
        self.rbtn_room.setGeometry(QRect(270, 25, 90, 16))
        self.address_frame = QFrame(Dialog)
        self.address_frame.setObjectName(u"address_frame")
        self.address_frame.setGeometry(QRect(20, 20, 361, 151))
        self.address_frame.setStyleSheet(u"#address_frame {\n"
"	background-color: white;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel {\n"
"	font: 13px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(127, 140, 141);\n"
"}")
        self.address_frame.setFrameShape(QFrame.StyledPanel)
        self.address_frame.setFrameShadow(QFrame.Raised)
        self.cbx_rooms = QComboBox(self.address_frame)
        self.cbx_rooms.addItem("")
        self.cbx_rooms.setObjectName(u"cbx_rooms")
        self.cbx_rooms.setGeometry(QRect(20, 95, 321, 40))
        self.cbx_rooms.setStyleSheet("""
        QComboBox {
            border: 2px solid rgb(240,240,240);
            padding-top: 4px;
            padding-left: 10px;
            min-width: 6em;
            background: rgb(255, 255, 255);
            font: 14px "웰컴체 Regular";
            color: rgb(44, 62, 80);
            border-radius: 5px;
        }
        
        QComboBox:hover {
            border-color: rgb(128,128,255);
        }
        
        QFrame {
            border: 1px solid lightgray;
            border-radius: 5px;
        }
        
        QComboBox QAbstractItemView { 
            border: 0px;
            outline: none;
            padding: 5px;
        }      
        
        QComboBox QAbstractItemView::item { 
            padding-left: 10px;
            min-height: 35px; 
        }    
        
        QComboBox QAbstractItemView::selection { 
            background: rgb(128,128,255);
        }
        
        QComboBox QAbstractItemView::item:hover { 
            border-radius: 5px;
            background: rgb(128,128,255);
        }
        
        QComboBox::drop-down {
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 30px;
        
            border-top-right-radius: 3px;
            border-bottom-right-radius: 3px;
        }
        
        QComboBox::down-arrow {
            image: url(../../data/img/system/down_arrow_icon.png);
            width: 22px;
            height: 22px;
        }
        
        QComboBox::setView {
            color: rgb(44, 62, 80);
            background-color: red
        }
        
        QScrollBar:vertical {
            width: 5px;
            border-radius: 2px;
            background: rgb(220,220,220);
        }
        
        QScrollBar::handle:vertical  {
            border-radius: 2px;
            background: rgba(84,102,120, 120);
            min-height: 0px;
        }
        
        QScrollBar::handle:vertical:hover  {
            border-radius: 2px;
            background: rgba(134,152,170, 120);
            min-height: 0px;
        }
        """)
        self.edt_address = QLineEdit(self.address_frame)
        self.edt_address.setObjectName(u"edt_address")
        self.edt_address.setGeometry(QRect(20, 40, 321, 45))
        self.edt_address.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(72,93,114);\n"
"    font: 16px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	border: 2px solid #3498db;\n"
"	padding-top: 3px;\n"
"	padding-left: 10px;\n"
"	padding-right: 70px;\n"
"}")
        self.lb_sub_title_1 = QLabel(self.address_frame)
        self.lb_sub_title_1.setObjectName(u"lb_sub_title_1")
        self.lb_sub_title_1.setGeometry(QRect(20, 20, 91, 16))
        self.lb_sub_title_1.setStyleSheet(u"")
        self.btn_issuance = QPushButton(Dialog)
        self.btn_issuance.setObjectName(u"btn_issuance")
        self.btn_issuance.setGeometry(QRect(80, 280, 241, 35))
        self.btn_issuance.setStyleSheet(u"QPushButton {\n"
"	font: 16px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: white;\n"
"	border: none;\n"
"	padding-top: 3px;\n"
"	padding-left: 2px;\n"
"    background: rgb(128,128,255);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(20, 83, 145);\n"
"	border-style: inset;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: rgb(166, 168, 171);\n"
"}")
        icon = QIcon()
        icon.addFile(u"E:/PyProject/Project/REI/building_info/image/bt_search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_issuance.setIcon(icon)
        self.btn_issuance.setIconSize(QSize(23, 23))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.rbtn_total.setText(QCoreApplication.translate("Dialog", u"\ucd1d\uad04\ud45c\uc81c\ubd80", None))
        self.rbtn_building.setText(QCoreApplication.translate("Dialog", u"\ud45c\uc81c\ubd80 (\uc77c\ubc18\uac74\ucd95\ubb3c)", None))
        self.rbtn_room.setText(QCoreApplication.translate("Dialog", u"\uc804\uc720\ubd80", None))
        self.cbx_rooms.setItemText(0, QCoreApplication.translate("Dialog", u"( \uc0c1\uc138\uc8fc\uc18c / \ud638 \uc120\ud0dd )", None))

        self.lb_sub_title_1.setText(QCoreApplication.translate("Dialog", u"\uc18c\uc7ac\uc9c0 \uac80\uc0c9", None))
        self.btn_issuance.setText(QCoreApplication.translate("Dialog", u"\uc18c\uc7ac\uc9c0 \uc785\ub825", None))
    # retranslateUi

