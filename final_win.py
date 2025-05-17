# напиши здесь код третьего экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)


from instr import *
app = QApplication([])

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()        
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height )
        self.move(win_x, win_y)

    def initUI(self):
        self.text1 = QLabel(txt_index)
        self.text2 = QLabel(txt_workheart)
        self.Layout1 = QHBoxLayout()
        self.Layout2 = QHBoxLayout()
        self.Layout1.addWidget(self.text1, alignment = Qt.AlignCenter)
        self.Layout2.addWidget(self.text2, alignment = Qt.AlignCenter)
        self.Layout3 = QVBoxLayout()
        self.Layout3.addLayout(self.Layout1)
        self.Layout3.addLayout(self.Layout2)
        self.setLayout(self.Layout3)

final_win = FinalWin()
app.exec_()



