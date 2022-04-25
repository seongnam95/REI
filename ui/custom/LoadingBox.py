from PySide6.QtWidgets import QFrame, QLabel, QGraphicsDropShadowEffect
from PySide6.QtGui import QMovie, Qt, QColor


class LoadingBox(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        w, h = parent.width(), parent.height()
        self.resize(w, h)
        self.setStyleSheet("QFrame { background-color: rgba(0,0,0,40)}")

        self.frame = QFrame(self)
        self.frame.setStyleSheet("""
        QFrame {
            background-color: rgb(255,255,255);
            border-radius: 10px;
        }        
        """)
        self.frame.resize(100, 100)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(25)
        shadow.setColor(QColor(0, 0, 0, 60))
        self.frame.setGraphicsEffect(shadow)

        frame_x = int((w / 2) - (self.frame.width() / 2))
        frame_y = int((h / 2) - (self.frame.height() / 2))
        self.frame.move(frame_x, frame_y)

        # 로딩 이미지
        self.movie = QMovie("../../data/img/animation/loading.gif")
        self.loading_img = QLabel(self.frame)
        self.loading_img.setStyleSheet("QLabel { background: rgba(0,0,0,0) }")
        self.loading_img.resize(70, 100)
        self.loading_img.setMovie(self.movie)
        self.loading_img.setScaledContents(True)

        img_x = int((self.frame.width() / 2) - (self.loading_img.width() / 2))
        self.loading_img.move(img_x, 0)

        self.hide()

    def show_loading(self):
        self.movie.start()
        self.show()

    def hide_loading(self):
        self.movie.stop()
        self.hide()
