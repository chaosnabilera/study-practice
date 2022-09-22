import random
import sys

from PyQt6.QtWidgets import QApplication, QLabel, QLCDNumber, QPushButton, QVBoxLayout, QWidget 
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QTime, QTimer


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("PyQt6 QLCDNumber")
        self.setWindowIcon(QIcon('images/python.png'))

        main_layout = QVBoxLayout()

        main_layout.addLayout(self.create_timer_LCD_layout())
        main_layout.addLayout(self.create_random_LCD_layout())

        self.setLayout(main_layout)

        # if we don't use self, this code won't work
        # somehow QTimer needs parent to work properly
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer_LCD)
        self.timer.start(1000)

    def create_timer_LCD_layout(self):
        layout = QVBoxLayout()
        
        label = QLabel()
        label.setText("Timer")
        label.setFont(QFont('Sanserif', 15))
        layout.addWidget(label)

        self.timer_lcd = QLCDNumber()
        self.timer_lcd.setDigitCount(8)
        self.timer_lcd.setStyleSheet('background:green')
        self.timer_lcd.setMinimumHeight(60)
        layout.addWidget(self.timer_lcd)

        layout.addStretch()

        return layout

    def update_timer_LCD(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm:ss')
        self.timer_lcd.display(text)

    def create_random_LCD_layout(self):
        layout = QVBoxLayout()

        label = QLabel()
        label.setText("Random hex number")
        label.setFont(QFont('Sanserif',15))
        layout.addWidget(label)

        self.rand_lcd = QLCDNumber()
        self.rand_lcd.setDigitCount(20)
        self.rand_lcd.setStyleSheet('background:gray')
        self.rand_lcd.setMinimumHeight(60)
        layout.addWidget(self.rand_lcd)

        button = QPushButton("Generate random number")
        button.setFont(QFont("Times", 14, QFont.Weight.Bold))
        button.clicked.connect(self.update_random_LCD)
        layout.addWidget(button)

        layout.addStretch()

        return layout

    def update_random_LCD(self):
        randnum = random.randint(0,0xFFFFFFFFFFFFFFFF)
        text = f'{randnum:016X}'
        self.rand_lcd.display(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())