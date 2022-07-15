import sys
import glob
from PySide2.QtCore import QDate
from PySide2.QtWidgets import QWidget, QApplication, QTabWidget, QVBoxLayout, QCheckBox, QPushButton, QRadioButton, \
    QLabel, QLineEdit, QHBoxLayout, QCalendarWidget


class Tab1(QWidget):
    def __init__(self):
        super().__init__()
        self.tab1()

    def tab1(self):
        txt = open("C:\woo_project\widget\widget\id",'a')
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

        box1 = QHBoxLayout()
        box1.addStretch(0)
        box1.addWidget(rad1)
        box1.addWidget(rad2)


        box2 = QHBoxLayout()
        box1.addWidget(btn1)
        box1.addWidget(btn2)

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(edt1)
        vbox.addWidget(label2)
        vbox.addWidget(edt2)
        vbox.addWidget(label3)
        vbox.addWidget(edt3)
        vbox.addLayout(box1)
        vbox.addLayout(box2)

        tab = QWidget()
        tab.setLayout(vbox)
        return tab
