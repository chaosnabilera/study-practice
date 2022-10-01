from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QMessageBox
from PyQt6.QtGui import QIcon, QFont
import sys

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("PyQt6 QTableWidget")
        self.setWindowIcon(QIcon('images/python.png'))

        main_layout = QVBoxLayout()
        main_layout.addLayout(self.create_message_button_layout())

        self.setLayout(main_layout)

    def create_message_button_layout(self):
        layout = QHBoxLayout()

        btn_warning = QPushButton("Warning")
        btn_warning.setFont(QFont("Times New Roman", 16))
        btn_warning.clicked.connect(self._warn_msg)

        btn_info = QPushButton("Info")
        btn_info.setFont(QFont("Times New Roman", 16))
        btn_info.clicked.connect(self._info_msg)

        btn_about = QPushButton("About")
        btn_about.setFont(QFont("Times New Roman", 16))
        btn_about.clicked.connect(self._about_msg)

        layout.addWidget(btn_warning)
        layout.addWidget(btn_info)
        layout.addWidget(btn_about)

        return layout
        
    
    def _warn_msg(self):
        QMessageBox.warning(self, "Warning", "This is a warning message")

    def _info_msg(self):
        QMessageBox.information(self, "Information", "This is information message")

    def _about_msg(self):
        QMessageBox.about(self, "About", "This is about message")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())