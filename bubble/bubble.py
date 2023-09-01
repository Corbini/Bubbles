from PyQt6.QtWidgets import QGraphicsPixmapItem, QGraphicsScene
from PyQt6.QtGui import QPixmap, QImage, QMouseEvent
from PyQt6.QtCore import QPointF
import time


class Bubble(QGraphicsPixmapItem):
    __scene: QGraphicsScene = None

    @classmethod
    def set_scene(cls, scene: QGraphicsScene):
        cls.__scene = scene

    def __init__(self, from_left: int = 0, from_top: int = 0):
        self.image = QPixmap(QImage("images/bubble.png"))
        self.width = 40.0

        QGraphicsPixmapItem.__init__(self, self.image)
        self.update_scale()
        self.setPos(from_left - self.width/2, from_top - self.width/2)
        self.__scene.addItem(self)
        self.timer = 0
        self.increment = 4

    def mousePressEvent(self, event) -> None:
        self.__scene.removeItem(self)
        self.timer = time.time_ns()

    def mouseReleaseEvent(self, event) -> None:
        duration = time.time_ns() - self.timer
        if duration < 200:
            self.__scene.removeItem(self)

    def update_scale(self):
        scale = self.width/self.image.width()
        self.setScale(scale)

    def grow(self):
        self.width += self.increment
        self.update_scale()
        self.moveBy(-self.increment/2, -self.increment/2)

    def float(self):
        pass
