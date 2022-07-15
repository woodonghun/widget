import sys

from PySide2.QtCore import QDate
from PySide2.QtWidgets import QWidget, QApplication, QTabWidget, QVBoxLayout, QCheckBox, QPushButton, QRadioButton, \
    QLabel, QLineEdit, QHBoxLayout, QCalendarWidget


class Tab1(QWidget):
    def __init__(self):
        super().__init__()
        self.tab1()

    def tab1(self):
        label1 = QLabel('이름 :')
        label2 = QLabel('나이 :')
        label3 = QLabel('국가 :')

        btn1 = QPushButton(self)
        btn1.setText('ok')
        btn2 = QPushButton(self)
        btn2.setText('cancel')

        rad1 = QRadioButton('남자', self)
        rad2 = QRadioButton('여자', self)

        edt1 = QLineEdit(self)
        edt2 = QLineEdit(self)
        edt3 = QLineEdit(self)

        box = QHBoxLayout()
        box.addStretch(1)
        box.addWidget(rad1)
        box.addWidget(rad2)
        box.addStretch(1)
        box.addWidget(btn1)
        box.addWidget(btn2)
        box.addStretch(0)

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(edt1)
        vbox.addWidget(label2)
        vbox.addWidget(edt2)
        vbox.addWidget(label3)
        vbox.addWidget(edt3)
        vbox.addLayout(box)

        tab = QWidget()
        tab.setLayout(vbox)
        return tab