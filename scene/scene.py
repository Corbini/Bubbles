from PyQt6.QtWidgets import QGraphicsView, QGraphicsScene
from PyQt6.QtGui import QResizeEvent
from bubble import BubbleCreator, Bubble
from PyQt6.QtCore import QPoint


class Scene(QGraphicsView):

    def __init__(self, parent,  width, height):
        self.plane = QGraphicsScene(0, 0, width, height)
        super().__init__(self.plane)
        self.setParent(parent)
        Bubble.set_scene(self.plane)

        self.builder = BubbleCreator()
        self.pressed = False

    def mousePressEvent(self, event) -> None:
        if self.pressed is False:
            super().mousePressEvent(event)

            if self.check_click(event):
                self.pressed = True

    def check_click(self, event):
        print(self.itemAt(event.pos()))
        if self.itemAt(event.pos()) is None:
            position = event.pos()
            self.builder.create(position)
            return

        return

    def mouseReleaseEvent(self, event) -> None:
        self.builder.stop_grow()
        self.pressed = False

    def resizeEvent(self, event: QResizeEvent) -> None:
        size = event.size()
        self.plane.setSceneRect(0, 0, size.width(), size.height())
