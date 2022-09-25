import sys

from PyQt6 import QtCore
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QListWidget, QLabel, QPushButton, QInputDialog, QLineEdit, QMessageBox, QHBoxLayout, QVBoxLayout


class ListWidgetExample(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(400,400, 640, 480)
        self.setWindowTitle("PyQt6 QListWidget")
        self.setWindowIcon(QIcon('images/python.png'))

        main_layout = QHBoxLayout()
        lw_layout = self._create_listwidget_layout()
        pb_layout = self._create_pushbutton_layout()
        main_layout.addLayout(lw_layout)
        main_layout.addLayout(pb_layout)

        self.setLayout(main_layout)

    def _create_listwidget_layout(self):
        lwlabel = QLabel("QListWidget items")
        lwlabel.setFont(QFont("Time",16))

        self._listwidget = QListWidget()
        self._listwidget.setFont(QFont("Times New Roman", 16))
        # self._listwidget.setSelectionMode()

        layout = QVBoxLayout()
        layout.addWidget(lwlabel)
        layout.addWidget(self._listwidget)

        return layout

    def _create_pushbutton_layout(self):
        self._pb_add = QPushButton("Add")
        self._pb_add.setFont(QFont("Times New Roman",16))
        self._pb_add.clicked.connect(self._add_button_clicked)

        self._pb_edit = QPushButton("Edit")
        self._pb_edit.setFont(QFont("Times New Roman", 16))
        self._pb_edit.clicked.connect(self._edit_button_clicked)

        self._pb_remove = QPushButton("Remove")
        self._pb_remove.setFont(QFont("Times New Roman", 16))
        self._pb_remove.clicked.connect(self._remove_button_clicked)

        self._pb_sort = QPushButton("Sort")
        self._pb_sort.setFont(QFont("Courier New", 21))
        self._pb_sort.clicked.connect(self._sort_button_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self._pb_add)
        layout.addWidget(self._pb_edit)
        layout.addWidget(self._pb_remove)
        layout.addStretch()
        layout.addWidget(self._pb_sort)

        return layout

    def _add_button_clicked(self):
        row = self._listwidget.currentRow()
        if len(self._listwidget.selectedIndexes()) == 0:
            row = self._listwidget.count()
        title = "Add Item"
        data, ok = QInputDialog.getText(self, title, title)

        if ok and data != None:
            self._listwidget.insertItem(row, data)

    def _edit_button_clicked(self):
        if len(self._listwidget.selectedIndexes()) == 0:
            return
        
        row = self._listwidget.currentRow()
        item = self._listwidget.item(row)

        if item == None:
            return

        title = "Edit Item"
        data, ok = QInputDialog.getText(self, title, title, QLineEdit.EchoMode.Normal, item.text())
        if ok and data is not None:
            item.setText(data)

    def _remove_button_clicked(self):
        if len(self._listwidget.selectedIndexes()) == 0:
            return

        row = self._listwidget.currentRow()
        item = self._listwidget.item(row)

        if item == None:
            return
        
        reply = QMessageBox.question(self, "Remove item", "Do you want to remove item?", 
                                            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.Yes:
            self._listwidget.takeItem(row)

    def _sort_button_clicked(self):
        self._listwidget.sortItems()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    lwe = ListWidgetExample()
    lwe.show()
    sys.exit(app.exec())