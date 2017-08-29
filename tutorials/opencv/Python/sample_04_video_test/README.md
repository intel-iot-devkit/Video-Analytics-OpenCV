# OpenCV Tutorial Sample 4: ocv_video_test
[Sample 04](ocv_video_test.py) is a sanity test that uses OpenCV to connect to a WebCam and display the video stream. This test serves to ensure that OpenCV WebCam installation is working and further validates the development environment. It also shows how to overlay text on video streams.

## Usage:
Launch the interactive tutorial by typing the following command in your comand window:

```
jupyter notebook ./ocv_video_test.ipynb
```
OR

You may run the script using the command:

```
python ./ocv_video_test.py
```
## Code Walkthrough:
We start by performing the basic initializations

```
#!/usr/bin/env python2

# Python 2/3 compatibility
from __future__ import print_function
# Allows use of print like a function in Python 2.x

# Import OpenCV and Numpy modules
import numpy as np
import cv2
```
First we need to initialize a Video Web Camera for capturing video with OpenCV. We do this transparently by using an OpenCV API 
**cv2.VideoCapture()**

**cv2.VideoCapture(Parameters)**

**Parameters:**

**filename – Name and path of file to be loaded.**

**device_id - Id of the opened video capturing device (i.e. a camera index)**

>Note about Device Id: The default camera is 0 (usually built-in).The second camera would be 1 and so on

>On the Intel® NUC which has no camera, the default Id of "0" should work. On a Laptop, you may need to try "0" or "1" if you have two cameras for front and back.

```
webcam = cv2.VideoCapture(0)
```
**cv2.videoCapture()** method has many calls and **isOpened()** returns **(True)** if the device is opened sucessfully

So we can check if Camera was initialized correctly

```
success = webcam.isOpened()
if success == False:
    print('Error: Camera could not be opened')
else:
    print('Success: Grabbed the camera')
Success: Grabbed the camera
```

Next we use the read() function from cv2.VideoCapure to read a video frame while this is (True)

To Read each frame in video stream:

```
ret, frame = webcam.read()
```

Once the frame is read, it is usually converted to grayscale before performing further operations. This avoids having to process color information in real-time. For this we use the same **cv2.cvtColor()** method from our previous example with just a different color space conversion code.

```
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
```

Overlay Text on the video frame with Exit instructions

```
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(gray, "Type q to Quit:",(50,50), font, 1,(0,0,0),2,cv2.LINE_AA)
```
Now display the captured frame with overlay text in a GUI window
```
cv2.namedWindow('Output', cv2.WINDOW_AUTOSIZE)
cv2.imshow('Output',gray)
```

Next comes the event handler where we wait for the q key and then release the devices and resources used
```
if cv2.waitKey(1) & 0xFF == ord('q'):
    print('Exiting ...')
```
>Note: Since the interactive tutorial mode is not well suited for handling video, the While(True) loop has been omited and so you will only see a still image. But you can see this working for video in the consolidated example and script.
Next we release the devices and all resources used.
```
webcam.release()
cv2.destroyAllWindows()
```

>Note: Ensure that the camera was released in the previous step. The camera light should go off. If not restart the kernel before continuing to the next step.

Now putting it all together with exception handling:

```
#!/usr/bin/env python2

# Python 2/3 compatibility
from __future__ import print_function
# Allows use of print like a function in Python 2.x

# Import OpenCV and Numpy modules
import numpy as np
import cv2
try:
    webcam = cv2.VideoCapture(0)
    # Check if Camera initialized correctly
    success = webcam.isOpened()
    if success == False:
        print('Error: Camera could not be opened')
    else:
        print('Success: Grabbed the camera')


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
            print('Exiting ...')
            break
    # Release all resources used
    webcam.release()
    cv2.destroyAllWindows()

except cv2.error as e:
    print('Please correct OpenCV Error')
Success: Grabbed the camera
```
