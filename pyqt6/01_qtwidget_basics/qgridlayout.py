from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("PyQt6 QGridLayout")
        self.setWindowIcon(QIcon('images/python.png'))

        grid = QGridLayout()

        # QGridLayout은 widget들의 사이즈를 보고 알아서 전체 grid사이즈를 조절해 줌
        # 아래를 실행해 보면 대충 알 수 있음

        btn1 = QPushButton("One")
        btn1.setFixedSize(QSize(100,200))
        btn2 = QPushButton("Two")
        btn3 = QPushButton("Three")
        btn3.setFixedSize(QSize(300,100))
        btn4 = QPushButton("Four")
        btn5 = QPushButton("Five")
        btn6 = QPushButton("Six")
        btn7 = QPushButton("Seven")
        btn7.setFixedSize(QSize(150,150))
        btn8 = QPushButton("Eight")

        grid.addWidget(btn1, 0,0)
        grid.addWidget(btn2, 0, 1)
        grid.addWidget(btn3, 0, 2)
        grid.addWidget(btn4, 0, 3)
        grid.addWidget(btn5, 1, 0)
        grid.addWidget(btn6, 1, 1)
        grid.addWidget(btn7, 1, 2)
        grid.addWidget(btn8, 1, 3)

        self.setLayout(grid)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())