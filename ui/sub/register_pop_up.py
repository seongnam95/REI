from PySide6.QtCore import QRect
from PySide6.QtWidgets import QComboBox, QFrame, QLabel, QPushButton, QRadioButton, QWidget

import rei_bot.issuance_registered as ir


class RegisterPopUp(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self._setup_ui()

        self.btn_save.clicked.connect(self.clicked_save_btn)
        self.btn_cancle.clicked.connect(self.hide_pop)

        self.api_data = {'HOST': 'https://api.tilko.net/',
                         'KEY': '6062d22d48734cd3af82837f696730fb'}
        self.user = {'user_id': 'mogsin21', 'user_pw': 'kim2588@',
                     'num_1': 'P3372711', 'num_2': '3234', 'num_pw': 'kim2588'}

    def _setup_ui(self):
        self.resize(240, 180)
        self.setGeometry(QRect(0, 0, 240, 180))
        main_style = """
        QRadioButton {
            font: 14px "웰컴체 Regular";
            color: white;
        }
        QFrame {
            background: rgba(0,0,0,210);
            border-radius: 10px;
        }
        """
        self.setStyleSheet(main_style)

        self.lb_title = QLabel(self)
        self.lb_title.setGeometry(QRect(76, 11, 91, 20))
        self.lb_title.setText("등기부등본 발급")
        self.lb_title.setStyleSheet("""QLabel { font: 15px "웰컴체 Regular";
                                                color: white;
                                                background: rgba(0,0,0,0); } """)

        self.lb_name = QLabel(self)
        self.lb_name.setGeometry(QRect(20, 57, 71, 16))
        self.lb_name.setText("등기기록상태")
        self.lb_name.setStyleSheet("""QLabel { font: 14px "웰컴체 Regular";
                                               color: white;
                                               background: rgba(0,0,0,0); } """)

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
        }
        
        QFrame {
            background: white;
            border: 1px solid gray;
            border-radius: 0px;
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
        self.rbtn_building.setGeometry(QRect(105, 90, 51, 16))
        self.rbtn_building.setText("건 물")

        self.rbtn_land = QRadioButton(self)
        self.rbtn_land.setGeometry(QRect(170, 90, 51, 16))
        self.rbtn_land.setText("토 지")

        btn_style = """
        QPushButton {
            font: 15px "웰컴체 Bold";
            color: rgb(235,235,235);
            border-radius: 7px;
            padding-top: 3px;
            padding-left: 3px;
            background-color: rgb(77,161,192);
        }
        QPushButton:hover { background-color: rgb(97,181,212); }
        QPushButton:pressed { background-color: rgb(57,141,172); }
        """
        self.btn_save = QPushButton(self)
        self.btn_save.setGeometry(QRect(100, 133, 121, 35))
        self.btn_save.setStyleSheet(btn_style)
        self.btn_save.setText("PDF 저 장")

        btn_style = """
        QPushButton {
            font: 15px "웰컴체 Bold";
            color: rgb(235,235,235);
            border-radius: 7px;
            padding-top: 3px;
            padding-left: 3px;
            background-color: rgb(191,77,76);
        }
        QPushButton:hover { background-color: rgb(212,97,86); }
        QPushButton:pressed { background-color: rgb(171,57,56); } """
        self.btn_cancle = QPushButton(self)
        self.btn_cancle.setGeometry(QRect(20, 133, 71, 35))
        self.btn_cancle.setStyleSheet(btn_style)
        self.btn_cancle.setText("취 소")

        self.line_1 = QFrame(self)
        self.line_1.setGeometry(QRect(10, 35, 222, 1))
        self.line_1.setStyleSheet("""
        QFrame {
            background-color: rgba(255,255,255,90);
            color: rgba(255,255,255,90);
        }""")

        self.line_2 = QFrame(self)
        self.line_2.setGeometry(QRect(10, 120, 222, 1))
        self.line_2.setStyleSheet("""
        QFrame {
            background-color: rgba(255,255,255,90);
            color: rgba(255,255,255,90);
        }""")

        self.hide()

    def show_pop(self):
        parent_w, parent_h = self.parent.width(), self.parent.height()
        x = (parent_w / 2) - (self.width() / 2)
        y = (parent_h / 2) - (self.height() / 2)
        self.move(int(x), int(y))

        self.show()

    def hide_pop(self):
        self.hide()

    def clicked_save_btn(self, address, flag, kind):
        self.issuance_thread = ir.IssuanceRegistered(self.api_data, self.user, address, flag, kind)
        self.issuance_thread.threadEvent.workerThreadDone.connect(lambda: self.btn_issuance.setEnabled(True))
        self.issuance_thread.threadEvent.progress.connect(self.issuance_progress_event)
        self.issuance_thread.start()

    def saved_pdf(self, data):
        t_key = data['TransactionKey']
        ir.saved_pdf(t_key)
        print(f'transaction_key : {t_key}')

        # 요청 된 바이너리 PDF 파일로 저장
        with open("new.pdf", "wb") as f:
            f.write(base64.b64decode(response.json()['Message']))