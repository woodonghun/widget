

from PySide2.QtCore import QDate, QTime
from PySide2.QtWidgets import QWidget, QApplication, QTabWidget, QVBoxLayout, QCheckBox, QPushButton, QRadioButton, \
    QLabel, QLineEdit, QHBoxLayout, QCalendarWidget, QTimeEdit


class Tab2(QWidget):
    def __init__(self):
        super().__init__()
        self.showDate()
        self.initUI()

    def initUI(self):
        label1 = QLabel('생년월일 시간 선택')

        btn1 = QPushButton(self)
        btn1.setText('ok')
        btn2 = QPushButton(self)
        btn2.setText('cancel')

        self.cal = QCalendarWidget(self)
        self.cal.setGridVisible(True)
        self.cal.selectionChanged.connect(self.showDate)

        self.lbl = QLabel(self)
        date = self.cal.selectedDate()
        self.lbl.setText(date.toString())

        timeedit = QTimeEdit(self)
        timeedit.setTime(QTime.currentTime())
        timeedit.setTimeRange(QTime(3, 00, 00), QTime(23, 30, 00))
        timeedit.setDisplayFormat('hh:mm:ss')

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addStretch(0)

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(self.cal)
        vbox.addWidget(self.lbl)
        vbox.addWidget(timeedit)
        vbox.addLayout(hbox)

        tab = QWidget()
        tab.setLayout(vbox)
        return tab

    def showDate(self):
        cal_date = self.cal.selectedDate()
        strDate = cal_date.toString('yyyy.MM.DD')
        self.lbl.setText(strDate)


