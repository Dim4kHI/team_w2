from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit)
from instr import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def connects(self):
        pass        


    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width,win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.my_hello_text = QLabel(txt_hello)
        self.my_instruction = QLabel(txt_instruction)
        self.button = QPushButton('Начать')
        self.main_layout =  QVBoxLayout()
        self.main_layout.addWidget(self.button)
        self.setLayout(self.main_layout)



app = QApplication([])
mw = MainWin()
app.exec_()



























