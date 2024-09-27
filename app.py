from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton,QMainWindow

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("sum tow number")
        self.setFixedSize(400, 120)

        self.label1 = QLabel("First number :", self)
        self.line_edit1 = QLineEdit(self)
        self.label2 = QLabel("Second number :", self)
        self.line_edit2 = QLineEdit(self)
        self.button = QPushButton("sum", self)
        self.result_label = QLabel("Result:", self)

        self.label1.move(50, 20)
        self.line_edit1.move(150, 20)
        self.label2.move(50, 50)
        self.line_edit2.move(150, 50)
        self.button.move(20, 80)
        self.result_label.move(150, 80)

        self.button.clicked.connect(self.sumNumbers)

    def sumNumbers(self):
        num1 = float(self.line_edit1.text())
        num2 = float(self.line_edit2.text())

        result = num1 + num2
        self.result_label.setText(str(result))

if __name__ == '__main__':
    app = QApplication([])
    calculator = Calculator()
    calculator.show()
    app.exec()
