import re
import sys
import pandas as pd
import module.open_api_pars as pars

from PySide6.QtGui import QMovie, QIcon, QColor
from PySide6.QtWidgets import QDialog, QLabel, QListWidgetItem, QMessageBox, QWidget, \
    QGridLayout, QApplication, QGraphicsOpacityEffect, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt, QPropertyAnimation, QTimer, QSize, QEvent

from ui.dialog.ui_address import Ui_FindAddress
from ui.custom import LoadingBox, BlackBoxMsg


class MsgContext:
    no_set_msg = "< 집합 > 건물이 아닙니다. < 일반 > 건물로 조회됩니다."
    no_gen_msg = "< 일반 > 건물이 아닙니다. < 집합 > 건물로 조회됩니다."
    failed_to_search = "조회되지 않는 건물입니다. \n\n(신축 건물 또는 건축물대장에 등재되지 않은 건물은 \n조회되지 않을 수 있습니다.)"
    network_err = "데이터 서버가 원할하지 않습니다. \n불편을 드려 죄송합니다. 잠시 후 다시 시도해주세요.\n\n( 에러코드 : %s )"
    loading_msg = "건축물대장 정보를 불러오는 중입니다.\n통신 서버 및 네트워크 상태에 따라\n지연 될 수 있습니다."
    failed_in_search = "정보를 불러오는 중 에러가 발생했습니다. 관리자에게 문의해주세요."


class AddressDetails(QDialog, Ui_FindAddress):
    def __init__(self, content=None):
        super().__init__()
        self.setupUi(self)

        # OPEN API KEY
        self.BULIDING_API_KEY = 'sfSPRX+xNEExRUqE4cdhNjBSk4uXIv8F1CfLen06hdPGn5cflLJqy/nxmh48uF8fvdGk68k6Z5jWsU1n6BeNPA=='
        self.ADDRESS_API_KEY = 'U01TX0FVVEgyMDIxMTIwMjEzNTc0MzExMTk4Mjc='
        self.DETAIL_ADDRESS_API_KEY = 'U01TX0FVVEgyMDIxMTIyMzEzMTE1NzExMjA2MTU='

        # 변수 선언
        self.address, self.select_address, self.binfo = None, None, None    # 주소
        self.buildings, self.select_building, self.total_buildings = None, None, None   # 건물 (동)
        self.detail, self.select_detail, self.exact_detail = None, None, None    # 상세 (호, 층)
        self.land, self.owners, self.prices = None, None, None   # 소유자, 공시가격
        self.get_building_thread, self.get_rooms_thread, self.get_layers_thread = None, None, None
        self.select_index, self.result = None, False
        self.detail_list = []

        self.msg_timer = False

        self._init_ui()
        self._init_interaction()
        self._init_shadow()

        if content:
            self.edt_address.setText(content)
            self.get_address_request()

    # init UI
    def _init_ui(self):
        self.edt_address.setFocus()

        self.btn_search.setIcon(QIcon('../../data/img/button/search_icon.png'))
        self.btn_search.setIconSize(QSize(30, 30))

        self.loading = LoadingBox.LoadingBox(self)
        self.msg = BlackBoxMsg.BoxMessage(self)

    # 상호작용
    def _init_interaction(self):
        self.cbx_buildings.activated.connect(self.select_building_event)
        self.cbx_rooms.activated.connect(self.select_room_event)
        self.edt_address.returnPressed.connect(self.get_address_request)
        self.btn_search.clicked.connect(self.get_address_request)
        self.list_address.itemDoubleClicked.connect(self.select_address_event)
        self.btn_input.clicked.connect(self.address_input_event)

    def _init_shadow(self):
        for c in [self.address_frame, self.list_frame, self.detail_frame]:
            shadow = QGraphicsDropShadowEffect(self)
            shadow.setBlurRadius(15)
            shadow.setXOffset(1)
            shadow.setYOffset(1)
            shadow.setColor(QColor(0, 0, 0, 35))
            c.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(15)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        shadow.setColor(QColor(0, 0, 0, 80))
        self.btn_input.setGraphicsEffect(shadow)

    ########################################################################################################

    # 주소 리스트 추가
    def get_address_request(self):
        if self.edt_address.text() == "": return
        self.list_address.clear()

        # 주소 양끝 공백제거 후 파싱
        txt = self.edt_address.text().strip()
        self.address = pars.OpenApiRequest.get_address(self.ADDRESS_API_KEY, txt)

        if self.address is None or self.address.empty:
            self.msg.show_msg(2000, 'center', "검색 결과가 없습니다")
            self.lb_hint_2.show()
            return

        # 메세지 숨기기
        self.lb_hint_2.hide()

        # 불러온 주소 리스트에 추가
        for i in range(len(self.address)):
            result = self.address.iloc[i]
            if result['건물명칭'] == "": bld_name = ""
            else: bld_name = " (%s)" % result['건물명칭']

            new = result['도로명주소'] + bld_name
            old = "%s %s %s %s" % (result['시도'], result['시군구'], result['읍면동'], result['번'])
            if result['지'] != "0": old = "%s-%s" % (old, result['지'])

            if len(new) > 33: new = new[0:33] + '···'

            custom_item = AddressListItem(new, old)
            item = QListWidgetItem(self.list_address)
            item.setSizeHint(custom_item.sizeHint())
            self.list_address.setItemWidget(item, custom_item)

    # 건물명칭(동) 콤보박스 추가
    def add_building_list(self, val):
        # 데이터가 없을 경우

        if val[0] is None: 
            self.msg.show_msg(2000, 'center', MsgContext.failed_in_search)
            return

        # 표제부 '주건축물'만 조회
        buildings = val[0][val[0]['주부속구분'] == '주건축물']
        self.total_buildings = val[1]

        # 주건축물 조회가 안 될 경우
        if buildings is None:
            self.msg.show_msg(2000, 'center', MsgContext.failed_to_search)
            return

        elif ('err' in buildings) or ('ERR' in buildings):
            self.msg.show_msg(2000, 'center', MsgContext.network_err % buildings)
            return

        # 건물 데이터 정렬
        buildings = buildings.sort_values(by=['동명칭'], axis=0)
        buildings.reset_index(drop=True, inplace=True)

        self.clear_cbx(True)

        # 콤보박스 아이템 추가
        for i in range(len(buildings)):
            result = buildings.iloc[i]
            if result['건물명칭'] == '':
                if self.select_address['건물명칭'] == '':
                    # 건물 이름, 동 이름이 없을 경우 (건물 명칭 없음 | 근린생활시설)
                    if result['동명칭'] == '': item = "건물 명칭 없음 | " + result['기타용도']

                    # 건물 이름만 없을 경우 (건물 명칭 없음 | 101동)
                    else: item = "%s동 | 건물 명칭 없음" % result['동명칭'].rstrip('동')
                else:
                    # 동 이름만 없을 경우 (다원빌 | 오피스텔)
                    if result['동명칭'] == '': item = "%s | %s" % (self.select_address['건물명칭'], result['기타용도'])

                    # 건물 이름, 동 이름이 모두 있는 경우 (다원빌 | A동)
                    else: item = "%s동 | %s" % (result['동명칭'].rstrip('동'), self.select_address['건물명칭'])
            else:
                # 동 이름만 없을 경우 (다원빌 | 오피스텔)
                if result['동명칭'] == '': item = "%s | %s" % (result['건물명칭'], result['기타용도'])

                # 건물 이름, 동 이름이 모두 있는 경우 (다원빌 | 101동)
                else: item = "%s동 | %s" % (result['동명칭'].rstrip('동'), result['건물명칭'])

            self.cbx_buildings.addItem(item)

        self.loading.hide_loading()
        self.buildings = buildings
        self.cbx_buildings.showPopup()

    # 집합건물(호) 콤보박스 추가
    def add_room_list(self, val):
        if val[0] is None:
            self.msg.show_msg(2000, 'center', MsgContext.failed_in_search)
            return

        if val[1] is not None: self.land = val[1]
        if val[2] is not None: self.owners = val[2]
        if val[3] is not None: self.prices = val[3]

        self.detail, self.land = val[0], val[1]
        self.exact_detail = details = sorted_rooms_len(get_exact_value(self.detail))

        for i in range(len(details)):
            ho = details.iloc[i]['호명칭'].rstrip('호')
            area = round(pd.to_numeric(details.iloc[i]['전용면적']), 2)
            item = '%s호 | %s m²' % (ho, str(area))

            self.cbx_rooms.addItem(item)
            self.detail_list.append(item)

        self.loading.hide_loading()
        self.cbx_rooms.showPopup()

    # 일반건물(층) 콤보박스 추가
    def add_layer_list(self, val):
        if val[0] is None:
            self.msg.show_msg(2000, 'center', MsgContext.failed_in_search)
            return
        if val[2] is not None: self.owners = val[2]
        if val[3] is not None: self.prices = val[3]

        self.detail, self.land = val[0], val[1]
        self.detail = sort_value_layer(val[0])

        self.clear_cbx(False)
        for i in range(len(self.detail)):
            layer = self.detail.loc[i]['층명칭']
            purps = self.detail.loc[i]['기타용도']
            item = '%s | %s' % (layer, purps)

            self.cbx_rooms.addItem(item)
            self.detail_list.append(item)

        self.loading.hide_loading()
        self.cbx_rooms.showPopup()

    ########################################################################################################

    # 주소 선택
    def select_address_event(self):
        self.select_address = self.address.iloc[self.list_address.currentRow()]
        self.binfo = dict(self.select_address)
        self.binfo['동명칭'] = ''

        self.binfo['동'] = self.binfo['동'].split(',')
        print(self.binfo)

        self.loading.show_loading()
        self.clear_cbx(True)

        # 표제부, 총괄표제부 파싱 쓰레드
        self.get_building_thread = pars.DataRequestThread(self.binfo, self.BULIDING_API_KEY, ['표제부', '총괄표제부'])
        self.get_building_thread.start()
        self.get_building_thread.threadEvent.searchDone.connect(self.add_building_list)

    # 건물명칭 콤보박스 선택
    def select_building_event(self):
        if self.cbx_buildings.currentIndex() == 0: return

        self.cbx_rooms.clear()
        self.cbx_rooms.addItem("( 상세주소 / 호 선택 )")

        self.loading.show_loading()
        self.select_building = self.buildings.iloc[self.cbx_buildings.currentIndex() - 1]

        # 대장구분 담기 (일반, 집합)
        self.binfo['타입'] = self.select_building['대장구분']

        # 일반일 경우
        if self.binfo['타입'] == '일반':
            self.get_building_thread = pars.DataRequestThread(self.binfo, self.BULIDING_API_KEY, ['층별', '토지', '소유자', '개별주택가격'])
            self.get_building_thread.start()
            self.get_building_thread.threadEvent.searchDone.connect(self.add_layer_list)

        # 건물 타입이 집합일 경우
        if self.binfo['타입'] == '집합':
            if len(self.buildings) > 1: self.binfo['동명칭'] = self.select_building['동명칭']
            self.get_building_thread = pars.DataRequestThread(self.binfo, self.BULIDING_API_KEY, ['전유부', '토지', '소유자', '공동주택가격'])
            self.get_building_thread.start()
            self.get_building_thread.threadEvent.searchDone.connect(self.add_room_list)

    # 상세주소 콤보박스 선택
    def select_room_event(self):
        if self.cbx_rooms.currentIndex() == 0:
            self.edt_result_address.clear()
            return

        select_index = self.cbx_rooms.currentIndex() - 1
        result = self.select_address

        old = "%s %s %s %s" % (result['시도'], result['시군구'], result['읍면동'], result['번'])
        if result['지'] != "0": old = "%s-%s" % (old, result['지'])

        # 일반일 경우
        if self.binfo['타입'] == '일반':
            self.select_detail = self.detail.iloc[select_index]  # 층별
            self.edt_result_address.setText("%s, %s" % (old, self.select_detail['층명칭']))

        # 집합일 경우
        elif self.binfo['타입'] == '집합':
            self.select_detail = self.exact_detail.iloc[select_index]
            dong = self.select_detail['동명칭'].rstrip('동')
            ho = self.select_detail['호명칭'].rstrip('호')

            if not dong: self.edt_result_address.setText("%s, %s호" % (old, ho))
            else: self.edt_result_address.setText("%s, %s동 %s호" % (old, dong, ho))

    # 소재지 입력 버튼
    def address_input_event(self):
        if self.edt_result_address.text() != "":
            self.select_index = self.cbx_rooms.currentIndex() - 1
            self.result = True
            self.close()

    ########################################################################################################

    # 클리어 함수
    def clear_cbx(self, all_clear):
        self.cbx_rooms.clear()
        self.cbx_rooms.addItem("( 상세주소 / 호 선택 )")
        self.edt_result_address.clear()

        if all_clear:
            self.detail_list.clear()
            self.cbx_buildings.clear()
            self.cbx_buildings.addItem("( 건물명칭 / 동 선택 )")

    # 메세지 함수
    def msg(self, ty, content):
        if ty == "기본": QMessageBox.about(self, self.windowTitle(), content)
        elif ty == "정보": QMessageBox.information(self, self.windowTitle(), content, QMessageBox.Ok)
        elif ty == "경고": QMessageBox.warning(self, self.windowTitle(), content, QMessageBox.Ok)
        elif ty == "위험": QMessageBox.critical(self, self.windowTitle(), content, QMessageBox.Ok)

    # 다이얼로그 엔터키 막기
    def keyPressEvent(self, event):
        if ((not event.modifiers() and
             event.key() == Qt.Key_Return) or
                (event.modifiers() == Qt.KeypadModifier)):
            event.accept()
        else: super(AddressDetails, self).keyPressEvent(event)
        
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
        y = round((self.height() / 2) - (self.msg_background.height() / 2)) - 90

        self.msg_background.move(x, y)

        effect = QGraphicsOpacityEffect(self.msg_background)
        self.msg_background.setGraphicsEffect(effect)

        self.anim = QPropertyAnimation(effect, b"opacity")
        self.anim.setStartValue(0)
        self.anim.setEndValue(1)
        self.anim.setDuration(100)
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

    ########################################################################################################


# 정확한 전유 호수 찾기
def get_exact_value(data):
    try:
        items = data
        # 전유 부분만
        items = items[items['전유공용구분'] == '전유']

        hos = set(items['호명칭'])

        if len(hos) == len(items):
            items.reset_index(drop=True, inplace=True)
            return items

        # 같은 층, 전유 항목이 2개 이상일 경우 면적 넓은 항목만 남기기
        items = items.astype({'전용면적': 'float'})

        for i in hos:
            res = items[items['호명칭'] == i]
            if len(res) == 1: continue
            items[items['호명칭'] == i] = res.nlargest(1, '전용면적', keep='first')

        items = items.astype({'전용면적': 'str'}).dropna(axis=0)
        items.reset_index(drop=True, inplace=True)
        return items

    except ValueError: return data


# 일반건물 층 정렬
def sort_value_layer(data):
    low = data[data['층구분'] == '지하'].sort_values(by=['층번호', '층명칭'], axis=0)
    mid = data[data['층구분'] == '지상'].sort_values(by=['층번호', '층명칭'], axis=0)
    top = data[data['층구분'] == '옥탑'].sort_values(by=['층번호', '층명칭'], axis=0)
    result = pd.concat([low, mid, top])
    result.reset_index(drop=True, inplace=True)
    return result


# 집합건물 호수 정렬
def sorted_rooms_len(data):
    data = data.copy()
    existing = data.sort_values(by=['층번호', '호명칭'], axis=0)
    existing.reset_index(drop=True, inplace=True)

    try:
        data['len'] = data.apply(lambda x: len(x['호명칭']), axis=1)

        name_len = list(set(data['len']))
        name_len.sort()

        # 명칭이 짧은 순서대로, 호수명대로 정렬
        rooms = []
        for i in name_len:
            value = data[data['len'] == i].sort_values(by=['층번호', '호명칭'], axis=0)
            rooms.append(value)
        result = pd.concat(rooms, ignore_index=True)

        low = result[result['층구분'] == '지하']
        top = result[result['층구분'] == '지상']

        result = pd.concat([low, top])
        result.reset_index(drop=True, inplace=True)
        return result

    except (ValueError, IndexError, TypeError) as e:
        print(e)
        return existing


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
                com2 = re.compile('(\w)(\d)(\d)(\d)')         # B101, 지101
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
        border_txt_old = """QLabel { font: 12px "웰컴체 Regular";
                        color: white;
                        border: none;
                        background: rgb(148,148,255);
                        padding-left: 5px;
                        padding-top: 3px;
                        border-radius: 5px;}"""

        border_txt_new = """QLabel { font: 12px "웰컴체 Regular";
                        color: white;
                        border: none;
                        background: rgb(148,148,255);
                        padding-left: 4px;
                        padding-top: 3px;
                        border-radius: 5px;}"""

        self.lb_old_icon = QLabel()
        self.lb_old_icon.setMaximumSize(44, 23)
        self.lb_old_icon.setText("지   번")
        self.lb_old_icon.setStyleSheet(border_txt_old)

        self.lb_old = QLabel()
        self.lb_old.setText(old)
        self.lb_old.setStyleSheet("""QLabel { font: 15px "웰컴체 Regular"; color: rgb(65,65,65); padding-top: 2px;}""")

        self.lb_new_icon = QLabel()
        self.lb_new_icon.setMaximumSize(44, 23)
        self.lb_new_icon.setText("도로명")
        self.lb_new_icon.setStyleSheet(border_txt_new)

        self.lb_new = QLabel()
        self.lb_new.setText(new)
        self.lb_new.setStyleSheet("""QLabel { font: 14px "웰컴체 Regular"; color: rgb(125,125,125); padding-left: 2px; padding-top: 2px;}""")

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

