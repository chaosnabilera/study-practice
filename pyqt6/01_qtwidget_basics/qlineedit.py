from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt6.QtGui import QIcon, QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("PyQt6 QLineEdit")
        self.setWindowIcon(QIcon('images/python.png'))

        line_edit1 = QLineEdit(self)
        line_edit1.setGeometry(0,0,400,40)
        line_edit1.setFont(QFont("Sanserif", 15))
        line_edit1.setText("Simple line edit")
        line_edit1.setPlaceholderText("Placeholder text is revealed if nothing is written")

        line_edit2 = QLineEdit(self)
        line_edit2.setGeometry(0,50,400,40)
        line_edit2.setPlaceholderText("This is disabled QLineEdit")
        line_edit2.setEnabled(False)

        line_edit3 = QLineEdit(self)
        line_edit3.setGeometry(0,100,400,40)
        line_edit3.setPlaceholderText("This is password type QLineEdit")
        line_edit3.setEchoMode(QLineEdit.EchoMode.Password)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())