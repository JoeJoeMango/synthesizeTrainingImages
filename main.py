from PIL import Image
import cv2
import numpy as np
import os.path
import os, sys
import re
import time
import glob
from PyQt5.QtWidgets import QFileDialog, QApplication, QMainWindow, \
    QPushButton, QVBoxLayout, QWidget
from PyQt5 import QtCore, QtWidgets
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

cwd = os.getcwd()

LEGOimages = cwd + '/ScreenShots/Session 0'
BGfile = cwd + '/BGImages/'
VideoFiles = cwd + '/video-files/video-frames/'

fileNames =[]
originalFileNames = []
pngImages = []

name = ''

resizeIMGfinsished = False

pngFolderDirectory = 'file'
videoFileDirectory = 'file'

dirs = os.listdir(BGfile)
finalSize = 1600

def openPNG():
    file = str(QFileDialog.getExistingDirectory(choosePNGbtn, "Select Directory"))
    global pngFolderDirectory
    pngFolderDirectory = file
    PNGpath.setText(pngFolderDirectory)
    print(file)

def openVideoFile():
    file = QFileDialog.getOpenFileName(chooseVideoBtn, 'Open')
    global videoFileDirectory
    videoFileDirectory = str(file[0])
    VideoPath.setText(videoFileDirectory)
    print(videoFileDirectory)
    
def processVideo():
    print('processing Video')
    for filename in os.listdir(pngFolderDirectory):
        try:
            pngImages.append(Image.open(pngFolderDirectory+"/"+filename))
            fileNames.append(filename)
        except OSError:
            print('error')

    for i in fileNames:
        i = i[:-4]
        originalFileNames.append(i)

    splitVideo()
    deleteDStore()
    resize_aspect_fit()

def synthesize():
    for filename in os.listdir(pngFolderDirectory):
        try:
            pngImages.append(Image.open(pngFolderDirectory+"/"+filename))
            fileNames.append(filename)
        except OSError:
                print('error')

    for i in fileNames:
        i = i[:-4]
        originalFileNames.append(i)
    
    compositImages()





#------------------Split video frames------------------
def splitVideo():
    cap = cv2.VideoCapture(videoFileDirectory)
    ProcessVideoSatus.setText('extracting video frames')
    currentFrame = 0
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if frame is None:
            break
        # Saves image of the current frame in jpg file
        global name
        name = BGfile + str(currentFrame) + '.jpg'
        print('Creating...' + name)

        cv2.imwrite(name, frame)
        # To stop duplicate images
        currentFrame += 1

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


#------Deletes '.DS_Store' hidden files--------#
def deleteDStore():
    for root, dirs, files in os.walk('.'):
        i = 0
        for file in files:
            if file.endswith('.DS_Store'):
                path = os.path.join(root, file)

                print ("Deleting: %s" % (path))

                if os.remove(path):
                    print ("Unable to delete!")
                else:
                    print ("Deleted...")
                    i += 1
    print ("Files Deleted: %d" % (i))

# ----------deletes all files that are not .jpg-----------# 
def jpgCheck():
    ProcessVideoSatus.setText('jpg check')
    print('-----------checking JPGS ------------')
    for item in dirs:
        if os.path.isfile(BGfile+item):
            try:
                im = Image.open(BGfile+item)
            except IOError as e:
                os.remove(BGfile+item)
                
            f, e = os.path.splitext(BGfile+item)
            if not item.endswith ('.jpg'):
                os.remove(BGfile+item)
                      
# -------- Resize all background images to fit PNG --------#
def resize_aspect_fit():
    ProcessVideoSatus.setText('Resizing Images')
    print('----------resizing images-------------')
    for item in dirs:
        if os.path.isfile(BGfile+item):
            im = Image.open(BGfile+item)
            f, e = os.path.splitext(BGfile+item)
            size = im.size
            cropPointX = (im.width/2)/4
            cropPointY = (im.height/2)+(finalSize/2)
            (width, height) = (finalSize, finalSize)
            crop_rectangle_wide = (cropPointX, 0, im.height+cropPointX, im.height)
            crop_rectangle_vertical = (0, 0, im.width, im.width)
            if im.size[0] > im.size[1]:
                im.crop(crop_rectangle_wide).resize((finalSize,finalSize), Image.ANTIALIAS).save(f + 'resized.jpg', 'JPEG', quality=90)
            if im.size[0] < im.size[1]:
                im.crop(crop_rectangle_vertical).resize((finalSize,finalSize), Image.ANTIALIAS).save(f + 'resized.jpg', 'JPEG', quality=90)
            if im.size[0] == im.size[1]:
                im.resize((finalSize,finalSize), Image.ANTIALIAS).save(f + 'resized.jpg', 'JPEG', quality=90)
            path = os.path.join(BGfile, item)
            os.remove(path)

    print('----------DONE-------------')
    ProcessVideoSatus.setText('FINISHED')
    global resizeIMGfinsished
    resizeIMGfinsished = True
# -------- Paste PNG on to JPG --------#

def compositImages():
    # print('--------------synthesing-------------')
    
    i = 0
    path = BGfile
    os.system(path)
    pngImages = pngFolderDirectory
    print(len(pngImages))
    while i in range(len(pngImages)):
        continue
        for item in dirs:
            if os.path.isfile(BGfile+item):
                try:
                    im = Image.open(BGfile+item)
                    im.resize((finalSize,finalSize))

                    BGimgWidth = im.width
                    BGimgheight = im.height
            
                    PNGwidth = pngImages[i].width
                    PNGheight = pngImages[i].height

                    imagePlacementW = (BGimgWidth - PNGwidth)/2
                    imagePlacementH = (BGimgheight - PNGheight)/2
                    
                    newImage = im.copy()
                
                    newImage.paste(pngImages[i], (int(imagePlacementW),int(imagePlacementH)), pngImages[i])
                    newImage.save("synthesized Images/"+str(i)+".jpg")
                    
                except IndexError:
                     print('ding dong its the end')
                     SynthesizeSatus.setText('FINSIHED')
                     break
                i+=1
            



app = QApplication([])
win = QMainWindow()
central_widget = QWidget()

choosePNGbtn = QPushButton('PNG data', central_widget)

PNGpath = QtWidgets.QLabel(central_widget)
PNGpath.setAlignment(QtCore.Qt.AlignCenter)

chooseVideoBtn = QPushButton('video', central_widget)

VideoPath = QtWidgets.QLabel(central_widget)
VideoPath.setAlignment(QtCore.Qt.AlignCenter)

processVideoFile = QPushButton('Process Video', central_widget)

ProcessVideoSatus = QtWidgets.QLabel(central_widget)
ProcessVideoSatus.setAlignment(QtCore.Qt.AlignCenter)

synthesizeData = QPushButton('synthesize',central_widget)

SynthesizeSatus = QtWidgets.QLabel(central_widget)
SynthesizeSatus.setAlignment(QtCore.Qt.AlignCenter)

choosePNGbtn.clicked.connect(openPNG)
chooseVideoBtn.clicked.connect(openVideoFile)
processVideoFile.clicked.connect(processVideo)
synthesizeData.clicked.connect(synthesize)

layout = QVBoxLayout(central_widget)

layout.addWidget(choosePNGbtn)
layout.addWidget(PNGpath)
layout.addWidget(chooseVideoBtn)
layout.addWidget(VideoPath)
layout.addWidget(processVideoFile)
layout.addWidget(ProcessVideoSatus)
layout.addWidget(synthesizeData)
layout.addWidget(SynthesizeSatus)

win.setCentralWidget(central_widget)
# win.setGeometry(300,300,300,200)
win.show()
app.exit(app.exec_())
