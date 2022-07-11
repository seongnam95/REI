import sys

import numpy as np
import pandas as pd
import module.mysql as sql

from PySide6.QtCore import Qt, QSize, QObject, QEvent
from PySide6.QtGui import QColor, QIcon
from PySide6.QtWidgets import QWidget, QDialog, QLabel, QHBoxLayout, QListWidgetItem, QGraphicsDropShadowEffect, \
    QMessageBox, QApplication

# from hanspell import spell_checker
from ui.custom.BlackBoxMsg import BoxMessage
from ui.custom.TextEditWidget import TextEditWidget
from ui.dialog.ui_agr_editor import Ui_AgrEditor


class AgrEditor(QDialog, Ui_AgrEditor):
    def __init__(self, agr, kind):
        super().__init__()
        self.setupUi(self)

        # 변수 선언
        self.agr, self.kind, self.response = agr, kind, None
        self.user_pk = '2207112600001'
        self.agr = sql.get_agrs(self.user_pk)

        self.edit_category, self.new_category, self.remove_category = pd.DataFrame, [], []
        self.category, self.title, self.last_txt = str, str, str
        self.contents = pd.DataFrame(columns=['title', 'title_num', 'content'])

        self.conn = sql.connection()
        self.cur = self.conn.cursor()

        # init
        self._init_ui()
        self._init_interaction()

        self.show_shadows()
        self.show()

        self.load_category()

    def _init_ui(self):
        self.edt_agr.setEnabled(False)

        self.msg = BoxMessage(self)

        self.text_edit_widget = TextEditWidget(self.text_frame, 610, self.edt_agr)
        self.text_edit_widget.move(20, 20)

        # 편집기 세팅
        self.editor_back.resize(self.width(), self.height())
        self.editor_back.move(0, 0)

        x = (self.width() / 2) - (self.editor_frame.width() / 2)
        y = (self.height() / 2) - (self.editor_frame.height() / 2)
        self.editor_frame.move(x, y)

        self.editor_back.hide()

        edit_icon = QIcon('../../static/img/button/plus_icon.png')
        self.btn_add_category.setIcon(edit_icon)
        self.btn_add_category.setIconSize(QSize(21, 21))

        edit_icon = QIcon('../../static/img/button/trash_icon.png')
        self.btn_del_category.setIcon(edit_icon)
        self.btn_del_category.setIconSize(QSize(19, 19))

        edit_icon = QIcon('../../static/img/button/plus_icon.png')
        self.btn_add_title.setIcon(edit_icon)
        self.btn_add_title.setIconSize(QSize(21, 21))

        edit_icon = QIcon('../../static/img/button/trash_icon.png')
        self.btn_del_title.setIcon(edit_icon)
        self.btn_del_title.setIconSize(QSize(19, 19))

    def _init_interaction(self):
        self.lst_category.itemClicked.connect(self.load_title)
        self.lst_title.itemClicked.connect(self.load_content)
        self.edt_agr.installEventFilter(self)

        # 메인
        self.btn_del_category.clicked.connect(lambda: self.delete_item('category'))
        self.btn_add_category.clicked.connect(lambda: self.show_item_editor('category', 'add'))
        self.lst_category.itemDoubleClicked.connect(lambda: self.show_item_editor('category', 'edit'))

        self.btn_del_title.clicked.connect(lambda: self.delete_item('title'))
        self.btn_add_title.clicked.connect(lambda: self.show_item_editor('title', 'add'))
        self.lst_title.itemDoubleClicked.connect(lambda: self.show_item_editor('title', 'edit'))

        self.btn_save.clicked.connect(self.clicked_save_btn)

        # 항목 편집기
        self.btn_editor_cancel.clicked.connect(self.hide_item_editor)
        self.btn_editor_save.clicked.connect(self.add_item)

    ## 상호작용 이벤트
    ############################################################################

    # 저장 버튼 클릭
    def clicked_save_btn(self):
        for row in self.agr.values:
            if '' in row:
                category = row[2]
                self.msg.show_msg(2000, 'center', f"'{category}' 카테고리가 비어있습니다.")
                return
        print(self.agr)
        sql.set_agrs(self.agr)

    ## 로드
    ############################################################################

    # 카테고리 로드
    def load_category(self, row=None):
        self.lst_category.clear()
        self.lst_title.clear()

        category = self.agr['category'].values.tolist()
        category = list(dict.fromkeys(category))

        for i in category:
            category_item = CategoryItem(i, self.lst_category)
            item = QListWidgetItem()
            item.setSizeHint(QSize(category_item.width(), 30))
            self.lst_category.addItem(item)
            self.lst_category.setItemWidget(item, category_item)

        if row == int: self.lst_category.setCurrentRow(row)

    # 타이틀 로드
    def load_title(self, row=None):
        self.lst_title.clear()
        self.edt_agr.clear()
        if self.edt_agr.isEnabled(): self.edt_agr.setEnabled(False)

        item = self.lst_category.item(self.lst_category.currentRow())
        item_widget = self.lst_category.itemWidget(item)
        self.category = item_widget.lb_category.text()

        titles = self.agr[self.agr['category'] == self.category]
        titles = titles.sort_values(['titleNum'], ascending=True)
        titles = titles.reset_index(drop=True)

        title = titles['title'].values.tolist()
        title = list(dict.fromkeys(title))

        for i in title:
            if i:
                category_item = CategoryItem(i, self.lst_title)
                item = QListWidgetItem()
                item.setSizeHint(QSize(category_item.width(), 30))
                self.lst_title.addItem(item)
                self.lst_title.setItemWidget(item, category_item)

        if row == int:
            self.lst_title.setCurrentRow(row)

    # 특약사항 로드
    def load_content(self):
        self.edt_agr.clear()
        self.last_txt = str

        if not self.edt_agr.isEnabled(): self.edt_agr.setEnabled(True)

        item = self.lst_title.item(self.lst_title.currentRow())
        item_widget = self.lst_title.itemWidget(item)
        self.title = item_widget.lb_category.text()

        category = self.agr[self.agr['category'] == self.category]
        content = category[category['title'] == self.title]['content']
        if content.iloc[0]:
            self.edt_agr.insertHtml(content.iloc[0])

        self.edt_agr.setFocus()

    ## 편집
    ############################################################################

    def changed_agr(self):
        if self.last_txt != self.edt_agr.toHtml():
            self.last_txt = self.edt_agr.toHtml()

            idx = self.agr.index[(self.agr['category'] == self.category) & (self.agr['title'] == self.title)]
            self.agr.loc[idx, 'content'] = self.last_txt

    # 편집기 활성화
    def show_item_editor(self, form, kind):
        if form == 'category':
            if kind == 'add':
                self.editor_title.setText('카테고리 추가')
                self.btn_editor_save.setText('추가')

            elif kind == 'edit':
                self.editor_title.setText('카테고리 편집')
                self.btn_editor_save.setText('저장')

                # 선택한 값 텍스트에 불러오기
                item = self.lst_category.item(self.lst_category.currentRow())
                item_widget = self.lst_category.itemWidget(item)
                self.edt_name.setText(item_widget.lb_category.text())

        elif form == 'title':
            if self.lst_category.currentRow() == -1: return

            if kind == 'add':
                self.editor_title.setText('특약사항 추가')
                self.btn_editor_save.setText('추가')

            elif kind == 'edit':
                self.editor_title.setText('특약사항 제목 편집')
                self.btn_editor_save.setText('저장')

                # 선택한 값 텍스트에 불러오기
                item = self.lst_title.item(self.lst_title.currentRow())
                item_widget = self.lst_title.itemWidget(item)
                self.edt_name.setText(item_widget.lb_category.text())

        self.hide_shadows()
        self.editor_back.show()
        self.edt_name.clear()

        self.edt_name.setFocus()

    # 편집기 비활성화
    def hide_item_editor(self):
        self.show_shadows()
        self.editor_back.hide()
        self.new_category.clear()

    # 아이템 추가
    def add_item(self):
        name = self.edt_name.text().strip()

        # 카테고리 추가
        if '카테고리' in self.editor_title.text():

            # 카테고리 중복 체크
            for i in range(self.lst_category.count()):
                item = self.lst_category.item(i)
                category = self.lst_category.itemWidget(item).lb_category.text()
                if name == category:
                    self.msg.show_msg(2000, 'center', '이미 존재하는 카테고리입니다.')
                    return

            # 데이터프레임 생성, 기존 데이터와 합치기
            new_category = {'userPk': self.user_pk,
                            'category': [name],
                            'categoryNum': self.lst_category.count()}

            new_df = pd.DataFrame(new_category)

            self.agr = pd.concat([self.agr, new_df])
            self.agr = self.agr.replace({np.nan: None})
            self.agr.reset_index(drop=True, inplace=True)

            category_item = CategoryItem(name, self.lst_category)
            item = QListWidgetItem()
            item.setSizeHint(QSize(category_item.width(), 30))
            self.lst_category.addItem(item)
            self.lst_category.setItemWidget(item, category_item)

            self.lst_category.setCurrentRow(self.lst_category.count() - 1)
            self.load_title()

        # 특약사항 추가
        else:

            # 특약사항 중복 체크
            for i in range(self.lst_title.count()):
                item = self.lst_title.item(i)
                title = self.lst_title.itemWidget(item).lb_category.text()
                if name == title:
                    self.msg.show_msg(2000, 'center', '이미 존재하는 특약사항입니다.')
                    return

            # 현재 카테고리
            crt_category = self.agr[self.agr['category'] == self.category]

            # 데이터프레임 생성, 기존 데이터와 합치기
            num = crt_category['categoryNum'].iloc[0]

            # 카테고리만 있을 경우
            if len(crt_category) == 1:
                if not crt_category['title'].iloc[0]:
                    idx = self.agr.index[self.agr['category'] == self.category]
                    self.agr = self.agr.drop(index=idx, axis=0)

            new_title = {'userPk': [self.user_pk], 'category': [self.category], 'categoryNum': [num],
                         'title': [name], 'titleNum': [self.lst_title.count()]}
            new_df = pd.DataFrame(new_title)
            self.agr = pd.concat([self.agr, new_df])
            self.agr = self.agr.replace({np.nan: None})
            self.agr.reset_index(drop=True, inplace=True)

            category_item = CategoryItem(name, self.lst_title)
            item = QListWidgetItem()
            item.setSizeHint(QSize(category_item.width(), 30))
            self.lst_title.addItem(item)
            self.lst_title.setItemWidget(item, category_item)

            self.lst_title.setCurrentRow(self.lst_title.count() - 1)

            self.load_content()

        self.hide_item_editor()

    # 아이템 삭제
    def delete_item(self, form):
        if form == 'category':
            row = self.lst_category.currentRow()
            if row != -1:
                res = self.msg_box('del_category')
                if res == 0:

                    # DB 삭제
                    sql.del_agrs([self.user_pk, self.category])

                    # 데이터프레임, 리스트 삭제
                    idx = self.agr.index[self.agr['category'] == self.category]
                    self.agr = self.agr.drop(idx, axis=0)
                    self.agr.reset_index(drop=True, inplace=True)

                    self.lst_category.takeItem(row)

        elif form == 'title':
            row = self.lst_title.currentRow()
            if row != -1:
                res = self.msg_box('del_title')
                if res == 0:

                    # 특약사항 삭제
                    idx = self.agr.index[(self.agr['category'] == self.category) & (self.agr['title'] == self.title)]
                    pk = self.agr[(self.agr['category'] == self.category) & (self.agr['title'] == self.title)]

                    sql.del_agrs(pk.iloc[0]['pk'])
                    self.agr = self.agr.drop(idx, axis=0)

                    self.lst_title.takeItem(row)

    ## 쉐도우 설정
    ############################################################################

    def show_shadows(self):
        frame_list = [self.category_frame, self.title_frame, self.text_frame]
        for child in frame_list:
            shadow = QGraphicsDropShadowEffect(self)
            shadow.setBlurRadius(15)
            shadow.setXOffset(1)
            shadow.setYOffset(1)
            shadow.setColor(QColor(0, 0, 0, 35))
            child.setGraphicsEffect(shadow)

    def hide_shadows(self):
        frame_list = [self.category_frame, self.title_frame, self.text_frame]
        for child in frame_list:
            shadow = QGraphicsDropShadowEffect(self)
            shadow.setEnabled(False)
            child.setGraphicsEffect(shadow)

    ############################################################################

    def eventFilter(self, widget, event):
        if event.type() == QEvent.FocusOut:
            self.changed_agr()
            return False
        else:
            return False

    # 다이얼로그 엔터키 막기
    def keyPressEvent(self, event):
        if ((not event.modifiers() and
             event.key() == Qt.Key_Return) or
                (event.modifiers() == Qt.KeypadModifier)):
            event.accept()
        else: super(AgrEditor, self).keyPressEvent(event)

    # 메세지 박스
    def msg_box(self, msg):
        msg_titles = {'del_category': '카테고리를 삭제하시겠습니까?',
                      'del_title': '특약사항을 삭제하시겠습니까?'}
        msg_context = {'del_category': '해당 카테고리에 있는 모든 특약사항이 모두 삭제됩니다.',
                       'del_title': ''}

        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("정보")  # 메세지창의 상단 제목
        msg_box.setIcon(QMessageBox.Information)  # 메세지창 내부에 표시될 아이콘
        msg_box.setText(msg_titles[msg])  # 메세지 제목
        msg_box.setInformativeText(msg_context[msg])  # 메세지 내용

        msg_box.addButton("삭제", QMessageBox.ActionRole)
        msg_box.addButton("취소", QMessageBox.ActionRole)

        return msg_box.exec()


# 리스트 아이템
class MyItem(QWidget):
    def __init__(self, num, agr):
        super(MyItem, self).__init__()
        border_txt = """QLabel { font: 11px "웰컴체 Regular";
                        color: rgb(70,70,255);
                        border: 1px solid rgb(125,125,255);
                        padding-top: 2px;
                        padding-left: 1px;
                        border-radius: 2px;}"""

        self.setMaximumWidth(750)

        self.lb_num_icon = QLabel(self)
        self.lb_num_icon.setText(num)
        self.lb_num_icon.setAlignment(Qt.AlignCenter)
        self.lb_num_icon.setMaximumSize(QSize(20, 20))
        self.lb_num_icon.setMinimumSize(QSize(20, 20))
        self.lb_num_icon.setStyleSheet(border_txt)

        self.lb_content = QLabel(self)
        self.lb_content.setWordWrap(True)
        self.lb_content.adjustSize()
        self.lb_content.setAlignment(Qt.AlignVCenter)
        self.lb_content.setMinimumSize(450, 15)
        self.lb_content.setMaximumSize(450, 160)
        self.lb_content.setText(agr)
        self.lb_content.setStyleSheet("""QLabel { font: 14px ; color: rgb(65,65,65); padding-top: 2px; margin: 0px;}""")

        self.set_ui()

    def set_ui(self):
        h_box = QHBoxLayout()
        h_box.addWidget(self.lb_num_icon)
        h_box.addWidget(self.lb_content)

        self.setLayout(h_box)


# 리스트 아이템
class CategoryItem(QWidget):
    def __init__(self, content, parent=None):
        super(CategoryItem, self).__init__()
        max_width = parent.width() - 8
        self.setMaximumWidth(max_width)

        out_width = max_width - 30
        self.lb_category = QLabel(self)
        self.lb_category.setEnabled(False)
        self.lb_category.setGeometry(3, 0, out_width, 30)
        self.lb_category.setText(content)
        self.lb_category.setStyleSheet(
            """QLabel { font: 14px ; 
            color: rgb(65,65,65); 
            border: none; 
            padding-top: 2px; 
            margin: 0px;
            background-color: rgba(0,0,0,0);
            }""")


# 예외 오류 처리
def my_exception_hook(exctype, value, traceback):
    sys.excepthook(exctype, value, traceback)


sys._excepthook = sys.excepthook
sys.excepthook = my_exception_hook

# app = QApplication()
# window = AgrEditor('', 'EDIT')
# app.exec()
