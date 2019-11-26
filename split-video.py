import cv2
import numpy as np
import os

# Playing video from file:
cap = cv2.VideoCapture('/Users/josephmango/Desktop/TrainingData/video_files/IMG_1281.mov')

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Saves image of the current frame in jpg file
    try:
        name = '/Users/josephmango/Desktop/TrainingData/video_files/video_frames/'+ str(currentFrame) + '.jpg'
        print ('Creating...' + name)
        cv2.imwrite(name, frame)
    except:
        print("got err")
    # To stop duplicate images

    currentFrame += 1
    if ret == False:
        break   
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
print("fuck you")