import sys
from time import sleep

from PyQt5.QtCore import QRect, Qt, QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit, \
    QProgressBar, QSlider, QMessageBox, QDialog, QVBoxLayout, QPushButton


class Message(QDialog):
    def __init__(self, msg):
        super().__init__()
        self.setUI()
        self.label.setText(msg)

    def setUI(self):
        self.verticalLayoutWidget = QWidget(self)
        self.verticalLayoutWidget.setGeometry(QRect(10, 9, 181, 121))

        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.label = QLabel(self.verticalLayoutWidget)
        self.verticalLayout_2.addWidget(self.label)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.close)
        self.retranslateUi()

    def retranslateUi(self):
        self.setWindowTitle("Message")
        self.pushButton.setText("Confirm")


class Login(QWidget):
    def __init__(self):
        super().__init__()

        self.setUI()

    def setUI(self):
        self.setObjectName("Form")
        self.resize(358, 246)

        self.gridLayoutWidget = QWidget(self)
        self.gridLayoutWidget.setGeometry(QRect(20, 20, 321, 111))

        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.horizontalSlider = QSlider(self)
        self.horizontalSlider.setGeometry(QRect(29, 220, 311, 20))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(QRect(20, 150, 321, 61))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.horizontalSlider.valueChanged.connect(self.setProgressvalue)
        self.label_3 = QLabel(self)
        self.label_3.setGeometry(QRect(120, 130, 141, 20))
        self.setContent()
        self.show()

    def setContent(self):
        self.setWindowTitle("Login")
        self.label.setText("Username:")
        self.lineEdit.setPlaceholderText("username")
        self.lineEdit_2.setPlaceholderText("password")
        self.label_2.setText("Password:")
        self.label_3.setText("请拖动滑块以登录")

    def setProgressvalue(self):
        self.progressBar.setValue(self.horizontalSlider.value() + 1)
        # print(self.progressBar.value())
        if self.progressBar.value() == 100:
            username = self.lineEdit.text()
            password = self.lineEdit_2.text()
            if username == 'zwlin' and password == '123456':
                sleep(1)
                self.msg = Message("Login Success")
                self.msg.show()
            else:
                sleep(1)
                self.msg = Message("Login Failed")
                self.msg.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Login()
    sys.exit(app.exec_())
