import sys

from PyQt6 import *
from PyQt6.QtWidgets import *

EXCHANGE_RATES ={
    'Рубль': 1,
    'Доллар': 70,
    'Евро': 80,
    'Тубрик': 30
}


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('Конвертер валют')
        self.setFixedSize(270, 90)

        self.input_value = QLineEdit(self)
        self.input_value.move(10, 10)
        self.input_value.resize(100, 30)

        self.input_type = QComboBox(self)
        self.input_type.move(10, 50)
        self.input_type.resize(100, 30)
        for currency in EXCHANGE_RATES.keys():
            self.input_type.addItem(currency)

        self.convert_button = QPushButton(self)
        self.convert_button.setText('->')
        self.convert_button.move(120, 10)
        self.convert_button.resize(30, 70)
        self.convert_button.clicked.connect(self.convert)

        self.output_value = QLineEdit(self)
        self.output_value.setEnabled(False)
        self.output_value.move(160, 10)
        self.output_value.resize(100, 30)

        self.output_type = QComboBox(self)
        self.output_type.move(160, 50)
        self.output_type.resize(100, 30)
        for currency in EXCHANGE_RATES.keys():
            self.output_type.addItem(currency)

    def convert(self):
        input = float(self.input_value.text()) * EXCHANGE_RATES[self.input_type.currentText()]
        output = input / EXCHANGE_RATES[self.output_type.currentText()]
        self.output_value.setText(f'{output:.2f}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())