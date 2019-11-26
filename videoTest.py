import cv2
import numpy as np
import os
cap = cv2.VideoCapture('/Users/josephmango/Desktop/TrainingData/video_files/IMG_1281.mov')
currentFrame = 0
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if frame is None:
        break
        
    # Saves image of the current frame in jpg file
    name = '/Users/josephmango/Desktop/TrainingData/video_files/video_frames/' + str(currentFrame) + '.jpg'
    print('Creating...' + name)
	
    cv2.imwrite(name, frame)
    # To stop duplicate images
    currentFrame += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()