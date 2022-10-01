from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QColorDialog, QLabel
from PyQt6.QtGui import QIcon, QFont
import sys

class ExampleColorDialog(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("PyQt6 QTableWidget")
        self.setWindowIcon(QIcon('images/python.png'))

        main_layout = QVBoxLayout()
        main_layout.addLayout(self._create_color_write_layout())

        self.setLayout(main_layout)

    def _create_color_write_layout(self):
        layout = QVBoxLayout()

        self._textedit = QTextEdit()

        pbtn = QPushButton("Choose text color")
        pbtn.setFont(QFont("Times New Roman", 16))
        pbtn.clicked.connect(self._set_textedit_color)

        self._show_color_name = QLabel("Color name:")
        self.setFont(QFont("Times New Roman", 16))

        layout.addWidget(self._textedit)
        layout.addWidget(pbtn)
        layout.addWidget(self._show_color_name)

        return layout

    def _set_textedit_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self._textedit.setTextColor(color)
            self._show_color_name.setText(f"Color name: {color.name()}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    excd = ExampleColorDialog()
    excd.show()
    sys.exit(app.exec())