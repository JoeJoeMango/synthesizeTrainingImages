from PIL import Image
# from resizeimage import resizeimage
import os.path
import os, sys
import re
import time
import glob
cwd = os.getcwd()

LEGOimage = cwd + '/ScreenShots/Session 0'
BGfile = cwd + '/BGImages/'
VideoFiles = cwd + '/video-files/video-frames/'

fileNames =[]
originalFileNames = []
pngImages = []


dirs = os.listdir(BGfile)
finalSize = 1600

for filename in os.listdir(LEGOimage):
        pngImages.append(Image.open("ScreenShots/Session 0/"+filename))
        fileNames.append(filename)

for i in fileNames:
    i = i[:-4]
    originalFileNames.append(i)

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
    for item in dirs:
        if item == '.DS_Store':
            continue
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
# -------- Paste PNG on to JPG --------#

def compositImages():
    i = 0
    path = "/Users/josephmango/Desktop/TrainingData/ScreenShots/Session\ 0/"
    os.system(path+'')
    while i in range(len(pngImages)):

        for item in dirs:
            if os.path.isfile(BGfile+item):
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
                newImage.save("Compositied Images/"+str(originalFileNames[i])+".jpg")
                i+=1


# deleteDStore()
# jpgCheck()
# resize_aspect_fit()
# compositImages()