from PySide6.QtCore import Qt, QEasingCurve, QPoint, Property, \
    QPropertyAnimation, QParallelAnimationGroup, QTimer, Slot, Signal
from PySide6.QtWidgets import QStackedWidget, QGraphicsOpacityEffect

class SlidingStackedWidget(QStackedWidget):
    LEFT2RIGHT, RIGHT2LEFT, TOP2BOTTOM, BOTTOM2TOP, AUTOMATIC = range(5)

    def __init__(self, *args, **kwargs):
        super(SlidingStackedWidget, self).__init__(*args, **kwargs)
        self._pnow = QPoint(0, 0)
        self._speed = 150
        self._now = 0
        self._current = 0
        self._next = 0
        self._active = 0
        self._orientation = Qt.Horizontal
        self._easing = QEasingCurve.Linear
        self.chan_event = "next"
        self._initAnimation()

    def setSpeed(self, speed=300):
        self._speed = speed

    @Property(int, fset=setSpeed)
    def speed(self):
        return self._speed

    def setOrientation(self, orientation=Qt.Horizontal):
        self._orientation = orientation

    @Property(int, fset=setOrientation)
    def orientation(self):
        return self._orientation

    def setEasing(self, easing=QEasingCurve.OutBack):
        self._easing = easing

    def getCurrent(self):
        return self._current

    @Property(int, fset=setEasing)
    def easing(self):
        return self._easing

    def slideInNext(self):
        now = self.currentIndex()
        if now < self.count() - 1:
            self.chan_event = "next"
            self.slideInIdx(now + 1)
            self._current = now + 1

    def slideInPrev(self):
        now = self.currentIndex()
        if now > 0:
            self.chan_event = "prev"
            self.slideInIdx(now - 1)
            self._current = now - 1

    def slideInIdx(self, idx, direction=4):
        if idx > self.count() - 1:
            direction = self.TOP2BOTTOM if self._orientation == Qt.Vertical else self.RIGHT2LEFT
            idx = idx % self.count()
        elif idx < 0:
            direction = self.BOTTOM2TOP if self._orientation == Qt.Vertical else self.LEFT2RIGHT
            idx = (idx + self.count()) % self.count()
        self.slideInWgt(self.widget(idx), direction)

    def slideInWgt(self, widget, direction):
        if self._active:
            return
        self._active = 1
        _now = self.currentIndex()
        _next = self.indexOf(widget)
        if _now == _next:
            self._active = 0
            return

        w_now = self.widget(_now)
        w_next = self.widget(_next)

        if _now < _next:
            directionhint = self.TOP2BOTTOM if self._orientation == Qt.Vertical else self.RIGHT2LEFT
        else:
            directionhint = self.BOTTOM2TOP if self._orientation == Qt.Vertical else self.LEFT2RIGHT
        if direction == self.AUTOMATIC:
            direction = directionhint

        offsetX = self.frameRect().width()
        offsetY = self.frameRect().height()
        w_next.setGeometry(0, 0, offsetX, offsetY)

        if direction == self.BOTTOM2TOP:
            offsetX = 0
            offsetY = -offsetY
        elif direction == self.TOP2BOTTOM:
            offsetX = 0
        elif direction == self.RIGHT2LEFT:
            offsetX = -offsetX
            offsetY = 0
        elif direction == self.LEFT2RIGHT:
            offsetY = 0

        pnext = w_next.pos()
        pnow = w_now.pos()
        self._pnow = pnow

        w_next.move(pnext.x() - offsetX, pnext.y() - offsetY)
        w_next.show()
        w_next.raise_()

        effect = QGraphicsOpacityEffect(w_now)
        w_now.setGraphicsEffect(effect)
        self._animnow_opa = QPropertyAnimation(effect, b"opacity")
        self._animnow_opa.setStartValue(1)
        self._animnow_opa.setEndValue(0)
        self._animnow_opa.setDuration(100)
        self._animgroup.addAnimation(self._animnow_opa)

        effect = QGraphicsOpacityEffect(w_next)
        w_next.setGraphicsEffect(effect)
        self._animnext_opa = QPropertyAnimation(effect, b"opacity")
        self._animnext_opa.setStartValue(0)
        self._animnext_opa.setEndValue(1)
        self._animnext_opa.setDuration(170)
        self._animgroup.addAnimation(self._animnext_opa)

        if self.chan_event == "next":
            now_x_offset = (offsetX + pnow.x()) + 550
            next_x_offset = (-offsetX + pnext.x()) - 550
        else:
            now_x_offset = offsetX + pnow.x() - 550
            next_x_offset = (-offsetX + pnext.x()) + 550

        self._animnow.setTargetObject(w_now)
        self._animnow.setDuration(self._speed)
        self._animnow.setEasingCurve(self._easing)
        self._animnow.setStartValue(QPoint(pnow.x(), pnow.y()))
        self._animnow.setEndValue(
            QPoint(now_x_offset, offsetY + pnow.y()))

        self._animnext.setTargetObject(w_next)
        self._animnext.setDuration(self._speed)
        self._animnext.setEasingCurve(self._easing)
        self._animnext.setStartValue(
            QPoint(next_x_offset, offsetY + pnext.y()))
        self._animnext.setEndValue(QPoint(pnext.x(), pnext.y()))

        self._next = _next
        self._now = _now
        self._active = 1
        self._animgroup.start()

    def _initAnimation(self):
        # 当前页的动画
        self._animnow = QPropertyAnimation(
            self, propertyName=b'pos', duration=self._speed,
            easingCurve=self._easing)

        # 下一页的动画
        self._animnext = QPropertyAnimation(
            self, propertyName=b'pos', duration=self._speed,
            easingCurve=self._easing)
        # 并行动画组
        self._animgroup = QParallelAnimationGroup(
            self, finished=self.animationDoneSlot)
        self._animgroup.addAnimation(self._animnow)
        self._animgroup.addAnimation(self._animnext)

    def setCurrentIndex(self, index):
        self.slideInIdx(index)

    def setCurrentWidget(self, widget):
        super(SlidingStackedWidget, self).setCurrentWidget(widget)
        self.setCurrentIndex(self.indexOf(widget))

    def animationDoneSlot(self):
        QStackedWidget.setCurrentIndex(self, self._next)
        w = self.widget(self._now)
        w.hide()
        w.move(self._pnow)
        self._active = 0

    def autoStop(self):
        if hasattr(self, '_autoTimer'):
            self._autoTimer.stop()

    def autoStart(self, msec=3000):
        if not hasattr(self, '_autoTimer'):
            self._autoTimer = QTimer(self, timeout=self._autoStart)
        self._autoTimer.stop()
        self._autoTimer.start(msec)

    def _autoStart(self):
        if self._current == self.count():
            self._current = 0
        self._current += 1
        self.setCurrentIndex(self._current)