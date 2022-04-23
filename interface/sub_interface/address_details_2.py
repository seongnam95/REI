import re
import sys
import pandas as pd
import requests
import json
import module.open_api_pars as pars

from PySide6.QtGui import QMovie, QIcon, QColor
from PySide6.QtWidgets import QDialog, QLabel, QListWidgetItem, QMessageBox, QWidget, \
    QGridLayout, QApplication, QGraphicsOpacityEffect, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt, QPropertyAnimation, QTimer, QSize, QEvent

from ui.dialog.ui_address import Ui_FindAddress


class MsgContext:
    no_set_msg = "< 집합 > 건물이 아닙니다. < 일반 > 건물로 조회됩니다."
    no_gen_msg = "< 일반 > 건물이 아닙니다. < 집합 > 건물로 조회됩니다."
    failed_to_search = "조회되지 않는 건물입니다. \n\n(신축 건물 또는 건축물대장에 등재되지 않은 건물은 \n조회되지 않을 수 있습니다.)"
    network_err = "데이터 서버가 원할하지 않습니다. \n불편을 드려 죄송합니다. 잠시 후 다시 시도해주세요.\n\n( 에러코드 : %s )"
    loading_msg = "건축물대장 정보를 불러오는 중입니다.\n통신 서버 및 네트워크 상태에 따라\n지연 될 수 있습니다."
    failed_in_search = "정보를 불러오는 중 에러가 발생했습니다. 관리자에게 문의해주세요."


class AddressDetails(QDialog, Ui_FindAddress):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        # OPEN API KEY
        self.ADDRESS_API_KEY = 'U01TX0FVVEgyMDIxMTIwMjEzNTc0MzExMTk4Mjc='

        # 변수 선언
        self.address, self.select_address = None, None    # 주소
        self.buildings, self.rooms = None, None

        self.s = requests.Session()
        self.headers = {
            "Referer": "https://cloud.eais.go.kr/moct/bci/aaa02/BCIAAA02L01",
            "Content-Type": "application/json;charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
        }

        self.msg_timer = False

        self._init_ui()
        self._init_interaction()
        self._init_shadow()

        self.show()

    # init UI
    def _init_ui(self):
        self.edt_address.setFocus()
        
        # 메세지
        self.msg_background = QLabel(self)
        self.msg_background.setAlignment(Qt.AlignCenter)
        self.msg_background.setStyleSheet("QLabel{background-color: rgba(0,0,0,150);"
                                          "font: 14px \uc6f0\ucef4\uccb4 Regular;"
                                          "color: white;"
                                          "padding-top: 3px;}")
        self.msg_background.hide()

        self.btn_search.setIcon(QIcon('../../data/img/button/search_icon.png'))
        self.btn_search.setIconSize(QSize(30, 30))

        # 로딩 구성
        self.movie = QMovie("../../data/img/animation/loading.gif")
        self.lb_back = QLabel(self)
        self.lb_loading = QLabel(self)
        self.lb_back_txt = QLabel(self)

        self.lb_back.hide()
        self.lb_back.setGeometry(0, 61, 461, 469)
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
        self.btn_search.clicked.connect(self.get_address_request)
        self.list_address.itemDoubleClicked.connect(self.select_address_event)
        self.btn_input.clicked.connect(self.address_input_event)

    def _init_shadow(self):
        for c in [self.address_frame, self.list_frame, self.detail_frame]:
            shadow = QGraphicsDropShadowEffect(self)
            shadow.setBlurRadius(30)
            shadow.setXOffset(3)
            shadow.setYOffset(3)
            shadow.setColor(QColor(0, 0, 0, 40))
            c.setGraphicsEffect(shadow)

    ########################################################################################################

    def get_address_request_re(self):
        if self.edt_address.text() == "": return

        self.list_address.clear()
        self.cbx_buildings.clear()
        self.cbx_rooms.clear()
        self.cbx_buildings.addItem("( 건물명칭 / 동 선택 )")
        self.cbx_rooms.addItem("( 상세주소 / 호 선택 )")

        txt = self.edt_address.text().strip()
        datas = {"query": {"multi_match": {"query": txt,
                                           "type": "cross_fields",
                                           "operator": "and",
                                           "fields": ["jibunAddr", "roadAddr^3"],
                                           "tie_breaker": 0.3}}, "size": 20}
        res = self.s.post('https://cloud.eais.go.kr/bldrgstmst/_search', headers=self.headers, json=datas)
        json_result = json.loads(res.text)['hits']

        self.lb_hint_2.hide()
        result = pd.DataFrame(columns=['주소', '도로명주소', 'PK'])
        for n, i in enumerate(json_result['hits']):
            old = i['_source']['roadAddr']
            new = i['_source']['jibunAddr']
            pk = i['_source']['mgmUpperBldrgstPk']

            result.loc[n] = {'주소': old, '도로명주소': new, 'ID': i['_id'], 'PK': pk}

            if len(old) > 28: old = old[0:28] + '···'
            if len(new) > 33: new = new[0:33] + '···'

            custom_item = AddressListItem(new, old)
            item = QListWidgetItem(self.list_address)
            item.setSizeHint(custom_item.sizeHint())
            self.list_address.setItemWidget(item, custom_item)

        self.address = result

    # 주소 리스트 추가
    def get_address_request(self):
        if self.edt_address.text() == "": return
        self.list_address.clear()

        # 주소 양끝 공백제거 후 파싱
        txt = self.edt_address.text().strip()
        self.address = pars.OpenApiRequest.get_address(self.ADDRESS_API_KEY, txt)

        # 주소 불러온 다음
        if self.address is None: self.info_msg(1, "검색 결과가 없습니다."); return
        if self.address.empty: self.info_msg(1, "검색 결과가 없습니다."); return

        self.lb_hint_2.hide()

        # 불러온 주소 리스트에 추가
        for i in range(len(self.address)):
            result = self.address.iloc[i]
            if result['건물명칭'] == "": bld_name = ""
            else: bld_name = " (%s)" % result['건물명칭']

            new = result['도로명주소'] + bld_name
            if result['지'] != '0': old = "%s %s %s %s-%s" % (result['시도'], result['시군구'], result['읍면동'], result['번'], result['지'])
            else: old = "%s %s %s %s" % (result['시도'], result['시군구'], result['읍면동'], result['번'])

            if len(new) > 33: new = new[0:33] + '···'

            custom_item = AddressListItem(new, old)
            item = QListWidgetItem(self.list_address)
            item.setSizeHint(custom_item.sizeHint())
            self.list_address.setItemWidget(item, custom_item)

    # 건물명칭(동) 콤보박스 추가
    def add_building_list(self, pk):

        datas = {"sort": [{"dongNm": "asc"}], "query": {"bool": {"filter": [{"term": {"mgmUpperBldrgstPk": pk}}]}},
                 "size": 100}
        res = self.s.post('https://cloud.eais.go.kr/bldrgsttitle/_search', headers=self.headers, json=datas)
        json_result = json.loads(res.text)['hits']

        result = pd.DataFrame(columns=['동명칭', 'PK'])
        for n, i in enumerate(json_result['hits']):
            result.loc[n] = {'동명칭': i['_source']['dongNm'], 'PK': i['_id']}

        result = result.sort_values(by=['동명칭'], axis=0)
        result.reset_index(drop=True, inplace=True)

        for i in range(len(result)):
            row = result.loc[i]
            self.cbx_buildings.addItem(row['동명칭'])

        self.cbx_buildings.showPopup()

    # 집합건물(호) 콤보박스 추가
    def add_room_list(self, val):
        if val[0] is None:
            self.msg('정보', MsgContext.failed_in_search)
            return
        if self.call_type == 1:
            if val[1] is not None: self.land = val[1]
            if val[2] is not None: self.owners = val[2]
            if val[3] is not None: self.prices = val[3]

        self.detail, self.land = val[0], val[1]
        self.exact_detail = details = sorted_rooms_len(get_exact_value(self.detail))

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
        if val[0] is None:
            self.msg("정보", MsgContext.failed_in_search)
            return

        if self.call_type == 1:
            if val[2] is not None: self.owners = val[2]
            if val[3] is not None: self.prices = val[3]

        self.detail, self.land = val[0], val[1]
        self.detail = sort_value_layer(val[0])

        self.clear_cbx(False)
        for i in range(len(self.detail)):
            layer = self.detail.loc[i]['층명칭']
            purps = self.detail.loc[i]['기타용도']
            area = round(pd.to_numeric(self.detail.iloc[i]['층면적']), 2)
            item = '%s | %s m² | %s' % (layer, str(area), purps)

            self.cbx_rooms.addItem(item)
            self.detail_list.append(item)

        self.loading(False)
        self.cbx_rooms.showPopup()

    ########################################################################################################

    # 주소 선택
    def select_address_event(self):
        self.select_address = self.address.iloc[self.list_address.currentRow()]
        result = self.select_address

        self.cbx_buildings.clear()
        self.cbx_buildings.addItem("( 건물명칭 / 동 선택 )")

        if result['지'] == '0': old = "%s %s %s %s" % (result['시도'], result['시군구'], result['읍면동'], result['번'])
        else: old = "%s %s %s %s-%s" % (result['시도'], result['시군구'], result['읍면동'], result['번'], result['지'])

        pk = self.get_address(old, result['도로명주소'])['ID']
        self.buildings = self.get_title(pk)

        if self.buildings.empty:
            self.cbx_buildings.setEnabled(False)
            self.cbx_rooms.setEnabled(False)
            self.edt_result_address.setText(result['도로명주소'])
            return

        for i in range(len(self.buildings)):
            row = self.buildings.loc[i]
            item = '%s (%s)' % (row['동명칭'], result['건물명칭']) if result['건물명칭'] else row['동명칭']
            self.cbx_buildings.addItem(item)

        self.cbx_buildings.showPopup()

    # 건물명칭 콤보박스 선택
    def select_building_event(self):
        if self.cbx_buildings.currentIndex() == 0: return
        building = self.buildings.iloc[self.cbx_buildings.currentIndex() - 1]

        self.cbx_rooms.clear()
        self.cbx_rooms.addItem("( 상세주소 / 호 선택 )")

        self.rooms = self.get_expos(building['PK'])
        for i in range(len(self.rooms)):
            row = self.rooms.loc[i]
            self.cbx_rooms.addItem(f"{row['호명칭']} 호")

        self.cbx_rooms.showPopup()

    # 상세주소 콤보박스 선택
    def select_room_event(self):
        if self.cbx_rooms.currentIndex() == 0:
            self.edt_result_address.clear()
            return
        if self.call_type == 0: self.ckb_part.setEnabled(True)

        select_index = self.cbx_rooms.currentIndex() - 1
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

            if not dong: self.edt_result_address.setText("%s, %s호" % (old, ho))
            else: self.edt_result_address.setText("%s, %s동 %s호" % (old, dong, ho))

    # 소재지 입력 버튼
    def address_input_event(self):
        if self.edt_result_address.text() != "":
            if self.ckb_part.isChecked(): self.binfo['일부'] = True
            self.select_index = self.cbx_rooms.currentIndex() - 1
            self.result = True
            self.hide()

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

    def get_address(self, old, new):
        datas = {"query": {"multi_match": {"query": new,
                                           "type": "cross_fields",
                                           "operator": "and",
                                           "fields": ["jibunAddr", "roadAddr^3"],
                                           "tie_breaker": 0.3}}, "size": 20}

        res = self.s.post('https://cloud.eais.go.kr/bldrgstmst/_search', headers=self.headers, json=datas)
        json_result = json.loads(res.text)['hits']

        for n, i in enumerate(json_result['hits']):
            res_old = i['_source']['jibunAddr']
            if old in res_old:
                info = i['_source']
                result = {'주소': info['jibunAddr'], '도로명주소': info['roadAddr'], 'ID': info['mgmUpperBldrgstPk'], 'PK': i['_id']}
                return result

    def get_title(self, pk):
        datas = {"sort": [{"dongNm": "asc"}], "query": {"bool": {"filter": [{"term": {"mgmUpperBldrgstPk": pk}}]}},
                 "size": 100}
        res = self.s.post('https://cloud.eais.go.kr/bldrgsttitle/_search', headers=self.headers, json=datas)
        json_result = json.loads(res.text)['hits']

        result = pd.DataFrame(columns=['동명칭', 'ID', 'PK'])

        for n, i in enumerate(json_result['hits']):
            result.loc[n] = {'동명칭': i['_source']['dongNm'], 'ID': i['_source']['mgmUpperBldrgstPk'], 'PK': i['_id']}

        result = result.sort_values(by=['동명칭'], axis=0)
        result.reset_index(drop=True, inplace=True)

        return result

    def get_expos(self, pk):
        datas = {"sort": [{"hoNm": "asc"}], "query": {"bool": {"filter": [{"term": {"mgmUpperBldrgstPk": pk}}]}},
                 "size": 200}
        res = self.s.post('https://cloud.eais.go.kr/bldrgstexpos/_search', headers=self.headers, json=datas)
        json_result = json.loads(res.text)['hits']

        result = pd.DataFrame(columns=['동명칭', '호명칭', 'PK'])

        for n, i in enumerate(json_result['hits']):
            info = i['_source']
            result.loc[n] = {'동명칭': info['dongNm'], '호명칭': info['hoNm'], 'PK': i['_id']}

        result['호명칭'] = pd.to_numeric(result['호명칭'])
        result = result.sort_values(by=['호명칭'], axis=0)
        result.reset_index(drop=True, inplace=True)

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

app = QApplication()
window = AddressDetails()
app.exec()

