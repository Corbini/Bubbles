from PyQt6.QtWidgets import QLabel, QMainWindow, QApplication
from PyQt6.QtGui import *
import sys


class Window(QMainWindow):

    def __init__(self):
        self.app = QApplication(sys.argv)

        # window setup
        super().__init__()
        self.setWindowTitle("Bubbles")
        self.setWindowIcon(QIcon('images/icon.png'))
        self.setFixedSize(1280, 960)
        self.background = QLabel()
        self.setCentralWidget(self.background)
        self.show()
        sys.exit(self.app.exec())

    def resizeEvent(self, event: QResizeEvent):
        super().resizeEvent(event)