from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtCore import Qt

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500,300)
        self.button = QPushButton(self)
        self.setMouseTracking(False)
        self.offset = None
        self.show()

    def keyPressEvent(self, event):
        key = event.key()
        x = self.button.x()
        y = self.button.y()
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

        if x + dx + self.button.width() > self.width():
            self.move(window_x + dx,window_y)
        elif x + dx < 0:
            self.move(window_x + dx, window_y)
        elif y + dy + self.button.height() > self.height():
            self.move(window_x + dx, window_y + dy)
        elif y + dy < 0:
            self.move(window_x + dx, window_y + dy)
        else:
            self.button.move(x+dx,y+dy)



    def keyReleaseEvent(self, event):
        key = event.key()
        print(f'release {key}')


    def mouseReleaseEvent(self, event):
        print('Release mouse')
    def mousePressEvent(self, event):
        self.offset = event.pos()
        print('press mouse')
    def mouseMoveEvent(self, event):
        print('move mouse')
        x = event.globalX()
        y = event.globalY()
        dx = self.offset.x()
        dy = self.offset.y()
        self.move(x+dx,y+dy)
    def mouseDoubleClickEvent(self, event):
        print('double click mouse')





if __name__ == '__main__':
    app = QApplication([])
    wnd = MyWindow()

    app.exec()

