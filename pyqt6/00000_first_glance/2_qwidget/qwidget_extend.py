# QWidget을 inherit하는 custom class 만들기
# 아마 이렇게 만드는 편이 더 편하니까 이런식으로 예제를 짠거겠지...

from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        # QWidget의 __init__을 실행해 주어야 함
        super().__init__()

        # 시작 x,y위치 / Width / Height
        # 아래와 바꿔가며 실행해 보면 차이를 알 수 있음
        self.setGeometry(400, 400, 700, 400)
        # self.setGeometry(0, 0, 400, 700)

        self.setWindowTitle("Python GUI Development")
        self.setWindowIcon(QIcon('python.png'))
        # 아래를 사용하면 Width와 height를 fix할 수 있다
        #self.setFixedWidth(700)
        #self.setFixedHeight(400)

        self.setStyleSheet('background-color:red')
        self.setWindowOpacity(0.5)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())


