from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 700)
        self.setWindowTitle("PyQt6 QVBoxLayout")
        self.setWindowIcon(QIcon('images/python.png'))

        vbox = QVBoxLayout()

        btn1 = QPushButton("Click 1")
        btn2 = QPushButton("Click 2")
        btn3 = QPushButton("Click 3")
        btn4 = QPushButton("Click 4")
        btn5 = QPushButton("Click 5")

        # 윈도우를 위 아래로 늘려보면 addSpacing과 addStretch가 어떻게 다른지 
        # 직관적으로 알 수 있음
        # addSpacing은 fixed size만큼만 늘림
        # addStretch는 stretch factor에 따라서 늘렸을때 늘어나는 양이 다르다

        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addSpacing(100)
        vbox.addWidget(btn3)
        vbox.addStretch(1)
        vbox.addWidget(btn4)
        vbox.addStretch(2)
        vbox.addWidget(btn5)

        self.setLayout(vbox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())