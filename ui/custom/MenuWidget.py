from PySide6.QtCore import QPropertyAnimation, Qt, QSize, QPoint
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QLabel, QListWidget, QListWidgetItem, QGraphicsOpacityEffect


class MenuWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent

        self.setStyleSheet("""QListWidget {
                                font: 14px "웰컴체 Regular";
                                color: white;
                                background-color: rgba(0,0,0,160);
                                border-radius: 5px;
                                padding: 5px;
                                outline: none;
                            }
                            QListWidget:item {
                                border-radius: 5px;
                            }
                            QListWidget:item:hover {
                                background-color: rgba(255, 255, 255, 80);
                            }""")

        effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(effect)
        self.anim_hide = QPropertyAnimation(effect, b"opacity")
        self.anim_show = QPropertyAnimation(effect, b"opacity")
        self.menu_toggle = False

        self.hide()

    # 메뉴, 항목 크기 설정
    def set_size(self, bx):
        font_sizes = []
        for i in range(bx.count()):     # 텍스트 길이 추출
            item = bx.itemWidget(bx.item(i))
            txt = item.lb_text.text()
            font_size = bx.fontMetrics().boundingRect(txt).width()
            font_sizes.append(font_size)

        w = max(font_sizes) + 50
        h = (30 * bx.count()) + 10
        self.setFixedSize(w, h)

        for i in range(bx.count()):
            item = bx.itemWidget(bx.item(i))
            txt = item.lb_text
            txt.resize(max(font_sizes), txt.height())

    # 메뉴 위치 설정
    def set_position(self, btn):
        btn_pos = btn.mapToParent(btn.parent().pos())
        btn_x, btn_y = btn_pos.x(), btn_pos.y()
        btn_w, btn_h = btn.width(), btn.height()
        menu_w, menu_h = self.width(), self.height()

        # X, Y 축 정렬
        x = (btn_x - menu_w - 5) if (btn_x - menu_w) > 0 else (btn_x + btn_w + 5)
        y = btn_y if (btn_y - (menu_h - btn_h - 10)) < 0 else (btn_y - menu_h + btn_h)

        self.move(x, y)

    # 아이템 추가
    def add_item(self, items):
        for i in items:
            custom_item = MenuItem(i['name'], i['img'])
            widget_item = QListWidgetItem()
            widget_item.setSizeHint(QSize(0, 30))
            self.addItem(widget_item)
            self.setItemWidget(widget_item, custom_item)

    def show_menu(self, btn):
        if self.isHidden(): self.show()

        self.set_position(btn)
        self.anim_show.setStartValue(0)
        self.anim_show.setEndValue(1)
        self.anim_show.setDuration(100)
        self.anim_show.start()
        self.menu_toggle = True

    def hide_menu(self):
        self.anim_hide.setStartValue(1)
        self.anim_hide.setEndValue(0)
        self.anim_hide.setDuration(100)
        self.anim_hide.start()
        self.menu_toggle = False


class MenuItem(QWidget):
    def __init__(self, txt, icon=None):
        super(MenuItem, self).__init__()

        if icon:
            icon = QPixmap(icon).scaled(23, 23)
            self.lb_icon = QLabel(self)
            self.lb_icon.setFixedSize(23, 23)
            self.lb_icon.setPixmap(icon)
            self.lb_icon.setGeometry(5, 4, 23, 23)

        self.lb_text = QLabel(self)
        self.lb_text.setFixedHeight(20)
        self.lb_text.setStyleSheet("QLabel {font: 14px '웰컴체 Regular'; color: white;}")
        self.lb_text.setAlignment(Qt.AlignVCenter)
        self.lb_text.setText(txt)
        self.lb_text.move(QPoint(35, 7) if icon else QPoint(5, 7))

