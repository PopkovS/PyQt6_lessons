from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# Only needed for access to command line arguments
import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("My app")
        label = QLabel("Test some text")
        label.setAlignment(Qt.AlignCenter)
        # self.setCentralWidget(label)
        self.setCentralWidget(label)


app = QApplication(sys.argv)

windows = MainWindow()
windows.show()

app.exec_()
