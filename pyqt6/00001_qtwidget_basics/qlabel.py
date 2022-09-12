from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 1000, 400)
        self.setWindowTitle("Python GUI Development")
        self.setWindowIcon(QIcon('images/python.png'))

        label1 = QLabel("label 1", self)
        label1.move(0,0)

        label2 = QLabel(self)
        label2.setText("This is Label 2!")
        label2.move(0,50)
        label2.setFont(QFont("Sanserif", 15))
        label2.setStyleSheet('color:red')

        label3 = QLabel(self)
        label3.setNum(333333)
        label3.move(0,100)
        # label3.clear()

        label4 = QLabel(self)
        label4.move(100,0)
        label4_pixmap = QPixmap('images/python.png')
        label4.setPixmap(label4_pixmap)
        
        label5 = QLabel(self)
        label5.move(400,0)
        label5_gifmovie = QMovie('images/rainbow_cat.gif')
        label5_gifmovie.setSpeed(100) # 100 = 100% speed
        label5.setMovie(label5_gifmovie)
        label5_gifmovie.start()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())