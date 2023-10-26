from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class SumApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Сумма X и Y")
        self.setStyleSheet("background-color: #F0F0F0;")

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.x_input = QLineEdit()
        self.y_input = QLineEdit()

        self.sum_label = QLabel()
        self.sum_label.setStyleSheet("background-color: white; color: black; font-weight: bold;")

        calculate_button = QPushButton("Посчитать")
        calculate_button.setStyleSheet("background-color: #0080FF; color: white;")

        layout.addWidget(QLabel("Введите X: "))
        layout.addWidget(self.x_input)
        layout.addWidget(QLabel("Введите Y: "))
        layout.addWidget(self.y_input)
        layout.addWidget(calculate_button)
        layout.addWidget(self.sum_label)

        calculate_button.clicked.connect(self.calculate_sum)

    def calculate_sum(self):
        x = int(self.x_input.text()) if self.x_input.text().isdigit() else 0
        y = int(self.y_input.text()) if self.y_input.text().isdigit() else 0
        self.sum_label.setText(f"Сумма: {x + y}")

if __name__ == "__main__":
    app = QApplication([])
    window = SumApp()
    window.show()
    app.exec()
