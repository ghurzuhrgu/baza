from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton)


def show_win():
    window = QMessageBox()
    window.setText('Верно! Вы отлично справились с заданием')
    window.exec_()


def show_loss():
    window = QMessageBox()
    window.setText('Нет, неверно. Попробуйте снова!')
    window.exec_()


app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Название')
question = QLabel('В каком году была основана алгоритмика?')
btn_answer1 = QRadioButton('2013')
btn_answer2 = QRadioButton('2010')
btn_answer3 = QRadioButton('2016')
btn_answer4 = QRadioButton('2019')
btn_answer3.clicked.connect(show_win)
btn_answer1.clicked.connect(show_loss)
btn_answer2.clicked.connect(show_loss)
btn_answer4.clicked.connect(show_loss)
layout_main = QVBoxLayout()
layout_main.addWidget(question)
hv1 = QHBoxLayout()
hv2 = QHBoxLayout()
hv1.addWidget(btn_answer1, alignment=Qt.AlignLeft)
hv1.addWidget(btn_answer2, alignment=Qt.AlignRight)
hv2.addWidget(btn_answer3, alignment=Qt.AlignCenter)
hv2.addWidget(btn_answer4, alignment=Qt.AlignCenter)
layout_main.addLayout(hv1)
layout_main.addLayout(hv2)
main_win.setLayout(layout_main)
main_win.show()
app.exec_()