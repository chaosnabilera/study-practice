from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("PyQt6 QTableWidget")
        self.setWindowIcon(QIcon('images/python.png'))

        main_layout = QVBoxLayout()
        table_widget = self.create_tablewidget()
        main_layout.addWidget(table_widget)

        self.setLayout(main_layout)

    def create_tablewidget(self):
        table_widget = QTableWidget()
        table_widget.setRowCount(2)
        table_widget.setColumnCount(3)

        table_widget.setHorizontalHeaderLabels(["Name","Email","Phone"])

        table_widget.setItem(0, 0, QTableWidgetItem("Parwiz"))
        table_widget.setItem(0, 1, QTableWidgetItem("parwiz@gmail.com"))
        table_widget.setItem(0, 2, QTableWidgetItem("666556"))

        table_widget.setItem(1, 0, QTableWidgetItem("John"))
        table_widget.setItem(1, 1, QTableWidgetItem("john@gmail.com"))
        table_widget.setItem(1, 2, QTableWidgetItem("88888"))

        return table_widget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())