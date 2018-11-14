import sys

from PyQt5.QtCore import QBasicTimer, pyqtSignal, Qt, QCoreApplication
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtWidgets import QDialog, QApplication, QLabel, QLineEdit, QPushButton, QGridLayout

from prb2 import *


class MAT(QDialog):
    step = 1
    stepsignal = pyqtSignal()

    def __init__(self, mx=5, my=5, size=50):
        super().__init__()
        self.mx = mx
        self.my = my
        self.size = size
        self.setUI()

    def setUI(self):
        self.timer = QBasicTimer()
        self.mat = Matrix(self.mx, self.my)
        self.resize(self.size * self.my + 1, self.size * self.mx + 1)
        self.info = self.mat.draw(self.size)
        self.setWindowTitle("走格子")
        self.timer.start(100, self)
        #self.stepsignal.connect(self.doAction)
        # self.show()

    def timerEvent(self, QTimerEvent):
        if self.step >= self.mx * self.my - 1:
            self.timer.stop()

        self.step += 1
        self.update()


    def paintEvent(self, QPaintEvent):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor("#66ccff"))
        for i in range(self.step):
            qp.drawRect(self.info[i].sx, self.info[i].sy, self.info[i].size, self.info[i].size)
        qp.end()

    def doAction(self):
        self.update()


class UI2(QWidget):
    mx = 8
    my = 8
    size = 5

    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.resize(50, 70)
        self.setWindowTitle("走格子")
        lbX = QLabel(self)
        lbX.setText("棋盘大小 X轴")
        inX = QLineEdit("8", self)
        inX.textChanged[str].connect(self.onChangeX)

        lbY = QLabel(self)
        lbY.setText("棋盘大小 Y轴")
        inY = QLineEdit("8", self)
        inY.textChanged[str].connect(self.onChangeY)

        self.btne = QPushButton('退出程序', self)
        self.btng = QPushButton("演示", self)
        self.btne.clicked.connect(QCoreApplication.instance().quit)
        self.btng.clicked.connect(self.generateImage)

        grid = QGridLayout()
        grid.setSpacing(8)

        grid.addWidget(lbX, 1, 0)
        grid.addWidget(inY, 1, 1)
        grid.addWidget(lbY, 2, 0)
        grid.addWidget(inX, 2, 1)
        grid.addWidget(self.btne, 3, 0)
        grid.addWidget(self.btng, 3, 1)

        self.setLayout(grid)
        self.show()

    def generateImage(self):
        self.play = MAT(self.mx, self.my)
        self.play.show()

    def onChangeX(self, mx):
        if mx != '':
            self.my = int(mx)

    def onChangeY(self, mx):
        if mx != '':
            self.mx = int(mx)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = UI2()
    sys.exit(app.exec_())
