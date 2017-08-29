# OpenCV Tutorial Sample 9: ocv_dog_vid
[Sample 09](ocv_dog_vid.py) is a program that overlays a **Digital On-Screen Graphic (DOG)** on the video display stream. 

## Usage:
Launch the interactive tutorial by typing the following command in your comand window:

```
jupyter notebook ./ocv_dog_vid.ipynb
```
OR

You may run the script using the command:

```
python ./ocv_dog_vid.py
```
## Code Walkthrough:
This program uses the same principles as used for the previous example for still images.

In fact, you can mash sample_04 and sample_08 together to create this sample. It's so simple! The procedure to load and process the image and to extract it from the background is only done once outside of the while loop. This is so you don't slow down the frame rate of the video.

Inside the while loop, all that is done is blacking out the logo area and adding the logo to each frame. Replacing the camera device id with a filename and path in **cv2.VideoCapture()** function allows you to watermark any video file from disk. You can write the resulting video back to disk with the watermark added using the **write()** method from **cv2.VideoCapture()**.

```
#!/usr/bin/env python

# Python 2/3 compatibility
from __future__ import print_function
# Allows use of print like a function in Python 2.x

# Import OpenCV and Numpy modules
import numpy as np
import cv2
 
try:
    # Create a named window to display video output
    cv2.namedWindow('Watermark', cv2.WINDOW_NORMAL)
    # This section is the same from previous Image example.
    # Load logo image
    dog = cv2.imread('Intel_Logo.png')
    # 
    rows,cols,channels = dog.shape
    # Convert the logo to grayscale
    dog_gray = cv2.cvtColor(dog,cv2.COLOR_BGR2GRAY)
    # Create a mask of the logo and its inverse mask
    ret, mask = cv2.threshold(dog_gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    # Now just extract the logo
    dog_fg = cv2.bitwise_and(dog,dog,mask = mask)
    
    # Initialize Default Video Web Camera for capture.
    webcam = cv2.VideoCapture(0)
    # Check if Camera initialized correctly
    success = webcam.isOpened()
    if success == False:
        print('Error: Camera could not be opened')
    else:
        print('Sucess: Grabbing the camera')
        webcam.set(cv2.CAP_PROP_FPS,30);
        webcam.set(cv2.CAP_PROP_FRAME_WIDTH,1024);
        webcam.set(cv2.CAP_PROP_FRAME_HEIGHT,768);

    while(True):
        # Read each frame in video stream
        ret, frame = webcam.read()
        # Perform operations on the video frames here
        # To put logo on top-left corner, create a Region of Interest (ROI)
        roi = frame[0:rows, 0:cols ] 
        # Now blackout the area of logo in ROI
        frm_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
        # Next add the logo to each video frame
        dst = cv2.add(frm_bg,dog_fg)
        frame[0:rows, 0:cols ] = dst
        # Overlay Text on the video frame with Exit instructions
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, "Type q to Quit:",(50,700), font, 1,(255,255,255),2,cv2.LINE_AA)
        # Display the resulting frame
        cv2.imshow('Watermark',frame)
        # Wait for exit key "q" to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print('Quitting ...')
            break

    # Release all resources used
    webcam.release()
    cv2.destroyAllWindows()

except cv2.error as e:
    print('Please correct OpenCV Error')
