import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QCalendarWidget
from PySide2.QtCore import QDate


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())

        cal.clicked[QDate].connect(self.showDate)

        vbox = QVBoxLayout()
        vbox.addWidget(cal)
        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setWindowTitle('QCalendarWidget')
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def showDate(self, date):
        self.lbl.setText(date.toString())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())