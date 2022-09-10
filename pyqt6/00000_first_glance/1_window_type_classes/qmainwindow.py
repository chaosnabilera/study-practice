import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv) # pass command line to QApplication
    mainwindow = QMainWindow()
    mainwindow.statusBar().showMessage("Hello from QMainWindow!")
    mainwindow.menuBar().addMenu("File")
    mainwindow.show()
    app_ret_code = app.exec()
    sys.exit(app_ret_code)