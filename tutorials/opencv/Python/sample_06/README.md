
# OpenCV Tutorial Sample 6: ocv_vid_cap
[Sample 06](ocv_vid_cap.py) is a simple program that uses OpenCV to connect to a WebCam in order to capture and save an image. This example is the basic first step for most video analytics programs. The video output of the WebCam is displayed and when the user inputs a keystroke, the frame is captured and written to an image file.

## Usage:
Launch the interactive tutorial by typing the following command in your comand window:

```
jupyter notebook ./ocv_vid_cap.ipynb
```
OR

You may run the script using the command:

```
python ./ocv_vid_cap.py
```
## Code Walkthrough:

Perform the usual initializations and print some debug info.

```
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
```
**Console Output:**
```

OpenCV Version: 3.2.0
Numpy Version: 1.12.1
OpenCV Video Capture Sample
Type c to Capture and q to Quit
```

Next, open a named GUI window for displaying the webcam video in real-time. Initialize a counter to keep track of captures and initialize the webcam. These are the same steps taken in sample_04 to test the camera.

```
# Initialize GUI window to grab keystrokes when it has focus.
cv2.namedWindow("Capture")
# Initialize Capture Counter
cap_cnt = 0
# Initialize Video Web Camera for capture. The default camera is 0 (usually built-in) 
# The second camera would be 1 and so on
webcam = cv2.VideoCapture(0)
# Check if Camera initialized correctly
success = webcam.isOpened()
if success == False:
    print('Error: Camera could not be opened')
else:
    print('Success: Grabbed the camera')
```
**Console output:** Assuming this was sucessful ...

```
Success: Grabbed the camera
```

Next we setup a loop that reads each frame and then displays it. We also setup an event handler that monitors the keyboard for the c and q keys to capture a framegrab or quit the program respectively. 

If the c key is pressed, we use the OpenCV API **cv2.imwrite()** to write the frame as an image file to disk. The filename is incremented with the counter we initialized before.

```
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
```

Now release all devices and resources used before exiting.

```
webcam.release()
cv2.destroyAllWindows()
```
