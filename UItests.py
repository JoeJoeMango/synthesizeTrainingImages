from PyQt5.QtWidgets import QFileDialog, QApplication, QMainWindow, \
    QPushButton, QVBoxLayout, QWidget
from PyQt5 import QtCore, QtWidgets
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QIcon

pngFile = 'empty'

def openPNG(self):
    file = str(QFileDialog.getExistingDirectory(choosePNGbtn, "Select Directory"))
    global pngFile
    pngFile = file
    print(file)

def openVideoFile():
    file = QFileDialog.getOpenFileName(chooseVideoBtn, 'Open')
    fileName = str(file[0])
    print(fileName)
    return fileName

def synthesize():
    print(pngFile)


app = QApplication([])
win = QMainWindow()
central_widget = QWidget()

choosePNGbtn = QPushButton('PNG data', central_widget)

# l1 = QtWidgets.QLabel(central_widget)
# l1.setAlignment(QtCore.Qt.AlignCenter)
# l1.move(50,20)

chooseVideoBtn = QPushButton('video', central_widget)
synthesizeData = QPushButton('synthesize',central_widget)

print(openVideoFile)

choosePNGbtn.clicked.connect(openPNG)
chooseVideoBtn.clicked.connect(openVideoFile)
synthesizeData.clicked.connect(synthesize)

layout = QVBoxLayout(central_widget)

layout.addWidget(choosePNGbtn)
layout.addWidget(chooseVideoBtn)
layout.addWidget(synthesizeData)

win.setCentralWidget(central_widget)
# win.setGeometry(300,300,300,200)
win.show()
app.exit(app.exec_())