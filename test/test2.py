import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import SIGNAL, QObject

def func():
    print("func has been called!")


app = QApplication(sys.argv)
button = QPushButton("Call func")
QObject.connect(button, SIGNAL('clicked()'), func)
button.show()

sys.exit(app.exec_())