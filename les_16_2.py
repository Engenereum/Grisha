from PyQt5.QtGui import QPainter, QBrush, QPen, QColor
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QApplication

from les14_2 import MyWindow

from PyQt5.QtCore import Qt, QTimer, QUrl

from les14_2 import random


class MyWindowRewrited(MyWindow):
    def __init__(self):
        super().__init__([5, 5])
        self.timer.stop()
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_func)
        self.is_need_to_draw_window = True
        self.timer.start(100)
        self.music = QMediaPlayer()
    def closeEvent(self, event):
        self.update()
        self.music.setMedia(QMediaContent(QUrl('strashno.mp3')))
        self.music.play()
        event.ignore()


    def timer_func(self):
        self.is_need_to_draw_window = not self.is_need_to_draw_window
        self.update()
    def keyPressEvent(self, event):
        key = event.key()
        window_x = self.x()
        window_y = self.y()
        dx = 0
        dy = 0

        if key == Qt.Key_W:
            dy = -5
        elif key == Qt.Key_S:
            dy = 5
        elif key == Qt.Key_A:
            dx = -5
        elif key == Qt.Key_D:
            dx = 5


        self.move(window_x + dx, window_y + dy)

    def paintEvent(self, event):
        if self.is_need_to_draw_window:
            painter = QPainter(self)
            pen = QPen()
            brush = QBrush()
            pen.setWidth(12)
            pen.setColor(QColor(0, 0, 0))
            painter.setPen(pen)

            painter.drawLine(0, 0, self.width(), self.height())
            painter.drawLine(self.width(), 0, 0, self.height())


if __name__ == "__main__":
    app = QApplication([])
    wnd = []
    for i in range(30):
        wnd.append(MyWindow([random.randint(1, 20), random.randint(1, 20)]))
    wnd2 = MyWindowRewrited()
    app.exec()
