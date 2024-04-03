from PySide6.QtWidgets import QMainWindow, QMessageBox
from UIs.main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


    def solve(self):
        base1 = self.ui.base1_label.text()
        base2 = self.ui.base2_label.text()
        height = self.ui.height_label.text()
        if (
            not base1
            or not base2
            or not height
        ):
            QMessageBox.warning(self, "Ошибка", "Некорректные данные")
            return
        answer = ((int(base1) + int(base2)) / 2) * int(height)
        QMessageBox.information(
            self, "Решение", str(answer)
        )  
