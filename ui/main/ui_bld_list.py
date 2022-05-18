# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1001, 809)
        mainWindow.setStyleSheet(u"\n"
"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(67,67,67);\n"
"	padding-top: 4px;\n"
"}\n"
"\n"
"\n"
"QCheckBox {\n"
"	font: 14px  \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(123,123,123);\n"
"	outline: none;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"	color: rgb(88,88,255);\n"
"}\n"
"\n"
"QLineEdit {\n"
"	font: 13;\n"
"	color:  rgb(85,85,85);\n"
"	border: 1px solid rgb(130,130,130);\n"
"	border-radius: 2px;\n"
"	padding-left: 5px;\n"
"	padding-top: 2px;\n"
"	padding-right: 22px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	color:  rgb(65,65,65);\n"
"	border: 1px solid rgb(148,148,255);\n"
"	border-radius: 2px;\n"
"	padding-right: 21px;\n"
"}\n"
"\n"
"QLineEdit:disabled{\n"
"	background: rgb(250,250,250);\n"
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
"    border-r"
                        "adius: 5px;\n"
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
"    b"
                        "order: none;\n"
"    background: none;\n"
"}")
        self.MainForm = QWidget(mainWindow)
        self.MainForm.setObjectName(u"MainForm")
        self.btn_frame = QFrame(self.MainForm)
        self.btn_frame.setObjectName(u"btn_frame")
        self.btn_frame.setGeometry(QRect(20, 0, 961, 181))
        self.btn_frame.setStyleSheet(u"#btn_frame {\n"
"	background-color: white;\n"
"	border-bottom-left-radius: 15px;\n"
"	border-bottom-right-radius: 15px;\n"
"}\n"
"")
        self.btn_frame.setFrameShape(QFrame.StyledPanel)
        self.btn_frame.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.btn_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(510, 20, 421, 31))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.checkBox = QCheckBox(self.frame)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(133, 10, 51, 16))
        self.checkBox.setChecked(True)
        self.checkBox_2 = QCheckBox(self.frame)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(213, 10, 51, 16))
        self.checkBox_3 = QCheckBox(self.frame)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(293, 10, 51, 16))
        self.checkBox_4 = QCheckBox(self.frame)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(373, 10, 51, 16))
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 0, 81, 30))
        self.frame_2 = QFrame(self.btn_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(510, 65, 421, 31))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(170, 0, 91, 30))
        self.comboBox_2 = QComboBox(self.frame_2)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(330, 0, 91, 30))
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 0, 56, 30))
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(280, 0, 56, 30))
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 81, 30))
        self.frame_3 = QFrame(self.btn_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(30, 65, 421, 31))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.comboBox_3 = QComboBox(self.frame_3)
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(130, 0, 91, 30))
        self.comboBox_4 = QComboBox(self.frame_3)
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setGeometry(QRect(230, 0, 91, 30))
        self.comboBox_5 = QComboBox(self.frame_3)
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setGeometry(QRect(330, 0, 91, 30))
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 81, 30))
        self.frame_4 = QFrame(self.btn_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(30, 110, 421, 31))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 0, 81, 30))
        self.comboBox_6 = QComboBox(self.frame_4)
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setGeometry(QRect(130, 0, 291, 30))
        self.frame_5 = QFrame(self.btn_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(510, 110, 421, 31))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.edt_sub_1_4 = QLineEdit(self.frame_5)
        self.edt_sub_1_4.setObjectName(u"edt_sub_1_4")
        self.edt_sub_1_4.setGeometry(QRect(130, 0, 161, 30))
        self.edt_sub_1_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 0, 81, 30))
        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(310, 0, 101, 30))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
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
        self.frame_6 = QFrame(self.btn_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(30, 20, 421, 31))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 0, 81, 30))
        self.cbx_kind_1 = QComboBox(self.frame_6)
        self.cbx_kind_1.addItem("")
        self.cbx_kind_1.addItem("")
        self.cbx_kind_1.addItem("")
        self.cbx_kind_1.addItem("")
        self.cbx_kind_1.addItem("")
        self.cbx_kind_1.addItem("")
        self.cbx_kind_1.addItem("")
        self.cbx_kind_1.addItem("")
        self.cbx_kind_1.addItem("")
        self.cbx_kind_1.addItem("")
        self.cbx_kind_1.addItem("")
        self.cbx_kind_1.addItem("")
        self.cbx_kind_1.setObjectName(u"cbx_kind_1")
        self.cbx_kind_1.setGeometry(QRect(130, 0, 291, 30))
        self.btn_spread = QPushButton(self.btn_frame)
        self.btn_spread.setObjectName(u"btn_spread")
        self.btn_spread.setGeometry(QRect(440, 150, 75, 23))
        self.btn_spread.setStyleSheet(u"#btn_spread {\n"
"	background: white;\n"
"	border: none;\n"
"	outline: none;\n"
"}")
        self.content_frame = QFrame(self.MainForm)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setGeometry(QRect(20, 200, 961, 591))
        self.content_frame.setStyleSheet(u"#content_frame {\n"
"	background-color: white;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(67,67,67);\n"
"	padding-top: 4px;\n"
"}")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.lst_items = QListWidget(self.content_frame)
        self.lst_items.setObjectName(u"lst_items")
        self.lst_items.setGeometry(QRect(10, 50, 941, 521))
        self.frame_7 = QFrame(self.content_frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(10, 10, 941, 31))
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.comboBox_7 = QComboBox(self.frame_7)
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setGeometry(QRect(130, 0, 91, 30))
        self.comboBox_8 = QComboBox(self.frame_7)
        self.comboBox_8.addItem("")
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setGeometry(QRect(230, 0, 91, 30))
        self.comboBox_9 = QComboBox(self.frame_7)
        self.comboBox_9.addItem("")
        self.comboBox_9.setObjectName(u"comboBox_9")
        self.comboBox_9.setGeometry(QRect(330, 0, 91, 30))
        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 0, 41, 30))
        mainWindow.setCentralWidget(self.MainForm)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"MainWindow", None))
        self.checkBox.setText(QCoreApplication.translate("mainWindow", u"\uc804\uccb4", None))
        self.checkBox_2.setText(QCoreApplication.translate("mainWindow", u"\ub9e4\ub9e4", None))
        self.checkBox_3.setText(QCoreApplication.translate("mainWindow", u"\uc804\uc138", None))
        self.checkBox_4.setText(QCoreApplication.translate("mainWindow", u"\uc6d4\uc138", None))
        self.label_6.setText(QCoreApplication.translate("mainWindow", u"\uac70\ub798\uc885\ub958", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("mainWindow", u"1\uac1c", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("mainWindow", u"2\uac1c", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("mainWindow", u"3\uac1c", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("mainWindow", u"4\uac1c \uc774\uc0c1", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("mainWindow", u"1\uac1c", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("mainWindow", u"2\uac1c", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("mainWindow", u"3\uac1c", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("mainWindow", u"4\uac1c \uc774\uc0c1", None))

        self.label.setText(QCoreApplication.translate("mainWindow", u"\ubc29", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"\uc695\uc2e4", None))
        self.label_4.setText(QCoreApplication.translate("mainWindow", u"\ubc29/\uc695\uc2e4 \uc218", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("mainWindow", u"\uc11c\uc6b8\ud2b9\ubcc4\uc2dc", None))

        self.comboBox_4.setItemText(0, QCoreApplication.translate("mainWindow", u"\uc911\ub791\uad6c", None))

        self.comboBox_5.setItemText(0, QCoreApplication.translate("mainWindow", u"\uba74\ubaa9\ub3d9", None))

        self.label_3.setText(QCoreApplication.translate("mainWindow", u"\uc18c\uc7ac\uc9c0", None))
        self.label_7.setText(QCoreApplication.translate("mainWindow", u"\ub9e4\ubb3c \ub2f4\ub2f9\uc790", None))
        self.edt_sub_1_4.setText("")
        self.label_8.setText(QCoreApplication.translate("mainWindow", u"\ub9e4\ubb3c\ubc88\ud638", None))
        self.pushButton.setText(QCoreApplication.translate("mainWindow", u"\ub9e4\ubb3c\ubc88\ud638 \uc870\ud68c", None))
        self.label_9.setText(QCoreApplication.translate("mainWindow", u"\ub9e4\ubb3c\uad6c\ubd84", None))
        self.cbx_kind_1.setItemText(0, QCoreApplication.translate("mainWindow", u"\uc804\uccb4", None))
        self.cbx_kind_1.setItemText(1, QCoreApplication.translate("mainWindow", u"\uc544\ud30c\ud2b8", None))
        self.cbx_kind_1.setItemText(2, QCoreApplication.translate("mainWindow", u"\ubd84\uc591\uad8c", None))
        self.cbx_kind_1.setItemText(3, QCoreApplication.translate("mainWindow", u"\uc624\ud53c\uc2a4\ud154", None))
        self.cbx_kind_1.setItemText(4, QCoreApplication.translate("mainWindow", u"\uc7ac\uac1c\ubc1c", None))
        self.cbx_kind_1.setItemText(5, QCoreApplication.translate("mainWindow", u"\uc8fc\ud0dd", None))
        self.cbx_kind_1.setItemText(6, QCoreApplication.translate("mainWindow", u"\uc6d0\ub8f8", None))
        self.cbx_kind_1.setItemText(7, QCoreApplication.translate("mainWindow", u"\uc0c1\uac00\uc810\ud3ec", None))
        self.cbx_kind_1.setItemText(8, QCoreApplication.translate("mainWindow", u"\uc0ac\ubb34\uc2e4", None))
        self.cbx_kind_1.setItemText(9, QCoreApplication.translate("mainWindow", u"\uacf5\uc7a5/\ucc3d\uace0", None))
        self.cbx_kind_1.setItemText(10, QCoreApplication.translate("mainWindow", u"\ube4c\ub529 \uac74\ubb3c", None))
        self.cbx_kind_1.setItemText(11, QCoreApplication.translate("mainWindow", u"\ud1a0\uc9c0", None))

        self.btn_spread.setText(QCoreApplication.translate("mainWindow", u"\u25bc", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("mainWindow", u"\uc11c\uc6b8\ud2b9\ubcc4\uc2dc", None))

        self.comboBox_8.setItemText(0, QCoreApplication.translate("mainWindow", u"\uc911\ub791\uad6c", None))

        self.comboBox_9.setItemText(0, QCoreApplication.translate("mainWindow", u"\uba74\ubaa9\ub3d9", None))

        self.label_5.setText(QCoreApplication.translate("mainWindow", u"\uc815\ub82c", None))
    # retranslateUi

