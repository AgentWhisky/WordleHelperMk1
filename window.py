import sys
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication
from MainWindow import *
from wordle import wordle

default_ID = 0
yesLetters_ID = 1
noLetters_ID = 2
comboBoxNone = "*"


class Window(QMainWindow):
    def __init__(self, parent=None):
        # Do not touch
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.offset = None  # Movement Offset
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Remove Title Bar
        # Do not touch

        # Set Window Icons
        self.setup_title_bar()

        # Program Setup
        self._setLetterBox()

        # Wordle
        self.wordle = wordle()

        # Button Status
        self.button_status = {}
        self._setup_buttons()

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

    def _setLetterBox(self):
        letterStr = '*ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        letters = []
        for letter in letterStr:
            letters.append(letter)

        self._buildComboBox(self.ui.letterBox_1, letters)
        self._buildComboBox(self.ui.letterBox_2, letters)
        self._buildComboBox(self.ui.letterBox_3, letters)
        self._buildComboBox(self.ui.letterBox_4, letters)
        self._buildComboBox(self.ui.letterBox_5, letters)

    def _buildComboBox(self, comboBox, data):
        comboBox.addItems(data)

    def _setup_buttons(self):
        letterStr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        for letter in letterStr:
            self.button_status[letter] = 0

        # Connect Buttons

        # Connect Update Button
        self.ui.update_button.clicked.connect(self._update_button)

        self.ui.letterButton_A.clicked.connect(lambda: self._toggle_button('A', self.ui.letterButton_A))
        self.ui.letterButton_B.clicked.connect(lambda: self._toggle_button('B', self.ui.letterButton_B))
        self.ui.letterButton_C.clicked.connect(lambda: self._toggle_button('C', self.ui.letterButton_C))
        self.ui.letterButton_D.clicked.connect(lambda: self._toggle_button('D', self.ui.letterButton_D))
        self.ui.letterButton_E.clicked.connect(lambda: self._toggle_button('E', self.ui.letterButton_E))
        self.ui.letterButton_F.clicked.connect(lambda: self._toggle_button('F', self.ui.letterButton_F))
        self.ui.letterButton_G.clicked.connect(lambda: self._toggle_button('G', self.ui.letterButton_G))
        self.ui.letterButton_H.clicked.connect(lambda: self._toggle_button('H', self.ui.letterButton_H))
        self.ui.letterButton_I.clicked.connect(lambda: self._toggle_button('I', self.ui.letterButton_I))
        self.ui.letterButton_J.clicked.connect(lambda: self._toggle_button('J', self.ui.letterButton_J))
        self.ui.letterButton_K.clicked.connect(lambda: self._toggle_button('K', self.ui.letterButton_K))
        self.ui.letterButton_L.clicked.connect(lambda: self._toggle_button('L', self.ui.letterButton_L))
        self.ui.letterButton_M.clicked.connect(lambda: self._toggle_button('M', self.ui.letterButton_M))
        self.ui.letterButton_N.clicked.connect(lambda: self._toggle_button('N', self.ui.letterButton_N))
        self.ui.letterButton_O.clicked.connect(lambda: self._toggle_button('O', self.ui.letterButton_O))
        self.ui.letterButton_P.clicked.connect(lambda: self._toggle_button('P', self.ui.letterButton_P))
        self.ui.letterButton_Q.clicked.connect(lambda: self._toggle_button('Q', self.ui.letterButton_Q))
        self.ui.letterButton_R.clicked.connect(lambda: self._toggle_button('R', self.ui.letterButton_R))
        self.ui.letterButton_S.clicked.connect(lambda: self._toggle_button('S', self.ui.letterButton_S))
        self.ui.letterButton_T.clicked.connect(lambda: self._toggle_button('T', self.ui.letterButton_T))
        self.ui.letterButton_U.clicked.connect(lambda: self._toggle_button('U', self.ui.letterButton_U))
        self.ui.letterButton_V.clicked.connect(lambda: self._toggle_button('V', self.ui.letterButton_V))
        self.ui.letterButton_W.clicked.connect(lambda: self._toggle_button('W', self.ui.letterButton_W))
        self.ui.letterButton_X.clicked.connect(lambda: self._toggle_button('X', self.ui.letterButton_X))
        self.ui.letterButton_Y.clicked.connect(lambda: self._toggle_button('Y', self.ui.letterButton_Y))
        self.ui.letterButton_Z.clicked.connect(lambda: self._toggle_button('Z', self.ui.letterButton_Z))

    def _toggle_button(self, letter, button):
        num = self.button_status.get(letter)

        num += 1
        if num > noLetters_ID:
            num = default_ID

        self.button_status[letter] = num
        self._set_button_color(button, num)


    def _set_button_color(self, button, id):
        if id == 1:
            button.setStyleSheet('QPushButton {background-color: #A3C1DA;}')
        elif id == 2:
            button.setStyleSheet('QPushButton {background-color: #E1300A;}')
        else:
            button.setStyleSheet("")

    def _update_button(self):
        letterStr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        yesLetters = []
        noLetters = []
        setWords = ['*', '*', '*', '*', '*']

        # yesLetters and noLetters
        for letter in letterStr:
            # yesLetters
            if self.button_status.get(letter) == yesLetters_ID:
                yesLetters.append(letter)
            elif self.button_status.get(letter) == noLetters_ID:
                noLetters.append(letter)

        # Set Words
        if self.ui.letterBox_1.currentText() != comboBoxNone:
            setWords[0] = self.ui.letterBox_1.currentText()
        if self.ui.letterBox_2.currentText() != comboBoxNone:
            setWords[1] = self.ui.letterBox_2.currentText()
        if self.ui.letterBox_3.currentText() != comboBoxNone:
            setWords[2] = self.ui.letterBox_3.currentText()
        if self.ui.letterBox_4.currentText() != comboBoxNone:
            setWords[3] = self.ui.letterBox_4.currentText()
        if self.ui.letterBox_5.currentText() != comboBoxNone:
            setWords[4] = self.ui.letterBox_5.currentText()

        # Get Possible Words
        possibleWords = self.wordle.possibleWords(yesLetters, noLetters, setWords)

        self.ui.wordDisplay.clear()
        for word in possibleWords:
            self.ui.wordDisplay.append(word)


# Read StyleSheet of given name
def get_style_sheet(file_name):
    file = QFile(file_name)
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    return stream.readAll()


def main():
    app = QApplication(sys.argv)

    # Set Style Sheet
    app.setStyleSheet(get_style_sheet('luna.qss'))

    # Run
    win = Window()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
