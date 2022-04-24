import sys
from PyQt6.QtWidgets import QApplication, QWidget


def main():

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(450, 200)
    w.move(300, 300)
    w.move(600,300)

    w.setWindowTitle('Test Application')
    w.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()