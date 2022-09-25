from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 500, 200)
        self.setWindowTitle("PyQt6 QComboBox")
        self.setWindowIcon(QIcon('images/python.png'))

        main_layout = QVBoxLayout()

        self.label_text = QLabel("Selected text : ")
        self.label_text.setFont(QFont("Times", 15))
        main_layout.addWidget(self.label_text)

        self.label_idx = QLabel("Selected index : ")
        self.label_idx.setFont(QFont("Sanserif", 15))
        main_layout.addWidget(self.label_idx)

        main_layout.addLayout(self.create_combobox())
        self.setLayout(main_layout)

    def create_combobox(self):
        hbox = QHBoxLayout()
        label = QLabel("Select language: ")
        label.setFont(QFont("Times", 15))

        self.combobox = QComboBox()
        self.combobox.addItem("C")
        self.combobox.addItem("C++")
        self.combobox.addItem("Python")
        self.combobox.addItem("Java")

        self.combobox.currentIndexChanged.connect(self.combo_index_changed)
        self.combobox.currentTextChanged.connect(self.combo_text_changed)

        hbox.addWidget(label)
        hbox.addWidget(self.combobox)

        return hbox

    def combo_text_changed(self):
        item = self.combobox.currentText()
        self.label_text.setText(f"Text : {item}")

    def combo_index_changed(self):
        item = self.combobox.currentIndex()
        self.label_idx.setText(f"Index : {item}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())