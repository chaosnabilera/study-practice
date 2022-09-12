from PyQt6.QtWidgets import QApplication, QWidget, QRadioButton,QVBoxLayout ,QHBoxLayout, QLabel, QButtonGroup
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 300, 200)
        self.setWindowTitle("PyQt6 QRadioButton")
        self.setWindowIcon(QIcon('images/python.png'))

        main_layout = QHBoxLayout()
        
        left_layout = self.create_left_layout()
        right_layout = self.create_right_layout()

        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)
        self.setLayout(main_layout)

    def create_left_layout(self):
        self.label_left = QLabel("Left:")
        self.label_left.setFont(QFont("Sanserif", 15))

        rad1 = QRadioButton("Python",self)
        rad1.setIcon(QIcon("images/py.png"))
        rad1.setIconSize(QSize(40,40))
        rad1.setFont(QFont("Times", 14))
        # rad1.setChecked(True)
        rad1.toggled.connect(self.left_selected)

        rad2 = QRadioButton("Java",self)
        rad2.setIcon(QIcon("images/java.png"))
        rad2.setIconSize(QSize(40, 40))
        rad2.setFont(QFont("Times", 14))
        rad2.toggled.connect(self.left_selected)

        rad3 = QRadioButton("JavaScript",self)
        rad3.setIcon(QIcon("images/javascript.png"))
        rad3.setIconSize(QSize(40, 40))
        rad3.setFont(QFont("Times", 14))
        rad3.toggled.connect(self.left_selected)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label_left)
        vbox.addWidget(rad1)
        vbox.addWidget(rad2)
        vbox.addWidget(rad3)

        rd_group = QButtonGroup(self) # parent를 지정해 주지 않으면 제대로 작동하지 않음
        rd_group.addButton(rad1)
        rd_group.addButton(rad2)
        rd_group.addButton(rad3)

        return vbox

    def create_right_layout(self):
        self.label_right = QLabel("Right:")
        self.label_right.setFont(QFont("Sanserif", 15))

        rad1 = QRadioButton("C",self)
        rad1.setIcon(QIcon("images/py.png"))
        rad1.setIconSize(QSize(40,40))
        rad1.setFont(QFont("Times", 14))
        # rad1.setChecked(True)
        rad1.toggled.connect(self.right_selected)

        rad2 = QRadioButton("C++",self)
        rad2.setIcon(QIcon("images/java.png"))
        rad2.setIconSize(QSize(40, 40))
        rad2.setFont(QFont("Times", 14))
        rad2.toggled.connect(self.right_selected)

        rad3 = QRadioButton("C#",self)
        rad3.setIcon(QIcon("images/javascript.png"))
        rad3.setIconSize(QSize(40, 40))
        rad3.setFont(QFont("Times", 14))
        rad3.toggled.connect(self.right_selected)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label_right)
        vbox.addWidget(rad1)
        vbox.addWidget(rad2)
        vbox.addWidget(rad3)

        rd_group = QButtonGroup(self) # parent를 지정해 주지 않으면 제대로 작동하지 않음
        rd_group.addButton(rad1)
        rd_group.addButton(rad2)
        rd_group.addButton(rad3)

        return vbox

    def left_selected(self):
        radio_btn = self.sender()
        if radio_btn.isChecked():
            self.label_left.setText("Left : {} ".format(radio_btn.text()))

    def right_selected(self):
        radio_btn = self.sender()
        if radio_btn.isChecked():
            self.label_right.setText("Right : {} ".format(radio_btn.text()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())