# OpenCV Tutorial Sample 11: ocv_face_vid
[Sample 11](sample_11/ocv_face_vid.py) is a basic Face and Eye Detection program that uses OpenCV to analyze real-time video and detect human faces and eyes. The detected areas or Regions of Interest (ROI) are demarcated with rectangles. The program uses the OpenCV built-in pre-trained Haar feature-based cascade classifiers in order to perform this task.

This sample uses the same basic procedures from the previous samples to detect faces and eyes in real-time video. The detection is performed on every video frame.

The OS and SYS modules are also loaded in this sample in order to automatically locate the OpenCV libraries and use the Haar Cascade Classifier files.

## Usage:

Launch the interactive tutorial by typing the following command in your comand window:

```
jupyter notebook ./ocv_face_vid.ipynb
```
OR

You may run the script using the command:

```
python ./ocv_face_vid.py
```

## Code Walkthrough:
First the init code...
In this version we automatically find the OpenCV installation using the environment variables. We also print out some debug messages.

```
#!/usr/bin/env python2

# Python 2/3 compatibility
from __future__ import print_function
# Allows use of print like a function in Python 2.x

# Import Python modules
import numpy as np
import cv2
import sys
import os
print('Face and Eyes Tracker for Real-Time Video')
print('Type Esc to Exit Program ...')
try:
    # Checks to see if OpenCV can be found
    ocv = os.getenv("OPENCV_DIR")
    print(ocv)
except KeyError:
    print('Cannot find OpenCV')
# This automatically locates the cascade files within OpenCV
pri_cascade_file = os.path.join(ocv,'build\etc\haarcascades\haarcascade_frontalface_default.xml')
sec_cascade_file = os.path.join(ocv,'build\etc\haarcascades\haarcascade_eye_tree_eyeglasses.xml')

# Uncomment for Debug if needed
#print(pri_cascade_file)
#print(sec_cascade_file)
```
**Console Output:** If all goes well ...
```
Face and Eyes Tracker for Real-Time Video
Type Esc to Exit Program ...
C:\opencv_pre\
```

Setup the classifiers to use. We are still using the pre-trained classifiers provided as part of OpenCV.
```
face_cascade = cv2.CascadeClassifier(pri_cascade_file)
eye_cascade = cv2.CascadeClassifier(sec_cascade_file)
```
Now we grab the webcam and configure it
```
webcam = cv2.VideoCapture(0)
```
Check if Camera initialized correctly
```
success = webcam.isOpened()
if success == True:
    print('Grabbing Camera ..')
        # Uncomment and adjust according to your webcam capabilities
        #webcam.set(cv2.CAP_PROP_FPS,30);
        #webcam.set(cv2.CAP_PROP_FRAME_WIDTH,1024);
        #webcam.set(cv2.CAP_PROP_FRAME_HEIGHT,768);
elif success == False:
    print('Error: Camera could not be opened')
```
**Console Output:** Assuming all goes well ...
```
Grabbing Camera ..
```
This section is a mashup of the video camera test sample_04 and the previous sample_10 for face and eye detection on a still image. Only difference is that it is done on each video frame within the while loop.

Video is converted to grayscale and histogram equalization filter is applied to improve the contrast. This helps the Haar Cascade Classifiers. Everything else stays the same.

```
while(True):
    # Read each frame in video stream
    ret, frame = webcam.read()
    # Perform operations on the frame here
    # First convert to Grayscale 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Next run filters
    gray = cv2.equalizeHist(gray)
    # Uncomment for Debug if needed
    #cv2.imshow('Grayscale', gray)
    # Face detection using Haar Cascades
    # Detects objects of different sizes in the input image which are returned as a list of rectangles.
    # cv2.CascadeClassifier.detectMultiScale(image[,scaleFactor[,minNeighbors[,flags[,minSize[,maxSize]]]]])
    faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    # Draw the rectangles around detected Regions of Interest [ROI] - faces
    # cv2.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]])
    out = frame.copy()
    for (x,y,w,h) in faces:
        cv2.rectangle(out,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = out[y:y+h, x:x+w]
        # Since eyes are a part of face, limit eye detection to face regions to improve accuracy
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            # Draw the rectangles around detected Regions of Interest [ROI] - eyes
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('Facetracker', out)
    # Wait for Esc Key to quit
    if cv2.waitKey(5) == 27:
        print('Quitting ...')
        break
# Release all resources used
webcam.release()
cv2.destroyAllWindows()
```
