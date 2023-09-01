import unittest
import sys
from PyQt6.QtWidgets import QGraphicsScene, QApplication
from PyQt6.QtCore import QPointF
from bubble.bubble import Bubble


class TestBubble(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance()
        if cls.app is None:
            cls.app = QApplication(sys.argv)

        cls.scene = QGraphicsScene()

        Bubble.set_scene(cls.scene)

    def tearDown(self):
        self.scene.clear()

    def test_init(self):
        Bubble.set_scene(None)
        with self.assertRaises(Exception):
            Bubble()

        Bubble.set_scene(self.scene)

        first_bubble = Bubble()
        pos = QPointF(10, 12)
        second_bubble = Bubble(pos.x(), pos.y())
        get_pos = second_bubble.pos()
        offset = QPointF(20, 20)
        self.assertEqual(pos.x() - offset.x(), get_pos.x())
        self.assertEqual(pos.y() - offset.y(), get_pos.y())


if __name__ == '__main__':
    unittest.main()
