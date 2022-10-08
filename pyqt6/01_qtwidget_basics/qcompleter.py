import sys

from random import randint

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QCompleter
from PyQt6.QtGui import QIcon, QFont


class ExampleCompleter(QWidget):
    def __init__(self):
        super().__init__()

        random_strings = self._generate_random_strings(20,100000)

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 QTableWidget")
        self.setWindowIcon(QIcon('images/python.png'))

        main_layout = QVBoxLayout()
        main_layout.addWidget(self._create_lineedit_with_completer(random_strings))

        self.label = QLabel()
        self.label.setText("")
        self.label.setFont(QFont("Times New Roman", 16))

        main_layout.addWidget(self.label)

        self.setLayout(main_layout)

    def _generate_random_strings(self, str_len, str_cnt):
        result = []
        alphanum = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        len_lim = len(alphanum)-1

        for i in range(str_cnt):
            sl = []
            for j in range(str_len):
                sl.append(alphanum[randint(0,len_lim)])
            result.append(''.join(sl))
        
        return result

    def _create_lineedit_with_completer(self, wordlist):
        self.lineedit = QLineEdit()
        self.lineedit.setFont(QFont("Times New Roman", 16))
        completer = QCompleter(wordlist)
        self.lineedit.setCompleter(completer)
        self.lineedit.returnPressed.connect(self._show_lineedit)

        return self.lineedit

    def _show_lineedit(self):
        self.label.setText(self.lineedit.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    excd = ExampleCompleter()
    excd.show()
    sys.exit(app.exec())