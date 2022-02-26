import sys
import pandas as pd
import module.open_api_pars as pars

from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QDialog, QLabel, QListWidgetItem, QMessageBox, QWidget, QGridLayout, QApplication, QMainWindow
from PySide6.QtCore import Qt, QTimer

from ui.dialog.ui_address import Ui_FindAddress


class MsgContext:
    no_set_msg = "< 집합 > 건물이 아닙니다. < 일반 > 건물로 조회됩니다."
    no_gen_msg = "< 일반 > 건물이 아닙니다. < 집합 > 건물로 조회됩니다."
    failed_to_search = "조회되지 않는 건물입니다. \n\n(건축물대장에 등재되지 않은 건물은 조회되지 않을 수 있습니다)"
    network_err = "데이터 서버가 원할하지 않습니다. \n불편을 드려 죄송합니다. 잠시 후 다시 시도해주세요.\n\n( 에러코드 : %s )"
    loading_msg = "건축물대장 정보를 불러오는 중입니다.\n통신 서버 및 네트워크 상태에 따라\n지연 될 수 있습니다."


class Address(QDialog, Ui_FindAddress):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.result_data = None

        self.ADDRESS_API_KEY = 'U01TX0FVVEgyMDIxMTIwMjEzNTc0MzExMTk4Mjc='
        self.DETAIL_ADDRESS_API_KEY = 'U01TX0FVVEgyMDIxMTIyMzEzMTE1NzExMjA2MTU='

        self.binfo, self.address, self.select_address,  self.address_detail = None, None, None, None
        self.old, self.new, self.buildings, self.rooms = None, None, None, None

        self._init_ui()
        self._init_interaction()

    # init UI
    def _init_ui(self):
        self.setWindowTitle("Real estate Information")
        self.edt_address.setFocus()
        self.ckb_part.setEnabled(False)

    # 상호작용
    def _init_interaction(self):
        self.cbx_buildings.activated.connect(self.select_building_event)
        self.cbx_rooms.activated.connect(self.select_room_event)
        self.edt_address.returnPressed.connect(self.find_event)
        self.list_address.itemDoubleClicked.connect(self.select_address_event)
        self.btn_input.clicked.connect(self.address_input_event)

    # 주소 찾기
    def find_event(self):
        if self.edt_address.text() == "": return
        self.list_address.clear()

        txt = self.edt_address.text().strip()
        self.address = pars.OpenApiRequest.get_address(self.ADDRESS_API_KEY, txt)

        self.lb_notfind.hide()
        if self.address is None: self.lb_notfind.show(); return
        if len(self.address) == 0: self.lb_notfind.show(); return

        for i in range(len(self.address)):
            result = self.address.iloc[i]
            if result['건물명칭'] == "": bld_name = ""
            else: bld_name = " (%s)" % result['건물명칭']

            new = result['도로명주소'] + bld_name
            old = "%s %s %s %s" % (result['시도'], result['시군구'], result['읍면동'], result['번'])
            if result['지'] != "0":
                old = "%s-%s" % (old, result['지'])

            if len(new) > 35: new = new[0:35] + '···'

            custom_item = AddressListItem(new, old)
            item = QListWidgetItem(self.list_address)
            item.setSizeHint(custom_item.sizeHint())
            self.list_address.setItemWidget(item, custom_item)

    # 주소 선택
    def select_address_event(self):
        self.select_address = self.address.iloc[self.list_address.currentRow()]
        result = self.select_address
        self.clear_cbx()

        self.binfo = {'주소코드': result['주소코드'],
                      '번': result['번'].zfill(4),
                      '지': result['지'].zfill(4),
                      '도로명주소': result['도로명주소'],
                      '도로명코드': result['도로명코드'],
                      '건물본번': result['건물본번'],
                      '건물부번': result['건물부번'],
                      '지하여부': result['지하여부'],
                      '타입': None}

        if self.rbt_set.isChecked(): self.binfo['타입'] = '집합'
        elif self.rbt_solo.isChecked(): self.binfo['타입'] = '일반'

        if self.select_address['공동주택여부'] == "0":
            if self.rbt_set.isChecked():
                self.msg('정보', 'ADDRESS', MsgContext.no_set_msg)

                self.binfo['타입'] = '일반'
                self.rbt_set.setChecked(False)
                self.rbt_solo.setChecked(True)

        elif self.select_address['공동주택여부'] == "1":
            if self.rbt_solo.isChecked():
                self.msg('정보', 'ADDRESS', MsgContext.no_gen_msg)

                self.binfo['타입'] = '집합'
                self.rbt_set.setChecked(True)
                self.rbt_solo.setChecked(False)

        if result['동'] == "":
            if result['건물명칭'] == "": self.cbx_buildings.addItem("건물 명칭 없음")
            else: self.cbx_buildings.addItem(result['건물명칭'])
        else:
            buildings = result['동'].split(', ')
            self.buildings = sorted(buildings)
            self.cbx_buildings.addItems(self.buildings)

        QTimer.singleShot(150, self.show_popup)

    # 건물명칭 콤보박스 선택
    def select_building_event(self):
        if (self.cbx_buildings.currentIndex()) == 0: return
        select_building, count = None, self.cbx_buildings.count()

        self.cbx_rooms.clear()
        if self.binfo['타입'] == "일반":
            self.cbx_rooms.addItem(" ( 상세주소 없음 )")
            self.select_room_event()

        elif self.binfo['타입'] == "집합":
            if count > 2: select_building = self.cbx_buildings.currentText()
            else: select_building = ""

            self.cbx_rooms.addItem(" ( 상세주소 / 호 선택 )")
            self.address_detail = pars.OpenApiRequest.get_address_detail(self.DETAIL_ADDRESS_API_KEY, self.binfo, select_building)
            self.cbx_rooms.addItems(self.address_detail['호명칭'])

            self.cbx_rooms.showPopup()

    # 상세주소 콤보박스 선택
    def select_room_event(self):
        count = self.cbx_buildings.count()
        result = self.select_address

        new = result['도로명주소']
        old = "%s %s %s %s" % (result['시도'], result['시군구'], result['읍면동'], result['번'])
        if result['지'] != "0":
            old = "%s-%s" % (old, result['지'])

        # 집합일 경우
        if self.binfo['타입'] == '집합':
            ho = self.cbx_rooms.currentText().rstrip("호")
            if count > 2:
                dong = self.cbx_buildings.currentText().rstrip("동")
                old = "%s, %s동 %s호" % (old, dong, ho)
                new = "%s, %s동 %s호" % (new, dong, ho)
            else:
                old = "%s, %s호" % (old, ho)
                new = "%s, %s호" % (new, ho)

        if result['건물명칭'] != "":
            old = "%s (%s)" % (old, result['건물명칭'])
            new = "%s (%s)" % (new, result['건물명칭'])

        self.old = old
        self.new = new

        self.edt_result_address.setText(new)

    # 소재지 입력 버튼
    def address_input_event(self):
        if self.edt_result_address == "": return

        self.result_data = {'정보': self.binfo,
                            '주소': self.old,
                            '도로명주소': self.new}
        self.hide()

    # 클리어 함수
    def clear_cbx(self):
        self.cbx_buildings.clear()
        self.cbx_buildings.addItem(" ( 건물명칭 / 동 선택 )")
        self.cbx_rooms.clear()
        self.cbx_rooms.addItem(" ( 상세주소 / 호 선택 )")

    # 콤보박스 항목 보이기
    def show_popup(self):
        self.cbx_buildings.showPopup()

    # 메세지 함수
    def msg(self, ty, title, content):
        if ty == "기본": QMessageBox.about(self, title, content)
        elif ty == "정보": QMessageBox.information(self, title, content, QMessageBox.Ok)
        elif ty == "경고": QMessageBox.warning(self, title, content, QMessageBox.Ok)
        elif ty == "위험": QMessageBox.critical(self, title, content, QMessageBox.Ok)

    # 다이얼로그 엔터키 막기
    def keyPressEvent(self, event):
        if ((not event.modifiers() and
             event.key() == Qt.Key_Return) or
                (event.modifiers() == Qt.KeypadModifier)):
            event.accept()
        else: super(AddressDetails, self).keyPressEvent(event)


class AddressListItem(QWidget):
    def __init__(self, new, old):
        super(AddressListItem, self).__init__()
        border_txt = """QLabel { font: 12px "웰컴체 Regular";
                        color: rgb(52, 152, 219);
                        border: 1px solid #3498db;
                        padding: 5px 3px 3px 3px;
                        border-radius: 5px;}"""

        self.lb_old_icon = QLabel()
        self.lb_old_icon.setMaximumSize(44, 23)
        self.lb_old_icon.setText("지   번")
        self.lb_old_icon.setStyleSheet(border_txt)

        self.lb_old = QLabel()
        self.lb_old.setText(old)
        self.lb_old.setStyleSheet("""QLabel { font: 15px "웰컴체 Regular"; color: rgb(44, 62, 80); padding-top: 2px;}""")

        self.lb_new_icon = QLabel()
        self.lb_new_icon.setMaximumSize(44, 23)
        self.lb_new_icon.setText("도로명")
        self.lb_new_icon.setStyleSheet(border_txt)

        self.lb_new = QLabel()
        self.lb_new.setText(new)
        self.lb_new.setStyleSheet("""QLabel { font: 14px "웰컴체 Regular"; color: rgb(75, 101, 132); padding-top: 2px;}""")

        self.set_ui()

    def set_ui(self):
        grid_box = QGridLayout()
        grid_box.addWidget(self.lb_old_icon, 0, 0)
        grid_box.addWidget(self.lb_new_icon, 1, 0)
        grid_box.addWidget(self.lb_old, 0, 1)
        grid_box.addWidget(self.lb_new, 1, 1)

        self.setLayout(grid_box)

# 예외 오류 처리
def my_exception_hook(exctype, value, traceback):
    sys.excepthook(exctype, value, traceback)


sys._excepthook = sys.excepthook
sys.excepthook = my_exception_hook

