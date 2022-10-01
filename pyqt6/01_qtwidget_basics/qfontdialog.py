from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QFontDialog, QLabel
from PyQt6.QtGui import QIcon, QFont
import sys

class ExampleFontDialog(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 QTableWidget")
        self.setWindowIcon(QIcon('images/python.png'))

        main_layout = QVBoxLayout()
        main_layout.addLayout(self._create_font_write_layout())

        self.setLayout(main_layout)

    def _create_font_write_layout(self):
        layout = QVBoxLayout()

        self._textedit = QTextEdit()

        pbtn = QPushButton("Choose font")
        pbtn.setFont(QFont("Times New Roman", 16))
        pbtn.clicked.connect(self._set_textedit_font)

        self._show_font_name = QLabel("Font name:")
        self.setFont(QFont("Times New Roman", 16))

        layout.addWidget(self._textedit)
        layout.addWidget(pbtn)
        layout.addWidget(self._show_font_name)

        return layout

    def _set_textedit_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self._textedit.setFont(font)
            self._show_font_name.setText(font.toString())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    excd = ExampleFontDialog()
    excd.show()
    sys.exit(app.exec())