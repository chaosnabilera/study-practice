from PyQt6.QtWidgets import QApplication, QWidget, QDoubleSpinBox, QSpinBox, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit
from PyQt6.QtGui import QIcon, QFont

import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 800, 200)
        self.setWindowTitle("PyQt6 QSpinBox")
        self.setWindowIcon(QIcon('images/python.png'))
        
        main_layout = QVBoxLayout()
        main_layout.addLayout(self.create_value_changed_example())
        main_layout.addLayout(self.create_editing_finished_example())
        main_layout.addStretch()

        self.setLayout(main_layout)

    def create_value_changed_example(self):
        layout = QVBoxLayout()

        label = QLabel("QSpinBox + valueChanged : value is changed when clicked")
        label.setFont(QFont("Times", 15))
        layout.addWidget(label)

        sublayout = QHBoxLayout()
        self.vc_lineedit = QLineEdit()
        self.vc_spinbox = QSpinBox()
        self.vc_spinbox.valueChanged.connect(self.value_changed_slot)
        self.vc_result = QLineEdit()
        sublayout.addWidget(self.vc_lineedit)
        sublayout.addWidget(self.vc_spinbox)
        sublayout.addWidget(self.vc_result)
        layout.addLayout(sublayout)

        return layout

    def value_changed_slot(self):
        try:
            price = int(self.vc_lineedit.text())
            total_price = self.vc_spinbox.value() * price
            self.vc_result.setText(str(total_price))
        except:
            self.vc_result.setText("")

    def create_editing_finished_example(self):
        layout = QVBoxLayout()

        label = QLabel("QDoubleSpinBox + editingFinished : value is changed when focus is removed")
        label.setFont(QFont("Times",15))
        layout.addWidget(label)

        sublayout = QHBoxLayout()
        self.ef_lineedit = QLineEdit()
        self.ef_doublespinbox = QDoubleSpinBox()
        self.ef_doublespinbox.editingFinished.connect(self.editing_finished_slot)
        self.ef_result = QLineEdit()
        sublayout.addWidget(self.ef_lineedit)
        sublayout.addWidget(self.ef_doublespinbox)
        sublayout.addWidget(self.ef_result)
        layout.addLayout(sublayout)

        return layout

    def editing_finished_slot(self):
        try:
            price = float(self.ef_lineedit.text())
            total_price = self.ef_doublespinbox.value() * price
            self.ef_result.setText(str(total_price))
        except:
            self.ef_result.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())