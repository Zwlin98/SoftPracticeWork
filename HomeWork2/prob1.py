import os
import signal

import psutil
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QTableWidget, QHeaderView, \
    QTableWidgetItem, QAbstractItemView, QVBoxLayout, QMessageBox

import sys


class ListOfProcess(QWidget):

    def __init__(self):
        super().__init__()

        self.setUI()

    def getTable(self):
        ppids = psutil.pids()
        self.pids = []
        for p in ppids:
            try:
                if psutil.Process(p).username() == 'zwlin':
                    self.pids.append(p)
            except:
                pass

        self.table = QTableWidget(len(self.pids), 3)
        self.table.setHorizontalHeaderLabels(['PID', '进程名', '用户'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setVisible(False)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        i = 0
        for pid in self.pids:
            process = psutil.Process(pid)
            self.table.setItem(i, 0, QTableWidgetItem(str(pid)))
            self.table.setItem(i, 1, QTableWidgetItem(process.name()))
            self.table.setItem(i, 2, QTableWidgetItem(process.username()))
            i += 1

    def setUI(self):
        self.getTable()

        self.setWindowTitle("List of Process")

        self.resize(500, 600)
        self.btnk = QPushButton("Kill")
        self.btnq = QPushButton('Exit')

        self.btnk.clicked.connect(self.killProcess)
        self.btnq.clicked.connect(QCoreApplication.instance().quit)

        grid = QVBoxLayout()

        grid.addWidget(self.table)
        grid.addWidget(self.btnk)
        grid.addWidget(self.btnq)

        self.setLayout(grid)

        self.show()

    def killProcess(self):
        row = self.table.currentRow()
        pid = self.pids[row]
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to kill this process", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            try:
                os.kill(pid, signal.SIGKILL)
                pass
            except:
                pass
        self.table.removeRow(row)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ListOfProcess()
    sys.exit(app.exec_())
