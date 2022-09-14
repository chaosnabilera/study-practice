from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QHBoxLayout, QLabel, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys



class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("PyQt6 QCheckBox")
        self.setWindowIcon(QIcon('images/python.png'))

        self.label = QLabel('Nothing')
        self.label.setFont(QFont("Sanserif", 15))

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.label)
        main_layout.addLayout(self.create_checkboxes())

        self.setLayout(main_layout)

    def create_checkboxes(self):
        self.check1 = QCheckBox("Python")
        self.check1.setIcon(QIcon("images/py.png"))
        self.check1.setIconSize(QSize(40,40))
        self.check1.setFont(QFont("Sanserif", 13))
        self.check1.stateChanged.connect(self.item_selected)

        self.check2 = QCheckBox("Java")
        self.check2.setIcon(QIcon("images/java.png"))
        self.check2.setIconSize(QSize(40, 40))
        self.check2.setFont(QFont("Sanserif", 13))
        self.check2.stateChanged.connect(self.item_selected)

        self.check3 = QCheckBox("JavaScript")
        self.check3.setIcon(QIcon("images/javascript.png"))
        self.check3.setIconSize(QSize(40, 40))
        self.check3.setFont(QFont("Sanserif", 13))
        self.check3.stateChanged.connect(self.item_selected)

        checkbox_layout = QHBoxLayout()
        checkbox_layout.addWidget(self.check1)
        checkbox_layout.addWidget(self.check2)
        checkbox_layout.addWidget(self.check3)

        return checkbox_layout

    def item_selected(self):
        value = []

        if self.check1.isChecked():
            value.append(self.check1.text())
        if self.check2.isChecked():
            value.append(self.check2.text())
        if self.check3.isChecked():
            value.append(self.check3.text())

        if len(value) > 0:
            self.label.setText(f"Selected : {' '.join(value)}")
        else:
            self.label.setText('Nothing')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())