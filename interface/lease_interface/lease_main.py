import sys
import re
import pandas as pd
from screeninfo import get_monitors

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QComboBox, \
    QListWidgetItem, QMenu, QGraphicsDropShadowEffect, QPushButton, QDialog
from PySide6.QtCore import QPropertyAnimation, Qt, QSize, QRegularExpression, QRect, QEvent, Signal, QObject
from PySide6.QtGui import QIcon, QRegularExpressionValidator, QFont, QColor, QScreen, QGuiApplication
from urllib3.connectionpool import xrange

from ui.main.ui_lease import Ui_MainWindow
from ui.custom.BlackBoxMsg import BoxMessage
from interface.sub_interface import find_address_details
from interface.lease_interface import agr_edit
import time


class ClickedSignal(QObject):
    clickedSig = Signal(str)


class MainLease(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainLease, self).__init__(*args, **kwargs)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_row', None)
        pd.set_option('display.width', None)

        # 특약 불러오기
        try: self.agrs_data = pd.read_csv('../../data/val/agrs.csv', sep=",")
        except FileNotFoundError: return

        self._init_ui()
        self.set_shadows()

        self._init_interaction()

        self.load_category()

        self.btn_provisions.clicked.connect(self.test)
        self.get_building_thread = None  # 토지, 지역지구, 공시지가 스레드
        self.binfo, self.result_address, self.land = None, None, None  # 주소
        self.select_detail, self.select_building, self.total_buildings = None, None, None  # 표제부, 총괄 표제부
        self.owners, self.prices, self.pk = None, None, None  # 소유자, 공시가격, 건축물대장 PK

        self.page, self.contract = None, None  # 페이지, 계약 종류
        self.a_count, self.b_count, self.c_count = 0, 0, 0  # 계약자 카운트
        self.editing_data = []
        self.cnt = 0

        for i in range(0, 3): self.insert_contractor(True, i, i)

        # self.btn_contract_0.click()

    def testt(self, cnt):
        print('시그널', cnt)

    def set_shadows(self):
        frame_list = [self.info_frame, self.agrs_frame, self.money_frame, self.sc_frame, self.my_sc_frame]
        for child in frame_list:
            shadow = QGraphicsDropShadowEffect(self)
            shadow.setBlurRadius(15)
            shadow.setXOffset(1)
            shadow.setYOffset(1)
            shadow.setColor(QColor(0, 0, 0, 35))
            child.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(40)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        shadow.setColor(QColor(0, 0, 0, 60))
        # self.btn_next.setGraphicsEffect(shadow)

    # UI init
    def _init_ui(self):
        self.setupUi(self)
        self.msg = BoxMessage(self)

        # 콤보박스 아이템 추가
        self.cbx_land_details.addItems(str_list.land_details_list)
        self.cbx_structure.addItems(str_list.structure_list)
        self.cbx_purposes.addItems(str_list.purposes_list)

        # 금액 정규식
        regExp = QRegularExpression("^[0-9]*|\,")
        validator = QRegularExpressionValidator(regExp, self)
        self.edt_price.setValidator(validator)
        self.edt_down_pay.setValidator(validator)
        self.edt_mid_pay_1st.setValidator(validator)
        self.edt_mid_pay_2st.setValidator(validator)
        self.edt_balance_pay.setValidator(validator)
        self.edt_sub_1.setValidator(validator)
        self.edt_sub_2.setValidator(validator)

        # 달력 버튼 이미지
        calendar_icon = QIcon('../../data/img/button/calendar_icon.png')
        self.btn_1st_cal.setIcon(calendar_icon)
        self.btn_1st_cal.setIconSize(QSize(22, 22))
        self.btn_2st_cal.setIcon(calendar_icon)
        self.btn_2st_cal.setIconSize(QSize(22, 22))
        self.btn_balance_cal.setIcon(calendar_icon)
        self.btn_balance_cal.setIconSize(QSize(22, 22))

        # 폰트 스페이싱
        font = self.edt_agrs.font()
        font.setLetterSpacing(QFont.PercentageSpacing, 103)
        self.edt_agrs.setFont(font)

        font = self.name_land.font()
        font.setLetterSpacing(QFont.AbsoluteSpacing, 8)
        self.name_land.setFont(font)
        self.name_bld.setFont(font)
        self.lb_item_nm_27.setFont(font)

        self.btn_back.hide()

        self.show()

    def test(self):
        self.cnt += 1
        a = Ui_Form(self, self.cnt)
        a.exec()

    # 상호작용 init
    def _init_interaction(self):
        # 에디트 마우스 클릭
        # self.edt_c_company.mousePressEvent = self.find_company_event

        # 텍스트 체인지 이벤트
        self.edt_price.textChanged.connect(self.changed_amount_edit)
        self.edt_mid_pay_1st.textChanged.connect(self.insert_balance_edt)
        self.edt_mid_pay_1st.textChanged.connect(lambda: self.translation_into_kor("1st"))
        self.edt_mid_pay_2st.textChanged.connect(self.insert_balance_edt)
        self.edt_mid_pay_2st.textChanged.connect(lambda: self.translation_into_kor("2st"))
        self.edt_balance_pay.textChanged.connect(lambda: self.translation_into_kor("balance"))
        self.edt_down_pay.textChanged.connect(self.insert_balance_edt)
        self.edt_down_pay.textChanged.connect(lambda: self.format_num("down"))
        self.edt_sub_1.textChanged.connect(lambda: self.format_num("sub1"))
        self.edt_sub_2.textChanged.connect(lambda: self.format_num("sub2"))

        # 버튼 클릭 이벤트
        self.btn_back.clicked.connect(lambda: self.page_change_event(self.stackedWidget.currentIndex() - 1))
        self.btn_next.clicked.connect(lambda: self.page_change_event(self.stackedWidget.currentIndex() + 1))

        self.btn_agr_edit.clicked.connect(self.clicked_edit_btn)
        self.cbx_down_pay.activated.connect(self.activated_deposit_cbx)
        self.cbx_category.activated.connect(self.load_title)
        self.cbx_title.activated.connect(self.load_content)

        # 계약자 추가 이벤트
        self.btn_add_a.clicked.connect(lambda: self.clicked_insert_btn(0))
        self.btn_add_b.clicked.connect(lambda: self.clicked_insert_btn(1))
        self.btn_add_c.clicked.connect(lambda: self.clicked_insert_btn(2))

        # 리스트 이벤트 필터
        # self.lst_category.installEventFilter(self)
        # self.lst_title.installEventFilter(self)
        # self.lst_contractor.installEventFilter(self)

        # 리스트 아이템 클릭
        # self.lst_category.itemClicked.connect(self.load_title)
        # self.lst_title.itemClicked.connect(self.load_content)

    ## 계약 선택 페이지
    ################################################################################################

    # 계약종류 선택 후 라벨 세팅
    def setting_ui_form(self):
        select_item = self.cbx_contract.currentText()
        set_list = ["아파트", "다세대주택", "연립주택", "도시형생활주택", "주상복합", "오피스텔", "사무실"]

        # 임대일 경우 임대부분 추가
        self.set_rantal.show() if self.contract != 0 else self.set_rantal.hide()

        # 집합 건물일 경우 대지권 추가
        self.set_ratio.show() if select_item in set_list else self.set_ratio.hide()
        self.set_ratio.move(0, 70 if self.set_rantal.isHidden() else 110)

        # 토지 항목 위치 설정
        land_y = 70 if self.set_rantal.isHidden() and self.set_ratio.isHidden() \
            else 110 if self.set_rantal.isHidden() or self.set_ratio.isHidden() else 150
        self.set_land.move(0, land_y)

        # '토지'일 경우 건물 항목 숨김
        if select_item == "토지":
            self.set_building.hide()
            self.set_ratio.show()
            self.set_ratio.move(0, land_y + 40)
            self.lb_item_nm_22.setText("거 래 지 분")
            self.lb_item_nm_23.hide()
            self.cbx_land_type.hide()

        else:
            self.set_building.show()
            self.lb_item_nm_22.setText("대지권비율")
            self.lb_item_nm_23.show()
            self.cbx_land_type.show()

        self.set_building.move(0, land_y + 40)

        # 라벨 설정
        self.lb_item_nm_8.setText("매 매 대 금") if self.contract == 0 else self.lb_item_nm_8.setText("보 증 금")
        self.lb_item_nm_7.setText("전 용 면 적") if select_item in set_list else self.lb_item_nm_7.setText("연 면 적")

        # 매매 계약일 경우
        if self.contract == 0:
            self.set_sub_1.show()
            self.set_sub_2.show()
            self.lb_item_nm_12.setText("융 자 금")

        # 월세일 경우
        elif self.contract == 2:
            self.set_sub_1.show()
            self.set_sub_2.hide()
            self.lb_item_nm_12.setText("월 차 임")

        # 전세일 경우
        else:
            self.set_sub_1.hide()
            self.set_sub_2.hide()

    ## 부동산, 계약 금액 페이지
    ################################################################################################

    # 소재지 찾기 에디트 클릭
    def clicked_address_edit(self, e):
        dialog = find_address_details.AddressDetails(0, self.edt_address.text())
        dialog.exec()

        if dialog.result:
            self.binfo, self.address = dialog.binfo, dialog.select_address
            self.land, self.select_detail = dialog.land, dialog.select_detail
            self.select_building, self.total_buildings = dialog.select_building, dialog.total_buildings
            self.owners, self.prices = dialog.owners, dialog.prices

            select_item = self.cbx_contract.currentText()
            set_list = ["아파트", "다세대주택", "연립주택", "도시형생활주택", "주상복합", "오피스텔", "사무실"]

            # 집합건물 계약서일 경우
            if select_item in set_list:
                if self.binfo['타입'] == "일반":
                    self.msg.show_msg(5000, 'center', "입력하신 소재지는 집합 건물입니다. 소재지 또는 계약서 종류를 확인해주세요.\n계속 동일한 문제 발생시, 소재지 검색이 아닌 직접 입력하여 작성해주세요.")
                else: self.insert_set_event(self.address, self.select_building, self.select_detail)

            # 일반건물, 토지 계약서일 경우
            elif select_item not in set_list:
                if self.binfo['타입'] == "집합":
                    self.msg.show_msg(5000, 'center', """입력하신 소재지는 일반 건물입니다. 소재지 또는 계약서 종류를 확인해주세요.\n
                                                         계속 동일한 문제 발생시, 소재지 검색이 아닌 직접 입력하여 작성해주세요.""")
                else: self.insert_general_event(self.address, self.select_building, self.select_detail)

    # 일반 건축물 입력
    def insert_general_event(self, address, building, detail):
        self.edt_area_rental.clear()

        # 소재지
        old = "%s %s %s %s" % (address['시도'], address['시군구'], address['읍면동'], address['번'])
        if address['지'] != "0": old = "%s-%s" % (old, address['지'])

        # 상세주소
        room = "%s층" % detail['층명칭'].rstrip("층")
        if self.binfo['일부']: room = room + " 일부"
        else:
            if not self.set_rantal.isHidden():
                self.edt_area_rental.setText(detail['층면적'])

        # 건물명칭 있으면 입력
        if self.address['건물명칭'] != "": old = "%s (%s)" % (old, self.address['건물명칭'])

        self.edt_address.setText(old)  # 소재지
        if self.land:
            self.edt_ratio_1.setText(self.land['대지면적'].values[0])
            self.edt_area_land.setText(self.land['대지면적'].values[0])  # 대지면적
            self.cbx_land_details.setCurrentIndex(self.cbx_land_details.findText(self.land['지목'].values[0], Qt.MatchFixedString))

        # 임대일 경우
        if not self.set_rantal.isHidden(): self.edt_address_details.setText(room)  # 임대부분

        # 건물이 있을 경우
        if not self.set_building.isHidden():
            self.edt_area_total.setText(building['연면적']) if self.lb_item_nm_7.text() == "연 면 적" \
                else self.edt_area_total.setText(detail['전용면적'])

            structure_index, purposes_index = [], []

            # 구조 세팅
            structure_list = [detail['주구조'], detail['기타구조'], building['주구조'], building['기타구조']]
            for i in structure_list:
                structure_index = self.cbx_structure.findText(i, Qt.MatchFixedString)
                if structure_index > -1:
                    self.cbx_structure.setCurrentIndex(structure_index)
                    break

            if structure_index == -1:
                self.cbx_structure.setItemText(self.cbx_structure.count() - 1, building['기타구조'])
                self.cbx_structure.setCurrentIndex(self.cbx_structure.count() - 1)

            # 용도 세팅
            find_purpose = False
            for i in range(self.cbx_purposes.count()):
                item = self.cbx_purposes.itemText(i)
                if item in building['기타용도']:
                    find_purpose = True
                    self.cbx_purposes.setCurrentIndex(i)
                    break
            if not find_purpose:
                self.cbx_purposes.addItem(building['기타용도'])
                self.cbx_purposes.setCurrentIndex(self.cbx_purposes.count() - 1)

    # 집합 건축물 입력
    def insert_set_event(self, address, building, detail):
        self.edt_area_rental.clear()

        # 주소지
        old = "%s %s %s %s" % (address['시도'], address['시군구'], address['읍면동'], address['번'])
        if address['지'] != "0": old = "%s-%s" % (old, address['지'])

        # 상세주소
        room = "%s호" % detail['호명칭'].rstrip("호")
        if len(detail['동명칭']) > 1: room = "%s동 " % (detail['동명칭'].rstrip("동")) + room

        if self.binfo['일부']: room = room + " 일부"
        else:
            if not self.set_rantal.isHidden():
                self.edt_area_rental.setText(detail['전용면적'])

        old = "%s, %s" % (old, room)

        # 건물명칭 있으면 입력
        if self.address['건물명칭']: old = "%s (%s)" % (old, self.address['건물명칭'])

        self.edt_address.setText(old)  # 소재지
        if self.land:
            self.edt_ratio_1.setText(self.land['대지면적'].values[0])  # 대지면적
            self.edt_area_land.setText(self.land['대지면적'].values[0])
            self.cbx_land_details.setCurrentIndex(self.cbx_land_details.findText(self.land['지목'].values[0], Qt.MatchFixedString))

        # 임대부분
        if not self.set_rantal.isHidden():
            self.edt_address_details.setText(room)

        # 건물
        if not self.set_building.isHidden():
            self.edt_area_total.setText(building['연면적']) if self.lb_item_nm_7.text() == "연 면 적" \
                else self.edt_area_total.setText(detail['전용면적'])

            structure_index, purposes_index = [], []

            # 구조 세팅
            structure_list = [detail['주구조'], detail['기타구조'], building['주구조'], building['기타구조']]
            for i in structure_list:
                structure_index = self.cbx_structure.findText(i, Qt.MatchFixedString)
                if structure_index > -1:
                    self.cbx_structure.setCurrentIndex(structure_index)
                    break
            if structure_index == -1:
                self.cbx_structure.setItemText(self.cbx_structure.count() - 1, detail['기타구조'])
                self.cbx_structure.setCurrentIndex(self.cbx_structure.count() - 1)

            # 용도 세팅
            purposes_index = self.cbx_purposes.findText(detail['기타용도'], Qt.MatchFixedString)
            if purposes_index > -1:     # 콤보박스에 있을 경우
                self.cbx_purposes.setCurrentIndex(purposes_index)

            elif purposes_index == -1:  # 콤보박스에 없을 경우
                find_purpose = False
                purpose = detail['기타용도']
                for i in range(self.cbx_purposes.count()):
                    item = self.cbx_purposes.itemText(i)
                    if item in purpose:
                        find_purpose = True
                        self.cbx_purposes.setCurrentIndex(i)
                        break
                if not find_purpose:
                    self.cbx_purposes.addItem(detail['기타용도'])
                    self.cbx_purposes.setCurrentIndex(self.cbx_purposes.count() - 1)

    # 매매대금/보증금 입력 이벤트
    def changed_amount_edit(self):
        self.changed_down_pay_edit()
        self.insert_balance_edt()
        self.translation_into_kor("amount")

    # 계약금 입력 이벤트
    def changed_down_pay_edit(self):
        amount = self.edt_price.text()
        select_item = self.cbx_down_pay.currentIndex()

        if amount == "":
            if select_item != 2:
                self.edt_down_pay.clear()
        else:
            amount = int(re.sub(r'[^0-9]', '', amount))

            if select_item == 0:
                down_pay = int(amount * 0.1)
            elif select_item == 1:
                down_pay = int(amount * 0.05)
            else:
                down_pay = self.edt_down_pay.text()

            self.edt_down_pay.setText(str(down_pay))

    # 계약금 퍼센트 선택
    def activated_deposit_cbx(self):

        select_item = self.cbx_down_pay.currentIndex()
        if select_item == 0:
            self.edt_down_pay.setReadOnly(True)
        elif select_item == 1:
            self.edt_down_pay.setReadOnly(True)
        else:  # 직접 입력
            self.edt_down_pay.setReadOnly(False)
            self.edt_down_pay.setFocus()

        self.changed_down_pay_edit()

    # 잔금 계산 후 입력
    def insert_balance_edt(self):

        # 입력된 값이 있다면 int로 변환, 없다면 0
        amount = int(re.sub(r'[^0-9]', '', self.edt_price.text())) if self.edt_price.text() != "" else 0
        down_pay = int(re.sub(r'[^0-9]', '', self.edt_down_pay.text())) if self.edt_down_pay.text() != "" else 0
        mid_pay_1st = int(
            re.sub(r'[^0-9]', '', self.edt_mid_pay_1st.text())) if self.edt_mid_pay_1st.text() != "" else 0
        mid_pay_2st = int(
            re.sub(r'[^0-9]', '', self.edt_mid_pay_2st.text())) if self.edt_mid_pay_2st.text() != "" else 0
        minus_pay = down_pay + mid_pay_1st + mid_pay_2st

        if amount < minus_pay:
            if self.focusWidget() == self.edt_price:
                self.edt_balance_pay.clear()
                return

            if self.contract == 0: self.msg.show_msg(2500, 'center', "계약금과 중도금의 합은 매매대금 보다 많을 수 없습니다.")
            else: self.msg.show_msg(2500, 'center', "계약금과 중도금의 합은 보증금 보다 많을 수 없습니다.")
            self.focusWidget().clear()

        else:
            balance = amount - minus_pay
            self.edt_balance_pay.setText(str(balance))

    ## 특약사항 페이지
    ################################################################################################

    # 키워드 로드
    def load_category(self):
        category = self.agrs_data.category.values.tolist()
        category = list(dict.fromkeys(category))

        self.cbx_title.clear()
        self.cbx_title.addItem("( 특약사항 선택 )")

        self.cbx_category.clear()
        self.cbx_category.addItem("( 직접입력 )")
        self.cbx_category.addItems(category)

    # 제목 로드
    def load_title(self):
        if self.cbx_category.currentIndex() == 0:
            self.cbx_title.clear()
            self.cbx_title.addItem("( 특약사항 선택 )")

            self.edt_agrs.clear()
            self.edt_agrs.setFocus()

        else:
            category = self.cbx_category.currentText()
            title = self.agrs_data.title[self.agrs_data.category == category]
            title = list(dict.fromkeys(title))

            self.cbx_title.clear()
            self.cbx_title.addItems(title)
            self.cbx_title.showPopup()

    # 내용 로드
    def load_content(self):
        category = self.cbx_category.currentText()
        title = self.cbx_title.currentText()

        result = self.agrs_data[self.agrs_data.category == category]
        result = result[result.title == title]

        content_list = list("%s. %s" % (n, c) for n, c in zip(result.num, result.content))
        content_text = "\n".join(content_list)
        self.edt_agrs.setText(content_text)

        self.edt_agrs.setFocus()

    # 특약사항 편집 이벤트
    def clicked_edit_btn(self):
        if self.cbx_category.currentIndex() != 0:

            category = self.cbx_category.currentText()
            title = self.cbx_title.currentText()

            dialog = agr_edit.AgrEditor(self.agrs_data, category, title)
            dialog.exec()
        else:

            dialog = agr_edit.AgrEditor(self.agrs_data)
            dialog.exec()

        #     if dialog.response is not None:
        #         response = dialog.response
        #
        #         self.agrs_data = self.agrs_data.drop(self.editing_data.index)
        #         self.agrs_data = self.agrs_data.append(response)
        #
        #         self.agrs_data.reset_index(drop=True, inplace=True)
        #         self.agrs_data.to_csv("../../data/val/agrs.csv", sep=",", index=False)
        #
        #         category = response['category'].iloc[0]
        #         title = response['title'].iloc[0]
        #
        #         self.visit_item(category, title)
        #
        # else:
        #     dialog = agr_edit.AgrEditor(self.agrs_data)
        #     dialog.exec()
        #
        #     if dialog.response is not None:
        #         response = dialog.response
        #
        #         self.agrs_data = self.agrs_data.append(response)
        #
        #         self.agrs_data.reset_index(drop=True, inplace=True)
        #         self.agrs_data.to_csv("../../data/val/agrs.csv", sep=",", index=False)
        #
        #         category = response['category'].iloc[0]
        #         title = response['title'].iloc[0]
        #
        #         self.visit_item(category, title)

    # 특약사항 삭제 이벤트
    def clicked_remove_btn(self):
        category = self.lst_category.currentRow()
        title = self.lst_title.currentRow()

        # 키워드 삭제
        if title == -1 and category != 0:
            category_text = self.lst_category.currentItem().text()
            result = self.agrs_data[self.agrs_data['category'] == category_text].index

            self.agrs_data = self.agrs_data.drop(result)
            self.lst_category.model().removeRow(category)

            self.lst_title.clear()
            self.edt_agreement.clear()

        # 타이틀 삭제
        elif category != 0:
            category_text = self.lst_category.currentItem().text()
            title_text = self.lst_title.currentItem().text()

            result = self.agrs_data[self.agrs_data.category == category_text]
            result = result[result.title == title_text].index

            self.agrs_data = self.agrs_data.drop(result)
            self.lst_title.model().removeRow(title)

            self.edt_agreement.clear()

            result = self.agrs_data[self.agrs_data.category == category_text]
            if result.empty: self.lst_category.model().removeRow(self.lst_category.currentRow())

        self.agrs_data.reset_index(drop=True, inplace=True)
        self.agrs_data.to_csv("../../data/val/agrs.csv", sep=",", index=False)

    ## 계약자 정보 페이지
    ################################################################################################

    # 계약자 추가 버튼
    def clicked_insert_btn(self, cont, pos=0):
        item_size = self.lst_contractor.model().rowCount()
        for i in range(item_size):
            item = self.lst_contractor.item(i)
            item_widget = self.lst_contractor.itemWidget(item)
            name = item_widget.cbx_name.currentText().replace(" ", "").replace("\n", "")

            # 매도/임대인
            if cont == 0:
                if name == "매도인" or name == "임대인": pos = i

            # 매수/임차인
            elif cont == 1:
                if name == "매수인" or name == "임차인": pos = i

            # 중개사
            elif cont == 2:
                if name == "개업공인중개사": pos = i
        self.insert_contractor(False, cont, pos)

    # 계약자 추가
    def insert_contractor(self, first, cont, pos=0):
        custom_item = ContractorItem(first, self.contract, cont)
        item = QListWidgetItem()
        item.setSizeHint(QSize(custom_item.width(), 80))

        if first: self.lst_contractor.addItem(item)
        else: self.lst_contractor.insertItem(pos + 1, item)

        self.lst_contractor.setItemWidget(item, custom_item)

    # 사무소찾기 에디트 클릭
    def clicked_company_edit(self):
        if len(self.address) != 0:
            key = 'ff8e71ba71f059c00ec57f'
            code = self.address[0]

            # dialog = func_dialog.Company(key, code[0:5])
            # dialog.exec()
            #
            # if len(dialog.data) != 0:
            #     self.company = dialog.data
            #     self.edt_c_name.setText(self.company[3])
            #     self.edt_c_company.setText(self.company[2])

    # QMenu 이벤트
    def eventFilter(self, source, event):
        # 항목 리스트
        if event.type() == QEvent.ContextMenu and source is self.lst_contractor:

            # 클릭한 아이템 인덱스
            item = source.itemAt(event.pos())
            item_index = self.lst_contractor.indexFromItem(item)

            # 우측 클릭 QMenu
            menu = QMenu(self)

            remove_action = menu.addAction("삭 제")
            menu.addAction(remove_action)

            menu_click = menu.exec(event.globalPos())

            # QMenu '삭제' 클릭 시
            if menu_click == remove_action:
                item = self.lst_contractor.currentItem()
                item_widget = self.lst_contractor.itemWidget(item)
                name = item_widget.cbx_name.currentText().replace(" ", "").replace("\n", "")

                if name not in ["매도인", "매수인", "임대인", "임차인", "개업공인중개사"]:
                    self.lst_contractor.model().removeRow(item_index.row())
                else:
                    self.msg.show_msg(1500, 543, "해당 계약자 정보는 필수 입력 사항입니다.")

            return True

        return super(MainLease, self).eventFilter(source, event)

    ## 기타 기능, 함수
    ################################################################################################

    # 페이지 전환 이벤트
    def page_change_event(self, page):
        self.stackedWidget.setCurrentIndex(page)

        # page_btn = {0: self.btn_page_1, 1: self.btn_page_2, 2: self.btn_page_3}
        current_idx = self.stackedWidget.currentIndex()

        # for btn in page_btn.values():
        #     btn.setChecked(False)
        #     page_btn[current_idx].setChecked(True)

        if current_idx == 0: self.btn_back.hide()
        elif current_idx == 1: self.btn_back.show()
        elif current_idx == 2: self.btn_back.show()

    # 금액 한글로 변경
    def translation_into_kor(self, category):
        pays = {"amount": self.edt_price,
                "1st": self.edt_mid_pay_1st,
                "2st": self.edt_mid_pay_2st,
                "balance": self.edt_balance_pay}

        ko_pays = {"amount": self.lb_korean_amount,
                   "1st": self.lb_korean_1st,
                   "2st": self.lb_korean_2st,
                   "balance": self.lb_korean_balance}

        num = pays[category].text()

        if (num == "") | (num == "0"):
            ko_pays[category].clear()
            return

        num = re.sub(r'[^0-9]', '', num)
        result = num_kor_read(list(map(int, num + "0000")))
        ko_pays[category].setText(result + "원")
        pays[category].setText(mask_money(num))

    # 금액 정규식
    def format_num(self, category):
        pays = {"down": self.edt_down_pay,
                "sub1": self.edt_sub_1,
                "sub2": self.edt_sub_2}

        num = pays[category].text()
        num = re.sub(",", "", num)
        pays[category].setText(mask_money(num))

# 돈 정규식
def mask_money(money):
    if money == '': return
    money = re.sub(r'[^0-9]', '', money)
    money = format(int(money), ',')
    return str(money)

# 폰 번호 정규식
def mask_phone(num):
    num = re.sub(r'[^0-9]', '', num)
    num = re.sub(r'(\d{3})(\d{3,4})(\d{4})', r'\1-\2-\3', num)
    return num

# 대표번호 정규식
def mask_call(num):
    num = re.sub(r'[^0-9]', '', num)
    num = re.sub(r'(\d{2,3})(\d{3,4})(\d{4})', r'\1-\2-\3', num)
    return num

# 숫자 -> 한글 변환 함수
def num_kor_read(num):  # num은 각 자리 숫자들의 리스트
    ONE_DIGIT = ['', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    UNIT_S = [u'십', u'백', u'천']
    UNIT_B = ['', '만', '억', '조']

    digits = len(num)  # 숫자 자릿수
    if digits == 1:
        return ONE_DIGIT[num[0]]  # 한 자릿수 숫자의 경우 one_digit에서 해당하는 숫자를 돌려준다.
    if digits <= 4:  # 숫자 자릿수가 4자리 이하일 경우 가장 앞자리를 뽑아 먼저 읽고 나머지를 처리한다.
        head = num[0]  # 가장 앞자리 수
        if head == 0:  # 가장 앞자리가 0인 경우
            return num_kor_read(num[1:])
        part_read = []
        if head != 1:  # 가장 앞자리가 1이 아닌 경우
            part_read.append(ONE_DIGIT[head])
        part_read.append(UNIT_S[digits - 2])  # 단위 추
        part_read.append(num_kor_read(num[1:]))  # 뒷부분을 재귀를 이용해 읽는다.
        return ''.join(part_read)

    else:  # 가독성을 위해 else 문을 사용한다.
        # 자릿수가 4의 배수가 아니면 앞자리에 0을 추가해 4의 배수로 만든다.
        if digits % 4 != 0:
            longer_num = [0 for i in xrange(4 - digits % 4)]
            digits += 4 - digits % 4
        else:
            longer_num = []
        longer_num.extend(num)
        part_read = []
        for i in xrange(int(digits / 4)):  # 앞에서부터 네 자리씩 처리한다.
            temp = num_kor_read(longer_num[4 * i:4 * i + 4])
            if temp == '':
                continue  # 0000의 예외처리
            part_read.append(temp)
            part_read.append(UNIT_B[int(digits / 4 - i - 1)])  # 단위 추가
        return ''.join(part_read)

# 등록번호 정규식
def mask_number(idx, num):
    num = re.sub(r'[^0-9]', '', num)

    if idx == 0 or idx == 1 or idx == 3 or idx == 5 or idx == 6 or idx == 7 or idx == 8:
        num = re.sub(r'(\d{6})(\d{7})', r'\1-\2', num)

    elif idx == 2:
        num = re.sub(r'(\d{3})(\d{2})(\d{5})', r'\1-\2-\3', num)

    return num


# 예외 오류 처리
def my_exception_hook(exctype, value, traceback):
    sys.excepthook(exctype, value, traceback)


class ContractorItem(QWidget):
    def __init__(self, first, contract, contractor):
        super(ContractorItem, self).__init__()
        self.edt_css = """QLineEdit { padding-left: 55px; padding-right: 0px; padding-bottom: 1px;}"""
        self.edt_num_css = """QLineEdit { padding-left: 5px; padding-right: 0px; padding-bottom: 1px; }"""
        self.hint_css = """QLabel { font: 13px "웰컴체 Regular";
                               color: rgb(125,125,125);
                               padding-top: 3px;
                               background-color: white; }"""
        self.num_list = ["주민등록번호", "법인등록번호", "사업자등록번호", "외국인등록번호", "여권번호", "종중등록번호", "재외국민주민번호",
                         "종교단체등록번호", "기타단체등록번호"]

        cbx_name_css = """QComboBox { border: None; }"""
        self.cbx_name = QComboBox(self)
        self.cbx_name.setGeometry(QRect(0, 20, 90, 40))
        self.cbx_name.setStyleSheet(cbx_name_css)

        names = ["공동명의인", "대 리 인", "(직접입력)"]

        # contractor [ 0: 매도인/임대인, 1: 매수인/임차인, 2: 중개사 ]
        if contractor == 0:
            if first: names[0] = "매 도 인" if contract == 0 else "임 대 인"
            else: names[0] = "공동매도인" if contract == 0 else "공동임대인"
            self.cbx_name.addItems(names)
            self._contractor_ab()

        elif contractor == 1:
            if first: names[0] = "매 수 인" if contract == 0 else "임 차 인"
            else: names[0] = "공동매수인" if contract == 0 else "공동임차인"
            self.cbx_name.addItems(names)
            self._contractor_ab()

        elif contractor == 2:
            if first: self.cbx_name.addItem("개 업\n공인중개사")
            else: self.cbx_name.addItem("개업 (공동)\n공인중개사")
            self._contractor_c()

    def _contractor_ab(self):
        # 폰트 스페이싱

        self.edt_name = QLineEdit(self)
        self.edt_name.setGeometry(QRect(100, 5, 130, 30))
        self.edt_name.setStyleSheet(self.edt_css)

        self.lb_name_hint = QLabel(self)
        self.lb_name_hint.setGeometry(QRect(104, 9, 50, 22))
        self.lb_name_hint.setStyleSheet(self.hint_css)
        self.lb_name_hint.setText("성명")

        font = self.lb_name_hint.font()
        font.setLetterSpacing(QFont.AbsoluteSpacing, 21)
        self.lb_name_hint.setFont(font)

        self.edt_phone = QLineEdit(self)
        self.edt_phone.setGeometry(QRect(240, 5, 170, 30))
        self.edt_phone.setStyleSheet(self.edt_css)
        self.edt_phone.textChanged.connect(lambda: self.edt_phone.setText(mask_phone(self.edt_phone.text())))

        self.lb_phone_hint = QLabel(self)
        self.lb_phone_hint.setGeometry(QRect(244, 9, 50, 22))
        self.lb_phone_hint.setStyleSheet(self.hint_css)
        self.lb_phone_hint.setText("연락처")

        font = self.lb_phone_hint.font()
        font.setLetterSpacing(QFont.AbsoluteSpacing, 5)
        self.lb_phone_hint.setFont(font)

        self.cbx_number = QComboBox(self)
        self.cbx_number.setGeometry(QRect(421, 5, 125, 30))
        self.cbx_number.addItems(self.num_list)

        self.edt_number = QLineEdit(self)
        self.edt_number.setGeometry(QRect(555, 5, 125, 30))
        self.edt_number.setStyleSheet(self.edt_num_css)
        self.edt_number.textChanged.connect(lambda: self.edt_number.setText(
            mask_number(self.cbx_number.currentIndex(), self.edt_number.text())))

        self.edt_address = QLineEdit(self)
        self.edt_address.setGeometry(QRect(100, 43, 580, 30))
        self.edt_address.setStyleSheet(self.edt_css)

        self.lb_address_hint = QLabel(self)
        self.lb_address_hint.setGeometry(QRect(104, 47, 50, 22))
        self.lb_address_hint.setStyleSheet(self.hint_css)
        self.lb_address_hint.setText("주소")

        font = self.lb_address_hint.font()
        font.setLetterSpacing(QFont.AbsoluteSpacing, 21)
        self.lb_address_hint.setFont(font)

    def _contractor_c(self):
        self.edt_name = QLineEdit(self)
        self.edt_name.setGeometry(QRect(100, 5, 160, 30))
        self.edt_name.setStyleSheet(self.edt_css)

        self.lb_name_hint = QLabel(self)
        self.lb_name_hint.setGeometry(QRect(104, 9, 50, 22))
        self.lb_name_hint.setStyleSheet(self.hint_css)
        self.lb_name_hint.setAlignment(Qt.AlignCenter)
        self.lb_name_hint.setText("대표자명")

        self.edt_phone = QLineEdit(self)
        self.edt_phone.setGeometry(QRect(270, 5, 170, 30))
        self.edt_phone.setStyleSheet(self.edt_css)
        self.edt_phone.textChanged.connect(lambda: self.edt_phone.setText(mask_call(self.edt_phone.text())))

        self.lb_phone_hint = QLabel(self)
        self.lb_phone_hint.setGeometry(QRect(274, 9, 50, 22))
        self.lb_phone_hint.setStyleSheet(self.hint_css)
        self.lb_phone_hint.setAlignment(Qt.AlignCenter)
        self.lb_phone_hint.setText("대표번호")

        self.edt_number = QLineEdit(self)
        self.edt_number.setGeometry(QRect(450, 5, 230, 30))
        self.edt_number.setStyleSheet(self.edt_css)

        self.lb_number_hint = QLabel(self)
        self.lb_number_hint.setGeometry(QRect(454, 9, 50, 22))
        self.lb_number_hint.setStyleSheet(self.hint_css)
        self.lb_number_hint.setAlignment(Qt.AlignCenter)
        self.lb_number_hint.setText("등록번호")

        self.edt_company = QLineEdit(self)
        self.edt_company.setGeometry(QRect(100, 43, 160, 30))
        self.edt_company.setStyleSheet(self.edt_css)

        self.lb_company_hint = QLabel(self)
        self.lb_company_hint.setGeometry(QRect(104, 47, 50, 22))
        self.lb_company_hint.setStyleSheet(self.hint_css)
        self.lb_company_hint.setAlignment(Qt.AlignCenter)
        self.lb_company_hint.setText("사무소명")

        self.edt_address = QLineEdit(self)
        self.edt_address.setGeometry(QRect(270, 43, 410, 30))
        self.edt_address.setStyleSheet(self.edt_css)

        self.lb_address_hint = QLabel(self)
        self.lb_address_hint.setGeometry(QRect(274, 47, 50, 22))
        self.lb_address_hint.setStyleSheet(self.hint_css)
        self.lb_address_hint.setText("주소")

        font = self.lb_address_hint.font()
        font.setLetterSpacing(QFont.AbsoluteSpacing, 21)
        self.lb_address_hint.setFont(font)


class Ui_Form(QDialog):
    def __init__(self, main, con):
        super().__init__()
        self.resize(200, 130)
        self.threadEvent = ClickedSignal()

        self.main = main
        self.con = con

        screen = QGuiApplication.primaryScreen().availableGeometry()
        w, h = screen.size().width(), screen.size().height()
        x = w - self.width()
        y = h - self.height()

        self.move(x, y)
        print(self.x(), self.y())
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 56, 12))
        self.pushButton = QPushButton(self)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(110, 30, 75, 23))
        self.pushButton.clicked.connect(self.test)

        self.show()
    # retranslateUi

    def test(self):
        self.main.testt(self.con)
        print(self.x(), self.y())


# 문자열
class str_list:
    contract_list = ["( 선택 )", "아파트", "다세대주택", "연립주택", "다가구주택", "단독주택", "다중주택", "도시형생활주택", "주상복합",
                     "오피스텔", "원룸", "상가", "상가점포", "상가주택", "상가건물", "건물", "사무실", "토지", "공장", "창고", "( 직접입력 )"]
    land_details_list = ["( 선택 )", "대", "전", "답", "임야", "공원", "구거", "도로", "염전", "제방", "하천", "유지", "묘지", "과수원",
                         "양어장", "주차장", "유원지", "광천지", "사적지", "잡종지", "공장용지", "창고용지", "학교용지", "종교용지",
                         "체육용지", "수도용지", "목장용지", "철도용지", "주유소용지", "기타", "( 직접입력 )"]
    structure_list = ["( 선택 )", "연와조", "석회조", "철골조", "흙벽돌조", "철파이프조", "시멘트벽돌조", "시멘트블럭조",
                      "철근콘크리트구조", "철골철근콘크리트", "한옥", "석조", "스틸", "통나무", "조립식", "없음", "( 직접입력 )"]
    purposes_list = ["( 선택 )", "아파트", "공동주택", "다중주택", "연립주택", "오피스텔", "다세대주택", "도시형생활주택", "단독주택", "다가구주택",
                     "제1종근린생활시설", "제2종근린생활시설", "근린생활시설", "근린생활시설 및 주택", "공장", "업무시설", "창고시설", "없음", "( 직접입력 )"]


sys._excepthook = sys.excepthook
sys.excepthook = my_exception_hook

app = QApplication()
window = MainLease()
app.exec()
