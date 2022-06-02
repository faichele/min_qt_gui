from PySide6.QtWidgets import QApplication,QMainWindow
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic

class Frm_main(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("form.ui", self)

app = QApplication([])
frm_main = Frm_main()
frm_main.show()
app.exec()
