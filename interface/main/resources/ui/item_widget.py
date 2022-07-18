from PySide6.QtCore import QRect, QSize, QCoreApplication
from PySide6.QtWidgets import QWidget, QLabel, QGridLayout, QHBoxLayout, QVBoxLayout, QSizePolicy, QLayout, QPushButton


class Item(QWidget):
    css_point = """
    QLabel {
        font: 18px "웰컴체 Regular";
        color: rgb(66, 66, 255);
    }
    """
    css_title = """
    QLabel {
        font: 16px "웰컴체 Regular";
        color: rgb(65,65,65);
    }
    """
    css_name = """
    QLabel {
        font: 14px "웰컴체 Regular";
        color: rgb(65,65,65);
    }
    """
    css_item = """
    QLabel {
        font: 14px "웰컴체 Regular";
        color: rgb(95,95,95);
    }
    """

    def __init__(self, data, parent=None):
        super(Item, self).__init__(parent)

        # 레이아웃 위젯
        self.layout_widget = QWidget(self)
        self.layout_widget.setGeometry(QRect(0, 0, 1200, 60))

        # 전체 레이아웃
        self.layout_tot = QHBoxLayout(self.layout_widget)
        self.layout_tot.setSpacing(15)
        self.layout_tot.setContentsMargins(5, 5, 5, 5)

        self.layout_main = QVBoxLayout()
        self.layout_type = QHBoxLayout()
        self.layout_type.setSpacing(20)

        self.item_type = QLabel(self.layout_widget)
        self.item_type.setStyleSheet(self.css_point)
        self.item_type.setText(data['type'])

        self.layout_type.addWidget(self.item_type)

        price = "%s %s" % (data['kind'], data['price'])
        self.item_price = QLabel(self.layout_widget)
        self.item_price.setStyleSheet(self.css_title)
        self.item_price.setText(price)

        self.layout_type.addWidget(self.item_price)
        self.layout_type.setStretch(1, 1)

        self.layout_main.addLayout(self.layout_type)

        self.item_address = QLabel(self.layout_widget)
        self.item_address.setStyleSheet(self.css_item)
        self.item_address.setText(data['address'])

        self.layout_main.addWidget(self.item_address)

        self.layout_tot.addLayout(self.layout_main)

        self.layout_sub = QGridLayout()
        self.layout_sub.setVerticalSpacing(2)
        self.layout_sub.setContentsMargins(-1, 5, -1, 5)

        # 방 레이아웃 추가
        self._room(data)
        self.layout_tot.addLayout(self.layout_sub)

        self.setLayout(self.layout_tot)

    def _room(self, data):

        # 방
        self.case_room = QWidget(self.layout_widget)

        self.name_tot = QLabel(self.case_room)
        self.name_tot.setGeometry(QRect(0, 0, 61, 25))
        self.name_tot.setStyleSheet(self.css_name)
        self.name_tot.setText("방")

        self.item_tot = QLabel(self.case_room)
        self.item_tot.setGeometry(QRect(80, 0, 71, 25))
        self.item_tot.setStyleSheet(self.css_item)
        self.item_tot.setText(data['room'])

        self.layout_sub.addWidget(self.case_room, 0, 0, 1, 1)

        # 욕실
        self.case_bath = QWidget(self.layout_widget)

        self.name_area = QLabel(self.case_bath)
        self.name_area.setGeometry(QRect(0, 0, 61, 25))
        self.name_area.setStyleSheet(self.css_name)
        self.name_area.setText("욕 실")

        self.item_area = QLabel(self.case_bath)
        self.item_area.setGeometry(QRect(80, 0, 71, 25))
        self.item_area.setStyleSheet(self.css_item)
        self.item_area.setText(data['bath'])

        self.layout_sub.addWidget(self.case_bath, 1, 0, 1, 1)

        # 공급면적
        self.case_tot = QWidget(self.layout_widget)

        self.name_tot = QLabel(self.case_tot)
        self.name_tot.setGeometry(QRect(0, 0, 61, 25))
        self.name_tot.setStyleSheet(self.css_name)
        self.name_tot.setText("공급면적")

        self.item_tot = QLabel(self.case_tot)
        self.item_tot.setGeometry(QRect(80, 0, 71, 25))
        self.item_tot.setStyleSheet(self.css_item)
        self.item_tot.setText(data['tot'])

        self.layout_sub.addWidget(self.case_tot, 0, 1, 1, 1)

        # 전용면적
        self.case_area = QWidget(self.layout_widget)

        self.name_area = QLabel(self.case_area)
        self.name_area.setGeometry(QRect(0, 0, 61, 25))
        self.name_area.setStyleSheet(self.css_name)
        self.name_area.setText("전용면적")

        self.item_area = QLabel(self.case_area)
        self.item_area.setGeometry(QRect(80, 0, 71, 25))
        self.item_area.setStyleSheet(self.css_item)
        self.item_area.setText(data['area'])

        self.layout_sub.addWidget(self.case_area, 1, 1, 1, 1)

        # 주차
        self.case_parking = QWidget(self.layout_widget)

        self.name_parking = QLabel(self.case_parking)
        self.name_parking.setGeometry(QRect(0, 0, 61, 25))
        self.name_parking.setStyleSheet(self.css_name)
        self.name_parking.setText("주 차")

        self.item_parking = QLabel(self.case_parking)
        self.item_parking.setGeometry(QRect(80, 0, 31, 25))
        self.item_parking.setStyleSheet(self.css_item)
        self.item_parking.setText(data['parking'])

        self.layout_sub.addWidget(self.case_parking, 0, 2, 1, 1)

        # 승강기
        self.case_ev = QWidget(self.layout_widget)

        self.name_ev = QLabel(self.case_ev)
        self.name_ev.setGeometry(QRect(0, 0, 61, 25))
        self.name_ev.setStyleSheet(self.css_name)
        self.name_ev.setText("승강기")

        self.item_ev = QLabel(self.case_ev)
        self.item_ev.setGeometry(QRect(80, 0, 31, 25))
        self.item_ev.setStyleSheet(self.css_item)
        self.item_ev.setText(data['ev'])

        self.layout_sub.addWidget(self.case_ev, 1, 2, 1, 1)

        # # 반려동물
        # self.case_pet = QWidget(self.layout_widget)
        # self.case_pet.setMinimumSize(QSize(150, 0))
        #
        # self.name_pet = QLabel(self.case_pet)
        # self.name_pet.setGeometry(QRect(0, 0, 61, 25))
        # self.name_pet.setStyleSheet(self.css_name)
        # self.name_pet.setText("반려동물")
        #
        # self.item_pet = QLabel(self.case_pet)
        # self.item_pet.setGeometry(QRect(80, 0, 31, 25))
        # self.item_pet.setStyleSheet(self.css_item)
        # self.item_pet.setText(data['pet'])
        #
        # self.layout_sub.addWidget(self.case_pet, 1, 0, 1, 1)

        # 연락처 1
        self.case_num_1 = QWidget(self.layout_widget)

        self.name_num_1 = QLabel(self.case_num_1)
        self.name_num_1.setGeometry(QRect(0, 0, 61, 25))
        self.name_num_1.setStyleSheet(self.css_name)
        self.name_num_1.setText("연락처")

        self.item_num_1 = QLabel(self.case_num_1)
        self.item_num_1.setGeometry(QRect(80, 0, 141, 25))
        self.item_num_1.setStyleSheet(self.css_item)
        self.item_num_1.setText(data['num_1'])

        self.layout_sub.addWidget(self.case_num_1, 0, 3, 1, 1)

        # 연락처 2
        self.case_num_2 = QWidget(self.layout_widget)

        self.name_num_2 = QLabel(self.case_num_2)
        self.name_num_2.setGeometry(QRect(0, 0, 61, 25))
        self.name_num_2.setStyleSheet(self.css_name)
        self.name_num_2.setText("연락처")

        self.item_num_2 = QLabel(self.case_num_2)
        self.item_num_2.setGeometry(QRect(80, 0, 141, 25))
        self.item_num_2.setStyleSheet(self.css_item)
        self.item_num_2.setText(data['num_2'])

        self.layout_sub.addWidget(self.case_num_2, 1, 3, 1, 1)

        # 연락처 2
        self.case_num_4 = QWidget(self.layout_widget)

        self.name_num_4 = QLabel(self.case_num_4)
        self.name_num_4.setGeometry(QRect(0, 0, 61, 25))
        self.name_num_4.setStyleSheet(self.css_name)
        self.name_num_4.setText("연락처")

        self.item_num_4 = QLabel(self.case_num_4)
        self.item_num_4.setGeometry(QRect(80, 0, 141, 25))
        self.item_num_4.setStyleSheet(self.css_item)
        self.item_num_4.setText(data['num_2'])

        self.layout_sub.addWidget(self.case_num_4, 0, 4, 1, 1)

        # 연락처 2
        self.case_num_3 = QWidget(self.layout_widget)

        self.name_num_3 = QLabel(self.case_num_3)
        self.name_num_3.setGeometry(QRect(0, 0, 61, 25))
        self.name_num_3.setStyleSheet(self.css_name)
        self.name_num_3.setText("연락처")

        self.item_num_3 = QPushButton(self.case_num_3)
        self.item_num_3.setGeometry(QRect(80, 0, 141, 25))
        self.item_num_3.setStyleSheet(self.css_item)
        self.item_num_3.setText(data['num_2'])
        self.item_num_3.clicked.connect(lambda: print(self.))

        self.layout_sub.addWidget(self.case_num_3, 1, 4, 1, 1)

        # 레이아웃 설정
        self.layout_sub.setColumnMinimumWidth(0, 150)
        self.layout_sub.setColumnMinimumWidth(1, 150)
        self.layout_sub.setColumnMinimumWidth(2, 150)
        self.layout_sub.setColumnMinimumWidth(3, 200)
        self.layout_sub.setColumnMinimumWidth(4, 200)
        self.layout_sub.setRowMinimumHeight(0, 25)
        self.layout_sub.setRowMinimumHeight(1, 25)
