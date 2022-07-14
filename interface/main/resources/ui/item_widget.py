from PySide6.QtCore import QRect, QSize
from PySide6.QtWidgets import QWidget, QLabel, QGridLayout


class Item(QWidget):
    point_css = 'QLabel { font: 18px "웰컴체 Regular"; color: rgb(66, 66, 255); }'
    title_css = 'QLabel { font: 16px "웰컴체 Regular"; color: rgb(65, 65, 65); }'
    emphasis_css = 'QLabel { font: 14px "웰컴체 Regular"; color: rgb(65, 65, 65); }'
    normal_css = 'QLabel { font: 14px "웰컴체 Regular"; color: rgb(110, 110, 110); }'

    def __init__(self, data):
        super(Item, self).__init__()
        self.data = data

        # 매물 종류
        self.item_type = QLabel(self)
        self.item_type.setGeometry(QRect(10, 10, 50, 20))
        self.item_type.setStyleSheet(self.point_css)
        self.item_type.setText(data['type'])

        # 매물 분류/가격
        price = "%s %s" % (data['kind'], data['price'])
        self.item_price = QLabel(self)
        self.item_price.setGeometry(QRect(70, 10, 170, 20))
        self.item_price.setStyleSheet(self.title_css)
        self.item_price.setText(price)

        # 소재지
        self.item_address = QLabel(self)
        self.item_address.setGeometry(QRect(10, 40, 340, 20))
        self.item_address.setStyleSheet(self.normal_css)
        self.item_address.setText(data['address'])

        # 위젯
        self.housing_widget = QWidget(self)
        self.housing_widget.setGeometry(QRect(350, 0, 670, 60))
        print(self.size())

        self._add_housing()

    #
    def _add_housing(self):
        data = self.data

        # 방/욕실 수
        self.item_count = QLabel(self.housing_widget)
        self.item_count.setStyleSheet(self.point_css)
        self.item_count.setMinimumSize(QSize(150, 30))
        self.item_count.setStyleSheet(self.emphasis_css)
        self.item_count.setText(data['count'])

        # 공급면적
        self.case_tot = QWidget(self.housing_widget)
        self.case_tot.setMinimumSize(QSize(150, 30))

        self.name_tot = QLabel(self.case_tot)
        self.name_tot.setGeometry(QRect(0, 0, 60, 30))
        self.name_tot.setStyleSheet(self.emphasis_css)
        self.name_tot.setText("공급면적")

        self.item_tot = QLabel(self.case_tot)
        self.item_tot.setGeometry(QRect(80, 0, 70, 30))
        self.item_tot.setStyleSheet(self.normal_css)
        self.item_tot.setText(data['tot'])

        # 전용면적
        self.case_area = QWidget(self.housing_widget)
        self.case_area.setMinimumSize(QSize(150, 30))

        self.name_area = QLabel(self.case_area)
        self.name_area.setGeometry(QRect(0, 0, 60, 30))
        self.name_area.setStyleSheet(self.emphasis_css)
        self.name_area.setText("전용면적")

        self.item_area = QLabel(self.case_area)
        self.item_area.setGeometry(QRect(80, 0, 70, 30))
        self.item_area.setStyleSheet(self.normal_css)
        self.item_area.setText(data['area'])

        # 연락처 1
        self.case_num_1 = QWidget(self.housing_widget)
        self.case_num_1.setMinimumSize(QSize(200, 30))

        self.name_num_1 = QLabel(self.case_num_1)
        self.name_num_1.setGeometry(QRect(0, 0, 60, 30))
        self.name_num_1.setStyleSheet(self.emphasis_css)
        self.name_num_1.setText("연락처")

        self.item_num_1 = QLabel(self.case_num_1)
        self.item_num_1.setGeometry(QRect(80, 0, 140, 30))
        self.item_num_1.setStyleSheet(self.normal_css)
        self.item_num_1.setText(data['num_1'])

        # 연락처 2
        self.case_num_2 = QWidget(self.housing_widget)
        self.case_num_2.setMinimumSize(QSize(200, 30))

        self.name_num_2 = QLabel(self.case_num_2)
        self.name_num_2.setGeometry(QRect(0, 0, 60, 30))
        self.name_num_2.setStyleSheet(self.emphasis_css)
        self.name_num_2.setText("연락처")

        self.item_num_2 = QLabel(self.case_num_2)
        self.item_num_2.setGeometry(QRect(80, 0, 140, 30))
        self.item_num_2.setStyleSheet(self.normal_css)
        self.item_num_2.setText(data['num_2'])

        # 애완동물
        self.case_pet = QWidget(self.housing_widget)
        self.case_pet.setMinimumSize(QSize(150, 30))

        self.name_pet = QLabel(self.case_pet)
        self.name_pet.setGeometry(QRect(0, 0, 60, 30))
        self.name_pet.setStyleSheet(self.emphasis_css)
        self.name_pet.setText("애완동물")

        self.item_pet = QLabel(self.case_pet)
        self.item_pet.setGeometry(QRect(80, 0, 30, 30))
        self.item_pet.setStyleSheet(self.normal_css)
        self.item_pet.setText(data['pet'])

        # 주차
        self.case_parking = QWidget(self.housing_widget)
        self.case_parking.setMinimumSize(QSize(150, 30))

        self.name_parking = QLabel(self.case_parking)
        self.name_parking.setGeometry(QRect(0, 0, 60, 30))
        self.name_parking.setStyleSheet(self.emphasis_css)
        self.name_parking.setText("주 차")

        self.item_parking = QLabel(self.case_parking)
        self.item_parking.setGeometry(QRect(80, 0, 30, 30))
        self.item_parking.setStyleSheet(self.normal_css)
        self.item_parking.setText(data['parking'])

        # 승강기
        self.case_ev = QWidget(self.housing_widget)
        self.case_ev.setMinimumSize(QSize(150, 30))

        self.name_ev = QLabel(self.case_ev)
        self.name_ev.setGeometry(QRect(0, 0, 60, 30))
        self.name_ev.setStyleSheet(self.emphasis_css)
        self.name_ev.setText("승강기")

        self.item_ev = QLabel(self.case_ev)
        self.item_ev.setGeometry(QRect(80, 0, 30, 30))
        self.item_ev.setStyleSheet(self.normal_css)
        self.item_ev.setText(data['ev'])

        self.housing_layout = QGridLayout(self.housing_widget)
        self.housing_layout.setContentsMargins(0, 2, 5, 3)

        self.housing_layout.addWidget(self.item_count, 0, 0)
        self.housing_layout.addWidget(self.case_tot, 0, 1)
        self.housing_layout.addWidget(self.case_area, 0, 2)
        self.housing_layout.addWidget(self.case_num_1, 0, 3)

        self.housing_layout.addWidget(self.case_pet, 1, 0)
        self.housing_layout.addWidget(self.case_parking, 1, 1)
        self.housing_layout.addWidget(self.case_ev, 1, 2)
        self.housing_layout.addWidget(self.case_num_2, 1, 3)
