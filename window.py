from PyQt6.QtWidgets import QLabel, QMainWindow, QApplication
from PyQt6.QtGui import *
import sys
from scene import Scene


class Window(QMainWindow):

    def __init__(self):
        self.app = QApplication(sys.argv)

        # window setup
        super().__init__()
        self.setWindowTitle("Bubbles")
        self.setWindowIcon(QIcon('images/icon.png'))
        width = 640
        height = 640
        self.setMinimumSize(width, height)
        self.background = QLabel()
        self.setCentralWidget(self.background)

        self.scene = Scene(self, width, height)

        self.show()
        sys.exit(self.app.exec())

    def resizeEvent(self, event: QResizeEvent):
        super().resizeEvent(event)
        self.scene.resize(event.size())
