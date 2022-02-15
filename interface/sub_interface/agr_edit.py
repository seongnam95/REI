import sys
import csv
import pandas as pd

from ui.dialog.ui_agr_editor import Ui_AgreementEditor
from PySide6.QtWidgets import QWidget, QApplication, QDialog, QLabel, QMessageBox, QHBoxLayout, QListWidgetItem, QMenu
from PySide6.QtCore import Qt, QEvent, QRect, QSize
from PySide6.QtGui import QTextCursor, QFontMetrics

from hanspell import spell_checker
from ui.custom.TitleBarWidget import TitleBarWidget


class AgrEditor(QDialog, Ui_AgreementEditor):
    def __init__(self, agr):
        super().__init__()

        self._setupUi(self)

        # 변수 선언
        self.agr = agr
        self.editing, self.editing_row, self.save_row = False, 0, 0

        self._init_interaction()
        self.load_content()

    # UI 상호작용 컨넥트
    def _init_interaction(self):
        self.btn_add.clicked.connect(self.clicked_add)
        self.lst_content.installEventFilter(self)

    ## UI 세팅
    ############################################################################

    # 내용 로드
    def load_content(self):
        keyword = self.agr['keyword'].iloc[0]
        title = self.agr['title'].iloc[0]

        self.cbx_keyword.addItem(keyword)
        self.edt_title.setText(title)
        self.lst_content.clear()

        [self.add_conent_item(count, content) for count, content in zip(self.agr['num'], self.agr['content'])]

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
    def clicked_save(self):
        if self.edt_title.text() == "":
            self.msg("정보", "My 특약 제목을 입력해주세요.")
            return
        elif self.lst_content.count() == 0:
            self.msg("정보", "My 특약 리스트가 비어있습니다.")
            return

        f = open('../../data/val/agrs.csv', 'a', newline='')
        wr = csv.writer(f)

        item_keyword = self.cbx_keyword.currentText()
        item_title = self.edt_title.text()

        for i in range(self.lst_content.count()):
            item = self.lst_content.item(i)
            item_widget = self.lst_content.itemWidget(item)

            item_num = item_widget.lb_num_icon.text()
            item_content = item_widget.lb_content.text()

            wr.writerow([item_keyword, item_title, item_num, item_content])

        f.close()

        self.load_keyword()

    ## 항목 함수
    ############################################################################

    # 항목 추가
    def clicked_add(self):
        content = self.edt_add.toPlainText()

        if content == "": return
        count = self.lst_content.count() + 1

        # '수정' 클릭 이벤트
        if self.editing:
            item = self.lst_content.item(self.editing_row)

            item_widget = self.lst_content.itemWidget(item)
            item_widget.lb_content.setText(content)

            self.btn_add.setText("작  성")
            self.editing = False

        # '추가' 클릭 이벤트
        else: self.add_conent_item(count, content)

        self.lb_number.setText(str(count))

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

        elif cbx == "keyword":
            self.lst_keyword.model().removeRow(item_index.row())

        elif cbx == "title":
            self.lst_title.model().removeRow(item_index.row())

    ############################################################################

    # 리스트 순서 정렬
    def sorted_row(self):
        for i in range(self.lst_content.count()):
            item = self.lst_content.item(i)

            item_widget = self.lst_content.itemWidget(item)
            item_widget.lb_num_icon.setText(str(i + 1))

        count = self.lst_content.count() + 1
        self.lb_number.setText(str(count))

    # 특약 아이템 추가 함수
    def add_conent_item(self, count, content):
        custom_item = MyItem(str(count), content)
        item = QListWidgetItem(self.lst_content)
        item.setSizeHint(QSize(self.lst_content.width() - 10, 15))
        item.setSizeHint(QSize(custom_item.sizeHint()))
        self.lst_content.setItemWidget(item, custom_item)

    # 메세지 함수
    def msg(self, ty, content):
        title = "레이 - Real estate Information"
        if ty == "기본":
            QMessageBox.about(self, title, content)
        elif ty == "정보":
            QMessageBox.information(self, title, content, QMessageBox.Ok)
        elif ty == "경고":
            QMessageBox.warning(self, title, content, QMessageBox.Ok)
        elif ty == "에러":
            QMessageBox.critical(self, title, content, QMessageBox.Ok)


# 맞춤법, 띄어쓰기 교정
def spell_check_module(content):
    content = spell_checker.check(content).checked
    return content


# 리스트 아이템
class MyItem(QWidget):
    def __init__(self, num, agr):
        super(MyItem, self).__init__()
        border_txt = """QLabel { font: 11px "웰컴체 Regular";
                        color: white;
                        background-color: rgb(82, 103, 124);
                        padding-top: 2px;
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
        self.lb_content.setStyleSheet("""QLabel { font: 12px ; color: rgb(45, 71, 102); padding-top: 2px; margin: 0px;}""")

        self.set_ui()

    def set_ui(self):
        h_box = QHBoxLayout()
        h_box.addWidget(self.lb_num_icon)
        h_box.addWidget(self.lb_content)

        self.setLayout(h_box)


# 예외 오류 처리
def my_exception_hook(exctype, value, traceback):
    sys.excepthook(exctype, value, traceback)


sys._excepthook = sys.excepthook
sys.excepthook = my_exception_hook


