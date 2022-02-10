import sys
import re
import csv
import pandas as pd

from PySide6.QtWidgets import QApplication, QMainWindow, QButtonGroup, QWidget, QLabel, QLineEdit, QComboBox, \
    QListWidgetItem, QMenu, QGraphicsOpacityEffect
from PySide6.QtCore import QPropertyAnimation, Qt, QSize, QRegularExpression, QRect, QEvent, QTimer
from PySide6.QtGui import QIcon, QRegularExpressionValidator, QPixmap
from urllib3.connectionpool import xrange

from ui.main.ui_lease import Ui_MainWindow
from interface.sub_interface import address_details


class MainLease(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainLease, self).__init__(*args, **kwargs)

        # 특약 불러오기
        try:  self.agrs_data = pd.read_csv('../../data/val/agrs.csv', sep=",", encoding='cp949')
        except FileNotFoundError: return

        self._init_ui()
        self._init_interaction()

        self.get_building_thread = None     # 토지, 지역지구, 공시지가 스레드
        self.binfo, self.address = None, None   # 주소
        self.select_detail, self.select_building, self.total_buildings = None, None, None    # 표제부, 총괄 표제부
        self.owners, self.prices, self.pk = None, None, None  # 소유자, 공시가격, 건축물대장 PK

        self.page, self.contract = None, None  # 페이지, 계약 종류
        self.a_count, self.b_count, self.c_count = 0, 0, 0  # 계약자 카운트
        self.part_list = [self.part_0, self.part_1, self.part_2]
        self.contract_btn = {self.btn_contract_0: 0,
                             self.btn_contract_1: 1,
                             self.btn_contract_2: 2,
                             self.btn_contract_3: 3}

        self.msg_timer = False

        self.btn_contract_0.click()
        self.btn_provisions.hide()
        self.btn_back.hide()

    # UI init
    def _init_ui(self):
        self._setupUi(self)
        self.show()

        # 폼 로드 애니메이션
        self.animation = QPropertyAnimation(self, b'windowOpacity')
        self.animation.setDuration(100)
        self.animation.stop()
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

        # 계약 선택 버튼 토글
        self.btn_group = QButtonGroup()
        self.btn_group.addButton(self.btn_contract_0)
        self.btn_group.addButton(self.btn_contract_1)
        self.btn_group.addButton(self.btn_contract_2)
        self.btn_group.addButton(self.btn_contract_3)
        self.btn_group.buttonClicked.connect(self.clicked_contract_btn)

        # 콤보박스 아이템 추가
        self.cbx_contract.addItems(str_list.contract_list)
        self.cbx_land_details.addItems(str_list.land_details_list)
        self.cbx_structure.addItems(str_list.structure_list)
        self.cbx_purposes.addItems(str_list.purposes_list)

        # 금액 정규식
        regExp = QRegularExpression("^[0-9]*|\,")
        validator = QRegularExpressionValidator(regExp, self)
        self.edt_amount.setValidator(validator)
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
        self.lb_icon.setStyleSheet("QLabel { image: url(../../data/img/system/down_arrow_icon.png);}")

        # 메세지
        self.msg_background = QLabel(self)
        self.msg_background.setAlignment(Qt.AlignCenter)
        self.msg_background.setStyleSheet("QLabel{background-color: rgba(0,0,0,150);"
                                          "font: 14px \uc6f0\ucef4\uccb4 Regular;"
                                          "color: white;"
                                          "padding-top: 3px;}")
        self.msg_background.hide()
        self.load_keyword()

    # 상호작용 init
    def _init_interaction(self):
        # 에디트 마우스 클릭
        self.edt_address.mousePressEvent = self.clicked_address_edit
        # self.edt_c_company.mousePressEvent = self.find_company_event

        # 텍스트 체인지 이벤트
        self.edt_amount.textChanged.connect(self.changed_amount_edit)
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
        self.btn_next.clicked.connect(lambda: self.page_change_event("next"))
        self.btn_back.clicked.connect(lambda: self.page_change_event("back"))
        self.cbx_down_pay.activated.connect(self.activated_deposit_cbx)

        # 계약자 추가 이벤트
        self.btn_add_a.clicked.connect(lambda: self.insert_contractor(0))
        self.btn_add_b.clicked.connect(lambda: self.insert_contractor(1))
        self.btn_add_c.clicked.connect(lambda: self.insert_contractor(2))

        # 리스트 이벤트 필터
        self.lst_keyword.installEventFilter(self)
        self.lst_title.installEventFilter(self)
        self.lst_contractor.installEventFilter(self)

        # 리스트 아이템 클릭
        self.lst_keyword.itemClicked.connect(self.load_title)
        self.lst_title.itemClicked.connect(self.load_content)

    # 키워드 로드
    def load_keyword(self):
        keyword = self.agrs_data.keyword.values.tolist()
        keyword = list(dict.fromkeys(keyword))

        self.lst_keyword.clear()
        self.lst_keyword.addItem("( 직접입력 )")
        self.lst_keyword.addItems(keyword)
        self.lst_keyword.setCurrentRow(0)

    # 제목 로드
    def load_title(self):
        if self.lst_keyword.currentRow() == 0:
            self.lst_title.clear()
            self.edt_agreement.clear()
            return
        keyword = self.lst_keyword.currentItem().text()
        title = self.agrs_data.title[self.agrs_data.keyword == keyword]
        title = list(dict.fromkeys(title))

        self.lst_title.clear()
        self.lst_title.addItems(title)

    # 내용 로드
    def load_content(self):
        keyword = self.lst_keyword.currentItem().text()
        title = self.lst_title.currentItem().text()

        result = self.agrs_data[self.agrs_data.keyword == keyword]
        result = result[result.title == title]

        content_list = list("%s. %s" % (n, c) for n, c in zip(result.num, result.content))
        content_text = "\n".join(content_list)
        self.edt_agreement.setText(content_text)

    ## UI 상호작용 이벤트
    ################################################################################################

    # 계약 종류토글 선택
    def clicked_contract_btn(self, button):
        if self.contract == self.contract_btn[button]: return

        btn_style_on = """QPushButton {
                        font: 20px "웰컴체 Bold";
                        border: 2px solid rgb(44,62,80);
                        color: white;
                        background-color: rgb(24,42,60);
                        border-style: inset;
                        border-radius: 5px; }"""
        btn_style_off = """QPushButton {
                        font: 20px "웰컴체 Bold";
                        color: rgb(44,62,80);
                        border: 2px solid rgb(44,62,80);
                        padding-top: 3px;
                        background-color: white;
                        border-radius: 5px; }

                    QPushButton::hover {
                        border: 0px;
                        color: white;
                        background-color: rgb(64,82,100);
                        border-style: inset; }

                    QPushButton:pressed {
                        border: 0px;
                        color: white;
                        background-color: rgb(24,42,60);
                        border-style: inset; }
                    """

        for i in self.btn_group.buttons(): i.setStyleSheet(btn_style_off)
        button.setStyleSheet(btn_style_on)
        self.contract = self.contract_btn[button]

    # 페이지 전환 이벤트
    def page_change_event(self, v):
        current_count = self.stackedWidget.getCurrent()
        if v == "back":
            if current_count == 1:
                self.btn_provisions.hide()
                self.btn_back.hide()
            self.stackedWidget.slideInPrev()

        elif v == "next":
            if current_count == 0:
                self.btn_back.show()
                self.btn_provisions.show()
                if self.lst_contractor.count() < 1:
                    [self.insert_contractor(i) for i in range(3)]   # 기본 계약자 추가
                self.setting_ui_form()
            self.stackedWidget.slideInNext()

    # 소재지 찾기 에디트 클릭
    def clicked_address_edit(self, e):
        dialog = address_details.AddressDetails(0, self.edt_address.text())
        dialog.exec()

        if dialog.result:
            self.binfo, self.address = dialog.binfo, dialog.select_address
            self.select_detail = dialog.select_detail
            self.select_building, self.total_buildings = dialog.select_building, dialog.total_buildings
            self.owners, self.prices = dialog.owners, dialog.prices

            self.insert_address_event()

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

    # 매매대금/보증금 입력 이벤트
    def changed_amount_edit(self):
        self.changed_down_pay_edit()
        self.insert_balance_edt()
        self.translation_into_kor("amount")
    
    # 계약금 입력 이벤트
    def changed_down_pay_edit(self):
        amount = self.edt_amount.text()
        select_item = self.cbx_down_pay.currentIndex()

        if amount == "":
            if select_item != 2:
                self.edt_down_pay.clear()
        else:
            amount = int(re.sub(r'[^0-9]', '', amount))

            if select_item == 0: down_pay = int(amount * 0.1)
            elif select_item == 1: down_pay = int(amount * 0.05)
            else: down_pay = self.edt_down_pay.text()

            self.edt_down_pay.setText(str(down_pay))

    # 계약금 퍼센트 선택
    def activated_deposit_cbx(self):

        select_item = self.cbx_down_pay.currentIndex()
        if select_item == 0: self.edt_down_pay.setReadOnly(True)
        elif select_item == 1: self.edt_down_pay.setReadOnly(True)
        else:   # 직접 입력
            self.edt_down_pay.setReadOnly(False)
            self.edt_down_pay.setFocus()

        self.changed_down_pay_edit()

    # 잔금 계산 후 입력
    def insert_balance_edt(self):

        # 입력된 값이 있다면 int로 변환, 없다면 0
        amount = int(re.sub(r'[^0-9]', '', self.edt_amount.text())) if self.edt_amount.text() != "" else 0
        down_pay = int(re.sub(r'[^0-9]', '', self.edt_down_pay.text())) if self.edt_down_pay.text() != "" else 0
        mid_pay_1st = int(re.sub(r'[^0-9]', '', self.edt_mid_pay_1st.text())) if self.edt_mid_pay_1st.text() != "" else 0
        mid_pay_2st = int(re.sub(r'[^0-9]', '', self.edt_mid_pay_2st.text())) if self.edt_mid_pay_2st.text() != "" else 0
        minus_pay = down_pay + mid_pay_1st + mid_pay_2st

        if amount < minus_pay:
            if self.focusWidget() == self.edt_amount:
                self.edt_balance_pay.clear()
                return
            if self.contract == 0: self.info_msg(2, "계약금과 중도금의 합은 매매대금 보다 많을 수 없습니다.")
            else: self.info_msg(2, "계약금과 중도금의 합은 보증금 보다 많을 수 없습니다.")
            self.focusWidget().clear()

        else:
            balance = amount - minus_pay
            self.edt_balance_pay.setText(str(balance))

    # QMenu 이벤트
    def eventFilter(self, source, event):

        # 키워드 리스트
        if event.type() == QEvent.ContextMenu and source is self.lst_keyword:

            # 클릭한 아이템 인덱스
            item = source.itemAt(event.pos())
            item_index = self.lst_keyword.indexFromItem(item)

            # 우측 클릭 QMenu
            menu = QMenu(self)

            remove_action = menu.addAction("삭 제")
            menu.addAction(remove_action)

            menu_click = menu.exec(event.globalPos())

            # QMenu '삭제' 클릭 시
            if menu_click == remove_action:
                self.delete_item("keyword", item_index)

            return True

        # 특약 리스트
        elif event.type() == QEvent.ContextMenu and source is self.lst_title:

            # 클릭한 아이템 인덱스
            item = source.itemAt(event.pos())
            item_index = self.lst_title.indexFromItem(item)

            # 우측 클릭 QMenu
            menu = QMenu(self)

            remove_action = menu.addAction("삭 제")
            menu.addAction(remove_action)

            menu_click = menu.exec(event.globalPos())

            # QMenu '삭제' 클릭 시
            if menu_click == remove_action:
                self.delete_item("title", item_index)

            return True

        # 항목 리스트
        elif event.type() == QEvent.ContextMenu and source is self.lst_contractor:

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
                self.delete_item("contractor", item_index)

            return True

        return super(MainLease, self).eventFilter(source, event)

    # 항목 삭제
    def delete_item(self, cbx, item_index):
        # 계약자 정보 삭제
        if cbx == "contractor":
            item = self.lst_contractor.currentItem()
            item_widget = self.lst_contractor.itemWidget(item)
            name = item_widget.cbx_name.currentText().replace(" ", "")
            if "매도인" in name or "임대인" in name:
                if self.a_count == 1: return
                self.a_count -= 1
            if "매수인" in name or "임차인" in name:
                if self.b_count == 1: return
                self.b_count -= 1
            if "중개사" in name:
                if self.c_count == 1: return
                self.c_count -= 1
            self.lst_contractor.model().removeRow(item_index.row())

        # 특약 ) 키워드 삭제
        elif cbx == "keyword":
            if self.lst_keyword.currentRow() == 0: return
            keyword = self.lst_keyword.currentItem().text()
            
            result = self.agrs_data[self.agrs_data['keyword'] == keyword].index
            self.agrs_data = self.agrs_data.drop(result)
            self.lst_keyword.model().removeRow(item_index.row())

        # 특약) 타이틀 삭제
        elif cbx == "title":
            keyword = self.lst_keyword.currentItem()
            title = self.lst_title.currentItem().text()

            result = self.agrs_data[self.agrs_data.keyword == keyword.text()]
            result = result[result.title == title].index
            self.agrs_data = self.agrs_data.drop(result)
            self.lst_title.model().removeRow(item_index.row())

            result = self.agrs_data[self.agrs_data.keyword == keyword.text()]
            if result.empty:
                self.delete_item("keyword", self.lst_keyword.indexFromItem(keyword))

    ## 기타 함수
    ################################################################################################

    # 계약종류 선택 후 라벨 세팅
    def setting_ui_form(self):

        self.lb_item_nm_8.setText("보 증 금")

        # 매매 계약일 경우
        if self.contract == 0:
            self.lb_item_nm_8.setText("매 매 대 금")

            # 서브 1
            self.lb_item_nm_12.setText("융 자 금")
            self.lb_item_nm_12.show()
            self.edt_sub_1.show()
            self.lb_price_sub_1.show()

            # 서브 2
            self.lb_item_nm_13.show()
            self.edt_sub_2.show()
            self.lb_price_sub_2.show()

            # 임대부분
            self.lb_item_nm_2.setText("대지권종류")

            # 임대면적
            self.lb_item_nm_5.setText("대지권비율")

            # 대지권종류
            self.lb_item_nm_5.hide()
            self.edt_land_type.hide()

        elif self.contract == 1:
            # 서브 1
            self.lb_item_nm_12.hide()
            self.edt_sub_1.hide()
            self.lb_price_sub_1.hide()

            # 서브 2
            self.lb_item_nm_13.hide()
            self.edt_sub_2.hide()
            self.lb_price_sub_2.hide()

        elif (self.contract == 2) | (self.contract == 3):
            self.lb_item_nm_12.setText("월 차 임")

            # 서브 1
            self.lb_item_nm_12.show()
            self.edt_sub_1.show()
            self.lb_price_sub_1.show()

            # 서브 2
            self.lb_item_nm_13.hide()
            self.edt_sub_2.hide()
            self.lb_price_sub_2.hide()

    # 계약자 추가
    def insert_contractor(self, cont):
        current_count = [self.a_count, self.b_count, self.c_count]

        custom_item = ContractorItem(self.contract, cont, current_count)
        item = QListWidgetItem(self.lst_contractor)
        item.setSizeHint(QSize(custom_item.width(), 80))
        self.lst_contractor.setItemWidget(item, custom_item)

        if cont == 0: self.a_count += 1
        elif cont == 1: self.b_count += 1
        elif cont == 2: self.c_count += 1

    #
    def insert_brief_event(self, category, intent_data):
        obj = {"a": self.edt_a_address,
               "b": self.edt_b_address}
        obj[category].setText(intent_data['도로명주소'])

    # 받아온 주소 데이터 입력
    def insert_address_event(self):
        self.edt_area_rental.clear()
        room = None
        address, building, detail = self.address, self.select_building, self.select_detail

        print(self.address)
        print(self.binfo)
        print(self.select_detail)
        print(self.select_building)

        self.cbx_structure.setItemText(self.cbx_structure.count() - 1, "직접입력")
        self.cbx_purposes.setItemText(self.cbx_purposes.count() - 1, "직접입력")

        if address['지'] == "0":
            old = "%s %s %s %s" % (address['시도'], address['시군구'], address['읍면동'], address['번'])
        else: old = "%s %s %s %s-%s" % (address['시도'], address['시군구'], address['읍면동'], address['번'], address['지'])

        if self.binfo['타입'] == '일반':
            room = "%s층" % detail['층명칭'].rstrip("층")

            if self.binfo['일부']: room = room + " 일부"
            else: self.edt_area_rental.setText(detail['층면적'])

        elif self.binfo['타입'] == '집합':
            room = "%s호" % detail['호명칭'].rstrip("호")

            if len(detail['동명칭']) > 0:
                room = "%s동 " % (detail['동명칭'].rstrip("동")) + room

            if self.binfo['일부']: room = room + " 일부"
            else: self.edt_area_rental.setText(detail['전용면적'])

            old = "%s, %s" % (old, room)

        # 건물명칭 있으면 입력
        if self.address['건물명칭'] != "": old = "%s (%s)" % (old, self.address['건물명칭'])

        self.edt_address.setText(old)   # 소재지
        self.edt_address_details.setText(room)  # 임대부분
        self.edt_area_land.setText(building['대지면적'])    # 대지면적 
        self.edt_area_total.setText(building['연면적'])    # 연면적

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
        purposes_list = [detail['주용도'], detail['기타용도'], building['주용도'], building['기타용도']]
        for i in purposes_list:
            purposes_index = self.cbx_purposes.findText(i, Qt.MatchFixedString)
            if purposes_index > -1:
                self.cbx_purposes.setCurrentIndex(purposes_index)
                break
        if purposes_index == -1:
            self.cbx_purposes.setItemText(self.cbx_purposes.count() - 1, detail['기타용도'])
            self.cbx_purposes.setCurrentIndex(self.cbx_purposes.count() - 1)

    ## 정규식, 텍스트 변환
    ################################################################################################

    # 금액 한글로 변경
    def translation_into_kor(self, category):
        pays = {"amount": self.edt_amount,
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

    # 번호 정규식
    def format_phone(self, category):
        obj = {"a": self.edt_a_phone,
               "b": self.edt_b_phone}

        phone = obj[category].text()
        phone = re.sub(r'[^0-9]', '', phone)
        phone = re.sub(r'(\d{3})(\d{3,4})(\d{4})', r'\1-\2-\3', phone)

        obj[category].setText(phone)

    # 번호 정규식
    def format_call(self):
        call = self.edt_c_phone.text()
        call = re.sub(r'[^0-9]', '', call)
        call = re.sub(r'(\d{2,3})(\d{3,4})(\d{4})', r'\1-\2-\3', call)

        self.edt_c_phone.setText(call)

    # 등록번호 정규식
    def format_number(self, category):
        obj = {"a": self.cbx_a_num,
               "b": self.cbx_b_num}
        obj_edt = {"a": self.edt_a_num,
                   "b": self.edt_b_num}

        num = obj_edt[category].text()
        num = re.sub(r'[^0-9]', '', num)

        idx = obj[category].currentIndex()

        if idx == 0 or idx == 1 or idx == 3 or idx == 5 or idx == 6 or idx == 7 or idx == 8:
            num = re.sub(r'(\d{6})(\d{7})', r'\1-\2', num)

        elif idx == 2:
            num = re.sub(r'(\d{3})(\d{2})(\d{5})', r'\1-\2-\3', num)

        obj_edt[category].setText(num)

    # 알림 메세지
    def info_msg(self, sec, content):
        if self.msg_background.isHidden():
            self.msg_background.show()

        if self.msg_timer:
            self.timer.stop()
            self.msg_timer = False

        self.msg_timer = True
        self.msg_background.setText(content)
        font_size = self.msg_background.fontMetrics().boundingRect(content)

        if '\n' in content:
            line_width = []
            for i in content.split('\n'):
                line_width.append(self.msg_background.fontMetrics().boundingRect(i).width())
            w = max(line_width)
        else: w = font_size.width()

        h = font_size.height() * (content.count('\n') + 1)
        self.msg_background.resize(w + 20, h + 14)

        x = round((self.width() / 2) - (self.msg_background.width() / 2))
        y = round((self.height() / 2) - (self.msg_background.height() / 2))

        self.msg_background.move(x, y)

        effect = QGraphicsOpacityEffect(self.msg_background)
        self.msg_background.setGraphicsEffect(effect)

        self.anim = QPropertyAnimation(effect, b"opacity")
        self.anim.setStartValue(0)
        self.anim.setEndValue(1)
        self.anim.setDuration(60)
        self.anim.start()

        self.timer = QTimer(self)
        self.timer.start(sec * 1300)
        self.timer.timeout.connect(self.hide_msg)

    # 메세지 타이머 종료
    def hide_msg(self):
        effect = QGraphicsOpacityEffect(self.msg_background)
        self.msg_background.setGraphicsEffect(effect)

        self.anim = QPropertyAnimation(effect, b"opacity")
        self.anim.setStartValue(1)
        self.anim.setEndValue(0)
        self.anim.setDuration(500)
        self.anim.start()

        self.timer.stop()
        self.msg_timer = False

# 돈 정규식
def mask_money(txt):
    if txt == '': return
    txt = re.sub(r'[^0-9]', '', txt)
    txt = format(int(txt), ',')
    return str(txt)


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


# 예외 오류 처리
def my_exception_hook(exctype, value, traceback):
    sys.excepthook(exctype, value, traceback)


class ContractorItem(QWidget):
    def __init__(self, contract, contractor, current_count):
        super(ContractorItem, self).__init__()
        self.edt_css = """QLineEdit {
                     color: rgb(72,93,114);
                     font: 13px "웰컴체 Regular";
                     border: 1px solid #34495e;
                     padding-left: 55px;
                     padding-top: 3px;
                 }
                     QLineEdit::hover { border: 1px solid #3498db; }
                     QLineEdit:focus { border: 2px solid #3498db; } """
        self.edt_num_css = """QLineEdit {
                             color: rgb(72,93,114);
                             font: 13px "웰컴체 Regular";
                             border: 1px solid #34495e;
                             padding-left: 5px;
                             padding-top: 3px; }
                         QLineEdit::hover { border: 1px solid #3498db; }
                         QLineEdit:focus { border: 2px solid #3498db; } """
        self.cbx_css = """QComboBox {border: 1px solid gray;
                                padding: 3px 1px 1px 10px;
                                min-width: 4em;
                                background: rgb(255, 255, 255);
                                font: 14px "웰컴체 Regular";
                                color: rgb(44, 62, 80);
                            }

                            QComboBox:focus {
                                padding: 3px 1px 1px 10px;
                                color: rgb(127, 140, 141);
                            }

                            QComboBox:on { 
                                padding-top: 3px;
                                padding-left: 4px;
                            }

                            QComboBox QAbstractItemView::item { 
                                min-height: 30px; 
                            }

                            QComboBox::drop-down {
                                subcontrol-origin: padding;
                                subcontrol-position: top right;
                                width: 23px;

                                border-left-width: 1px;
                                border-left-style: solid;
                                border-left-color: darkgray;
                                border-top-right-radius: 3px;
                                border-bottom-right-radius: 3px;
                            }

                            QComboBox::down-arrow {
                                image: url(../../data/img/system/down_arrow_icon.png);
                                width: 22px;
                                height: 22px;
                            }

                            QComboBox::down-arrow:on {
                                top: 1px;
                                left: 1px;
                            }
                            QComboBox::setView {
                                color: rgb(44, 62, 80);
                                background-color: lightblue
                            }
                            comboBox->setView(view);
                            QListView::item:selected {
                                color: rgb(44, 62, 80);
                                background-color: lightblue
                            }"""
        self.hint_css = """QLabel { font: 13px "웰컴체 Regular";
                               color: white;
                               padding-top: 3px;
                               background-color: rgb(149, 165, 166); }"""
        self.num_list = ["주민등록번호", "법인등록번호", "사업자등록번호", "외국인등록번호", "여권번호", "종중등록번호", "재외국민주민번호",
                         "종교단체등록번호", "기타단체등록번호"]

        cbx_name_css = """QComboBox { 
                            border: None;
                            padding: 3px 1px 1px 3px;
                            min-width: 4em;
                            background: white;
                            font: 14px "웰컴체 Regular";
                            color: rgb(44, 62, 80); }
                        QComboBox:hover { color: rgb(104, 122, 140); }

                        QComboBox QAbstractItemView::item { min-height: 30px; }
                        QComboBox::drop-down { width: 15px; border: None; }
                        QComboBox::down-arrow {
                            image: url(../../data/img/system/down_arrow_icon.png);
                            width: 22px;
                            height: 22px;
                        }

                        QComboBox::down-arrow:on {
                            top: 1px;
                            left: 1px;
                        }
                        QComboBox::setView {
                            color: rgb(44, 62, 80);
                            background-color: lightblue
                        }
                        comboBox->setView(view);
                        QListView::item:selected {
                            color: rgb(44, 62, 80);
                            background-color: lightblue
                        }
                        """
        item_css = """QListWidget::item { border: none; }
                      QListWidget { outline: 0px; }"""
        self.setStyleSheet(item_css)

        self.cbx_name = QComboBox(self)
        self.cbx_name.setGeometry(QRect(0, 20, 80, 40))
        self.cbx_name.setStyleSheet(cbx_name_css)

        names = ["공동명의인", "대리인", "(수기 입력)"]

        # contractor [ 0: 매도인/임대인, 1: 매수인/임차인, 2: 중개사 ]
        if contractor == 0:
            if current_count[0] == 0:    # 매도/임대인이 아이템이 없을 경우
                if contract == 0: self.cbx_name.addItem("매 도 인")
                else: self.cbx_name.addItem("임 대 인")
            else: self.cbx_name.addItems(names)

            self._contractor_ab()

        elif contractor == 1:
            if current_count[1] == 0:  # 매도/임대인이 아이템이 없을 경우
                if contract == 0: self.cbx_name.addItem("매 수 인")
                else: self.cbx_name.addItem("임 차 인")
            else: self.cbx_name.addItems(names)

            self._contractor_ab()

        elif contractor == 2:
            if current_count[2] == 0:    # 중개사 아이템이 없을 경우
                self.cbx_name.addItem("개 업\n공인중개사")
            else: self.cbx_name.addItem("개 업 (공동)\n공인중개사")
            self._contractor_c()

    def _contractor_ab(self):
        self.edt_name = QLineEdit(self)
        self.edt_name.setGeometry(QRect(90, 5, 130, 30))
        self.edt_name.setStyleSheet(self.edt_css)

        self.lb_name_hint = QLabel(self)
        self.lb_name_hint.setGeometry(QRect(94, 9, 50, 22))
        self.lb_name_hint.setStyleSheet(self.hint_css)
        self.lb_name_hint.setAlignment(Qt.AlignCenter)
        self.lb_name_hint.setText("성 　 명")

        self.edt_phone = QLineEdit(self)
        self.edt_phone.setGeometry(QRect(230, 5, 170, 30))
        self.edt_phone.setStyleSheet(self.edt_css)

        self.lb_phone_hint = QLabel(self)
        self.lb_phone_hint.setGeometry(QRect(234, 9, 50, 22))
        self.lb_phone_hint.setStyleSheet(self.hint_css)
        self.lb_phone_hint.setAlignment(Qt.AlignCenter)
        self.lb_phone_hint.setText("연 락 처")

        self.cbx_number = QComboBox(self)
        self.cbx_number.setGeometry(QRect(411, 5, 130, 30))
        self.cbx_number.setStyleSheet(self.cbx_css)
        self.cbx_number.addItems(self.num_list)
        self.cbx_number.setCurrentIndex(0)

        self.edt_number = QLineEdit(self)
        self.edt_number.setGeometry(QRect(540, 5, 130, 30))
        self.edt_number.setStyleSheet(self.edt_num_css)

        self.edt_address = QLineEdit(self)
        self.edt_address.setGeometry(QRect(90, 43, 580, 30))
        self.edt_address.setStyleSheet(self.edt_css)

        self.lb_address_hint = QLabel(self)
        self.lb_address_hint.setGeometry(QRect(94, 47, 50, 22))
        self.lb_address_hint.setStyleSheet(self.hint_css)
        self.lb_name_hint.setAlignment(Qt.AlignCenter)
        self.lb_address_hint.setText("신 주 소")

    def _contractor_c(self):
        self.edt_name = QLineEdit(self)
        self.edt_name.setGeometry(QRect(90, 5, 160, 30))
        self.edt_name.setStyleSheet(self.edt_css)

        self.lb_name_hint = QLabel(self)
        self.lb_name_hint.setGeometry(QRect(94, 9, 50, 22))
        self.lb_name_hint.setStyleSheet(self.hint_css)
        self.lb_name_hint.setAlignment(Qt.AlignCenter)
        self.lb_name_hint.setText("대표자명")

        self.edt_phone = QLineEdit(self)
        self.edt_phone.setGeometry(QRect(260, 5, 170, 30))
        self.edt_phone.setStyleSheet(self.edt_css)

        self.lb_phone_hint = QLabel(self)
        self.lb_phone_hint.setGeometry(QRect(264, 9, 50, 22))
        self.lb_phone_hint.setStyleSheet(self.hint_css)
        self.lb_phone_hint.setAlignment(Qt.AlignCenter)
        self.lb_phone_hint.setText("대표번호")

        self.edt_number = QLineEdit(self)
        self.edt_number.setGeometry(QRect(440, 5, 230, 30))
        self.edt_number.setStyleSheet(self.edt_css)

        self.lb_number_hint = QLabel(self)
        self.lb_number_hint.setGeometry(QRect(444, 9, 50, 22))
        self.lb_number_hint.setStyleSheet(self.hint_css)
        self.lb_number_hint.setAlignment(Qt.AlignCenter)
        self.lb_number_hint.setText("등록번호")

        self.edt_company = QLineEdit(self)
        self.edt_company.setGeometry(QRect(90, 43, 160, 30))
        self.edt_company.setStyleSheet(self.edt_css)

        self.lb_company_hint = QLabel(self)
        self.lb_company_hint.setGeometry(QRect(94, 47, 50, 22))
        self.lb_company_hint.setStyleSheet(self.hint_css)
        self.lb_company_hint.setAlignment(Qt.AlignCenter)
        self.lb_company_hint.setText("사무소명")

        self.edt_address = QLineEdit(self)
        self.edt_address.setGeometry(QRect(260, 43, 410, 30))
        self.edt_address.setStyleSheet(self.edt_css)

        self.lb_address_hint = QLabel(self)
        self.lb_address_hint.setGeometry(QRect(264, 47, 50, 22))
        self.lb_address_hint.setStyleSheet(self.hint_css)
        self.lb_address_hint.setAlignment(Qt.AlignCenter)
        self.lb_address_hint.setText("주 　 소")


# 문자열
class str_list:
    contract_list = ["아파트", "주상복합", "연립주택", "다중주택", "다세대주택", "단독주택", "다가구주택", "도시형생활주택", "주택",
                     "오피스텔", "원룸", "상가", "상가점포", "상가주택", "상가건물", "건물", "사무실", "토지", "공장", "창고", "( 직접입력 )"]
    land_details_list = ["대", "전", "답", "임야", "공원", "구거", "도로", "염전", "제방", "하천", "유지", "묘지", "과수원",
                         "양어장", "주차장", "유원지", "광천지", "사적지", "잡종지", "공장용지", "창고용지", "학교용지", "종교용지",
                         "체육용지", "수도용지", "목장용지", "철도용지", "주유소용지", "기타", "( 직접입력 )"]
    structure_list = ["( 선택 )", "연와조", "석회조", "철골조", "흙벽돌조", "철파이프조", "시멘트벽돌조", "시멘트블럭조",
                      "철근콘크리트구조", "철골철근콘크리트", "한옥", "석조", "스틸", "통나무", "조립식", "없음", "( 직접입력 )"]
    purposes_list = ["( 선택 )", "아파트", "공동주택", "다중주택", "연립주택", "오피스텔", "다세대주택", "도시형생활주택", "단독주택", "다가구주택",
                     "근린생활시설", "근린생활시설 및 주택", "제1종근린생활시설", "제2종근린생활시설", "공장", "업무시설", "창고시설", "없음", "( 직접입력 )"]


sys._excepthook = sys.excepthook
sys.excepthook = my_exception_hook

app = QApplication()
window = MainLease()
app.exec()
