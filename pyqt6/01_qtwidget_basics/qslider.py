from PyQt6.QtWidgets import QApplication, QWidget, QSlider, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit
from PyQt6.QtGui import QIcon, QFont, QIntValidator
from PyQt6.QtCore import Qt
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("PyQt6 QSlider")
        self.setWindowIcon(QIcon('images/python.png'))

        top_level_layout = QHBoxLayout()

        left_layout = self._create_vertical_slider()
        right_layout = self._create_horizontal_slider()

        top_level_layout.addLayout(left_layout)
        top_level_layout.addLayout(right_layout)

        self.setLayout(top_level_layout)


    def _create_vertical_slider(self):
        self._vslider = QSlider()
        self._vslider.setOrientation(Qt.Orientation.Vertical)
        self._vslider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self._vslider.setTickInterval(10)

        self._vslider.setMinimum(0)
        self._vslider.setMaximum(100)
        self._vslider.valueChanged.connect(self._vslider_changed)
        self._vslider.setValue(0)

        self._vlabel = QLabel(str(self._vslider.value()))
        self._vlabel.setFont(QFont("Time",16))

        layout = QVBoxLayout()
        layout.addWidget(self._vslider)
        layout.addWidget(self._vlabel)

        return layout

    def _vslider_changed(self):
        self._vlabel.setText(str(self._vslider.value()))

    def _create_horizontal_slider(self):
        self._hslider = QSlider()
        self._hslider.setOrientation(Qt.Orientation.Horizontal)
        self._hslider.setTickPosition(QSlider.TickPosition.TicksAbove)
        self._hslider.setTickInterval(5)

        self._hslider.setMinimum(0)
        self._hslider.setMaximum(100)
        
        self._hlineedit = QLineEdit()
        self._hlineedit.setFont(QFont("Sanserif",16))
        self._hlineedit.setText(str(self._hslider.value()))
        self._hlineedit.setValidator(QIntValidator(0,100, self._hlineedit))
        self._hlineedit.setAlignment(Qt.AlignmentFlag.AlignRight)

        self._hslider.valueChanged.connect(self._hslider_changed)
        self._hlineedit.returnPressed.connect(self._hlineedit_changed)

        layout = QVBoxLayout()
        layout.addWidget(self._hslider)
        layout.addWidget(self._hlineedit)
        layout.addStretch()

        return layout

    def _hslider_changed(self):
        self._hlineedit.setText(str(self._hslider.value()))

    def _hlineedit_changed(self):
        self._hslider.setValue(int(self._hlineedit.text()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())