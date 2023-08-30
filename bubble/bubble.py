from PyQt6.QtWidgets import QGraphicsPixmapItem, QGraphicsScene
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import QPointF


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

    def mousePressEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        self.__scene.removeItem(self)

    def update_scale(self):
        scale = self.width/self.image.width()
        self.setScale(scale)

    def grow(self):
        self.width += 4
        self.update_scale()
        self.moveBy(-2, -2)

    def float(self):
        pass
