import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


class TrayIcon(QSystemTrayIcon):
    def __init__(self, parent=None):
        super(TrayIcon, self).__init__(parent)
        self.showMenu()
        self.other()

    def showMenu(self):


        self.menu1.addAction(self.showAction1)
        self.menu1.addAction(self.showAction2)
        self.menu.addMenu(self.menu1, )

        self.menu.addAction(self.showAction1)
        self.menu.addAction(self.showAction2)
        self.menu.addAction(self.quitAction)
        self.menu1.setTitle("    ")
        self.setContextMenu(self.menu)

    def other(self):
        self.activated.connect(self.iconClied)
        #
        self.messageClicked.connect(self.mClied)
        #
        self.setIcon(QIcon("ico.ico"))
        self.icon = self.MessageIcon()
        #

    def iconClied(self, reason):
        "    icon              ，1       ，2   ，3     ，4        "
        if reason == 2 or reason == 3:
            pw = self.parent()
            if pw.isVisible():
                pw.hide()
            else:
                pw.show()
        print(reason)

    def mClied(self):
        self.showMessage("  ", "     ", self.icon)

    def showM(self):

        self.showMessage("  ", "    ", self.icon)

    def quit(self):
        "    ，       "
        self.setVisible(False)
        self.parent().exit()
        qApp.quit()
        sys.exit()

class window(QWidget):
    def __init__(self, parent=None):
        super(window, self).__init__(parent)
        ti = TrayIcon(self)
        ti.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = window()
    w.show()
    sys.exit(app.exec_())