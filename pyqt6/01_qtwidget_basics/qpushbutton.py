from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMenu
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys



class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("PyQt6 QPushButton")
        self.setWindowIcon(QIcon('images/python.png'))

        self.create_text_only_button()
        self.create_icon_only_button()
        self.create_text_and_icon_button()
        self.create_text_icon_menu_button()

    def create_text_only_button(self):
        btn = QPushButton("Text only simple button", self)
        btn.setGeometry(0, 0, 300, 30)
        btn.setFont(QFont("Times", 14, QFont.Weight.ExtraBold))

    def create_icon_only_button(self):
        btn = QPushButton(self)
        btn.setGeometry(0,50,200,100)
        btn.setIcon(QIcon('images/doge.jpg')) # 800 * 450 image
        btn.setIconSize(QSize(160,90))

    def create_text_and_icon_button(self):
        btn = QPushButton("Text and Icon", self)
        btn.setGeometry(0,180, 200,50)
        btn.setFont(QFont("Times", 14, QFont.Weight.ExtraBold))
        btn.setIcon(QIcon("images/python.png"))
        btn.setIconSize(QSize(36,36))

    def create_text_icon_menu_button(self):
        btn = QPushButton("Text+Icon+Menu", self)
        btn.setGeometry(0,250, 250, 80)
        btn.setFont(QFont("Times", 14, QFont.Weight.ExtraBold))
        btn.setIcon(QIcon("images/python.png"))
        btn.setIconSize(QSize(36,36))

        #popup menu
        menu = QMenu()
        menu.setFont(QFont("Times", 14, QFont.Weight.ExtraBold))
        menu.setStyleSheet('background-color:green')
        menu.addAction("Copy")
        menu.addAction("Cut")
        menu.addAction("Paste")
        btn.setMenu(menu)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())