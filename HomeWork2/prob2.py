import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout


class Judge(QWidget):
    def __init__(self):
        super().__init__()

        self.setUI()

    def setUI(self):
        self.setWindowTitle("判断汉字")
        lbX = QLabel(self)
        lbX.setText("请输入内容")
        self.inX = QLineEdit("我是汉字", self)

        lbY = QLabel(self)
        lbY.setText("判断结果")
        self.inY = QLineEdit("请单击判断结果", self)
        self.inY.setReadOnly(True)

        self.btne = QPushButton('退出程序', self)
        self.btng = QPushButton("判断结果", self)
        self.btne.clicked.connect(QCoreApplication.instance().quit)
        self.btng.clicked.connect(self.judge)

        grid = QGridLayout()
        grid.setSpacing(8)

        grid.addWidget(lbX, 1, 0)
        grid.addWidget(self.inX, 1, 1)
        grid.addWidget(lbY, 2, 0)
        grid.addWidget(self.inY, 2, 1)
        grid.addWidget(self.btne, 3, 0)
        grid.addWidget(self.btng, 3, 1)

        self.setLayout(grid)
        self.resize(300, 180)
        self.show()

    def judge(self):
        str = self.inX.text()
        for char in str:
            if not '\u4e00' <= char <= '\u9fff':
                self.inY.setText("输入的不全是汉字")
                return
        self.inY.setText("输入的全是汉字")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Judge()
    sys.exit(app.exec_())
