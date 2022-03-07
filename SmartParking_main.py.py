import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('SmartParking APP')
window.setGeometry(100, 100, 500, 200)
window.move(60, 60)
helloMsg = QLabel('<h1>Hadzo i Mido! TEST\n TEST</h1>', parent=window)
helloMsg.move(60, 15)

window.show()
sys.exit(app.exec_())
