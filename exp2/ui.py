import sys

from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QPushButton, QDialog, QLineEdit, QLabel, QGridLayout

from Board import *


class GridX(QDialog):

    def __init__(self, k, sx, sy, size=30):
        super().__init__()
        self.k = k
        self.sx = sx
        self.sy = sy
        self.size = size
        self.setUI()

    def setUI(self):
        self.resize(self.size * (1 << self.k) + 1, self.size * (1 << self.k) + 1)
        self.setWindowTitle("棋盘覆盖图像")

    def paintEvent(self, QPaintEvent):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        g = Grid(self.k)
        drawGrid(g, self.sx, self.sy, g.getK(), 1, 1)
        info = g.generateInfo(self.size)
        for i in range(len(info)):
            if info[i].color == 0:
                brush = QBrush()
                brush.setStyle(Qt.DiagCrossPattern)
                qp.setBrush(brush)
                qp.drawRect(info[i].sx, info[i].sy, self.size, self.size)
            else:
                qp.setBrush(
                    QColor((info[i].color * 123) % 256, (info[i].color * 456) % 256, (info[i].color * 789) % 256))
                qp.drawRect(info[i].sx, info[i].sy, self.size, self.size)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def showImage(self):
        self.show()


class UI(QWidget):

    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        #self.resize(50, 50)
        self.setWindowTitle("棋盘覆盖")
        self.center()

        lbK = QLabel(self)
        lbK.setText("K值")
        qleK = QLineEdit(self)
        qleK.setText('3')
        qleK.textChanged[str].connect(self.onChangeK)
        self.k = 3

        lbSX = QLabel(self)
        lbSX.setText("特殊块坐标X")
        qleSX = QLineEdit(self)
        qleSX.setText('2')
        qleSX.textChanged[str].connect(self.onChangeSX)
        self.sx = 2

        lbSY = QLabel(self)
        lbSY.setText("特殊块坐标Y")
        qleSY = QLineEdit(self)
        qleSY.setText('3')
        qleSY.textChanged[str].connect(self.onChangeSY)
        self.sy = 3

        self.btne = QPushButton('退出程序', self)
        self.btng = QPushButton("生成棋盘", self)
        self.btne.clicked.connect(QCoreApplication.instance().quit)
        self.btng.clicked.connect(self.generateImage)

        grid = QGridLayout()
        grid.setSpacing(8)

        grid.addWidget(lbK, 1, 0)
        grid.addWidget(qleK, 1, 1)

        grid.addWidget(lbSX, 2, 0)
        grid.addWidget(qleSX, 2, 1)

        grid.addWidget(lbSY, 3, 0)
        grid.addWidget(qleSY, 3, 1)

        grid.addWidget(self.btne, 4, 1)
        grid.addWidget(self.btng, 4, 0)
        self.setLayout(grid)
        self.show()

    def generateImage(self):
        self.image = GridX(self.k, self.sx, self.sy)
        self.image.show()

    def onChangeK(self, text):
        try:
            self.k = int(text)
        except:
            pass

    def onChangeSX(self, text):
        try:
            self.sx = int(text)
        except:
            pass

    def onChangeSY(self, text):
        try:
            self.sy = int(text)
        except:
            pass

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = UI()
    sys.exit(app.exec_())
