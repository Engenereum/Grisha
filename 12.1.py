import random

from PyQt5 import QtCore
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel





def pipi():
    window = QMainWindow()
    window.setWindowTitle('PiPiDastr')
    window.setFixedSize(500,300)
    pixmap = QPixmap()
    pixmap.load('metelka-pipidastr.jpg')


    label = QLabel(window)
    label.setPixmap(pixmap.scaled(500,300))
    label.setFixedSize(500,300)

    label2 = QLabel(window)
    font=QFont('times',80)
    label2.setFont(font)
    label2.setFixedSize(500,250)
    label2.move(0,50)
    label2.setText('PIPIDASTR')
    x, y = random.randint(0, 1920),random.randint(0, 1080)
    window.move(x,y)
    window.show()
    return window

app = QApplication([])
windows = []
for i in range(10):
    windows.append(pipi())


app.exec()