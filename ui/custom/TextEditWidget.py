from PySide6.QtWidgets import QWidget, QFrame, QPushButton, QComboBox, QFontComboBox
from PySide6.QtCore import QRect
from PySide6.QtGui import QFont, QTextCharFormat


class TextEditWidget(QWidget):
    def __init__(self, parent, width, edt):
        super().__init__(parent)
        self.resize(width, 30)
        self._set_ui()

        self.edt = edt
        self.bold, self.underline, self.italic = False, False, False

        self.set_font_size()

    def _set_ui(self):
        self.setStyleSheet("""
        QComboBox {
            border: none;
            padding-top: 4px;
            padding-left: 10px;
            min-width: 3em;
            background: rgb(255, 255, 255);
            font: 14px "웰컴체 Regular";
            color: rgb(65, 65, 65);
        }
        
        QComboBox QAbstractItemView { 
            border: 1px solid lightgray;
            outline: none;
            padding: 5px;
        }      
        
        QComboBox QAbstractItemView::item { 
            color: rgb(65, 65, 65);
            border-radius: 5px;
            padding-left: 10px;
            padding-top: 3px;
            min-height: 30px; 
        }    
        
        QComboBox QAbstractItemView::item:focus { 
            selection-color: white;
            background-color: rgb(128,128,255);
        }
        
        QComboBox QAbstractItemView::item:hover { 
            selection-color: white;
            background-color: rgb(128,128,255);
        }
        
        QComboBox::drop-down {
            width: 20px;
        
            border-top-right-radius: 3px;
            border-bottom-right-radius: 3px;
        }
        
        QComboBox::down-arrow {
            image: url(../../data/img/system/down_arrow_icon.png);
            width: 8px;
            height: 8px;
        }
        
        QScrollBar:vertical {
            width: 5px;
            border: none;
        }
        
        QScrollBar::handle {
            background: rgb(235,235,235);
            border: none;
        }
        
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            border: none;
            background: none;
        }
        
        QPushButton {
            padding-top: 4px;
            padding-left: 5px;
            background: white;
            outline: none;
            border: none;
        }
        """)

        self.cbx_font = QFontComboBox(self)
        self.cbx_font.setGeometry(0, 0, 150, 30)

        font_sizes = ["8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
        self.cbx_fontsize = QComboBox(self)
        self.cbx_fontsize.addItems(font_sizes)
        self.cbx_fontsize.setCurrentIndex(2)
        self.cbx_fontsize.setGeometry(160, 0, 60, 30)
        self.cbx_fontsize.activated.connect(self.set_font_size)

        # 버튼
        self.btn_frame = QFrame(self)
        self.btn_frame.setGeometry(240, 0, 180, 30)

        self.btn_bold = QPushButton(self.btn_frame)
        self.btn_bold.setObjectName('btn_bold')
        self.btn_bold.setGeometry(QRect(0, 0, 30, 30))
        self.btn_bold.setStyleSheet("""
        #btn_bold {
            image: url(../../data/img/button/bold_icon.png);
        }
        
        #btn_bold:hover {
            image: url(../../data/img/button/bold_hover_icon.png);
        }
        """)
        self.btn_bold.clicked.connect(self.set_bold)

        self.btn_italic = QPushButton(self.btn_frame)
        self.btn_italic.setObjectName('btn_italic')
        self.btn_italic.setGeometry(QRect(30, 0, 30, 30))
        self.btn_italic.setStyleSheet("""
        #btn_italic {
            image: url(../../data/img/button/italic_icon.png);
        }
        
        #btn_italic:hover {
            image: url(../../data/img/button/italic_hover_icon.png);
        }""")
        self.btn_italic.clicked.connect(self.set_italic)

        self.btn_under_line = QPushButton(self.btn_frame)
        self.btn_under_line.setObjectName('btn_under_line')
        self.btn_under_line.setGeometry(QRect(60, 0, 30, 30))
        self.btn_under_line.setStyleSheet("""
        #btn_under_line {
            image: url(../../data/img/button/under_icon.png);
        }
        
        #btn_under_line:hover {
            image: url(../../data/img/button/under_hover_icon.png);
        }""")
        self.btn_under_line.clicked.connect(self.set_underline)

        self.btn_color = QPushButton(self.btn_frame)
        self.btn_color.setObjectName('btn_color')
        self.btn_color.setGeometry(QRect(90, 0, 30, 30))
        self.btn_color.setStyleSheet("""
        #btn_under_line {
            image: url(../../data/img/button/color_icon.png);
        }
        
        #btn_under_line:hover {
            image: url(../../data/img/button/color_hover_icon.png);
        }""")

        # 맞춤법 체크 버튼
        self.btn_spelling = QPushButton(self)
        self.btn_spelling.setObjectName('btn_spelling')
        self.btn_spelling.resize(80, 30)
        self.btn_spelling.setText('맞춤법검사')

        spell_x = self.width() - self.btn_spelling.width()
        self.btn_spelling.move(spell_x, 0)
        self.btn_spelling.setStyleSheet("""
        #btn_spelling {
            font: 14px "웰컴체 Regular";
            color: rgb(88,88,255);
        }
        
        #btn_spelling:hover {
            font: 14px "웰컴체 Regular";
            color: rgb(128,128,255);
        }
        
        #btn_spelling:pressed {
            font: 14px "웰컴체 Regular";
            color: rgb(88,88,255);
            padding-left: 6px;
            padding-top: 5px;
        }""")

    # 굵게
    def set_bold(self):
        if self.bold:
            self.edt.setFontWeight(QFont.Normal)
            self.bold = False
        else:
            self.edt.setFontWeight(QFont.Bold)
            self.bold = True

    # 기울기
    def set_italic(self):
        italic = bool(self.edt.fontItalic())
        self.edt.setFontItalic(False) if italic else self.edt.setFontItalic(True)

    # 밑줄
    def set_underline(self):
        under = bool(self.edt.fontItalic())
        self.edt.setFontUnderline(False) if under else self.edt.setFontUnderline(True)

    # 폰트 사이즈 변경
    def set_font_size(self):
        size = int(self.cbx_fontsize.currentText())
        self.edt.selectAll()
        self.edt.setFontPointSize(size)

