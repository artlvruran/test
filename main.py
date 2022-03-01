import sys
import random

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor
from Ui import Ui_Form


class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.do_Paint = False

        self.pushButton.clicked.connect(self.drawCircle)

    def drawCircle(self):
        self.do_Paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_Paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
            self.do_Paint = False

    def draw(self, qp):
        x = random.randint(0, self.width())
        y = random.randint(0, self.height())
        d = random.randint(0, min(x, y))
        qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        qp.drawEllipse(x - d, y - d, 2 * d, 2 * d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
