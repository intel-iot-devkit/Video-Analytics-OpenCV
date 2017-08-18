#!/usr/bin/env python

# Python 2/3 compatibility
from __future__ import print_function
# Allows use of print like a function in Python 2.x

# Import OpenCV and Numpy modules
import numpy as np
import cv2

# Initialize Video Web Camera for capture. 
# The default camera is 0 (usually built-in) 
# The second camera would be 1 and so on

try:
    webcam = cv2.VideoCapture(0)
    # Check if Camera initialized correctly
    success = webcam.isOpened()
    if success == False:
        print('Error: Camera could not be opened')


    while(True):
        # Read each frame in video stream
        ret, frame = webcam.read()
        # Perform operations on the frame here
        # For example convert to Grayscale 
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Overlay Text on the video frame with Exit instructions
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(gray, "Type q to Quit:",(50,50), font, 1,(0,0,0),2,cv2.LINE_AA)
        # Display the resulting frame
        cv2.imshow('frame',gray)
        # Wait for exit key "q" to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Release all resources used
    webcam.release()
    cv2.destroyAllWindows()

except cv2.error as e:
    print('Please correct OpenCV Error')