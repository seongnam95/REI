import sys
import bs4
import requests
import pandas as pd
from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt, QSize
from urllib.parse import quote_plus, urlencode

ADDRESS_UI = uic.loadUiType('./data/uiDialog/ui_address.ui')[0]
COMPANY_UI = uic.loadUiType('./data/uiDialog/ui_find_company.ui')[0]


class Address(QDialog, ADDRESS_UI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.lb_notfind.hide()
        self.jusoKey = 'U01TX0FVVEgyMDIxMTIwMjEzNTc0MzExMTk4Mjc='
        self.address, self.data = "", []

        exit_btn_x = self.line.x() + self.line.width() - self.btn_exit.width()
        self.btn_exit.move(exit_btn_x, 4)
        self.btn_exit.setIcon(QIcon('../../data/img/button/exit.png'))
        self.btn_exit.setIconSize(QSize(22, 22))

        self.btn_exit.clicked.connect(self.exit_btn)
        self.btn_search.clicked.connect(self.btn_event)
        self.edt_address.returnPressed.connect(self.btn_event)
        self.list.itemDoubleClicked.connect(self.select_event)

    def select_event(self):
        result = self.address.iloc[self.list.currentRow()]

        old = result.siNm + " " + result.sggNm + " " + result.emdNm + " " + \
              result.bun + "-" + result.ji

        self.data.append(result.code)
        self.data.append(result.nm)
        self.data.append(result.new_address)
        self.data.append(old)

        self.close()

    def btn_event(self):
        if self.edt_address.text() == "": return
        self.list.clear()

        txt = self.edt_address.text().strip()
        self.address = self.address_pars(txt, self.jusoKey)

        self.lb_notfind.hide()
        if len(self.address) == 0:
            self.lb_notfind.show()

        for i in range(len(self.address)):
            result = self.address.iloc[i]

            if result.nm == "":
                nm = ""
            else:
                nm = " (" + result.nm + ")"

            new = result.new_address + nm
            old = result.siNm + " " + result.sggNm + " " + result.emdNm + " " + \
                  result.bun + "-" + result.ji

            custom_item = AddressListItem(new, old)
            item = QListWidgetItem(self.list)
            item.setSizeHint(custom_item.sizeHint())
            self.list.setItemWidget(item, custom_item)

    # 주소 조회
    @staticmethod
    def address_pars(juso, key):
        # 주소 조회 후 pnu 전역 변수에 저장)
        colm = ['code', 'under', 'bon', 'bu', 'nm',
                'new_address', 'siNm', 'sggNm', 'emdNm', 'bun', 'ji']
        pars = ['admCd', 'udrtYn', 'buldMnnm', 'buldSlno', 'bdNm',
                'roadAddrPart1', 'siNm', 'sggNm', 'emdNm', 'lnbrMnnm', 'lnbrSlno']

        xml_url = 'https://www.juso.go.kr/addrlink/addrLinkApi.do'
        query_params = '?' + urlencode(
            {
                quote_plus('confmKey'): key,
                quote_plus('currentPage'): '1',
                quote_plus('countPerPage'): '20',
                quote_plus('resultType'): 'xml',
                quote_plus('keyword'): juso
            }
        )
        response = requests.get(xml_url + query_params).text.encode('utf-8')
        xmlobj = bs4.BeautifulSoup(response, 'xml')
        rowlist = []

        df = pd.DataFrame(columns=colm)

        for i in range(len(colm)):
            for tag in xmlobj.find_all(pars[i]):
                rowlist.append(tag.text.strip())
            df[colm[i]] = rowlist
            rowlist = []

        try:  # 중복 주소지 찾으면 테스트 해야함
            if '-' in juso:
                res = juso.split(' ')[-1]
                res = res.split('-')
                redf = df[(df.lnbrMnnm == res[0]) & (df.lnbrSlno == res[1])]
                if len(redf) == 0:
                    return df
                return redf
        except:
            return df
        return df

    def exit_btn(self):
        self.close()

    # 폼 이동 이벤트
    def mousePressEvent(self, event):
        if event.btn_modify() == Qt.LeftButton:
            self.offset = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        try:
            desktop_height = QDesktopWidget().availableGeometry().height()
            desktop_width = QDesktopWidget().availableGeometry().width()

            if self.offset is not None and event.buttons() == Qt.LeftButton:
                pos = self.pos() + event.pos() - self.offset

                # 우측
                if (desktop_width - self.width() + 15) > pos.x() > (desktop_width - self.width() - 15):
                    if pos.y() < 10:
                        self.move(desktop_width - self.width(), 0)
                    elif (desktop_height - self.height() + 15) > pos.y() > (desktop_height - self.height() - 15):
                        self.move(desktop_width - self.width(), desktop_height - self.height())
                    else:
                        self.move(desktop_width - self.width(), pos.y())
                    return

                # 좌측
                if -15 < pos.x() < 15:
                    if pos.y() < 10:
                        self.move(0, 0)
                    elif (desktop_height - self.height() + 15) > pos.y() > (desktop_height - self.height() - 15):
                        self.move(0, desktop_height - self.height())
                    else:
                        self.move(0, pos.y())
                    return

                # 상단
                if (desktop_height - self.height() + 15) > pos.y() > (desktop_height - self.height() - 15):
                    self.move(pos.x(), desktop_height - self.height())
                    return

                # 하단
                if pos.y() < 15:
                    self.move(pos.x(), 0)
                    return

                self.move(pos)
            else:
                super().mouseMoveEvent(event)
        except AttributeError:
            return

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)

    # 다이얼로그 엔터키 막기
    def keyPressEvent(self, event):
        if ((not event.modifiers() and
             event.key() == Qt.Key_Return) or
                (event.modifiers() == Qt.KeypadModifier)):
            event.accept()
        else:
            super(Address, self).keyPressEvent(event)

    # 예외 오류 처리
    def my_exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)

    sys._excepthook = sys.excepthook
    sys.excepthook = my_exception_hook


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


class Company(QDialog, COMPANY_UI):
    def __init__(self, key, code):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.key, self.code, self.company, self.data = key, code, '', []

        self.lb_notfind.hide()
        self.edt_find.setFocus()
        self.cbx_choise.setView(QListView())

        exit_btn_x = self.line.x() + self.line.width() - self.btn_exit.width()
        self.btn_exit.move(exit_btn_x, 4)
        self.btn_exit.setIcon(QIcon('../../data/img/button/exit.png'))
        self.btn_exit.setIconSize(QSize(22, 22))

        self.edt_find.returnPressed.connect(self.btn_event)
        self.btn_find.clicked.connect(self.btn_event)
        self.btn_exit.clicked.connect(self.exit_btn)
        self.list.itemDoubleClicked.connect(self.select_event)

    def btn_event(self):
        if self.edt_find.text() == "": return
        self.list.clear()

        colm = ['code', 'number', 'company', 'name', 'bosscode', 'rank']
        pars = ['ldCode', 'jurirno', 'bsnmCmpnm', 'brkrNm', 'ofcpsSeCodeNm', 'brkrAsortCodeNm']

        if self.cbx_choise.currentText() == "중개사무소명":
            self.company = self.company_pars(self.key, self.code, colm, pars, self.edt_find.text(), '')
        else:
            self.company = self.company_pars(self.key, self.code, colm, pars, '', self.edt_find.text())
        self.company = self.company[self.company['bosscode'] == '대표']

        self.lb_notfind.hide()
        if len(self.company) == 0:
            self.lb_notfind.show()

        for i in range(len(self.company)):
            result = self.company.iloc[i]

            custom_item = CompanyListItem(result['company'], result['rank'], result['name'],
                                          result['bosscode'], result['number'])

            item = QListWidgetItem(self.list)
            item.setSizeHint(custom_item.sizeHint())
            self.list.setItemWidget(item, custom_item)

    def select_event(self):
        result = self.company.iloc[self.list.currentRow()]

        self.data.append(result['code'])
        self.data.append(result['number'])
        self.data.append(result['company'])
        self.data.append(result['name'])
        self.data.append(result['bosscode'])
        self.data.append(result['rank'])

        self.close()

    @staticmethod
    def company_pars(key, code, colm, pars, company, boss):

        xml_url = 'http://openapi.nsdi.go.kr/nsdi/EstateBrkpgService/attr/getEBBrokerInfo'
        query_params = '?' + urlencode(
            {
                quote_plus('authkey'): key,
                quote_plus('ldCode'): code,
                quote_plus('bsnmCmpnm'): company,
                quote_plus('brkrNm'): boss,
                quote_plus('format'): 'xml',
                quote_plus('numOfRows'): '100'
            }
        )
        response = requests.get(xml_url + query_params).text.encode('utf-8')
        xmlobj = bs4.BeautifulSoup(response, 'xml')
        rowlist = []

        df = pd.DataFrame(columns=colm)

        for i in range(len(colm)):
            for tag in xmlobj.find_all(pars[i]):
                rowlist.append(tag.text.strip())
            df[colm[i]] = rowlist
            rowlist = []

        return df

    def exit_btn(self):
        self.close()

    # 폼 이동 이벤트
    def mousePressEvent(self, event):
        if event.btn_modify() == Qt.LeftButton:
            self.offset = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        try:
            desktop_height = QDesktopWidget().availableGeometry().height()
            desktop_width = QDesktopWidget().availableGeometry().width()

            if self.offset is not None and event.buttons() == Qt.LeftButton:
                pos = self.pos() + event.pos() - self.offset

                # 우측
                if (desktop_width - self.width() + 15) > pos.x() > (desktop_width - self.width() - 15):
                    if pos.y() < 10:
                        self.move(desktop_width - self.width(), 0)
                    elif (desktop_height - self.height() + 15) > pos.y() > (desktop_height - self.height() - 15):
                        self.move(desktop_width - self.width(), desktop_height - self.height())
                    else:
                        self.move(desktop_width - self.width(), pos.y())
                    return

                # 좌측
                if -15 < pos.x() < 15:
                    if pos.y() < 10:
                        self.move(0, 0)
                    elif (desktop_height - self.height() + 15) > pos.y() > (desktop_height - self.height() - 15):
                        self.move(0, desktop_height - self.height())
                    else:
                        self.move(0, pos.y())
                    return

                # 상단
                if (desktop_height - self.height() + 15) > pos.y() > (desktop_height - self.height() - 15):
                    self.move(pos.x(), desktop_height - self.height())
                    return

                # 하단
                if pos.y() < 15:
                    self.move(pos.x(), 0)
                    return

                self.move(pos)
            else:
                super().mouseMoveEvent(event)
        except AttributeError:
            return

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)

    # 다이얼로그 엔터키 막기
    def keyPressEvent(self, event):
        if ((not event.modifiers() and
             event.key() == Qt.Key_Return) or
                (event.modifiers() == Qt.KeypadModifier)):
            event.accept()
        else:
            super(Company, self).keyPressEvent(event)

    # 예외 오류 처리
    def my_exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)

    sys._excepthook = sys.excepthook
    sys.excepthook = my_exception_hook


class CompanyListItem(QWidget):
    def __init__(self, company, user_rank, user_name, bosscode, company_number):
        super(CompanyListItem, self).__init__()

        self.lb_boss = QLabel()
        self.lb_boss.setText(bosscode)
        self.lb_boss.setStyleSheet("""QLabel { font: 13px "웰컴체 Regular"; 
                                               color: white; 
                                               padding-left: 5px;
                                               padding-top: 3px;}""")

        self.lb_company = QLabel()
        self.lb_company.setAlignment(Qt.AlignCenter)
        self.lb_company.setText(company)
        self.lb_company.setStyleSheet("""QLabel { font: 16px "웰컴체 Regular";
                                         color: white;
                                         border: 0px;
                                         background-color: rgb(42, 142, 209);
                                         padding: 5px 3px 3px 3px;}""")

        self.lb_name = QLabel()
        self.lb_name.setAlignment(Qt.AlignCenter)
        self.lb_name.setText(user_name)
        self.lb_name.setStyleSheet("""QLabel { font: 16px "웰컴체 Regular"; 
                                               color: rgb(24, 42, 60); 
                                               padding-top: 5px;
                                               padding-left: 5px;}""")
        self.lb_rank = QLabel()
        self.lb_rank.setAlignment(Qt.AlignCenter)
        self.lb_rank.setText(user_rank)
        self.lb_rank.setStyleSheet("""QLabel { font: 14px "웰컴체 Regular"; 
                                               color: rgb(44, 62, 80); 
                                               padding-left: 30px;
                                               padding-top: 5px;}""")

        self.lb_number = QLabel()
        self.lb_number.setText(company_number)
        self.lb_number.setStyleSheet("""QLabel { font: 14px "웰컴체 Regular"; 
                                               color: rgb(44, 62, 80); 
                                               padding-left: 30px;
                                               padding-top: 5px;}""")
        self.set_ui()

    def set_ui(self):
        grid_box = QGridLayout()
        grid_box.addWidget(self.lb_company, 0, 0, 1, 4)
        grid_box.addWidget(self.lb_boss, 0, 0)
        grid_box.addWidget(self.lb_name, 1, 0, 1, 1)
        grid_box.addWidget(self.lb_rank, 1, 1, 1, 1)
        grid_box.addWidget(self.lb_number, 1, 2, 1, 1)

        self.setLayout(grid_box)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Company()
    form.show()
    app.exec_()
