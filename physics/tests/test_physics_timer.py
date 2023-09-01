import unittest
import time
from PyQt6.QtWidgets import QApplication
import sys
from physics.physics_timer import PhysicsTimer


class TestPhysicsTimer(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.app = QApplication.instance()
        if cls.app is None:
            cls.app = QApplication(sys.argv)

    def setUp(self) -> None:
        self.run = TestRun()

    def test_init(self):
        physics = PhysicsTimer()

    def test_add_function(self):
        physics = PhysicsTimer()
        physics.add_function(self.run.function)
        physics.timer.timeout.connect(self.run.function)

    def test_remove_function(self):
        physics = PhysicsTimer()
        physics.add_function(self.run.function)
        physics.add_function(self.run.function)

        physics.remove_function(self.run.function)
        physics.remove_function(self.run.function)


class TestRun:
    def __init__(self):
        self.run = False

    def function(self):
        self.run = True
