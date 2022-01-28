import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QIcon, QMovie
from PyQt5.QtCore import QSize, Qt
import pandas as pd
import module.open_api_pars as f


class InfoMain(QDialog, FROM_CLASS):
    def __init__(self):
        super().__init__()

        # 변수 선언
        self.dataKey = 'sfSPRX+xNEExRUqE4cdhNjBSk4uXIv8F1CfLen06hdPGn5cflLJqy/nxmh48uF8fvdGk68k6Z5jWsU1n6BeNPA=='
        self.jusoKey = 'devU01TX0FVVEgyMDIxMTAxMzEwNDgyMzExMTc1MjU='
        self.gisKey = '68506e6c486a736e35377562445658'

        self.data_juso = ""         # 주소
        self.pnu = ""               # PNU
        self.data_head = ""         # 표제부
        self.data_head_result = ""  # 단일 표제부
        self.data_head_all = None   # 총괄 표제부
        self.data_flrs = ""         # 층별 조회
        self.data_each = ""         # 전유부 (선택 호수)
        self.data_each_all = ""     # 전유부

        self.dl = []
        self.keypress = False
        self.detail = False
        self.detail_dong = ""

        # UI 부가 세팅
        self.setupUi(self)
        self.cbx_juso.setView(QListView())
        self.cbx_dong.setView(QListView())
        self.cbx_ho.setView(QListView())
        self.btn_search.setIcon(QIcon('./func/info/data/img/search.png'))
        self.btn_search.setIconSize(QSize(23, 23))
        self.btn_exit.setIcon(QIcon('./data/img/exit.png'))
        self.btn_exit.setIconSize(QSize(22, 22))
        self.btn_minimize.setIcon(QIcon('./data/img/minimize.png'))
        self.btn_minimize.setIconSize(QSize(12, 12))
        self.lb_jiji1.setWordWrap(True)
        self.lb_landetc1.setWordWrap(True)
        self.lb_landJiji1.setWordWrap(True)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        # 로딩
        self.movie = QMovie("./func/info/data/img/loading.gif")
        self.lb_loading = QLabel(self)
        self.lb_loading.setStyleSheet("background-color: rgb(0, 0, 0, 0);")
        self.lb_loading.resize(70, 100)
        self.lb_loading.move(155, 225)
        self.lb_loading.setHidden(True)
        self.lb_loading.setMovie(self.movie)
        self.lb_loading.setScaledContents(True)
        self.lb_loading_back = QLabel(self)
        self.lb_loading_back.setStyleSheet("background-color: rgb(0, 0, 0, 50);")
        self.lb_loading_back.resize(380, 551)
        self.lb_loading_back.setHidden(True)

        self.ui_interaction()   # UI 상호작용
        self.ui_reset_title('nomal')

        self.cbx_juso.setFocus()

    # UI 상호작용
    def ui_interaction(self):
        self.btn_search.clicked.connect(self.clicked_search_bt)
        self.btn_viol.clicked.connect(self.clicked_viol_bt)
        self.btn_details.clicked.connect(self.clicked_details_bt)
        self.btn_minimize.clicked.connect(self.clicked_mini)
        self.btn_exit.clicked.connect(self.clicked_exit_bt)
        self.cbx_juso.activated.connect(self.select_juso)
        self.cbx_dong.activated.connect(self.select_dong)
        self.cbx_ho.activated.connect(self.select_ho)

        edit = QLineEdit(self)
        self.cbx_juso.setLineEdit(edit)
        edit.returnPressed.connect(self.clicked_search_bt)

    def ui_reset_title(self, ty):
        if ty == 'detail':
            self.resize(711, 571)

        elif ty == 'nomal':
            self.resize(381, 571)

        self.lb_titlebar.resize(self.width(), self.height())
        self.line.resize(self.width() - 20, 20)
        exit_btn_x = self.line.x() + self.line.width() - self.btn_exit.width()
        self.btn_exit.move(exit_btn_x, 4)
        minimize_btn_x = exit_btn_x - self.btn_minimize.width() - 2
        self.btn_minimize.move(minimize_btn_x, 4)

    # UI 리셋
    def clear_label(self, ty):
        if ty == 0:
            self.cbx_dong.clear()
            self.cbx_dong.addItem(" ( 건물명칭 / 동 선택 )")
            self.cbx_ho.clear()
            self.cbx_ho.addItem(" ( 상세주소 / 호 선택 )")

        elif ty == 1:
            self.cbx_ho.clear()
            self.cbx_ho.addItem(" ( 상세주소 / 호 선택 )")

        self.lb_viol.setText('')
        self.lb_viol.setStyleSheet('')
        self.lb_juso.setText('')
        self.lb_etcpurps1.setText('')
        self.lb_totalarea1.setText('')
        self.lb_area1.setText('')
        self.lb_elvtcnt1.setText('')
        self.lb_grndflrcnt1.setText('')
        self.lb_oudr1.setText('')
        self.lb_name1.setText('')
        self.lb_hocnt1.setText('')
        self.lb_useaprday1.setText('')
        self.lb_price1.setText('')

        self.detail = False
        self.ui_reset_title('nomal')

    # 라벨에 정보 표시
    def set_label(self, dl, ty):
        if ty == 0:
            self.lb_juso.setText(dl['주소'].item())
            self.lb_etcpurps1.setText(dl['주용도'].item())
            self.lb_totalarea1.setText(dl['공용면적'].item())
            self.lb_area1.setText(dl['전용면적'].item())
            self.lb_elvtcnt1.setText(dl['승강기'].item())
            self.lb_grndflrcnt1.setText(dl['총층수'].item())
            self.lb_oudr1.setText(dl['주차장'].item())
            self.lb_name1.setText(str(dl['소유자'].item()))
            self.lb_hocnt1.setText(dl['호가구세대'].item())
            self.lb_useaprday1.setText(dl['사용승인일'].item())
            self.lb_price1.setText(dl['공시가격'].item())
            self.lb_price0.setText(dl['공시날짜'].item())

        if ty == 1:
            self.lb_etcStrct1.setText(dl['주구조'].item())
            self.lb_jiji1.setText(dl['지역지구'].item())
            self.lb_platArea1.setText(dl['대지면적'].item())
            self.lb_totArea1.setText(dl['연면적'].item())
            self.lb_archArea1.setText(dl['건축면적'].item())
            self.lb_heit1.setText(dl['높이'].item())
            self.lb_bcRat1.setText(dl['건폐율'].item())
            self.lb_vlRat1.setText(dl['용적률'].item())

            self.lb_indrAuto1.setText(dl['옥내자주식'].item())
            self.lb_indrMech1.setText(dl['옥내기계식'].item())
            self.lb_oudrAuto1.setText(dl['옥외자주식'].item())
            self.lb_oudrMech1.setText(dl['옥외기계식'].item())

            self.lb_landPrice1.setText(dl['공시지가'].item())
            self.lb_landJiji1.setText(dl['토지지역지구'].item())
            self.lb_landetc1.setText(dl['토지기타'].item())

    # 로딩
    def loading_img(self, run):
        if run:
            self.lb_loading.setHidden(False)
            self.lb_loading_back.setHidden(False)
            self.movie.start()
        else:
            self.lb_loading.setHidden(True)
            self.lb_loading_back.setHidden(True)
            self.movie.stop()

    # 검색 버튼 클릭
    def clicked_search_bt(self):
        # 주소 입력 안 했을 경우
        juso = self.cbx_juso.currentText().strip()
        if juso == "":
            self.msg('정보', '주소를 입력해주세요.    ')
            return

        self.clear_label(0)             # UI 모두 클리어
        self.pnu = ""
        self.data_head = ""
        self.data_head_all = None
        self.data_flrs = ""
        self.data_each_all = ""
        self.data_juso = ""
        self.keypress = True

        # 주소 API 조회
        dfjuso = self.data_juso = self.ld.get_address(juso, self.jusoKey)

        if len(dfjuso) == 0:  # 주소 검색 결과가 없을 시
            self.msg('정보', '검색 결과가 없습니다.    ')
            return

        self.cbx_juso.clear()

        for i in range(len(dfjuso)):
            resdfjuso = dfjuso.iloc[i]
            if resdfjuso['lnbrSlno'] == '0':
                if resdfjuso.bdNm == '':
                    js = resdfjuso['sggNm'] + ' ' + resdfjuso['emdNm'] + ' ' + resdfjuso['lnbrMnnm']
                else:
                    js = resdfjuso['sggNm'] + ' ' + resdfjuso['emdNm'] + ' ' + resdfjuso['lnbrMnnm'] + \
                         ' (' + resdfjuso.bdNm + ')'
                self.cbx_juso.addItem(js.strip())
            else:
                if resdfjuso.bdNm == '':
                    js = resdfjuso['sggNm'] + ' ' + resdfjuso['emdNm'] + ' ' + \
                         resdfjuso['lnbrMnnm'] + '-' + resdfjuso['lnbrSlno']
                else:
                    js = resdfjuso['sggNm'] + ' ' + resdfjuso['emdNm'] + ' ' + \
                         resdfjuso['lnbrMnnm'] + '-' + resdfjuso['lnbrSlno'] + ' (' + resdfjuso.bdNm + ')'
                self.cbx_juso.addItem(js.strip())

        # 주소지가 하나일 경우 자동 show
        if len(dfjuso) > 1: self.cbx_juso.showPopup()
        else: self.select_juso()

    # 주소가 있다면
    def select_juso(self):
        if not self.keypress: return
        self.keypress = False

        self.clear_label(0)             # UI 모두 클리어

        dfjuso = self.data_juso = self.data_juso.iloc[self.cbx_juso.currentIndex()]

        pnu = [dfjuso['admCd'], dfjuso['lnbrMnnm'].zfill(4), dfjuso['lnbrSlno'].zfill(4), dfjuso['rnMgtSn'],
               dfjuso['udrtYn'], dfjuso['buldMnnm'], dfjuso['buldSlno'], dfjuso['roadAddrPart1']]

        if self.rb_set.isChecked():
            pnu.append('1')
        elif self.rb_nomal.isChecked():
            pnu.append('0')
        self.pnu = pnu

        self.loading_img(True)

        self.th = f.DataRequestThread(pnu, ['표제부', '총괄표제부'])
        self.th.threadEvent.connect(self.input_dong)
        self.th.start()

    # '동' 콤보박스 추가
    def input_dong(self, val):
        pnu = self.pnu
        self.loading_img(False)
        if val[0] is None:
            self.msg('정보', "조회되지 않는 건물입니다. \n \n (건축물대장에 등재되지 않은 건물은 조회되지 않을 수 있습니다)")
            return
        elif ('err' in val[0]) or ('ERR' in val[0]):
            self.msg('오류', "데이터 서버가 원할하지 않습니다. \n불편을 드려 죄송합니다. 잠시 후 다시 시도해주세요. "
                           "\n\n ( 에러코드 : " + val[0] + " )")
            return

        df = val[0][val[0].mainAtchGbCdNm == '주건축물']
        self.data_head_all = val[1]
        if df is None:
            self.msg('정보', "조회되지 않는 건물입니다. \n \n (건축물대장에 등재되지 않은 건물은 조회되지 않을 수 있습니다)")
            return

        if pnu[8] == '0':       # 일반일 경우
            if len(df[df.regstrGbCdNm == '일반']) == 0:
                df = df[df.regstrGbCdNm == '집합']
                self.msg('정보', '< 일반 > 건물이 아닙니다. < 집합 > 건물로 조회됩니다.')

                pnu[8] = '1'
                self.rb_nomal.setChecked(False)
                self.rb_set.setChecked(True)
            else:
                df = df[df.regstrGbCdNm == '일반']

        elif pnu[8] == '1':     # 집합일 경우
            if len(df[df.regstrGbCdNm == '집합']) == 0:
                df = df[df.regstrGbCdNm == '일반']
                self.msg('정보', '< 집합 > 건물이 아닙니다. < 일반 > 건물로 조회됩니다.')

                pnu[8] = '0'
                self.rb_set.setChecked(False)
                self.rb_nomal.setChecked(True)
            else:
                df = df[df.regstrGbCdNm == '집합']

        df['convert_dong'] = df['dongNm']
        df['convert_dong'] = df['convert_dong'].str.rstrip('동')
        df = df.sort_values(by=['dongNm'], axis=0)
        df.reset_index(drop=True, inplace=True)

        self.data_head = df
        self.pnu = pnu

        for i in range(len(df)):
            res = df.iloc[i]
            if res.bldNm == '':
                if self.data_juso['bdNm'] == '':
                    if res.dongNm == '':                                               # 건물 이름, 동 이름이 없을 경우
                        self.cbx_dong.addItem("건물 명칭 없음 | " + res.etcPurps)
                    else:                                                               # 건물 이름만 없을 경우
                        self.cbx_dong.addItem("건물 명칭 없음 | " + res.convert_dong + "동")
                else:
                    if res.dongNm == '':                                            # 동 이름만 없을 경우
                        self.cbx_dong.addItem(self.data_juso.bdNm + " | " + res.etcPurps)
                    else:                                                           # 건물 이름, 동 이름이 모두 있는 경우
                        self.cbx_dong.addItem(self.data_juso.bdNm + " | " + res.convert_dong + "동")
            else:
                if res.dongNm == '':                                               # 동 이름만 없을 경우
                    self.cbx_dong.addItem(res.bldNm + " | " + res.etcPurps)
                else:                                                               # 건물 이름, 동 이름이 모두 있는 경우
                    self.cbx_dong.addItem(res.bldNm + " | " + res.convert_dong + "동")

        self.cbx_dong.showPopup()

    # 건물명칭 콤보박스 선택
    def select_dong(self):
        ind = self.cbx_dong.currentIndex() - 1
        if ind == -1: return

        self.clear_label(1)  # UI 클리어

        df = self.data_head_result = self.data_head.iloc[ind]
        self.loading_img(True)

        # 건물 타입이 집합일 경우
        if self.pnu[8] == '1':
            # 전유부 조회
            dong_count = len(self.data_head)
            self.th_ho = f.SetParsingThread(self.pnu, self.dataKey, dong_count, df.dongNm)
            self.th_ho.threadEvent.connect(self.show_ho_set)
            self.th_ho.start()

        # 일반일 경우
        if self.pnu[8] == '0':
            self.th_gen = f.GenParsingThread(self.pnu, self.dataKey, df)
            self.th_gen.threadEvent.connect(self.show_ho_gen)
            self.th_gen.start()

    # 집합 건물 '호' 콤보박스 추가
    def show_ho_set(self, df):
        self.data_each_all = df
        dfres = df[df['exposPubuseGbCdNm'].str.contains('전유')]
        dfres.reset_index(drop=True, inplace=True)
        self.data_each = dfres

        for i in range(len(dfres)):
            ho = dfres.iloc[i].hoNm.rstrip('호')
            purps = dfres.iloc[i].etcPurps
            area = round(pd.to_numeric(dfres.iloc[i].area), 2)
            self.cbx_ho.addItem(ho + '호 | ' + str(area) + ' m² | ' + purps)

        self.loading_img(False)
        self.cbx_ho.showPopup()

    # 일반 건물 '층' 콤보박스 추가
    def show_ho_gen(self, val):
        self.data_head_result = val[0]
        flrs = self.data_flrs = val[1]

        for i in range(len(flrs)):
            flr = flrs.loc[i].flrNoNm
            purps = flrs.loc[i].etcPurps
            area = round(pd.to_numeric(flrs.iloc[i].area), 2)
            self.cbx_ho.addItem(flr + ' | ' + str(area) + ' m² | ' + purps)
        self.loading_img(False)
        self.cbx_ho.showPopup()

    # 상세주소 콤보박스 선택
    def select_ho(self):
        if self.cbx_ho.currentIndex() == 0:
            return

        # 위반 건축물 표시 클리어
        self.lb_viol.setText('')
        self.lb_viol.setStyleSheet('')

        dl = pd.DataFrame(index=range(0, 1))

        index_ho = self.cbx_ho.currentIndex() - 1
        data_head = self.data_head_result           # 단일 표제부

        # 집합일 경우
        if self.pnu[8] == '1':
            data_each = self.data_each.iloc[index_ho]
            data_each_all = self.data_each_all              # 전유부
            dong = data_each.dongNm.rstrip('동')
            ho = data_each.hoNm.rstrip('호')

            if dong == '':
                juso = data_head.platPlc.split(' ')[1:]
                juso = " ".join(juso) + ' ' + ho + '호'

            else:
                juso = data_head.platPlc.split(' ')[1:]
                juso = " ".join(juso) + ' ' + dong + '동 ' + ho + '호'

            expos_public = data_each_all[data_each_all.convert_ho == data_each.sort_value_ho]         # 전유 + 공용
            total_area = str(round(pd.to_numeric(expos_public['area']).sum(), 2)) + ' m²'

            purps = data_each.etcPurps
            area = data_each.area + ' m²'
            jmgb = data_each.jm_gb_nm
            if jmgb == '':
                name = data_each.nm
            else:
                name = jmgb + ' | ' + data_each.nm

            if data_each.pblntfPc == '':
                price = '조회 결과 없음'
                price_day = '공 시 가 격'
            else:
                price = data_each.pblntfPc
                price = "{:,}".format(int(price))
                price = str(price + ' 원')
                day = data_each.lastUpdtDt.split('-')[0]
                price_day = '공 시 가 격 (' + day + '년)'

        # 일반일 경우
        elif self.pnu[8] == '0':
            flr = self.data_flrs.iloc[index_ho]     # 층별

            area = total_area = str(flr.area) + ' m²'
            juso = data_head.platPlc
            purps = data_head.etcPurps

            jmgb = data_head.jm_gb_nm
            if jmgb == '':
                name = data_head.nm
            else:
                name = jmgb + ' | ' + data_head.nm

            # 공시가격 있다면
            if not data_head.housePc == '':
                price = int(data_head.housePc)
                price = "{:,}".format(price)
                price = str(price + ' 원')
                day = data_head.lastUpdtDt.split('-')[0]
                price_day = '공 시 가 격 (' + day + '년)'
            else:
                price = '조회 결과 없음'
                price_day = '공 시 가 격'

        totelv = int(data_head.rideUseElvtCnt) + int(data_head.emgenUseElvtCnt)
        if totelv > 0: elv = '있음'
        elif totelv == 0: elv = '없음'

        # 총 층 수
        if data_head.ugrndFlrCnt == "0": ugr = ''
        else: ugr = '-'

        # 주차
        if self.data_head_all is None:
            indr_mech = int(data_head.indrMechUtcnt)
            oudr_mech = int(data_head.oudrMechUtcnt)
            indr_auto = int(data_head.indrAutoUtcnt)
            oudr_auto = int(data_head.oudrAutoUtcnt)
        else:
            dfres = self.data_head_all
            indr_mech = int(data_head.indrMechUtcnt)
            oudr_mech = int(data_head.oudrMechUtcnt)
            indr_auto = int(data_head.indrAutoUtcnt)
            oudr_auto = int(data_head.oudrAutoUtcnt)
            indr_mech = indr_mech + int(dfres.indrMechUtcnt.item())
            oudr_mech = oudr_mech + int(dfres.oudrMechUtcnt.item())
            indr_auto = indr_auto + int(dfres.indrAutoUtcnt.item())
            oudr_auto = oudr_auto + int(dfres.oudrAutoUtcnt.item())

        oudr = [indr_mech, oudr_mech, indr_auto, oudr_auto]

        # 호/가구/세대
        hocnt = str(data_head.hoCnt) + ' 호 | ' + str(data_head.fmlyCnt) + ' 가구 | ' + str(data_head.hhldCnt) + ' 세대'

        # 사용승인일
        day = str(data_head.useAprDay)
        day = day[:4] + '년 ' + day[4:6] + '월 ' + day[6:8] + '일'

        dl['주소'] = juso           # 일반) 주소
        dl['주용도'] = purps         # 일반) 주용도
        dl['공용면적'] = total_area              # 일반) 공용면적
        dl['전용면적'] = area              # 일반) 전용면적
        dl['공시가격'] = price
        dl['공시날짜'] = price_day
        dl['승강기'] = elv  # 승강기
        dl['총층수'] = ugr + data_head.ugrndFlrCnt + \
                      '층/' + data_head.grndFlrCnt + '층'
        dl['주차장'] = '총 ' + str(sum(oudr)) + ' 대'
        dl['옥내자주식'] = str(indr_auto) + ' 대'
        dl['옥내기계식'] = str(indr_mech) + ' 대'
        dl['옥외자주식'] = str(oudr_auto) + ' 대'
        dl['옥외기계식'] = str(oudr_mech) + ' 대'
        dl['소유자'] = name
        dl['호가구세대'] = hocnt
        dl['사용승인일'] = day
        dl['신주소'] = self.pnu[7] # 도로명 주소
        dl['주구조'] = data_head.strctCdNm             # 주구조
        dl['지역'] = '지역'                     # 지역
        dl['대지면적'] = data_head.platArea + ' m²'    # 대지면적
        dl['연면적'] = data_head.totArea + ' m²'       # 연면적
        dl['건축면적'] = data_head.archArea + ' m²'    # 건축면적
        dl['높이'] = data_head.heit + ' m'            # 높이
        dl['건폐율'] = data_head.bcRat + ' %'         # 건폐율
        dl['용적률'] = data_head.vlRat + ' %'         # 용적률

        self.dl = dl
        InfoMain.set_label(self, dl, 0)
        self.cbx_ho.setFocus()

    # 상세보기 버튼
    def clicked_details_bt(self):
        if not self.cbx_ho.currentText() == ' ( 상세주소 / 호 선택 )':
            if self.detail:
                self.ui_reset_title('nomal')
                self.detail = False
                return

            if self.cbx_dong.currentText() == self.detail_dong:
                self.ui_reset_title('detail')
                self.detail = True
                return

            self.loading_img(True)
            self.th = f.DataRequestThread(self.pnu, ['토지', '지역지구', '공시지가'])
            self.th.threadEvent.connect(self.input_detail)
            self.th.start()

    # 상세정보 불러오기
    def input_detail(self, val):
        dl = self.dl
        land = val[0]
        jiji = val[1]
        price = val[2]

        if jiji is None:
            dl['지역지구'] = '조회 결과 없음'
        else:
            dl['지역지구'] = ', '.join(jiji.etcJijigu)

        if land is None:
            dl['토지지역지구'] = '조회 결과 없음'
            dl['토지기타'] = '조회 결과 없음'
        else:
            land_jiji, etc = [], []
            for i in land.prposAreaDstrcCodeNm:
                if (i[-2:] == '지구') or (i[-2:] == '지역'): land_jiji.append(i)
                else: etc.append(i)
            dl['토지지역지구'] = ', '.join(land_jiji)
            dl['토지기타'] = ', '.join(etc)

        if price is not None:
            price = "{:,}".format(int(price.pblntfPclnd.item()))
            dl['공시지가'] = price + ' 원/㎡'
        else:
            dl['공시지가'] = '조회 결과 없음'

        self.set_label(dl, 1)
        self.ui_reset_title('detail')
        self.detail_dong = self.cbx_dong.currentText()
        self.detail = True
        self.loading_img(False)

