from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi

import sumTowNumbers

import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        loadUi("mainui.ui", self)

        self.sumButton.clicked.connect(self.process)

    def process(self):
        result = sumTowNumbers.sum(self.input1.text(), self.input2.text())
        self.result.setText(str(result))

    # def sumNumbers(self):
    #     num1 = self.input1.text()
    #     num2 = self.input2.text()

    #     result = int(num1) + int(num2)

    #     self.result.setText(str(result))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
