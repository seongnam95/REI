import sys

from PySide6.QtWidgets import *
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtGui import *
from PySide6.QtCore import *


class WebPageViewer(QMainWindow):
    def __init__(self):
        super(WebPageViewer, self).__init__()

        self.web_viewer = QWebEngineView(self)
        self.web_viewer.load(QUrl('https://cloud.eais.go.kr/report/BCIAAA04V01?param=U2FsdGVkX19OcmXf1Ku1fGlI94HlcKmT3SF3iPH7kR9q5t54Mqv3wHJlKwdIOFVLOnwJEzAmZfENRPWkzloRgWIa3jf0BxacGrza3%2Fp5O3z6u9XeJJASKoTA8EQUN2eNXkvKIpfYKkxEgb2arykSVgeEc8kogn1EKef0Q3CwjxFD8Tsh5Gq8MGWBl52bAF4eisJ%2FbIM876BE%2Bmqe8SxHnBdShOgPaye6nzIWwIkkVnlUjCrQf1IcR1xlpPonT15ehgv3NFgrPhHrrYTINAhj5YqFmlNQo0%2F9gO1d8f1xMy%2Fd6JNoozUtAazViTygvImd0WjXWboiLKaLWmPFnUXy9o4TaysoATKwfd%2FSrnDBRUTGK5miPUK2S4zNknowR5Qu5MDkna0vTtDlZU9EsAKUqIkGxqhVvYup3NFmnvNrsjxogBXwq5en0pdmI3RIheyKhZGm%2Fn7%2Fzf0carzn%2BxaKw0T16ZW0hwITB5i%2BvlMam9ViSj58RfusYTSO5QbI%2FD7WwuAuSlZimCitAhOH%2Bcr14NNTQXUJXbpv%2BatMKNweM3EL3Vwj4%2Bh0beUsHpWL84Zfgj7%2F1tN9H%2BMUNQmxxFDRkmamWvRK5%2FiMBSZfQr7QU0v0l4HJfdBX9zpjXRuXA4n7GZAMG6SspOlmV19Dd0OePFebQmlkEBn2bxdE6j47ykaZEObrqXzUn20bmIc8R3Hv&actionId=BCIAAA04L01'))
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
