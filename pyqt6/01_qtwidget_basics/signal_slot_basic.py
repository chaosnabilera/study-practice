from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("PyQt6 Event Handling")
        self.setWindowIcon(QIcon('images/python.png'))

        self.create_widget()


    def create_widget(self):
        hbox = QHBoxLayout()
        btn = QPushButton("Change Text")
        # signal
        btn.clicked.connect(self.clicked_btn)
        
        self.label = QLabel("Default Text")

        hbox.addWidget(btn)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

    # slot
    def clicked_btn(self):
        self.label.setText("Another Text")
        self.label.setFont(QFont("Times", 15))
        self.label.setStyleSheet('color:red')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())