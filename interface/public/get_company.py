from urllib.parse import quote_plus, urlencode

import bs4
import pandas as pd
import requests
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import *

from interface.public.resources.ui.ui_company import Ui_Company
from module.open_api_pars import OpenApiRequest


class Company(QDialog, Ui_Company):
    def __init__(self, key, code):
        super().__init__()
        self.key, self.code = key, code
        self.company, self.data = None, []
        self.get_data = OpenApiRequest()
        self.init_ui()
        self.init_interaction()

        # UI 설정
    def init_ui(self):
        self.cbx_choise.setView(QListView())

        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)

        exit_btn_x = self.line.x() + self.line.width() - self.btn_exit.width()
        self.btn_exit.move(exit_btn_x, 4)
        self.btn_exit.setIcon(QIcon('../../static/img/button/exit.png'))
        self.btn_exit.setIconSize(QSize(22, 22))

        self.lb_notfind.hide()
        self.edt_find.setFocus()

    # UI 상호작용 컨넥트
    def init_interaction(self):
        self.edt_find.returnPressed.connect(self.btn_event)
        self.btn_find.clicked.connect(self.btn_event)
        # self.btn_exit.clicked.connect(self.exit_btn)
        self.list.itemDoubleClicked.connect(self.select_event)

    def btn_event(self):
        if self.edt_find.text() == "": return
        self.list.clear()

        if self.cbx_choise.currentText() == "중개사무소명":
            self.company = self.get_data.get_company(self.key, self.code, self.edt_find.text(), '')
        else:
            self.company = self.get_data.get_company(self.key, self.code, '', self.edt_find.text())
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

        result = pd.DataFrame(columns=colm)

        for i in range(len(colm)):
            for tag in xmlobj.find_all(pars[i]):
                rowlist.append(tag.text.strip())
            result[colm[i]] = rowlist
            rowlist = []

        return result
