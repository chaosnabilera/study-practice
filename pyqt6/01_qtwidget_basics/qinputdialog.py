from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QInputDialog
from PyQt6.QtGui import QIcon, QFont
import sys

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("PyQt6 QInputDialog")
        self.setWindowIcon(QIcon('images/python.png'))

        main_layout = QVBoxLayout()
        country_selection = self._create_country_selection_layout()
        get_userename = self._create_get_username_layout()
        get_int = self._create_get_integer_layout()
        
        main_layout.addLayout(country_selection)
        main_layout.addLayout(get_userename)
        main_layout.addLayout(get_int)

        self.setLayout(main_layout)

    def _create_country_selection_layout(self):
        layout = QHBoxLayout()
        label = QLabel("Choose country : ")
        label.setFont(QFont("Times", 16))

        self._country_lineedit = QLineEdit()
        self._country_lineedit.setFont(QFont("Times",16))

        self._country_choice_button = QPushButton("Choose country")
        self._country_choice_button.setFont(QFont("Times",16))
        self._country_choice_button.clicked.connect(self._show_country_selection)

        layout.addWidget(label)
        layout.addWidget(self._country_lineedit)
        layout.addWidget(self._country_choice_button)
        layout.addStretch()

        return layout

    def _show_country_selection(self):
        countries = [
            "Afghanistan", "Albania", "India",
            "Algeria", "Barbados", "Belarus", "Belgium",
            "Kazakhstan", "Korea", 
            "United Kingdom", "United States", "Pakistan",

        ]

        country,ok = QInputDialog.getItem(self, "Input Dialog", "List Of Countries", countries, 0,False)

        if ok and country:
            self._country_lineedit.setText(country)

    
    def _create_get_username_layout(self):
        layout = QHBoxLayout()
        label = QLabel("Username : ")
        label.setFont(QFont("Times", 16))

        self._name_label = QLabel("")
        self._name_label.setFont(QFont("Times", 16))

        self._set_name_button = QPushButton("Get username")
        self._set_name_button.setFont(QFont("Times",16))
        self._set_name_button.clicked.connect(self._show_get_username)

        layout.addWidget(label)
        layout.addWidget(self._name_label)
        layout.addWidget(self._set_name_button)
        layout.addStretch()

        return layout
    
    def _show_get_username(self):
        mytext,ok = QInputDialog.getText(self, "Get Username", "Enter Your Name : ")
        if ok and mytext:
            self._name_label.setText(mytext)

    def _create_get_integer_layout(self):
        layout = QHBoxLayout()
        label = QLabel("Integer : ")
        label.setFont(QFont("Times", 16))

        self._int_label = QLabel("")
        self._int_label.setFont(QFont("Times", 16))

        self._set_int_button = QPushButton("Get int")
        self._set_int_button.setFont(QFont("Times",16))
        self._set_int_button.clicked.connect(self._show_get_int)

        layout.addWidget(label)
        layout.addWidget(self._int_label)
        layout.addWidget(self._set_int_button)
        layout.addStretch()

        return layout

    def _show_get_int(self):
        mynumber, ok = QInputDialog.getInt(self, "Get integer", "Enter integer : ", 0, 0, 100, 1)

        if ok and mynumber:
            self._int_label.setText(str(mynumber))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())