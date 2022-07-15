from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSlider, QDial, QLabel, QSpinBox, QDoubleSpinBox, \
    QTableWidget, QAbstractItemView, QHeaderView


class Tab4(QWidget):
    def __init__(self):
        super().__init__()
        self.tab3()

    def tab4(self):
        table = QTableWidget()
        table.setRowCount(20)
        table.setColumnCount(7)
        table.setHorizontalHeaderLabels(['이름', '성별', '국가', '나이', '생년월일', '키', '몸무게'])
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        layout = QVBoxLayout()
        layout.addWidget(table)
        tab = QWidget()
        tab.setLayout(layout)

        return tab