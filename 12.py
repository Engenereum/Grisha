import datetime

from PyQt5 import QtCore
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

click_count = 0
record = 0


def func():
    global click_count
    click_count += 1
    label.setText(str(click_count))


def timer_func():
    global click_count
    global record
    if click_count>record:
        record = click_count
    click_count = 0
    label2.setText(f"рекорд: {record}")


def timer2_func():
    now = datetime.datetime.now()
    label3.setText(str(now))

app = QApplication([])
window = QMainWindow()

window.setWindowTitle('Virus')
window.setFixedSize(500, 300)
# window.setCursor(QtCore.Qt.WaitCursor)
# window.setWindowOpacity(0.5)

button = QPushButton(window)
button.setFixedSize(70, 30)
button.move(200, 100)
button.setText('Click')
button.clicked.connect(func)

label = QLabel(window)
label.setText('0')
label.move(230, 150)


label2 = QLabel(window)
label2.setText('рекорд: 0')
label2.move(200, 175)


label3 = QLabel(window)
label3.setText('0')
label3.move(160, 200)
label3.setFixedSize(200,20)


timer = QTimer()
timer.timeout.connect(timer_func)
timer.start(10*1000)


timer2 = QTimer()
timer2.timeout.connect(timer2_func)
timer2.start(1*1000)

















window.show()
app.exec()
