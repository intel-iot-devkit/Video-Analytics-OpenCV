#!/usr/bin/env python

# Python 2/3 compatibility
from __future__ import print_function
# Allows use of print like a function in Python 2.x

# Import Numpy and OpenCV modules
import numpy as np
import cv2
# Print Debug Info
print('OpenCV Version:', cv2.__version__)
print('Numpy Version:', np.__version__)
print('OpenCV Video Capture Sample')
print('Type c to Capture and q to Quit')

try:
    # Initialize GUI window to grab keystrokes when it has focus
    cv2.namedWindow("Capture")
    # Initialize Capture Counter
    cap_cnt = 0
    # Initialize Video Web Camera for capture. 
    # The default camera is 0 (usually built-in) 
    # The second camera would be 1 and so on
    webcam = cv2.VideoCapture(0)
    # Check if Camera initialized correctly
    success = webcam.isOpened()
    if success == False:
        print('Error: Camera could not be opened')

    while True:
        # Read each frame in video stream
        ret, frame = webcam.read()
        # Display each frame in video stream
        cv2.imshow("Capture", frame)
        if not ret:
            break
        # Monitor keystrokes
        k = cv2.waitKey(1)

        if k & 0xFF == ord('q'):
            # q key pressed so quit
            print("Quitting...")
            break
        elif k & 0xFF == ord('c'):
            # c key pressed so capture frame to image file
            cap_name = "capture_{}.png".format(cap_cnt)
            cv2.imwrite(cap_name, frame)
            print("Saving {}!".format(cap_name))
            # Increment Capture Counter for next frame to capture
            cap_cnt += 1

    # Release all resources used
    webcam.release()
    cv2.destroyAllWindows()
    
except cv2.error as e:
    print('Please correct OpenCV Error')
