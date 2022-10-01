from PyQt6.QtWidgets import QApplication, QWidget, QCalendarWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QIcon, QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("PyQt6 QCalendarWidget")
        self.setWindowIcon(QIcon('images/python.png'))

        main_layout = QVBoxLayout()

        self.calendar = self.create_qcalendarwidget()
        self.label = QLabel("Selected : ")
        self.label.setFont(QFont("Times", 16))

        main_layout.addWidget(self.calendar)
        main_layout.addWidget(self.label)

        self.setLayout(main_layout)

    def create_qcalendarwidget(self):
        calendar = QCalendarWidget()
        calendar.setGridVisible(True)
        calendar.selectionChanged.connect(self.set_label)
        return calendar

    def set_label(self):
        date_selected = self.calendar.selectedDate()
        date_string = str(date_selected.toPyDate())
        self.label.setText("Selected : {}".format(date_string))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())