# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLineEdit, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(411, 590)
        self.btn_search = QPushButton(Form)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setGeometry(QRect(300, 20, 101, 31))
        self.edt_address = QLineEdit(Form)
        self.edt_address.setObjectName(u"edt_address")
        self.edt_address.setGeometry(QRect(10, 20, 281, 31))
        self.edt_headers = QTextEdit(Form)
        self.edt_headers.setObjectName(u"edt_headers")
        self.edt_headers.setGeometry(QRect(10, 150, 391, 191))
        self.cbx_dong = QComboBox(Form)
        self.cbx_dong.setObjectName(u"cbx_dong")
        self.cbx_dong.setGeometry(QRect(10, 100, 191, 31))
        self.cbx_ho = QComboBox(Form)
        self.cbx_ho.setObjectName(u"cbx_ho")
        self.cbx_ho.setGeometry(QRect(210, 100, 191, 31))
        self.edt_content = QTextEdit(Form)
        self.edt_content.setObjectName(u"edt_content")
        self.edt_content.setGeometry(QRect(10, 350, 391, 191))
        self.btn_next = QPushButton(Form)
        self.btn_next.setObjectName(u"btn_next")
        self.btn_next.setGeometry(QRect(300, 550, 101, 31))
        self.cbx_address = QComboBox(Form)
        self.cbx_address.setObjectName(u"cbx_address")
        self.cbx_address.setGeometry(QRect(10, 60, 391, 31))
        self.btn_reset = QPushButton(Form)
        self.btn_reset.setObjectName(u"btn_reset")
        self.btn_reset.setGeometry(QRect(10, 550, 101, 31))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_search.setText(QCoreApplication.translate("Form", u"SEARCH", None))
        self.btn_next.setText(QCoreApplication.translate("Form", u"NEXT", None))
        self.btn_reset.setText(QCoreApplication.translate("Form", u"RESET", None))
    # retranslateUi

