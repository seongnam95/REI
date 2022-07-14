# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLayout,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1151, 299)
        Form.setStyleSheet(u"QWidget {\n"
"	background: white;\n"
"}")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 1061, 65))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.item_type = QLabel(self.widget)
        self.item_type.setObjectName(u"item_type")
        self.item_type.setGeometry(QRect(10, 10, 51, 21))
        self.item_type.setStyleSheet(u"QLabel {\n"
"	font: 18px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(66, 66, 255);\n"
"}")
        self.item_price = QLabel(self.widget)
        self.item_price.setObjectName(u"item_price")
        self.item_price.setGeometry(QRect(70, 10, 171, 21))
        self.item_price.setStyleSheet(u"QLabel {\n"
"	font: 16px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(65,65,65);\n"
"}")

        self.gridLayoutWidget = QWidget(self.widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(350, 0, 671, 61))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.case_count = QWidget(self.gridLayoutWidget)
        self.case_count.setObjectName(u"case_count")
        self.case_count.setMinimumSize(QSize(15, 0))
        self.item_count = QLabel(self.case_count)
        self.item_count.setObjectName(u"item_count")
        self.item_count.setGeometry(QRect(0, 0, 131, 30))
        self.item_count.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(65,65,65);\n"
"}")

        self.gridLayout.addWidget(self.case_count, 0, 0, 1, 1)

        self.case_tot = QWidget(self.gridLayoutWidget)
        self.case_tot.setObjectName(u"case_tot")
        self.case_tot.setMinimumSize(QSize(150, 0))
        self.item_tot = QLabel(self.case_tot)
        self.item_tot.setObjectName(u"item_tot")
        self.item_tot.setGeometry(QRect(80, 0, 71, 30))
        self.item_tot.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(95,95,95);\n"
"}")
        self.name_tot = QLabel(self.case_tot)
        self.name_tot.setObjectName(u"name_tot")
        self.name_tot.setGeometry(QRect(0, 0, 61, 30))
        self.name_tot.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(65,65,65);\n"
"}")

        self.gridLayout.addWidget(self.case_tot, 0, 1, 1, 1)

        self.case_parking = QWidget(self.gridLayoutWidget)
        self.case_parking.setObjectName(u"case_parking")
        self.case_parking.setMinimumSize(QSize(150, 0))
        self.item_parking = QLabel(self.case_parking)
        self.item_parking.setObjectName(u"item_parking")
        self.item_parking.setGeometry(QRect(80, 0, 31, 30))
        self.item_parking.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(95,95,95);\n"
"}")
        self.name_parking = QLabel(self.case_parking)
        self.name_parking.setObjectName(u"name_parking")
        self.name_parking.setGeometry(QRect(0, 0, 61, 30))
        self.name_parking.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(65,65,65);\n"
"}")
        self.widget_9 = QWidget(self.case_parking)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(200, 0, 151, 30))
        self.label_22 = QLabel(self.widget_9)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(80, 0, 71, 30))
        self.label_22.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(95,95,95);\n"
"}")
        self.label_23 = QLabel(self.widget_9)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(0, 0, 61, 30))
        self.label_23.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(65,65,65);\n"
"}")
        self.widget_10 = QWidget(self.case_parking)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setGeometry(QRect(200, 30, 151, 30))
        self.label_24 = QLabel(self.widget_10)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(80, 0, 71, 30))
        self.label_24.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(95,95,95);\n"
"}")
        self.label_25 = QLabel(self.widget_10)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(0, 0, 61, 30))
        self.label_25.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(65,65,65);\n"
"}")

        self.gridLayout.addWidget(self.case_parking, 1, 1, 1, 1)

        self.case_pet = QWidget(self.gridLayoutWidget)
        self.case_pet.setObjectName(u"case_pet")
        self.case_pet.setMinimumSize(QSize(150, 0))
        self.item_pet = QLabel(self.case_pet)
        self.item_pet.setObjectName(u"item_pet")
        self.item_pet.setGeometry(QRect(80, 0, 31, 30))
        self.item_pet.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(95,95,95);\n"
"}")
        self.name_pet = QLabel(self.case_pet)
        self.name_pet.setObjectName(u"name_pet")
        self.name_pet.setGeometry(QRect(0, 0, 61, 30))
        self.name_pet.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(65,65,65);\n"
"}")

        self.gridLayout.addWidget(self.case_pet, 1, 0, 1, 1)

        self.case_area = QWidget(self.gridLayoutWidget)
        self.case_area.setObjectName(u"case_area")
        self.case_area.setMinimumSize(QSize(150, 0))
        self.item_area = QLabel(self.case_area)
        self.item_area.setObjectName(u"item_area")
        self.item_area.setGeometry(QRect(80, 0, 71, 30))
        self.item_area.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(95,95,95);\n"
"}")
        self.name_area = QLabel(self.case_area)
        self.name_area.setObjectName(u"name_area")
        self.name_area.setGeometry(QRect(0, 0, 61, 30))
        self.name_area.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(65,65,65);\n"
"}")
        self.widget_6 = QWidget(self.case_area)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(200, 0, 151, 30))
        self.label_16 = QLabel(self.widget_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(80, 0, 71, 30))
        self.label_16.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(95,95,95);\n"
"}")
        self.label_17 = QLabel(self.widget_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(0, 0, 61, 30))
        self.label_17.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(65,65,65);\n"
"}")
        self.widget_7 = QWidget(self.case_area)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(200, 30, 151, 30))
        self.label_18 = QLabel(self.widget_7)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(80, 0, 71, 30))
        self.label_18.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(95,95,95);\n"
"}")
        self.label_19 = QLabel(self.widget_7)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(0, 0, 61, 30))
        self.label_19.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(65,65,65);\n"
"}")

        self.gridLayout.addWidget(self.case_area, 0, 2, 1, 1)

        self.case_num_1 = QWidget(self.gridLayoutWidget)
        self.case_num_1.setObjectName(u"case_num_1")
        self.case_num_1.setMinimumSize(QSize(200, 0))
        self.item_num_1 = QLabel(self.case_num_1)
        self.item_num_1.setObjectName(u"item_num_1")
        self.item_num_1.setGeometry(QRect(80, 0, 141, 30))
        self.item_num_1.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(95,95,95);\n"
"}")
        self.name_num_1 = QLabel(self.case_num_1)
        self.name_num_1.setObjectName(u"name_num_1")
        self.name_num_1.setGeometry(QRect(0, 0, 61, 30))
        self.name_num_1.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(65,65,65);\n"
"}")

        self.gridLayout.addWidget(self.case_num_1, 0, 3, 1, 1)

        self.case_ev = QWidget(self.gridLayoutWidget)
        self.case_ev.setObjectName(u"case_ev")
        self.case_ev.setMinimumSize(QSize(150, 0))
        self.item_ev = QLabel(self.case_ev)
        self.item_ev.setObjectName(u"item_ev")
        self.item_ev.setGeometry(QRect(80, 0, 31, 30))
        self.item_ev.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(95,95,95);\n"
"}")
        self.name_ev = QLabel(self.case_ev)
        self.name_ev.setObjectName(u"name_ev")
        self.name_ev.setGeometry(QRect(0, 0, 61, 30))
        self.name_ev.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(65,65,65);\n"
"}")

        self.gridLayout.addWidget(self.case_ev, 1, 2, 1, 1)

        self.case_num_2 = QWidget(self.gridLayoutWidget)
        self.case_num_2.setObjectName(u"case_num_2")
        self.case_num_2.setMinimumSize(QSize(200, 0))
        self.item_num_2 = QLabel(self.case_num_2)
        self.item_num_2.setObjectName(u"item_num_2")
        self.item_num_2.setGeometry(QRect(80, 0, 141, 30))
        self.item_num_2.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(95,95,95);\n"
"}")
        self.name_num_2 = QLabel(self.case_num_2)
        self.name_num_2.setObjectName(u"name_num_2")
        self.name_num_2.setGeometry(QRect(0, 0, 61, 30))
        self.name_num_2.setStyleSheet(u"QLabel {\n"
"	font: 14px \"\uc6f0\ucef4\uccb4 Regular\";\n"
"	color: rgb(65,65,65);\n"
"}")

        self.gridLayout.addWidget(self.case_num_2, 1, 3, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("../../../../../../../Users/jsn_/OneDrive/바탕 화면/form", u"Form", None))
        self.item_type.setText(QCoreApplication.translate("../../../../../../../Users/jsn_/OneDrive/바탕 화면/form", u"\ub2e4\uac00\uad6c", None))
        self.item_price.setText(QCoreApplication.translate("../../../../../../../Users/jsn_/OneDrive/바탕 화면/form", u"\uc804\uc138 1\uc5b5 7,000\ub9cc", None))
        self.item_address.setText(QCoreApplication.translate("../../../../../../../Users/jsn_/OneDrive/바탕 화면/form", u"\uc11c\uc6b8\ud2b9\ubcc4\uc2dc \uc911\ub791\uad6c \ubd09\uc6b0\uc7ac\ub85c154, 702\ud638 (\ub2e4\uc6d0\ube4c)", None))
        self.item_count.setText(QCoreApplication.translate("../../../../../../../Users/jsn_/OneDrive/바탕 화면/form", u"\ubc29 2\uac1c / \uc695\uc2e4 1\uac1c", None))
        self.item_tot.setText(QCoreApplication.translate("../../../../../../../Users/jsn_/OneDrive/바탕 화면/form", u"52.3 \u33a1", None))
        self.name_tot.setText(QCoreApplication.translate("../../../../../../../Users/jsn_/OneDrive/바탕 화면/form", u"\uacf5\uae09\uba74\uc801", None))
        self.item_parking.setText(QCoreApplication.translate("../../../../../../../Users/jsn_/OneDrive/바탕 화면/form", u"\uac00\ub2a5", None))
        self.name_parking.setText(QCoreApplication.translate("../../../../../../../Users/jsn_/OneDrive/바탕 화면/form", u"\uc8fc \ucc28", None))
        self.label_22.setText(QCoreApplication.translate("../../../../../../../Users/jsn_/OneDrive/바탕 화면/form", u"32.12 \u33a1", None))
        self.label_23.setText(QCoreApplication.translate("../../../../../../../Users/jsn_/OneDrive/바탕 화면/form", u"\uc804\uc6a9\uba74\uc801", None))
        self.label_24.setText(QCoreApplication.translate("../../../../../../../Users/jsn_/OneDrive/바탕 화면/form", u"\uac00\ub2a5", None))
        self.label_25.setText(QCoreApplication.translate("../../../../../../../Users/jsn_/OneDrive/바탕 화면/form", u"\uc560\uc644\ub3d9\ubb3c", None))
        self.item_pet.setText(QCoreApplication.translate("../../../../../../../Users/jsn_/OneDrive/바탕 화면/form", u"\uac00\ub2a5", None))
        self.name_pet.setText(QCoreApplication.translate("../../../../../../../Users/jsn_/OneDrive/바탕 화면/form", u"\uc560\uc644\ub3d9\ubb3c", None))
        self.item_area.setText(QCoreApplication.translate("../../../../../../../Users/jsn_/OneDrive/바탕 화면/form", u"32.12 \u33a1", None))
        self.name_area.setText(QCoreApplication.translate("../../../../../../../Users/jsn_/OneDrive/바탕 화면/form", u"\uc804\uc6a9\uba74\uc801", None))
        self.label_16.setText(QCoreApplication.translate("../../../../../../../Users/jsn_/OneDrive/바탕 화면/form", u"32.12 \u33a1", None))
        self.label_17.setText(QCoreApplication.translate("../../../../../../../Users/jsn_/OneDrive/바탕 화면/form", u"\uc804\uc6a9\uba74\uc801", None))
        self.label_18.setText(QCoreApplication.translate("../../../../../../../Users/jsn_/OneDrive/바탕 화면/form", u"\uac00\ub2a5", None))
        self.label_19.setText(QCoreApplication.translate("../../../../../../../Users/jsn_/OneDrive/바탕 화면/form", u"\uc560\uc644\ub3d9\ubb3c", None))
        self.item_num_1.setText(QCoreApplication.translate("../../../../../../../Users/jsn_/OneDrive/바탕 화면/form", u"010-9386-7937", None))
        self.name_num_1.setText(QCoreApplication.translate("../../../../../../../Users/jsn_/OneDrive/바탕 화면/form", u"\uc5f0\ub77d\ucc98", None))
        self.item_ev.setText(QCoreApplication.translate("../../../../../../../Users/jsn_/OneDrive/바탕 화면/form", u"\uc788\uc74c", None))
        self.name_ev.setText(QCoreApplication.translate("../../../../../../../Users/jsn_/OneDrive/바탕 화면/form", u"\uc2b9\uac15\uae30", None))
        self.item_num_2.setText(QCoreApplication.translate("../../../../../../../Users/jsn_/OneDrive/바탕 화면/form", u"010-2486-1307", None))
        self.name_num_2.setText(QCoreApplication.translate("../../../../../../../Users/jsn_/OneDrive/바탕 화면/form", u"\uc5f0\ub77d\ucc98", None))
    # retranslateUi

