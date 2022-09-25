import sys

from PyQt6 import QtCore
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QFontComboBox, QPlainTextEdit, QLabel, QHBoxLayout, QVBoxLayout

class QFontComboExample(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(400,400, 640, 480)
        self.setWindowTitle("PyQt6 QListWidget")
        self.setWindowIcon(QIcon('images/python.png'))

        main_layout = QVBoxLayout()
        main_layout.addLayout(self._create_font_selector_layout())
        main_layout.addLayout(self._create_plaintextedit_layout())
        self.setLayout(main_layout)

    def _create_font_selector_layout(self):
        layout = QHBoxLayout()

        label = QLabel("Select font : ")
        label.setFont(QFont("Times New Roman",16))

        self._fontcombobox = QFontComboBox()
        self._fontcombobox.currentFontChanged.connect(self._font_changed)

        layout.addWidget(label)
        layout.addWidget(self._fontcombobox)
        return layout

    def _create_plaintextedit_layout(self):
        layout = QHBoxLayout()

        label = QLabel("Text : ")
        label.setFont(QFont("Times New Roman", 16))

        self._plaintextedit = QPlainTextEdit()

        layout.addWidget(label)
        layout.addWidget(self._plaintextedit)
        return layout

    def _font_changed(self):
        newfont = QFont(self._fontcombobox.itemText(self._fontcombobox.currentIndex()), 16)
        self._plaintextedit.setFont(newfont)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    qfce = QFontComboExample()
    qfce.show()
    sys.exit(app.exec())