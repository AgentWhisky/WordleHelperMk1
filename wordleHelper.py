
from window2 import *


# Function to read given Stylesheet
def get_style_sheet(file_name):
    file = QFile(file_name)
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    return stream.readAll()


# Main Function
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
