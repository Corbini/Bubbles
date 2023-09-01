from PyQt6.QtWidgets import QGraphicsPixmapItem, QGraphicsScene
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import QPointF
from physics import PhysicsTimer


class Bubble(QGraphicsPixmapItem):
    __scene: QGraphicsScene = None

    @classmethod
    def set_scene(cls, scene: QGraphicsScene):
        cls.__scene = scene
        cls.updater = PhysicsTimer()

    def __init__(self, from_left: int = 0, from_top: int = 0):
        self.image = QPixmap(QImage("images/bubble.png"))
        self.width = 40.0

        QGraphicsPixmapItem.__init__(self, self.image)
        self.update_scale()
        self.setPos(from_left - self.width/2, from_top - self.width/2)
        self.__scene.addItem(self)
        self.timer = 0
        self.increment = 4

        self.updater.add_function(self.physics)

    def __del__(self):
        self.updater.remove_function(self.physics)

    def mousePressEvent(self, event) -> None:
        super().mouseReleaseEvent(event)

    def mouseReleaseEvent(self, event) -> None:
        super().mouseReleaseEvent(event)

        self.__scene.removeItem(self)

    def update_scale(self):
        scale = self.width/self.image.width()
        self.setScale(scale)

    def grow(self):
        self.width += self.increment
        self.update_scale()
        self.moveBy(-self.increment/2, -self.increment/2)

    def physics(self):
        movement = QPointF(0, -1)
        pos = self.pos()
        if pos.y() + movement.y() < 0:
            movement.setY(0 - pos.y())

        self.moveBy(movement.x(), movement.y())
        for item in self.collidingItems():
            self.__scene.removeItem(item)
