import sys
import pandas as pd
import pymysql

from ui.dialog.ui_agr_editor import Ui_AgrEditor
from PySide6.QtWidgets import QWidget, QDialog, QLabel, QHBoxLayout, QListWidgetItem, QMenu, QGraphicsDropShadowEffect, \
    QPushButton, QMessageBox, QApplication, QLineEdit
from PySide6.QtCore import Qt, QEvent, QSize, Signal, QPoint, Slot
from PySide6.QtGui import QColor, QIcon

# from hanspell import spell_checker
from ui.custom.BlackBoxMsg import BoxMessage
from ui.custom.TextEditWidget import TextEditWidget


class AgrEditor(QDialog, Ui_AgrEditor):
    def __init__(self, agr, kind):
        super().__init__()
        self.setupUi(self)

        self.agr, self.kind, self.response = agr, kind, None
        self.user_id = 'jsn0509'
        self.edit_category, self.new_category, self.remove_category = pd.DataFrame, [], []

        self.conn = pymysql.connect(
            host='db.snserver.site', user='jsn0509', password='ks05090818@', db='dbjsn0509', charset='utf8')

        self.cur = self.conn.cursor()
        self.mysql_select()
        self._init_ui()
        self.show_shadows()
        self.show()
        self._init_interaction()

        self.load_category()

    def _init_ui(self):
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

        edit_icon = QIcon('../../data/img/button/plus_icon.png')
        self.btn_add_category.setIcon(edit_icon)
        self.btn_add_category.setIconSize(QSize(21, 21))

        edit_icon = QIcon('../../data/img/button/trash_icon.png')
        self.btn_del_category.setIcon(edit_icon)
        self.btn_del_category.setIconSize(QSize(19, 19))

        edit_icon = QIcon('../../data/img/button/plus_icon.png')
        self.btn_add_title.setIcon(edit_icon)
        self.btn_add_title.setIconSize(QSize(21, 21))

        edit_icon = QIcon('../../data/img/button/trash_icon.png')
        self.btn_del_title.setIcon(edit_icon)
        self.btn_del_title.setIconSize(QSize(19, 19))

    def _init_interaction(self):
        self.lst_category.itemClicked.connect(self.load_title)
        self.lst_title.itemClicked.connect(self.load_content)

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

    ## 상호작용 이벤트
    ############################################################################

    # 저장 버튼 클릭
    def clicked_save_btn(self):
        print(self.edt_agr.toHtml())
        self.conn.close()
        return
        category = self.cbx_category.currentText().strip()
        title = self.cbx_title.currentText().strip()
        print(category, title)

        # if not title: self.msg.show_msg(1500, 'center', "특약 제목을 입력해주세요.")
        # elif not self.lst_content.count(): self.msg.show_msg(1500, 'center', "특약내용 리스트가 비어있습니다.")
        #
        # else:
        #     result = self.agr[self.agr['category'] == category]
        #
        #     if title in result['title'].values.tolist():
        #         current_title = self.agr['title'].iloc[0]
        #         if title != current_title:
        #             self.msg.show_msg(1500, 'center', "중복되는 특약 제목입니다.")
        #             return
        #
        # column = ['category', 'title', 'num', 'content']
        # response = pd.DataFrame(columns=column)
        #
        # for i in range(self.lst_content.count()):
        #     item = self.lst_content.item(i)
        #     item_widget = self.lst_content.itemWidget(item)
        #
        #     item_num = item_widget.lb_num_icon.text()
        #     item_content = item_widget.lb_content.text()
        #
        #     result = pd.DataFrame([[category, title, item_num, item_content]], columns=column)
        #     response = response.append(result, ignore_index=True)
        #
        # self.response = response
        # self.hide()

    ## 카테고리, 타이틀
    ############################################################################

    # 카테고리 로드
    def load_category(self):
        try: self.agr = pd.read_csv('../../data/val/agrs.csv', sep="|")
        except FileNotFoundError: return

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

    # 타이틀 로드
    def load_title(self):
        self.lst_title.clear()

        item = self.lst_category.item(self.lst_category.currentRow())
        item_widget = self.lst_category.itemWidget(item)
        category = item_widget.lb_category.text()

        title = self.agr.title[self.agr.category == category]

        if not title.isnull().values.any():
            title = list(dict.fromkeys(title))
            print(type(title), title)
            if type(title) == list and title[0] == '': return

            for i in title:
                category_item = CategoryItem(i, self.lst_title)
                item = QListWidgetItem()
                item.setSizeHint(QSize(category_item.width(), 30))
                self.lst_title.addItem(item)
                self.lst_title.setItemWidget(item, category_item)

    # 특약사항 로드
    def load_content(self):
        try:
            self.edt_agr.clear()

            item = self.lst_category.item(self.lst_category.currentRow())
            category_widget = self.lst_category.itemWidget(item)
            category = self.agr[self.agr.category == category_widget.lb_category.text()]

            item = self.lst_title.item(self.lst_title.currentRow())
            title_widget = self.lst_title.itemWidget(item)
            title = category[category.title == title_widget.lb_category.text()]
            content = title.content.iloc[0]
            self.edt_agr.insertHtml(content)

        except: return

    ## 카테고리 편집
    ############################################################################

    # 편집기 활성화
    def show_item_editor(self, form, kind):
        self.hide_shadows()
        self.editor_back.show()
        self.edt_name.clear()

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

        self.edt_name.setFocus()

    # 편집기 비활성화
    def hide_item_editor(self):
        self.show_shadows()
        self.editor_back.hide()
        self.new_category.clear()

        crt_category = self.lst_category.currentRow()
        crt_title = self.lst_title.currentRow()

        self.load_category()
        # self.load_title()

        self.lst_category.setCurrentRow(crt_category)
        self.lst_title.setCurrentRow(crt_title)

    def add_item(self):
        name = self.edt_name.text().strip()

        if '|' in name:
            self.msg.show_msg(2000, 'center', "'|' 기호를 포함시킬 수 없습니다.")
            return

        form = 'category' if '카테고리' in self.editor_title.text() else 'title'

        if form == 'category':
            for i in range(self.lst_category.count()):
                item = self.lst_category.item(i)
                category = self.lst_category.itemWidget(item).lb_category.text()
                if name == category:
                    self.msg.show_msg(2000, 'center', '이미 존재하는 카테고리입니다.')
                    return

            new_category = {'category': [name], 'title': [''], 'content': ['']}
            new_df = pd.DataFrame(new_category)

            self.agr = pd.concat([self.agr, new_df])
            self.agr.reset_index(drop=True, inplace=True)
            self.agr.to_csv("../../data/val/agrs.csv", sep="|", index=False)

        elif form == 'title':
            for i in range(self.lst_title.count()):
                item = self.lst_title.item(i)
                category = self.lst_title.itemWidget(item).lb_category.text()
                if name == category:
                    self.msg.show_msg(2000, 'center', '이미 존재하는 특약사항 제목입니다.')
                    return

            item = self.lst_category.item(self.lst_category.currentRow())
            category = self.lst_category.itemWidget(item).lb_category.text()

            titles = self.agr[self.agr['category'] == category]['title']
            if titles.isnull().values.any():
                self.agr = self.agr.drop(self.agr[self.agr['category'] == category].index, axis=0)

            new_title = {'category': [category], 'title': [name], 'content': ['']}
            new_df = pd.DataFrame(new_title)

            self.agr = pd.concat([self.agr, new_df])
            self.agr.reset_index(drop=True, inplace=True)
            self.agr.to_csv("../../data/val/agrs.csv", sep="|", index=False)

        self.hide_item_editor()

    def delete_item(self, form):
        if form == 'category':
            row = self.lst_category.currentRow()
            if row != -1:
                res = self.msg_box('del_category')
                if res == 0:

                    item = self.lst_category.item(row)
                    item_widget = self.lst_category.itemWidget(item)
                    category = item_widget.lb_category.text()

                    self.agr = self.agr.drop(self.agr[self.agr['category'] == category].index, axis=0)
                    self.agr.reset_index(drop=True, inplace=True)
                    self.agr.to_csv("../../data/val/agrs.csv", sep="|", index=False)

                    self.lst_category.takeItem(row)

        elif form == 'title':
            row = self.lst_title.currentRow()
            if row != -1:
                res = self.msg_box('del_title')
                if res == 0:
                    item = self.lst_category.item(self.lst_category.currentRow())
                    item_widget = self.lst_category.itemWidget(item)
                    category = item_widget.lb_category.text()

                    item = self.lst_title.item(row)
                    item_widget = self.lst_title.itemWidget(item)
                    title = item_widget.lb_category.text()
                    print(category, title)
                    self.agr = self.agr.drop(self.agr[(self.agr['category'] == category) & (self.agr['title'] == title)].index, axis=0)

                    print(self.agr[(self.agr['category'] == category) & (self.agr['title'] == title)])
                    self.agr.reset_index(drop=True, inplace=True)
                    self.agr.to_csv("../../data/val/agrs.csv", sep="|", index=False)

                    self.lst_title.takeItem(row)
    #
    # # 카테고리 삭제
    # def delete_category(self):
    #     res = self.msg_box()
    #     if res == 0:
    #
    #         # 클릭 아이템 삭제
    #         widget = self.sender()
    #         gp = widget.mapToGlobal(QPoint())
    #         lp = self.lst_edit_category.viewport().mapFromGlobal(gp)
    #         row = self.lst_edit_category.row(self.lst_edit_category.itemAt(lp))
    #
    #         item = self.lst_edit_category.item(row)
    #         item_widget = self.lst_edit_category.itemWidget(item)
    #         category = item_widget.lb_category.text()
    #
    #         if category in self.new_category:
    #             self.new_category.remove(category)
    #
    #         self.lst_edit_category.model().removeRow(row)
    #         self.remove_category.append(category)
    #
    # # 카테고리 추가
    # def add_category(self):
    #     category = self.edt_category.text().strip()
    #
    #     categorys = self.agr.category.values.tolist()
    #     categorys = list(dict.fromkeys(categorys))
    #
    #     if '|' in category:
    #         self.msg.show_msg(2000, 'center', "카테고리명에 '|' 기호를 포함시킬 수 없습니다.")
    #         return
    #
    #     if category in categorys or category in self.new_category:
    #         self.msg.show_msg(2000, 'center', '이미 존재하는 카테고리입니다.')
    #
    #     else:
    #         new_category = {'category': [category], 'title': [''], 'content': ['']}
    #         new_df = pd.DataFrame(new_category)
    #
    #         self.agr = pd.concat([self.agr, new_df])
    #         self.new_category.append(category)
    #
    #         category_item = CategoryItem(category, True, self.lst_edit_category)
    #         category_item.btn_delete.clicked.connect(self.delete_category)
    #
    #         item = QListWidgetItem()
    #         item.setSizeHint(QSize(category_item.width(), 30))
    #         self.lst_edit_category.addItem(item)
    #         self.lst_edit_category.setItemWidget(item, category_item)
    #
    #         self.edt_category.clear()
    #
    #     self.edt_category.setFocus()
    #
    # # 카테고리 저장
    # def save_category(self):
    #     for category in self.remove_category:
    #         self.agr = self.agr.drop(self.agr[self.agr['category'] == category].index, axis=0)
    #
    #     self.agr.reset_index(drop=True, inplace=True)
    #     self.agr.to_csv("../../data/val/agrs.csv", sep="|", index=False)
    #
    #     self.show_add_category(False)
    #     self.load_category()

    ############################################################################

    # 다이얼로그 엔터키 막기
    def keyPressEvent(self, event):
        if ((not event.modifiers() and
             event.key() == Qt.Key_Return) or
                (event.modifiers() == Qt.KeypadModifier)):
            event.accept()
        else: super(AgrEditor, self).keyPressEvent(event)

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

    ## MySql
    #################################################################################
    def mysql_insert(self):

        self.cur.execute(f"INSERT INTO contract_condition VALUES(NULL, '{user_id}', '{category}', '매매 기본특약', '가나다라마바사')")
        self.conn.commit()

    # def mysql_update(self):

    def mysql_select(self):
        """ select [출력하고자 하는 Column] from [테이블 이름] where [조건] """

        columns = "`category`, `sort_num`, `title`, `content`"
        sql = f"SELECT {columns} FROM `contract_condition` WHERE `user_id`='{self.user_id}'"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        self.conn.commit()

        agrs = pd.DataFrame(columns=['category', 'sort_num', 'title', 'content'])
        for row in result:
            category = row[0]
            sort_num = list(map(int, row[1].split('{sep}')))
            titles = row[2].split('{sep}')
            contents = row[3].split('{sep}')

            items = pd.DataFrame(columns=['category', 'sort_num', 'title', 'content'])
            for i in range(len(titles)):
                agr_item = [category, sort_num[i], titles[i], contents[i]]
                items.loc[i] = agr_item

            items = items.sort_values(by=['sort_num'], axis=0)
            agrs = pd.concat([agrs, items])
            print(agrs)


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

app = QApplication()
window = AgrEditor('', 'EDIT')
app.exec()
