from PySide6.QtCore import QRect
from PySide6.QtWidgets import QComboBox, QFrame, QLabel, QPushButton, QRadioButton, QWidget


class RegisterPopUp(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.resize(240, 180)
        self.setGeometry(QRect(0, 0, 240, 180))
        main_style = """
        QRadioButton {
            font: 14px "웰컴체 Regular";
            color: white;
        }
        QFrame {
            background: rgba(0,0,0,200);
            border-radius: 10px;
        }
        #line_1 {
            color: rgba(255,255,255,90);
        }
        #line_2 {
            color: rgba(255,255,255,90);
        }
        """
        self.setStyleSheet(main_style)

        self.lb_title = QLabel(self)
        self.lb_title.setGeometry(QRect(76, 11, 91, 20))
        self.lb_title.setText("등기부등본 발급")
        self.lb_title.setStyleSheet("""QLabel { font: 15px "웰컴체 Regular";
                                                color: white;
                                                backgrond: white; } """)

        self.lb_name = QLabel(self)
        self.lb_name.setGeometry(QRect(20, 57, 71, 16))
        self.lb_name.setText("등기기록상태")
        self.lb_name.setStyleSheet("""QLabel { font: 14px "웰컴체 Regular";
                                               color: white;
                                               backgrond: white; } """)

        cbx_style = """
        QComboBox {
            border: 1px solid gray;
            padding-top: 3px;
            padding-left: 5px;
            min-width: 6em;
            background: rgb(255, 255, 255);
            font: 14px "웰컴체 Regular";
            color: rgb(40, 40, 40);
        }

        QComboBox:focus {
            color: rgb(70, 70, 70);
        }

        QComboBox:hover {
            border: 1px solid #3498db;
        }

        QComboBox QAbstractItemView::item {
            min-height: 30px;
        }

        QComboBox::drop-down {
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 30px;

            border-left-width: 1px;
            border-left-style: solid;
            border-left-color: darkgray;
            border-top-right-radius: 3px;
            border-bottom-right-radius: 3px;
        }
        """
        flag_items = ['현행', '폐쇄', '현행+폐쇄']
        self.cbx_flag = QComboBox(self)
        self.cbx_flag.addItems(flag_items)
        self.cbx_flag.setGeometry(QRect(100, 49, 121, 28))
        self.cbx_flag.setStyleSheet(cbx_style)

        self.rbtn_set = QRadioButton(self)
        self.rbtn_set.setGeometry(QRect(20, 90, 71, 16))
        self.rbtn_set.setText("집합건물")
        self.rbtn_set.setChecked(True)

        self.rbtn_building = QRadioButton(self)
        self.rbtn_building.setGeometry(QRect(110, 90, 51, 16))
        self.rbtn_building.setText("건 물")

        self.rbtn_land = QRadioButton(self)
        self.rbtn_land.setGeometry(QRect(180, 90, 51, 16))
        self.rbtn_land.setText("토 지")

        btn_style = """
        QPushButton {
            font: 14px "웰컴체 Regular";
            color: rgb(70, 70, 70);
            border-radius: 10px;
            padding-top: 2px;
            padding-left: 2px;
            background-color: rgb(235, 235, 235);
        }

        QPushButton:hover {
            background-color: rgb(235, 235, 235);
        }

        QPushButton:pressed {
            background-color: rgb(215, 215, 215);
        }
        """
        self.btn_save = QPushButton(self)
        self.btn_save.setGeometry(QRect(60, 133, 121, 35))
        self.btn_save.setStyleSheet(btn_style)
        self.btn_save.setText("PDF 저 장")

        self.line_1 = QFrame(self)
        self.line_1.setGeometry(QRect(10, 35, 222, 1))

        self.line_2 = QFrame(self)
        self.line_2.setGeometry(QRect(10, 120, 222, 1))

    def show_pop(self):
        self.show()
