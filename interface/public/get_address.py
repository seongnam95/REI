import sys

import pandas as pd
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon, QColor
from PySide6.QtWidgets import QDialog, QLabel, QListWidgetItem, QWidget, QGridLayout, QGraphicsDropShadowEffect

import data.sys_data as data
import module.open_api_pars as pars
from ui.custom import LoadingBox, BlackBoxMsg
from interface.public.resources.ui.ui_address import Ui_FindAddress


class MsgContext:
    no_set_msg = "< 집합 > 건물이 아닙니다. < 일반 > 건물로 조회됩니다."
    no_gen_msg = "< 일반 > 건물이 아닙니다. < 집합 > 건물로 조회됩니다."
    failed_to_search = "조회되지 않는 건물입니다. \n\n(신축 건물 또는 건축물대장에 등재되지 않은 건물은 \n조회되지 않을 수 있습니다.)"
    network_err = "데이터 서버가 원할하지 않습니다. \n불편을 드려 죄송합니다. 잠시 후 다시 시도해주세요.\n\n( 에러코드 : %s )"
    loading_msg = "건축물대장 정보를 불러오는 중입니다.\n통신 서버 및 네트워크 상태에 따라\n지연 될 수 있습니다."
    failed_in_search = "건축물 API 데이터가 조회되지 않습니다."


class AddressDetails(QDialog, Ui_FindAddress):
    def __init__(self, content=None):
        super().__init__()
        self.setupUi(self)

        # OPEN API KEY
        self.BULIDING_API_KEY = data.api_key['data']
        self.ADDRESS_API_KEY = data.api_key['address']
        self.DETAIL_ADDRESS_API_KEY = data.api_key['address_detail']

        # 변수 선언
        self.res_address, self.res_title, self.res_expos, self.res_exact_expos = None, None, None, None

        self.address, self.title, self.expos, self.expos_tot, self.total = None, None, None, None, None
        self.land, self.owners, self.prices = None, None, None

        self.get_buildings, self.get_building_info = None, None
        self.select_index, self.result = None, False
        self.expos_list = []

        self._init_ui()
        self._init_interaction()
        self._init_shadow()

        if content:
            self.edt_address.setText(content)
            self.get_address_request()

    # init UI
    def _init_ui(self):
        self.edt_address.setFocus()

        self.btn_search.setIcon(QIcon('../info/resources/img/search_icon.png'))
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
        self.res_address = pars.OpenApiRequest.get_address(self.ADDRESS_API_KEY, txt)

        if self.res_address is None or self.res_address.empty:
            self.msg.show_msg(2000, 'center', "검색 결과가 없습니다")
            self.lb_hint_2.show()
            return

        # 메세지 숨기기
        self.lb_hint_2.hide()

        # 불러온 주소 리스트에 추가
        for i in range(len(self.res_address)):
            result = self.res_address.iloc[i]
            if result['건물명칭'] == "": bld_name = ""
            else: bld_name = " (%s)" % result['건물명칭']

            new = result['도로명주소'] + bld_name
            bjr_nm = '' if result['법정리'] == '' else ' %s' % result['법정리']
            old = "%s %s %s%s %s" % (result['시도'], result['시군구'], result['읍면동'], bjr_nm, result['번'])
            if result['지'] != '0': old = "%s-%s" % (old, result['지'])

            if len(new) > 33: new = new[0:33] + '···'

            custom_item = AddressListItem(new, old)
            item = QListWidgetItem(self.list_address)
            item.setSizeHint(custom_item.sizeHint())
            self.list_address.setItemWidget(item, custom_item)

    # 건물명칭(동) 콤보박스 추가
    def add_building_list(self, val):
        self.loading.hide_loading()

        # 데이터가 없을 경우 리턴
        if val[0] is None: 
            self.msg.show_msg(2000, 'center', MsgContext.failed_in_search)
            return

        # 표제부 '주건축물'만 조회
        titles = val[0][val[0]['주부속구분'] == '주건축물']
        self.total = val[1]

        # 주건축물 조회가 안 될 경우
        if titles is None: self.msg.show_msg(2000, 'center', MsgContext.failed_to_search)
        elif ('err' in titles) or ('ERR' in titles): self.msg.show_msg(2000, 'center', MsgContext.network_err % titles)

        # 조회 되었을 경우
        else:
            # 건물 데이터 정렬
            self.res_title = titles.sort_values(by=['동명칭'], axis=0)
            self.res_title.reset_index(drop=True, inplace=True)
            titles = self.res_title

            self.clear_cbx(True)

            # 콤보박스 아이템 추가
            for i in range(len(titles)):
                result = titles.iloc[i]

                if result['동명칭'] != '': item = result['동명칭']
                elif result['건물명칭'] != '' and self.address['건물명칭'] != '': item = result['건물명칭']
                else: item = '동/건물 명칭 없음'

                self.cbx_buildings.addItem(item)

            # 동이 하나일 경우 '동 선택' 스킵
            if len(titles) == 1:
                self.cbx_buildings.setCurrentIndex(1)
                self.cbx_buildings.setEnabled(False)
                self.select_building_event()

            else:
                self.cbx_buildings.setEnabled(True)
                self.cbx_buildings.showPopup()

    # 집합건물(호) 콤보박스 추가
    def add_room_list(self, val):
        if val[0] is None: self.msg.show_msg(2000, 'center', MsgContext.failed_in_search)
        else:
            self.res_expos, self.land, self.owners, self.prices = val[0], val[1], val[2], val[3]
            self.res_exact_expos = res_exact_expos = sorted_rooms_len(get_exact_value(self.res_expos))
            print(self.owners)
            for i in range(len(res_exact_expos)):
                ho = res_exact_expos.iloc[i]['호명칭'].rstrip('호')
                area = round(pd.to_numeric(res_exact_expos.iloc[i]['전용면적']), 2)
                item = '%s호 (%s m²)' % (ho, str(area))

                self.cbx_rooms.addItem(item)
                self.expos_list.append(item)

            self.loading.hide_loading()
            self.cbx_rooms.showPopup()

    # 일반건물(층) 콤보박스 추가
    def add_layer_list(self, val):
        if val[0] is None: self.msg.show_msg(2000, 'center', MsgContext.failed_in_search)
        else:
            self.res_expos, self.land, self.owners, self.prices = val[0], val[1], val[2], val[3]
            self.res_expos = sort_value_layer(val[0])
            self.clear_cbx(False)
            for i in range(len(self.res_expos)):
                layer = self.res_expos.loc[i]['층명칭']
                purps = self.res_expos.loc[i]['기타용도']
                item = '%s | %s' % (layer, purps)

                self.cbx_rooms.addItem(item)
                self.expos_list.append(item)

            self.loading.hide_loading()
            self.cbx_rooms.showPopup()

    ########################################################################################################

    # 주소 선택
    def select_address_event(self):
        self.loading.show_loading()
        self.address = address = dict(self.res_address.iloc[self.list_address.currentRow()])

        # 구주소
        bjr_nm = '' if address['법정리'] == '' else ' %s' % address['법정리']
        old = "%s %s %s%s %s" % (address['시도'], address['시군구'], address['읍면동'], bjr_nm, address['번'])
        if address['지'] != '0': old = "%s-%s" % (old, address['지'])
        self.address['주소'] = old

        # UI 리셋
        self.edt_result_address.clear()
        self.cbx_buildings.clear()
        self.cbx_buildings.addItem("( 상세주소 / 동 선택 )")
        self.cbx_rooms.clear()
        self.cbx_rooms.addItem("( 상세주소 / 호 선택 )")

        # 표제부, 총괄표제부 파싱 쓰레드
        self.get_buildings = pars.DataRequestThread(self.address, self.BULIDING_API_KEY, ['표제부', '총괄표제부'])
        self.get_buildings.start()
        self.get_buildings.threadEvent.workerThreadDone.connect(self.add_building_list)

    # 건물명칭 콤보박스 선택
    def select_building_event(self):
        if self.cbx_buildings.currentIndex() == 0: return
        self.loading.show_loading()

        # UI 리셋
        self.edt_result_address.clear()
        self.cbx_rooms.clear()
        self.cbx_rooms.addItem("( 상세주소 / 호 선택 )")

        self.title = dict(self.res_title.iloc[self.cbx_buildings.currentIndex() - 1])

        # 일반일 경우
        if self.title['대장구분'] == '일반':
            self.get_building_info = pars.DataRequestThread(self.address, self.BULIDING_API_KEY, ['층별', '토지', '소유자', '개별주택가격'])
            self.get_building_info.start()
            self.get_building_info.threadEvent.workerThreadDone.connect(self.add_layer_list)

        # 건물 타입이 집합일 경우
        if self.title['대장구분'] == '집합':
            self.get_building_info = pars.DataRequestThread(self.address, self.BULIDING_API_KEY, ['전유부', '토지', '소유자', '공동주택가격'])
            self.get_building_info.start()
            self.get_building_info.threadEvent.workerThreadDone.connect(self.add_room_list)

    # 상세주소 콤보박스 선택
    def select_room_event(self):
        if self.cbx_rooms.currentIndex() == 0:
            self.edt_result_address.clear()
            return

        select_index = self.cbx_rooms.currentIndex() - 1

        # 일반일 경우
        if self.title['대장구분'] == '일반':
            self.expos = self.res_expos.iloc[select_index]  # 층별
            self.edt_result_address.setText("%s, %s" % (self.address['주소'], self.expos['층명칭']))

        # 집합일 경우
        elif self.title['대장구분'] == '집합':
            self.expos = self.res_exact_expos.iloc[select_index]
            dong = self.expos['동명칭'].rstrip('동')
            ho = self.expos['호명칭'].rstrip('호')
            self.expos_tot = self.res_expos[self.res_expos['호명칭'] == ho]

            if not dong: self.edt_result_address.setText("%s, %s호" % (self.address['주소'], ho))
            else: self.edt_result_address.setText("%s, %s동 %s호" % (self.address['주소'], dong, ho))

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
            self.expos_list.clear()
            self.cbx_buildings.clear()
            self.cbx_buildings.addItem("( 건물명칭 / 동 선택 )")

    # 다이얼로그 엔터키 막기
    def keyPressEvent(self, event):
        if ((not event.modifiers() and
             event.key() == Qt.Key_Return) or
                (event.modifiers() == Qt.KeypadModifier)):
            event.accept()
        else: super(AddressDetails, self).keyPressEvent(event)

    ########################################################################################################


# 정확한 전유 호수 찾기
def get_exact_value(target):
    try:
        items = target
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

    except ValueError: return target


# 일반건물 층 정렬
def sort_value_layer(target):
    low = target[target['층구분'] == '지하'].sort_values(by=['층번호', '층명칭'], axis=0)
    mid = target[target['층구분'] == '지상'].sort_values(by=['층번호', '층명칭'], axis=0)
    top = target[target['층구분'] == '옥탑'].sort_values(by=['층번호', '층명칭'], axis=0)
    result = pd.concat([low, mid, top])
    result.reset_index(drop=True, inplace=True)
    return result


# 집합건물 호수 정렬
def sorted_rooms_len(target):
    target = target.copy()
    existing = target.sort_values(by=['층번호', '호명칭'], axis=0)
    existing.reset_index(drop=True, inplace=True)

    try:
        target['len'] = target.apply(lambda x: len(x['호명칭']), axis=1)

        name_len = list(set(target['len']))
        name_len.sort()

        # 명칭이 짧은 순서대로, 호수명대로 정렬
        rooms = []
        for i in name_len:
            value = target[target['len'] == i].sort_values(by=['층번호', '호명칭'], axis=0)
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

