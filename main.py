import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from random import randint


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.btn = QPushButton(self)
        self.init_ui()

    def init_ui(self):
        self.resize(500, 530)
        self.btn.setGeometry(0, 480, 100, 20)
        self.btn.setText('Нажми меня')


class YellowCircle(Window, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.d = 0

    def setup_ui(self):
        self.btn.show()
        self.btn.clicked.connect(self.up)

    def up(self):
        self.d = 1
        self.update()

    def paintEvent(self, event):
        if self.d:
            qp = QPainter()
            qp.begin(self)
            self.circle(qp)
            qp.end()
            self.d = 0

    def circle(self, qp):
        r, g, b = [randint(0, 255) for _ in range(3)]
        qp.setBrush(QColor(r, g, b))
        x, y = randint(0, 450), randint(0, 430)
        d = (randint(10, min(500 - x, 480 - y)))
        qp.drawEllipse(x, y, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircle()
    ex.show()
    sys.exit(app.exec_())
