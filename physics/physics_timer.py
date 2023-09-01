from PyQt6.QtCore import QTimer


class PhysicsTimer:

    def __init__(self):
        self.list = list()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(50)

    def add_function(self, function):
        self.list.append(function)

    def remove_function(self, function):
        self.list.remove(function)

    def update(self):
        for function in self.list:
            function()
