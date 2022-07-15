

from PySide2.QtCore import QTime
from PySide2.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QCalendarWidget, QTimeEdit


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

        self.lbl = QLabel(self)
        date = self.cal.selectedDate()
        self.lbl.setText(date.toString())

        self.selectedDateVar = self.cal.selectedDate()

        self.cal.selectionChanged.connect(self.lbl.setText(self.selectedDateVar.toString()))

        timeedit = QTimeEdit(self)
        timeedit.setTime(QTime.currentTime())
        timeedit.setTimeRange(QTime(0, 00, 00), QTime(23, 00, 00))
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



