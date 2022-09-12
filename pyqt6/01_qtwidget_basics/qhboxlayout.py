from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("PyQt6 QHBoxLayout")
        self.setWindowIcon(QIcon('images/python.png'))

        hbox = QHBoxLayout()

        btn1 = QPushButton("Click 1")
        btn2 = QPushButton("Click 2")
        btn3 = QPushButton("Click 3")
        btn4 = QPushButton("Click 4")
        btn5 = QPushButton("Click 5")

        # 윈도우를 좌우로 늘려보면 addSpacing과 addStretch가 어떻게 다른지 
        # 직관적으로 알 수 있음
        # addSpacing은 fixed size만큼만 늘림
        # addStretch는 stretch factor에 따라서 늘렸을때 늘어나는 양이 다르다

        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addSpacing(100)
        hbox.addWidget(btn3)
        hbox.addStretch(1)
        hbox.addWidget(btn4)
        hbox.addStretch(2)
        hbox.addWidget(btn5)

        self.setLayout(hbox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())