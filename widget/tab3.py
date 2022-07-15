from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSlider, QDial, QLabel, QSpinBox, QDoubleSpinBox, \
    QPushButton


class Tab3(QWidget):
    def __init__(self):
        super().__init__()
        self.tab3()

    def tab3(self):
        btn1 = QPushButton(self)
        btn1.setText('ok')

        btn2 = QPushButton(self)
        btn2.setText('cancel')

        spin = QDoubleSpinBox()
        spin.setRange(0, 200)
        spin.setSingleStep(0.1)
        spin.setPrefix('키 : ')
        spin.setSuffix('cm')

        spin2 = QSpinBox()
        spin2.setRange(0, 120)
        spin2.setSingleStep(1)
        spin2.setPrefix('몸무게 : ')
        spin2.setSuffix('kg')

        slider = QSlider(Qt.Horizontal, self)
        slider.setRange(0, 200)
        slider.setSingleStep(0.1)
        slider.valueChanged.connect(spin.setValue)
        spin.valueChanged.connect(slider.setValue)

        dial = QDial(self)
        dial.setNotchesVisible(True)
        dial.setRange(0, 120)
        dial.setSingleStep(0.1)

        dial.valueChanged.connect(spin2.setValue)
        spin2.valueChanged.connect(dial.setValue)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(slider)
        hbox.addStretch(1)
        hbox.addWidget(dial)
        hbox.addStretch(1)
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(spin)
        vbox.addWidget(spin2)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        tab = QWidget()
        tab.setLayout(vbox)

        return tab