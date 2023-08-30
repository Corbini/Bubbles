from PyQt6.QtWidgets import QGraphicsView, QGraphicsScene
from PyQt6.QtGui import QResizeEvent
from bubble import Bubble


class Scene(QGraphicsView):

    def __init__(self, parent,  width, height):
        self.plane = QGraphicsScene(0, 0, width, height)
        super().__init__(self.plane)
        self.setParent(parent)
        # Bubble.set_scene(self.plane)

        # self.bubble = Bubble()

    def mousePressEvent(self, event) -> None:
        pass

    def mouseReleaseEvent(self, event) -> None:
        pass

    def resizeEvent(self, event: QResizeEvent) -> None:
        size = event.size()
        self.plane.setSceneRect(0, 0, size.width(), size.height())
