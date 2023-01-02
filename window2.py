import sys
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication
from MainWindow import *


class Window(QMainWindow):
    def __init__(self, parent=None):
        # ------Do Not Touch------
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.offset = None  # Movement Offset
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Remove Default Title Bar

        # Set Window Icons
        self.setup_title_bar()
        # ------Do Not Touch------

        # Methods to move the window

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.offset = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)

        # Method to setup the title bar

    def setup_title_bar(self):
        # Change Window Name
        self.ui.title_label.setText('Wordle Helper')
        # Set Icons
        self.ui.minimize_button.setIcon(QIcon('Icons/minimize_icon.png'))
        self.ui.maximize_button.setIcon(QIcon('Icons/maximize_icon.png'))
        self.ui.close_button.setIcon(QIcon('Icons/close_icon.png'))

        # Set Up Actions
        self.ui.minimize_button.clicked.connect(self.minimize_window)
        self.ui.maximize_button.clicked.connect(self.maximize_window)
        self.ui.close_button.clicked.connect(self.close)

    def minimize_window(self):
        self.showMinimized()

    def maximize_window(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def close_window(self):
        self.close()
