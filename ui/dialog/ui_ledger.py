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

class Ui_Ledger(object):
    def setupUi(self, Dialog):
        Dialog.resize(401, 362)
        Dialog.setStyleSheet("QDialog { background-color: rgb(255,255,255) }")

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
                                            "	color: rgb(120,120,120);\n"
                                            "}")

        self.lb_sub_title_1 = QLabel(self.address_frame)
        self.lb_sub_title_1.setObjectName(u"lb_sub_title_1")
        self.lb_sub_title_1.setGeometry(QRect(25, 20, 91, 16))

        self.edt_address = QLineEdit(self.address_frame)
        self.edt_address.setObjectName(u"edt_address")
        self.edt_address.setFocus()
        self.edt_address.setGeometry(QRect(20, 40, 321, 45))
        self.edt_address.setStyleSheet("""
        QLineEdit {
            color: rgb(125,125,125);
            font: 16px "웰컴체 Regular";
            border: 2px solid rgb(128,128,255);
            border-radius: 5px;
            padding-top: 3px;
            padding-left: 10px;
            padding-right: 40px;
        }
        
        QLineEdit:focus {
            color: rgb(65,65,65);
        }
        """)

        self.btn_search = QPushButton(self.address_frame)
        self.btn_search.setGeometry(QRect(298, 43, 39, 39))
        self.btn_search.setStyleSheet("""
        QPushButton {
            background-color: white;
            border: none;
            outline: none;}
        """)

        self.cbx_buildings = QComboBox(self.address_frame)
        self.cbx_buildings.addItem("( 건물명칭 / 동 )")
        self.cbx_buildings.setObjectName(u"cbx_rooms")
        self.cbx_buildings.setGeometry(QRect(20, 95, 161, 40))
        self.cbx_buildings.setStyleSheet("""
        QComboBox {
            border: 2px solid rgb(235,235,235);
            padding-top: 4px;
            padding-left: 10px;
            min-width: 6em;
            background: rgb(255, 255, 255);
            font: 14px "웰컴체 Regular";
            color: rgb(65, 65, 65);
            border-radius: 5px;
        }

        QComboBox QAbstractItemView { 
            border: 1px solid lightgray;
            outline: none;
            padding: 5px;
        }      

        QComboBox QAbstractItemView::item { 
            color: rgb(65, 65, 65);
            border-radius: 5px;
            padding-left: 10px;
            padding-top: 3px;
            min-height: 30px; 
        }    

        QComboBox QAbstractItemView::item:hover { 
            selection-color: white;
            background-color: rgb(128,128,255);
        }

        QComboBox::drop-down {
            width: 30px;

            border-top-right-radius: 3px;
            border-bottom-right-radius: 3px;
        }

        QComboBox::down-arrow {
            image: url(../../static/img/system/down_arrow_icon.png);
            width: 8px;
            height: 8px;
        }

        QScrollBar:vertical {
            width: 5px;
            border: none;
        }

        QScrollBar::handle {
            background: rgb(235,235,235);
            border: none;
        }

        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            border: none;
            background: none;
        }
        """)

        self.cbx_rooms = QComboBox(self.address_frame)
        self.cbx_rooms.addItem("( 상세주소 / 호)")
        self.cbx_rooms.setObjectName(u"cbx_rooms")
        self.cbx_rooms.setGeometry(QRect(185, 95, 156, 40))
        self.cbx_rooms.setStyleSheet("""
        QComboBox {
            border: 2px solid rgb(235,235,235);
            padding-top: 4px;
            padding-left: 10px;
            min-width: 6em;
            background: rgb(255, 255, 255);
            font: 14px "웰컴체 Regular";
            color: rgb(65, 65, 65);
            border-radius: 5px;
        }
        
        QComboBox QAbstractItemView { 
            border: 1px solid lightgray;
            outline: none;
            padding: 5px;
        }      

        QComboBox QAbstractItemView::item { 
            color: rgb(65, 65, 65);
            border-radius: 5px;
            padding-left: 10px;
            padding-top: 3px;
            min-height: 30px; 
        }    
        
        QComboBox QAbstractItemView::item:hover { 
            selection-color: white;
            background-color: rgb(128,128,255);
        }

        QComboBox::drop-down {
            width: 30px;

            border-top-right-radius: 3px;
            border-bottom-right-radius: 3px;
        }

        QComboBox::down-arrow {
            image: url(../../static/img/system/down_arrow_icon.png);
            width: 8px;
            height: 8px;
        }

        QScrollBar:vertical {
            width: 5px;
            border: none;
        }
        
        QScrollBar::handle {
            background: rgb(235,235,235);
            border: none;
        }
        
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            border: none;
            background: none;
        }
        """)

        self.type_frame = QFrame(Dialog)
        self.type_frame.setObjectName(u"type_frame")
        self.type_frame.setGeometry(QRect(20, 190, 361, 61))
        self.type_frame.setStyleSheet("""
        #type_frame {
            background-color: white;
            border-radius: 15px;
        }
        
        QRadioButton {
            font: 15px "웰컴체 Regular";
            color: rgb(85,85,85);
            outline: none;
            border: none;
        }
        
        QRadioButton:checked {
            color: rgb(108,108,255);
        }
        """)

        self.rbtn_total = QRadioButton(self.type_frame)
        self.rbtn_total.setObjectName(u"rbtn_total")
        self.rbtn_total.setEnabled(False)
        self.rbtn_total.setGeometry(QRect(25, 25, 90, 16))

        self.rbtn_building = QRadioButton(self.type_frame)
        self.rbtn_building.setObjectName(u"rbtn_building")
        self.rbtn_building.setEnabled(False)
        self.rbtn_building.setGeometry(QRect(125, 25, 131, 16))

        self.rbtn_room = QRadioButton(self.type_frame)
        self.rbtn_room.setObjectName(u"rbtn_room")
        self.rbtn_room.setEnabled(False)
        self.rbtn_room.setGeometry(QRect(275, 25, 90, 16))

        self.btn_issuance = QPushButton(Dialog)
        self.btn_issuance.setObjectName(u"btn_issuance")
        self.btn_issuance.setEnabled(False)
        self.btn_issuance.setGeometry(QRect(80, 280, 241, 45))
        self.btn_issuance.setStyleSheet("""
        QPushButton {
            font: 16px "웰컴체 Regular";
            color: white;
            border: none;
            padding-top: 3px;
            padding-left: 2px;
            background: rgb(128,128,255);
            border-radius: 22px;
            outline: none;
        }
        
        QPushButton:hover {
            background-color: rgb(148,148,255);
        }
        
        QPushButton:pressed {
            padding-left: 5px;
            padding-top: 6px;
            background-color: rgb(108,108,235);
        }
        
        QPushButton:disabled {
            background-color: rgb(166, 168, 171);
        }
        """)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"REI - 건축물대장 열람/발급", None))
        self.rbtn_total.setText(QCoreApplication.translate("Dialog", u"\ucd1d\uad04\ud45c\uc81c\ubd80", None))
        self.rbtn_building.setText(QCoreApplication.translate("Dialog", u"\ud45c\uc81c\ubd80 (\uc77c\ubc18\uac74\ucd95\ubb3c)", None))
        self.rbtn_room.setText(QCoreApplication.translate("Dialog", u"\uc804\uc720\ubd80", None))

        self.lb_sub_title_1.setText(QCoreApplication.translate("Dialog", u"\uc18c\uc7ac\uc9c0 \uac80\uc0c9", None))
        self.btn_issuance.setText(QCoreApplication.translate("Dialog", "건축물 대장 열람", None))
    # retranslateUi

