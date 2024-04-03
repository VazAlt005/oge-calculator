from PySide6.QtWidgets import QMainWindow, QMessageBox
from UIs.main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.solve_btn.clicked.connect(self.solve)  # 1 исправление

    def solve(self):
        base1 = self.ui.base1_label.text()
        base2 = self.ui.base2_label.text()
        height = self.ui.height_label.text()
        if (
            not base1
            or not base2
            or not height
            or not base1.isdigit()  # 2 исправление
            or not base2.isdigit()  # 2 исправление
            or not height.isdigit()  # 2 исправление
        ):
            QMessageBox.warning(self, "Ошибка", "Некорректные данные")
            return
        answer = ((int(base1) + int(base2)) / 2) * int(height)
        QMessageBox.information(
            self, "Решение", "Площадь черерехугольника = " + str(answer) # 3 исправление
        )  
