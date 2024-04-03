import signal
import sys

from main_window import MainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon, QPixmap


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    app.setWindowIcon(QIcon(QPixmap(":app/5.png")))
    main_window.setWindowIcon(QIcon(QPixmap(":app/5.png")))

    main_window.show()
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
