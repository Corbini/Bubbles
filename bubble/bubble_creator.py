from PyQt6.QtCore import QTimer, QPoint
from bubble.bubble import Bubble


class BubbleCreator:

    def __init__(self):

        self.grow_value = 1
        self.timer = None
        self.bubble = None

    def create(self, position: QPoint):
        if self.bubble is None:
            self.bubble = Bubble(position.x(), position.y())
            self.timer = QTimer()
            self.timer.timeout.connect(self.bubble.grow)
            self.timer.start(100)

    def stop_grow(self):
        if self.bubble is not None:
            del self.timer
            self.timer = None
            self.bubble = None
