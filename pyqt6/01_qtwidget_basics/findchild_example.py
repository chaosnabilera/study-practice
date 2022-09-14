from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QDoubleSpinBox
from PyQt6 import uic

# findChild를 이용하면 QObject.objectName을 이용해 ui안에 있는 child widget을 찾을 수 있다
# ui를 python으로 변환하면 나오기는 나오는데 복잡하니까 uic.loadUi 를 이용해 ui파일을 로드하고
# 여기의 element는 findChild로 찾아 연결해서 쓰는게 더 나을 수도 있음
# 아래는 그 예제
# ui는 Qt Designer로 열 수 있다

class UI(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("findchild_example.ui", self)

        self.linePrice = self.findChild(QLineEdit, "lineEdit_price")
        self.doublespin = self.findChild(QDoubleSpinBox, "doubleSpinBox")
        self.lineResult = self.findChild(QLineEdit, "lineEdit_total")

        self.doublespin.valueChanged.connect(self.spin_selected)


    def spin_selected(self):
        cur_text = self.linePrice.text()
        try:
            price = int(cur_text)
            totalPrice = self.doublespin.value() * price
            self.lineResult.setText(str(totalPrice))
        except:
            pass

if __name__ == '__main__':
    app = QApplication([])
    window = UI()
    window.show()
    app.exec()