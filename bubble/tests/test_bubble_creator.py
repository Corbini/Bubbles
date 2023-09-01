import unittest
import sys
import time
from PyQt6.QtWidgets import QGraphicsScene, QApplication
from PyQt6.QtCore import QPointF
from bubble.bubble_creator import BubbleCreator, Bubble


app = QApplication(sys.argv)


class TestBubbleCreator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance()
        if cls.app is None:
            cls.app = QApplication(sys.argv)

        cls.scene = QGraphicsScene()
        Bubble.set_scene(cls.scene)

    def setUp(self) -> None:
        self.creator = BubbleCreator()

    def tearDown(self):
        self.scene.clear()
        del self.creator

    def test_create(self):
        position = QPointF(10, 10)
        offset = QPointF(20, 20)
        self.creator.create(position)

        self.assertTrue(isinstance(self.creator.bubble, Bubble))
        self.assertEqual(position - offset, self.creator.bubble.pos())

    def test_stop_grow(self):
        position = QPointF(10, 10)
        offset = QPointF(20, 20)
        self.creator.create(position)

        time.sleep(1.01)

        bubble = self.creator.bubble
        calculated_width = bubble.increment*10
        self.assertEqual(calculated_width, bubble.width)

        self.creator.stop_grow()
        self.assertEqual(self.creator.bubble, None)
        self.assertEqual(self.creator.timer, None)


if __name__ == '__main__':
    unittest.main()
