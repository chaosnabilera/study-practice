import sys

from PyQt6.QtWidgets import QApplication, QWidget

def this_shows_window():
    window = QWidget()
    window.show()
    return app.exec()

def this_doesnt():  # but why? 
    window = QWidget()
    ret = app.exec() # this won't return. So window.show should be called before app.exec
    window.show()
    return ret

if __name__ == '__main__':
    app = QApplication(sys.argv) # pass command line to QApplication
    # ret = this_shows_window()
    ret = this_doesnt()
    sys.exit(ret)