import sys

from PyQt5.QtCore import QUrl, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QAction, QLineEdit, QTabWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.setWindowTitle('Browser')

        self.urlBar = QLineEdit()
        self.urlBar.returnPressed.connect(self.navigatorToUrl)

        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.tabBarDoubleClicked.connect(self.tabOpenDoubleClick)
        self.tabs.currentChanged.connect(self.currentTabChanged)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.closeCurrentTab)

        self.addNewTab(QUrl('https://baidu.com'), 'Homepage')
        self.setCentralWidget(self.tabs)

        navigationBar = QToolBar('Navigation')
        navigationBar.setIconSize(QSize(16, 16))
        self.addToolBar(navigationBar)

        backButton = QAction(QIcon('icons/back.png'), 'Back', self)
        nextButton = QAction(QIcon('icons/next.png'), 'Forward', self)
        stopButton = QAction(QIcon('icons/cross.png'), 'Stop', self)
        reloadButton = QAction(QIcon('icons/renew.png'), 'Reload', self)

        backButton.triggered.connect(self.tabs.currentWidget().back)
        nextButton.triggered.connect(self.tabs.currentWidget().forward)
        stopButton.triggered.connect(self.tabs.currentWidget().stop)
        reloadButton.triggered.connect(self.tabs.currentWidget().reload)

        navigationBar.addAction(backButton)
        navigationBar.addAction(nextButton)
        navigationBar.addAction(stopButton)
        navigationBar.addAction(reloadButton)
        navigationBar.addSeparator()
        navigationBar.addWidget(self.urlBar)
        self.resize(1500, 900)
        self.show()

    def addNewTab(self, qurl=QUrl(''), label='blank'):
        browser = QWebEngineView()
        browser.load(qurl)

        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)

        browser.urlChanged.connect(lambda qurl, browser=browser: self.reNewUrlBar(qurl, browser))
        self.urlBar.setText(qurl.toString())
        browser.loadFinished.connect(lambda _, i=i, browser=browser:
                                     self.tabs.setTabText(i, browser.page().title()))

    def navigatorToUrl(self):
        self.tabs.currentWidget().load(QUrl(self.urlBar.text()))

    def closeCurrentTab(self, i):
        if self.tabs.count() < 2:
            return
        self.tabs.removeTab(i)

    def currentTabChanged(self, i):
        qurl = self.tabs.currentWidget().url()
        self.reNewUrlBar(qurl, self.tabs.currentWidget())

    def tabOpenDoubleClick(self, i):
        if i == -1:
            self.addNewTab(QUrl("https://baidu.com"))

    def reNewUrlBar(self, q, browser=None):
        if browser != self.tabs.currentWidget():
            return
        self.urlBar.setText(q.toString())
        self.urlBar.setCursorPosition(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
