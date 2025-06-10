import random

from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow




class MyWindow(QMainWindow):
    def __init__(self,speed:list):
        super().__init__()
        self.window_speed = speed
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.move(0,0)

        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_func)
        self.timer.start(10)
        self.show()


    def timer_func(self):
        w = self.width()
        h = self.height()
        x = self.x()
        y = self.y()

        if self.window_speed[0] > 0 and x + w + self.window_speed[0] >= 1920:
            self.window_speed[0] = -self.window_speed[0]
        if self.window_speed[0] < 0 and x <= 0:
            self.window_speed[0] = -self.window_speed[0]
        if self.window_speed[1] > 0 and y + h + self.window_speed[1] >= 1080:
            self.window_speed[1] = -self.window_speed[1]
        if self.window_speed[1] < 0 and y + self.window_speed[1] <= 0:
            self.window_speed[1] = -self.window_speed[1]

        self.move(x + 1, y + 1)
        self.move(x + self.window_speed[0], y + self.window_speed[1])


if __name__ == "__main__":
    app = QApplication([])
    wnd = []
    for i in range(30):
        wnd.append(MyWindow([random.randint(1,20) , random.randint(1,20)]))

    app.exec()
