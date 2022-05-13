import sys

from PySide6.QtWidgets import *
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtGui import *
from PySide6.QtCore import *


class WebPageViewer(QMainWindow):
    def __init__(self):
        super(WebPageViewer, self).__init__()

        self.web_viewer = QWebEngineView(self)
        self.web_viewer.load(QUrl('https://cloud.eais.go.kr/report/BCIAAA04V01?param=U2FsdGVkX1%2BpoL5UMxW8v7V3xXBBAB4I1JMDDu77dK7RF8wUUzQn28MiUytAQ8uIviuWqHsK%2BPbFreC9N1TGGE%2BjmbPPMtyPyyUqDEkOJmNI%2F4nUCABw%2Bm4plddeEQFY77AKJCLVKQ6f9t%2FDb9Jlzl48lzlt5IVhdTWaa3iMNJL0S6XzYjs8NZwfQNSJ8txNHZtUC6kHWBmtcw8Te7OQAOy43OJM9Ov3qDo2oDK%2BPUrMiHByk3JWVkiYSSo%2BDW9N7NXvln0dFWLUeJtED3%2BPNYSG66Cp7YvQK8hu9vSwWfxZEeUg2hoXMLcUKqaE84CcqgFX%2Fx0N%2F9aQI5HCVyav8WGoXDHyahXZbZC6JUNnbMtTGU3rhRlANfNxQL%2Fu3H2dUtQUiCUKdTsM1GUdoLozuYHJgQONe%2F%2FrQ%2Fnl5M%2FduKzZgEA6%2B8Gf%2B89yJnxl2eUIXVp3T4x0aP7K1nldpWqlUTs8Bbz%2ByuSzz4orKYCKm2msZLhahwnyYq8cvNFyv%2B6jP49zCv%2FKizu1rTWvhy0xA6woCHOoMB9CLIQi5HtmfnJYZ97i%2Bc7DN%2FOueoi7HFzVMAIaH0wzkDCTV8b1PRyFcNXT%2BjXYutTgAK5kvyN7A5VDE4BiF%2FTZc6ljT0PnwVl30LjS%2FXOvwsIDvOgmiKLsNsznWGMMrVknviHx4%2B09a8jdoc9QdI7DUprtfpho8TW9&actionId=BCIAAA04L01'))
        self.web_viewer.setGeometry(0, 0, 1200, 900)
        self.web_viewer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.show()
        # self.webEngineView_Test.loadStarted.connect(self.printLoadStart)
        # self.webEngineView_Test.loadProgress.connect(self.printLoading)
        # self.webEngineView_Test.loadFinished.connect(self.printLoadFinished)
        # self.webEngineView_Test.urlChanged.connect(self.urlChangedFunction)


# 예외 오류 처리
def my_exception_hook(exctype, value, traceback):
    sys.excepthook(exctype, value, traceback)


sys._excepthook = sys.excepthook
sys.excepthook = my_exception_hook

app = QApplication()
window = WebPageViewer()
app.exec()
