from PySide6.QtWidgets import QApplication, QMainWindow, QButtonGroup, QWidget, QLabel, QLineEdit, QComboBox, \
    QListWidgetItem, QMenu, QGraphicsOpacityEffect
from PySide6.QtCore import QPropertyAnimation, Qt, QSize, QRegularExpression, QRect, QEvent, QTimer, QPoint
from PySide6.QtGui import QIcon, QRegularExpressionValidator, QPixmap

class BoxMessage(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.msg_timer = False
        self.timer = QTimer(self)

        self.hide()

        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("QLabel{background-color: rgba(0,0,0,150);"
                                          "font: 15px \uc6f0\ucef4\uccb4 Regular;"
                                          "color: white;"
                                          "border-radius: 3px;"
                                          "padding-top: 3px;}")
        self.parent_size = parent.size()

    def set_size(self, pos, content):
        font_size = self.fontMetrics().boundingRect(content)

        if '\n' in content:
            line_width = []
            for i in content.split('\n'):
                line_width.append(self.fontMetrics().boundingRect(i).width())
            w = max(line_width)

        else:
            w = font_size.width()

        h = 20 * (content.count('\n') + 1)
        self.resize(w + 20, h + 14)

        x, y = round((self.parent_size.width() / 2) - (self.width() / 2)), 0
        if type(pos) == str:
            if pos == 'center':
                y = round((self.parent_size.height() / 2) - (self.height() / 2))

            elif pos == 'bot':
                y = round((self.parent_size.height()) - (self.height() / 2) - 100)

            elif pos == 'top':
                y = round((self.height() / 2) + 100)

        elif type(pos) == int: y = pos
        elif type(pos) == QPoint: x, y = pos.x(), pos.y()

        self.move(x, y)

    def show_msg(self, sec, pos, content):
        self.setText(content)
        self.set_size(pos, content)

        if self.msg_timer:
            self.timer.stop()
            self.msg_timer = False
        else:
            if self.isHidden(): self.show()

            effect = QGraphicsOpacityEffect(self)
            self.setGraphicsEffect(effect)
            self.anim = QPropertyAnimation(effect, b"opacity")

            self.anim.setStartValue(0)
            self.anim.setEndValue(1)
            self.anim.setDuration(50)
            self.anim.start()

            self.timer.start(sec)
            self.timer.timeout.connect(self.hide_msg)

    # 메세지 타이머 종료
    def hide_msg(self):

        effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(effect)
        self.anim = QPropertyAnimation(effect, b"opacity")

        self.anim.setStartValue(1)
        self.anim.setEndValue(0)
        self.anim.setDuration(500)
        self.anim.start()

        self.timer.stop()
        self.msg_timer = False
