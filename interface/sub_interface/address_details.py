import re
import sys
import pandas as pd
import module.open_api_pars as pars

from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QDialog, QLabel, QListWidgetItem, QMessageBox, QWidget, QGridLayout, QApplication
from PySide6.QtCore import Qt

from ui.dialog.ui_address_detail import Ui_Address_Detaile


class MsgContext:
    no_set_msg = "< 집합 > 건물이 아닙니다. < 일반 > 건물로 조회됩니다."
    no_gen_msg = "< 일반 > 건물이 아닙니다. < 집합 > 건물로 조회됩니다."
    failed_to_search = "조회되지 않는 건물입니다. \n\n(건축물대장에 등재되지 않은 건물은 조회되지 않을 수 있습니다)"
    network_err = "데이터 서버가 원할하지 않습니다. \n불편을 드려 죄송합니다. 잠시 후 다시 시도해주세요.\n\n( 에러코드 : %s )"
    loading_msg = "건축물대장 정보를 불러오는 중입니다.\n통신 서버 및 네트워크 상태에 따라\n지연 될 수 있습니다."


class AddressDetails(QDialog, Ui_Address_Detaile):
    def __init__(self, call_type):
        super().__init__()

        self.setupUi(self)
        self.result_data = None

        self.BULIDING_API_KEY = 'sfSPRX+xNEExRUqE4cdhNjBSk4uXIv8F1CfLen06hdPGn5cflLJqy/nxmh48uF8fvdGk68k6Z5jWsU1n6BeNPA=='
        self.ADDRESS_API_KEY = 'U01TX0FVVEgyMDIxMTIwMjEzNTc0MzExMTk4Mjc='
        self.DETAIL_ADDRESS_API_KEY = 'U01TX0FVVEgyMDIxMTIyMzEzMTE1NzExMjA2MTU='

        self.address, self.select_address, self.binfo = None, None, None    # 주소
        self.buildings, self.select_building, self.total_buildings = None, None, None   # 건물 (동)
        self.detail, self.select_detail, self.exact_detail = None, None, None    # 상세 (호, 층)
        self.owners, self.prices = None, None   # 소유자, 공시가격
        self.get_building_thread, self.get_rooms_thread, self.get_layers_thread = None, None, None
        self.select_index, self.result = None, False

        self.detail_list = []

        # 0: 기본 데이터만 호출, 1: 모든 데이터 호출
        self.call_type = call_type

        self._init_ui()
        self._init_interaction()

    # init UI
    def _init_ui(self):
        self.setWindowTitle("Real estate Information")
        self.edt_address.setFocus()

        # 로딩 구성
        self.movie = QMovie("../../data/img/animation/loading.gif")
        self.lb_back = QLabel(self)
        self.lb_loading = QLabel(self)
        self.lb_back_txt = QLabel(self)

        self.lb_back.hide()
        self.lb_back.setGeometry(10, 137, 441, 360)
        self.lb_back.setStyleSheet("QLabel{background-color: rgba(0,0,0,40);}")

        self.lb_loading.resize(70, 100)
        x = (self.lb_back.width() / 2) + self.lb_back.x()
        y = (self.lb_back.height() / 2) + (self.lb_back.y()) - self.lb_loading.height()

        self.lb_loading.hide()
        self.lb_loading.move(int(x - (self.lb_loading.width() / 2)), int(y))
        self.lb_loading.setMovie(self.movie)
        self.lb_loading.setScaledContents(True)

        self.lb_back_txt.hide()
        self.lb_back_txt.resize(225, 80)
        self.lb_back_txt.setText(MsgContext.loading_msg)
        self.lb_back_txt.setAlignment(Qt.AlignCenter)
        self.lb_back_txt.move(int(x - (self.lb_back_txt.width() / 2)), int(y + self.lb_loading.height() - 20))
        self.lb_back_txt.setStyleSheet("QLabel{background-color: rgba(0,0,0,150);"
                                       "font: 14px \uc6f0\ucef4\uccb4 Regular;"
                                       "color: white;"
                                       "padding-top: 3px;"
                                       "padding-left: 5px;}")

        self.ckb_part.setEnabled(False)

    # 상호작용
    def _init_interaction(self):
        self.cbx_buildings.activated.connect(self.select_building_event)
        self.cbx_rooms.activated.connect(self.select_room_event)
        self.edt_address.returnPressed.connect(self.get_address_request)
        self.list_address.itemDoubleClicked.connect(self.select_address_event)
        self.btn_input.clicked.connect(self.address_input_event)
        self.ckb_part.clicked.connect(self.part_check_event)

    # 일부 체크
    def part_check_event(self):
        if self.cbx_rooms.currentIndex() == 0: return
        if self.ckb_part.isChecked():
            result = self.select_address
            old = "%s %s %s %s-%s" % (result['시도'], result['시군구'], result['읍면동'], result['번'], result['지'])

            # 일반일 경우
            if self.binfo['타입'] == '일반':
                self.edt_result_address.setText("%s, %s %s" % (old, self.select_detail['층명칭'], "일부"))

            # 집합일 경우
            elif self.binfo['타입'] == '집합':
                dong = self.select_detail['동명칭'].rstrip('동')
                ho = self.select_detail['호명칭'].rstrip('호')
                if len(dong) == 0: self.edt_result_address.setText("%s, %s호 %s" % (old, ho, "일부"))
                else: self.edt_result_address.setText("%s, %s동 %s호 %s" % (old, dong, ho, "일부"))

        else: self.edt_result_address.setText(self.edt_result_address.text().replace("일부", ""))

    # 주소 찾기
    def get_address_request(self):
        if self.edt_address.text() == "": return
        self.list_address.clear()

        # 주소 양끝 공백제거 후 파싱
        txt = self.edt_address.text().strip()
        self.address = pars.OpenApiRequest.get_address(self.ADDRESS_API_KEY, txt)

        # 주소 불러온 다음
        self.lb_notfind.hide()
        if self.address is None: self.lb_notfind.show(); return
        if len(self.address) == 0: self.lb_notfind.show(); return

        # 불러온 주소 리스트에 추가
        for i in range(len(self.address)):
            result = self.address.iloc[i]
            if result['건물명칭'] == "": bld_name = ""
            else: bld_name = " (%s)" % result['건물명칭']

            new = result['도로명주소'] + bld_name
            old = "%s %s %s %s-%s" % (result['시도'], result['시군구'], result['읍면동'], result['번'], result['지'])

            if len(new) > 35: new = new[0:35] + '···'

            custom_item = AddressListItem(new, old)
            item = QListWidgetItem(self.list_address)
            item.setSizeHint(custom_item.sizeHint())
            self.list_address.setItemWidget(item, custom_item)

    # 주소 선택
    def select_address_event(self):
        self.select_address = self.address.iloc[self.list_address.currentRow()]
        result = self.select_address

        self.binfo = {'주소코드': result['주소코드'],
                      '번': result['번'].zfill(4),
                      '지': result['지'].zfill(4),
                      '도로명주소': result['도로명주소'],
                      '도로명코드': result['도로명코드'],
                      '건물본번': result['건물본번'],
                      '건물부번': result['건물부번'],
                      '지하여부': result['지하여부'],
                      '동명칭': ''}

        if self.rbt_set.isChecked(): self.binfo['타입'] = '집합'
        elif self.rbt_solo.isChecked(): self.binfo['타입'] = '일반'

        self.loading(True)
        self.clear_cbx()

        # 표제부, 총괄표제부 파싱 쓰레드
        self.get_building_thread = pars.BuildingRegisterThread(self.binfo, ['표제부', '총괄표제부'])
        self.get_building_thread.start()
        self.get_building_thread.threadEvent.workerThreadDone.connect(self.add_building_list)

    # 건물명칭(동) 콤보박스 추가
    def add_building_list(self, val):
        self.loading(False)
        buildings = val[0][val[0]['주부속구분'] == '주건축물']
        self.total_buildings = val[1]

        if buildings is None:
            self.msg('정보', 'ADDRESS', MsgContext.failed_to_search)
            return
        elif ('err' in buildings) or ('ERR' in buildings):
            self.msg('오류', 'ADDRESS', MsgContext.network_err % buildings)
            return

        if self.binfo['타입'] == '일반':
            if len(buildings[buildings['대장구분'] == '일반']) == 0:
                buildings = buildings[buildings['대장구분'] == '집합']
                self.msg('정보', 'ADDRESS', MsgContext.no_gen_msg)

                self.binfo['타입'] = '집합'
                self.rbt_set.setChecked(True)

            else: buildings = buildings[buildings['대장구분'] == '일반']

        elif self.binfo['타입'] == '집합':
            if len(buildings[buildings['대장구분'] == '집합']) == 0:
                buildings = buildings[buildings['대장구분'] == '일반']
                self.msg('정보', 'ADDRESS', MsgContext.no_set_msg)

                self.binfo['타입'] = '일반'
                self.rbt_solo.setChecked(True)
            else: buildings = buildings[buildings['대장구분'] == '집합']

        buildings = buildings.sort_values(by=['동명칭'], axis=0)
        buildings.reset_index(drop=True, inplace=True)

        self.cbx_buildings.clear()
        print(buildings)
        for i in range(len(buildings)):
            result = buildings.iloc[i]
            if result['건물명칭'] == '':
                if self.select_address['건물명칭'] == '':
                    # 건물 이름, 동 이름이 없을 경우 (건물 명칭 없음 | 근린생활시설)
                    if result['동명칭'] == '': item = "건물 명칭 없음 | " + result['기타용도']

                    # 건물 이름만 없을 경우 (건물 명칭 없음 | 101동)
                    else: item = "건물 명칭 없음 | %s동" % result['동명칭'].rstrip('동')
                else:
                    # 동 이름만 없을 경우 (다원빌 | 오피스텔)
                    if result['동명칭'] == '': item = "%s | %s" % (self.select_address['건물명칭'], result['기타용도'])

                    # 건물 이름, 동 이름이 모두 있는 경우 (다원빌 | A동)
                    else: item = "%s | %s동" % (self.select_address['건물명칭'], result['동명칭'].rstrip('동'))
            else:
                # 동 이름만 없을 경우 (다원빌 | 오피스텔)
                if result['동명칭'] == '': item = "%s | %s" % (result['건물명칭'], result['기타용도'])

                # 건물 이름, 동 이름이 모두 있는 경우 (다원빌 | 101동)
                else: item = "%s | %s동" % (result['건물명칭'], result['동명칭'].rstrip('동'))

            self.cbx_buildings.addItem(item)

        self.buildings = buildings
        self.cbx_buildings.showPopup()

    # 건물명칭 콤보박스 선택
    def select_building_event(self):
        self.loading(True)
        self.select_building = self.buildings.iloc[self.cbx_buildings.currentIndex()]

        # 일반일 경우
        if self.binfo['타입'] == '일반':
            if self.call_type == 0: self.get_building_thread = pars.BuildingRegisterThread(self.binfo, ['층별'])
            if self.call_type == 1: self.get_building_thread = pars.BuildingRegisterThread(self.binfo, ['층별', '소유자', '개별주택가격'])
            self.get_building_thread.start()
            self.get_building_thread.threadEvent.workerThreadDone.connect(self.add_layer_list)

        # 건물 타입이 집합일 경우
        if self.binfo['타입'] == '집합':
            self.binfo['동명칭'] = self.select_building['동명칭']
            if self.call_type == 0: self.get_building_thread = pars.BuildingRegisterThread(self.binfo, ['전유부'])
            if self.call_type == 1: self.get_building_thread = pars.BuildingRegisterThread(self.binfo, ['전유부', '소유자', '공동주택가격'])
            self.get_building_thread.start()
            self.get_building_thread.threadEvent.workerThreadDone.connect(self.add_room_list)

    # 집합건물(호) 콤보박스 추가
    def add_room_list(self, val):
        if self.call_type == 1:
            self.owners = val[1]
            if val[2] is not None: self.prices = val[2]
        self.detail = convert_ho(val[0])
        print(self.binfo)
        self.exact_detail = details = get_exact_value(self.detail)

        self.cbx_rooms.clear()
        for i in range(len(details)):
            ho = details.iloc[i]['호명칭'].rstrip('호')
            purps = details.iloc[i]['기타용도']
            area = round(pd.to_numeric(details.iloc[i]['전용면적']), 2)
            item = '%s호 | %s m² | %s' % (ho, str(area), purps)

            self.cbx_rooms.addItem(item)
            self.detail_list.append(item)

        self.loading(False)
        self.cbx_rooms.showPopup()

    # 일반건물(층) 콤보박스 추가
    def add_layer_list(self, val):
        if self.call_type == 1:
            self.owners = val[1]
            if val[2] is not None: self.prices = val[2]

        self.detail = val[0].sort_values(by='층번호', ascending=True)

        self.cbx_rooms.clear()
        for i in range(len(self.detail)):
            layer = self.detail.loc[i]['층명칭']
            purps = self.detail.loc[i]['기타용도']
            area = round(pd.to_numeric(self.detail.iloc[i]['층면적']), 2)
            item = '%s | %s m² | %s' % (layer, str(area), purps)

            self.cbx_rooms.addItem(item)
            self.detail_list.append(item)

        self.loading(False)
        self.cbx_rooms.showPopup()

    # 상세주소 콤보박스 선택
    def select_room_event(self):
        if self.call_type == 0: self.ckb_part.setEnabled(True)

        select_index = self.cbx_rooms.currentIndex()
        result = self.select_address

        old = "%s %s %s %s-%s" % (result['시도'], result['시군구'], result['읍면동'], result['번'], result['지'])

        # 일반일 경우
        if self.binfo['타입'] == '일반':
            self.select_detail = self.detail.iloc[select_index]  # 층별
            self.edt_result_address.setText("%s, %s" % (old, self.select_detail['층명칭']))

        # 집합일 경우
        elif self.binfo['타입'] == '집합':
            self.select_detail = self.exact_detail.iloc[select_index]
            dong = self.select_detail['동명칭'].rstrip('동')
            ho = self.select_detail['호명칭'].rstrip('호')

            if len(dong) == 0: self.edt_result_address.setText("%s, %s호" % (old, ho))
            else: self.edt_result_address.setText("%s, %s동 %s호" % (old, dong, ho))

    # 소재지 입력 버튼
    def address_input_event(self):
        if self.edt_result_address.text() != "":
            self.select_index = self.cbx_rooms.currentIndex()
            self.result = True
            self.hide()

    # 클리어 함수
    def clear_cbx(self):
        self.detail_list.clear()
        self.cbx_buildings.clear()
        self.cbx_buildings.addItem(" ( 건물명칭 / 동 선택 )")
        self.cbx_rooms.clear()
        self.cbx_rooms.addItem(" ( 상세주소 / 호 선택 )")
        self.edt_result_address.clear()

    # 메세지 함수
    def msg(self, ty, title, content):
        if ty == "기본": QMessageBox.about(self, title, content)
        elif ty == "정보": QMessageBox.information(self, title, content, QMessageBox.Ok)
        elif ty == "경고": QMessageBox.warning(self, title, content, QMessageBox.Ok)
        elif ty == "위험": QMessageBox.critical(self, title, content, QMessageBox.Ok)

    # 로딩 함수
    def loading(self, run):
        if run:
            self.lb_loading.show()
            self.lb_back.show()
            self.lb_back_txt.show()
            self.btn_search.setEnabled(False)
            self.btn_input.setEnabled(False)
            self.movie.start()

        else:
            self.lb_loading.hide()
            self.lb_back.hide()
            self.lb_back_txt.hide()
            self.btn_search.setEnabled(True)
            self.btn_input.setEnabled(True)
            self.movie.stop()

    # 다이얼로그 엔터키 막기
    def keyPressEvent(self, event):
        if ((not event.modifiers() and
             event.key() == Qt.Key_Return) or
                (event.modifiers() == Qt.KeypadModifier)):
            event.accept()
        else: super(AddressDetails, self).keyPressEvent(event)

# 정확한 전유 호수 찾기
def get_exact_value(data):
    try:
        items = data

        # 전유 부분만
        items = items[items['전유공용구분'] == '전유']

        hos = set(items['호명칭'])
        if len(hos) == len(items): return items

        # 같은 층, 전유 항목이 2개 이상일 경우 면적 넓은 항목만 남기기
        items = items.astype({'전용면적': 'float'})

        for i in hos:
            res = items[items['호명칭'] == i]
            if len(res) == 1: continue
            items[items['호명칭'] == i] = res.nlargest(1, '전용면적', keep='first')

        items = items.astype({'전용면적': 'str'}).dropna(axis=0)
        return items

    except ValueError: return data

# 호수 INT 정렬
def convert_ho(data):

    data['호명칭(RE)'] = data['호명칭'].str.rstrip('호')

    under = data[data['층구분'] == '지하'].copy()
    top = data[data['층구분'] == '지상'].copy()

    under['호명칭(RE)'] = mask_ho('-', under['호명칭(RE)'].values.tolist())
    top['호명칭(RE)'] = mask_ho('', top['호명칭(RE)'].values.tolist())

    under = under.sort_values(by=['호명칭(RE)'], axis=0, ascending=False)
    top = top.sort_values(by=['호명칭(RE)'], axis=0)

    result = pd.concat([under, top], ignore_index=True)
    return result

# 호수 정규식
def mask_ho(un, val):
    result = []
    for i in val:
        try:
            if len(i) == 2:
                com1 = re.compile('(\d)(\d)')  # 01
                com2 = re.compile('(\w)(\d)')  # 지1

                mat = re.match(com1, i)
                if mat is not None:
                    conv = re.sub(r'(\d)(\d)', r'10\g<2>', mat.group())
                    result.append(int(un + conv))
                    continue

                mat = re.match(com2, i)
                if mat is not None:
                    conv = re.sub(r'(\w)(\d)', r'10\g<2>', mat.group())
                    result.append(int(un + conv))
                    continue

            elif len(i) == 3:
                com1 = re.compile('(\d)(\d)(\d)')     # 101
                com2 = re.compile('(\w)(\d)(\d)')  # B01, 지01
                com3 = re.compile('(\d)(\w)(\d)')     # 3층1
                com4 = re.compile('(\w)(\w)(\d)')     # 지층1

                mat = re.match(com1, i)
                if mat is not None:
                    result.append(int(i))
                    continue

                mat = re.match(com2, i)
                if mat is not None:
                    conv = re.sub(r'(\w)(\d)(\d)', r'10\g<3>', mat.group())
                    result.append(int(un + conv))
                    continue

                mat = re.match(com3, i)
                if mat is not None:
                    conv = re.sub(r'(\d)(\w)(\d)', r'\g<1>0\g<3>', mat.group())
                    result.append(int(un + conv))
                    continue

                mat = re.match(com4, i)
                if mat is not None:
                    conv = re.sub(r'(\w)(\w)(\d)', r'10\g<3>', mat.group())
                    result.append(int(un + conv))
                    continue

            elif len(i) == 4:
                com1 = re.compile('(\d)(\d)(\d)(\d)')         # 1001
                com2 = re.compile('(\w)(\d)(\d)(\d)')  # B101, 지101
                com3 = re.compile('(\w)(\w)(\d)(\d)')         # 지층01

                mat = re.match(com1, i)
                if mat is not None:
                    result.append(int(i))
                    continue

                mat = re.match(com2, i)
                if mat is not None:
                    conv = re.sub(r'(\w)(\d)(\d)(\d)', r'\g<2>\g<3>\g<4>', mat.group())
                    result.append(int(un + conv))
                    continue

                mat = re.match(com3, i)
                if mat is not None:
                    conv = re.sub(r'(\w)(\w)(\d)(\d)', r'10\g<4>', mat.group())
                    result.append(int(un + conv))
                    continue

            elif len(i) == 5:
                com = re.compile('(\w)(\w)(\d)(\d)(\d)')  # 지하101호

                mat = re.match(com, i)
                if mat is not None:
                    conv = re.sub(r'(\w)(\w)(\d)(\d)(\d)', r'\g<3>\g<4>\g<5>', mat.group())
                    result.append(int(un + conv))
                    continue

            result.append(i)

        except ValueError:
            result.append(i)

    return result


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

