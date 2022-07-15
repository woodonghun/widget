import sys
import widget.tab1
import widget.tab2
import widget.tab3
import widget.tab4
from PySide2.QtWidgets import QWidget, QApplication, QTabWidget, QVBoxLayout, QCheckBox, QPushButton, QRadioButton, \
    QHBoxLayout


# 이름 - 라인 에딧
# 성별 - 라디오 버튼
# 사는 지역 - 콤보 박스
# 생년월일시간 - 캘린더, 타임 에딧
#
class Main(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        tab1 = widget.tab1.Tab1
        tab2 = widget.tab2.Tab2
        tab3 = widget.tab3.Tab3
        tab4 = widget.tab4.Tab4

        tabs = QTabWidget()

        tabs.addTab(tab1.tab1(self), 'tab1')
        tabs.addTab(tab2.initUI(self), 'tab2')
        tabs.addTab(tab3.tab3(self), 'tab3')
        tabs.addTab(tab4.tab4(self), 'tab4')

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)

        self.setLayout(vbox)

        self.setWindowTitle('Widget')
        self.setGeometry(300, 300, 400, 300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())
