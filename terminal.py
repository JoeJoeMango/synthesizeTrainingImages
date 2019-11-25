from PyQt5.QtWidgets import QFileDialog, QApplication, QMainWindow, \
    QPushButton, QVBoxLayout, QWidget
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import datetime

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    def update_label():
        current_time = str(datetime.datetime.now().time())
        ui.label.setText(current_time)

    timer = QtCore.QTimer()
    timer.timeout.connect(update_label)
    timer.start(10000)  # every 10,000 milliseconds

    sys.exit(app.exec_())