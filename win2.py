from instr import *
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (
QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit)

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        main_line = QHBoxLayout()
        left_line = QVBoxLayout()
        right_line = QVBoxLayout()
        main_line.addLayout(right_line)
        main_line.addLayout(left_line)

        self.timer_label = QLabel('00:00')
        
        self.label_name = QLabel(txt_name)
        self.edit_name = QLineEdit(txt_hintname)
        self.label_age = QLabel(txt_age)
        self.edit_age = QLineEdit(txt_hintage)
        self.label_first_test = QLabel(txt_test1)
        self.button_first_test = QPushButton(txt_starttest1)
        self.edit_result_first_test = QLineEdit(txt_hinttest1)  #😱
        self.label_second_test = QLabel(txt_test2)
        self.button_second_test = QPushButton(txt_starttest2)
        self.label_third_test = QLabel(txt_test3)
        self.button_third_test = QPushButton(txt_starttest3)
        self.edit_result_second_test = QLineEdit(txt_hinttest2)
        self.edit_result_third_test = QLineEdit(txt_hinttest3)
        self.button_send = QPushButton(txt_sendresults)

        left_line.addWidget(self.label_name)
        left_line.addWidget(self.edit_name)
        left_line.addWidget(self.label_age)
        left_line.addWidget(self.edit_age)
        left_line.addWidget(self.label_first_test)
        left_line.addWidget(self.button_first_test)
        left_line.addWidget(self.edit_result_first_test)  #ужас какой-то
        left_line.addWidget(self.label_second_test)
        left_line.addWidget(self.button_second_test)
        left_line.addWidget(self.label_third_test)
        left_line.addWidget(self.button_third_test)
        left_line.addWidget(self.edit_result_second_test)
        left_line.addWidget(self.edit_result_third_test)
        left_line.addWidget(self.button_send)
        right_line.addWidget(self.timer_label)

        self.setLayout(main_line)

        self.timer = QTimer()
        self.time_left = 0
    def connects(self):
        self.button_first_test.clicked.connect(self.save)
        self.button_second_test.clicked.connect(self.save)
        self.button_third_test.clicked.connect(self.save)
        self.button_first_test.clicked.connect(lambda: self.start_timer(16))
        self.button_second_test.clicked.connect(lambda: self.start_timer(46))
        self.button_third_test.clicked.connect(lambda: self.start_timer(61))
        self.timer.timeout.connect(self.update_timer)
    
    def save(self):
        txt_hintname = self.edit_name.text()
        txt_hintage = self.edit_age.text()
        txt_hinttest1 = self.edit_result_first_test.text()
        txt_hinttest2 = self.edit_result_second_test.text()
        txt_hinttest3 = self.edit_result_third_test.text()
    def start_timer(self, seconds):
        self.time_left = seconds
        self.update_timer()
        self.timer.start(1000)
    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.setText(f"00:{self.time_left}")
        else:
            self.timer.stop()
    # def show(self):
    #     pass
app = QApplication([])
mm = TestWin()
app.exec_()