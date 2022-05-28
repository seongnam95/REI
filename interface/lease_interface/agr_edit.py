import sys
import pandas as pd

from ui.dialog.ui_agr_editor import Ui_AgreementEditor
from PySide6.QtWidgets import QWidget, QDialog, QLabel, QHBoxLayout, QListWidgetItem, QMenu, QGraphicsDropShadowEffect, \
    QPushButton
from PySide6.QtCore import Qt, QEvent, QSize, Signal
from PySide6.QtGui import QColor, QIcon

# from hanspell import spell_checker
from ui.custom.BlackBoxMsg import BoxMessage


class AgrEditor(QDialog, Ui_AgreementEditor):
    def __init__(self, agr, category=None, title=None):
        super().__init__()
        self.setupUi(self)
        self.show_shadows()

        self.msg = BoxMessage(self)
        self.agr, self.category, self.title, self.response = agr, category, title, None
        self.editing, self.editing_row, self.save_row = False, 0, 0

        edit_icon = QIcon('../../data/img/button/edit_icon.png')
        self.btn_add_category.setIcon(edit_icon)
        self.btn_add_category.setIconSize(QSize(18, 18))

        plus_icon = QIcon('../../data/img/button/plus_icon.png')
        self.btn_category_add.setIcon(plus_icon)
        self.btn_category_add.setIconSize(QSize(18, 18))

        # 시그널
        self.cbx_category.activated.connect(self.load_title)
        self.cbx_title.activated.connect(self.load_content)

        self.btn_category_cancel.clicked.connect(lambda: self.show_add_category(False))
        self.btn_add_category.clicked.connect(lambda: self.show_add_category(True))
        self.btn_add.clicked.connect(self.add_item)
        self.btn_save.clicked.connect(self.clicked_save_btn)
        self.lst_content.installEventFilter(self)

        self.lst_category.itemPressed.connect(self.on_itemClicked)

        category_item = CategoryItem('안녕하세요')
        item = QListWidgetItem()
        item.setSizeHint(QSize(category_item.width(), 30))
        self.lst_category.addItem(item)
        self.lst_category.setItemWidget(item, category_item)

        self.load_category()

    def show_shadows(self):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(15)
        shadow.setXOffset(1)
        shadow.setYOffset(1)
        shadow.setColor(QColor(0, 0, 0, 35))
        self.edt_frame.setGraphicsEffect(shadow)

    def hide_shadows(self):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setEnabled(False)
        self.edt_frame.setGraphicsEffect(shadow)

    ## 상호작용 이벤트
    ############################################################################

    # QMenu 이벤트
    def eventFilter(self, source, event):

        # 항목 리스트
        if event.type() == QEvent.ContextMenu and source is self.lst_content:

            # 클릭한 아이템 인덱스
            item = source.itemAt(event.pos())
            item_index = self.lst_content.indexFromItem(item)

            # 우측 클릭 QMenu
            menu = QMenu(self)

            modify_action = menu.addAction("편 집")
            remove_action = menu.addAction("삭 제")

            menu.addAction(modify_action)
            menu.addAction(remove_action)

            menu_click = menu.exec(event.globalPos())

            # QMenu '편집' 클릭 시
            if menu_click == modify_action:
                if type(item) == QListWidgetItem:
                    self.edit_item(item, item_index)

            # QMenu '삭제' 클릭 시
            elif menu_click == remove_action:
                self.editing = False
                self.btn_add.setText("작  성")
                self.lst_content.model().removeRow(item_index.row())
                self.sorted_row()

            return True

        return super(AgrEditor, self).eventFilter(source, event)

    # 저장 버튼 클릭
    def clicked_save_btn(self):
        category = self.cbx_category.currentText().strip()
        title = self.cbx_title.text().strip()

        if not title:
            self.msg.show_msg(1500, 'center', "특약 제목을 입력해주세요.")

        elif not self.lst_content.count():
            self.msg.show_msg(1500, 'center', "특약내용 리스트가 비어있습니다.")

        else:
            result = self.agr[self.agr['category'] == category]

            if title in result['title'].values.tolist():
                current_title = self.agr['title'].iloc[0]
                if title != current_title:
                    self.msg.show_msg(1500, 'center', "중복되는 특약 제목입니다.")
                    return

        column = ['category', 'title', 'num', 'content']
        response = pd.DataFrame(columns=column)

        for i in range(self.lst_content.count()):
            item = self.lst_content.item(i)
            item_widget = self.lst_content.itemWidget(item)

            item_num = item_widget.lb_num_icon.text()
            item_content = item_widget.lb_content.text()

            result = pd.DataFrame([[category, title, item_num, item_content]], columns=column)
            response = response.append(result, ignore_index=True)

        self.response = response
        self.hide()

    ## 키워드, 타이틀
    ############################################################################

    # 카테고리 로드
    def load_category(self):
        category = self.agr.category.values.tolist()
        category = list(dict.fromkeys(category))
        self.cbx_category.addItems(category)

        self.load_title()

    # 타이틀 로드
    def load_title(self):
        category = self.cbx_category.currentText()
        title = self.agr.title[self.agr.category == category]
        title = list(dict.fromkeys(title))

        self.cbx_title.clear()
        self.cbx_title.addItems(title)
        self.cbx_title.showPopup()

    # 특약사항 로드
    def load_content(self):
        self.lst_content.clear()

        category = self.cbx_category.currentText()
        title = self.cbx_title.currentText()

        self.edt_title.setText(title)

        result = self.agr[self.agr.category == category]
        editing_data = result[result.title == title]

        [self.add_conent_item(count, content) for count, content in zip(editing_data['num'], editing_data['content'])]
        self.lb_number.setText(str(self.lst_content.count() + 1))

    ## 항목 제어
    ############################################################################

    # 항목 추가
    def add_item(self):
        content = self.edt_add.toPlainText()#

        if not content:
            self.msg.show_msg(1800, 'center', "특약사항 내용을 입력해주세요.")
            return

        # '수정' 클릭 이벤트
        if self.editing:
            item = self.lst_content.item(self.editing_row)

            item_widget = self.lst_content.itemWidget(item)
            item_widget.lb_content.setText(content)

            self.btn_add.setText("작  성")
            self.editing = False

        # '추가' 클릭 이벤트
        else:
            count = self.lst_content.count() + 1
            self.add_conent_item(count, content)

        self.lb_number.setText(str(self.lst_content.count() + 1))

        self.edt_add.clear()
        self.edt_add.setFocus()

    # 항목 편집
    def edit_item(self, item, item_index):
        item_widget = self.lst_content.itemWidget(item)
        item_text = item_widget.lb_content.text()

        self.edt_add.setText(item_text)
        self.btn_add.setText("수  정")
        self.lb_number.setText(item_widget.lb_num_icon.text())
        self.editing = True
        self.editing_row = item_index.row()

        # 에디트 포커싱 후 커서 끝으로 이동
        self.edt_add.setFocus()
        cursor = self.edt_add.textCursor()
        cursor.setPosition(len(item_text))
        self.edt_add.setTextCursor(cursor)

    # 항목 삭제
    def delete_item(self, cbx, item_index):
        if cbx == "content":
            self.editing = False
            self.btn_add.setText("작  성")
            self.lst_content.model().removeRow(item_index.row())
            self.sorted_row()

        elif cbx == "category":
            self.lst_category.model().removeRow(item_index.row())

        elif cbx == "title":
            self.lst_title.model().removeRow(item_index.row())

    ############################################################################

    def show_add_category(self, act):
        if act:
            self.hide_shadows()

            self.category_back.setStyleSheet('#category_back { background: rgba(0,0,0,160) }')
            self.category_back.resize(self.width(), self.height())
            self.category_back.move(0, 0)

            x = (self.width() / 2) - (self.category_frame.width() / 2)
            y = (self.height() / 2) - (self.category_frame.height() / 2)
            self.category_frame.move(x, y)

        else:
            self.show_shadows()
            self.category_back.move(self.width(), 0)

    # 리스트 순서 정렬
    def sorted_row(self):
        for i in range(self.lst_content.count()):
            item = self.lst_content.item(i)

            item_widget = self.lst_content.itemWidget(item)
            item_widget.lb_num_icon.setText(str(i + 1))

        self.lb_number.setText(str(self.lst_content.count() + 1))

    # 특약 아이템 추가 함수
    def add_conent_item(self, count, content):
        custom_item = MyItem(str(count), content)
        item = QListWidgetItem()
        item.setSizeHint(QSize(self.lst_content.width() - 10, 15))
        item.setSizeHint(QSize(custom_item.sizeHint()))

        self.lst_content.addItem(item)
        self.lst_content.setItemWidget(item, custom_item)


# 맞춤법, 띄어쓰기 교정
def spell_check_module(content):
    content = spell_checker.check(content).checked
    return content


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


# 카테고리 아이템
class CategoryItem(QWidget):
    RemoveSignal = Signal()

    def __init__(self, category):
        super(CategoryItem, self).__init__()
        self.setMinimumHeight(30)
        self.setMaximumWidth(237)

        self.category = QLabel(self)
        self.category.setGeometry(0, 0, 207, 30)
        self.category.setText(category)
        self.category.setStyleSheet("""QLabel { font: 14px ; color: rgb(65,65,65); padding-top: 2px; margin: 0px;}""")

        del_icon = QIcon('../../data/img/button/delete_icon.png')
        self.btn_delete = QPushButton(self)
        self.btn_delete.setGeometry(207, 0, 30, 30)
        self.btn_delete.setIcon(del_icon)
        self.btn_delete.setIconSize(QSize(18, 18))
        self.btn_delete.setStyleSheet("""
            QPushButton {
                background: rgba(0,0,0,0);
                border: none;
                outline: none;
            }
        """)
        self.btn_delete.clicked.connect(self.RemoveSignal)

    def delete_category(self):
        print(self.sender().rem)


# 예외 오류 처리
def my_exception_hook(exctype, value, traceback):
    sys.excepthook(exctype, value, traceback)


sys._excepthook = sys.excepthook
sys.excepthook = my_exception_hook


