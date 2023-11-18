import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from random import randint


class YellowCircle(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
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
        qp.setBrush(QColor(255, 255, 0))
        x, y = randint(0, 450), randint(0, 430)
        d = (randint(10, min(500 - x, 480 - y)))
        qp.drawEllipse(x, y, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircle()
    ex.show()
    sys.exit(app.exec_())
