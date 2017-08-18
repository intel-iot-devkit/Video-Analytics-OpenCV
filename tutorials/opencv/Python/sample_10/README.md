# OpenCV Tutorial Sample 10: ocv_face_img

[Sample 10](ocv_face_img.py) is a basic Face and Eye Detection program that uses OpenCV to analyze an image and detect human faces and eyes. The detected areas or Regions of Interest (ROI) are demarcated with rectangles. The program uses the OpenCV built-in pre-trained Haar feature-based cascade classifiers in order to perform this task.

## What are Cascade Classifiers?
Cascade Classifiers are a form of ensemble learning systems. Such systems use a collection of a large number of simple classifiers in a cascade. This leads to accurate yet computationally efficient detection systems.

## What are Haar feature-based Cascade Classifiers?
Haar features are named after Haar wavelets in mathematics. The are patterns in the pixel values of an image such as edges, lines and neighbors that are used with a windowing technique to extract features from an image. Since the features could be different, a collection of specialized but simple pattern classifiers are used in a cascade to perform the feature detection.

The Viola–Jones object detection framework was the first object detection framework using these Haar features to provide acceptable object detection rates in real-time and were proposed in 2001 by Prof. Paul Viola and Prof. Michael Jones.

## References:
1. Rapid Object Detection using a Boosted Cascade of Simple Features [pdf](http://wearables.cc.gatech.edu/paper_of_week/viola01rapid.pdf)
  [_This is the original paper by Prof. Viola and Prof. Jones_]
2. An Analysis of the Viola-Jones Face Detection Algorithm [pdf](http://www.ipol.im/pub/art/2014/104/article.pdf)
3. A review on Face Detection and study of Viola Jones method [pdf](http://www.ijcttjournal.org/2015/Volume25/number-1/IJCTT-V25P110.pdf)
4. Explaining AdaBoost [pdf](http://rob.schapire.net/papers/explaining-adaboost.pdf)
5. Face detection using Haar Cascades [Tutorial link](http://docs.opencv.org/trunk/d7/d8b/tutorial_py_face_detection.html)

## Usage:
Launch the interactive tutorial by typing the following command in your comand window:

```
jupyter notebook ./ocv_face_img.ipynb
```
OR

You may run the script using the command:

```
python ./ocv_face_img.py
```
## Code Walkthrough:

First we do the usual initializations ...
```
from __future__ import print_function
#!/usr/bin/env python

# Python 2/3 compatibility
from __future__ import print_function
# Allows use of print like a function in Python 2.x

# Import the Numby and OpenCV2 Python modules
import numpy as np
import cv2
```
Select the pre-trained Haar Cascade Classifier file to use for face and eye detection respectively and pass it to the OpenCV API cv2.CascadeClassifier()

This section selects the Haar Cascade Classifer File to use. Ensure that the path to the xml files are correct. In this example, the files have been copied to the local folder

```
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
```
Next load an image to analyze. Several examples are provided. Make sure that only one **cv2.imread()** command is active and all the rest are commented out. These example images have all been copied to the local folder.
```
img = cv2.imread('brian-krzanich_2.jpg')
#img = cv2.imread('Intel_Board_of_Directors.jpg')
#img = cv2.imread('bmw-group-intel-mobileye-3.jpg')
```
Now convert the image to Grayscale to make it easier to process
```
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```
The detectMultiScale method of the OpenCV Cascade Classifier API detects features of different sizes in the input image. The detected objects are returned as a list of rectangles.

**cv2.CascadeClassifier.detectMultiScale(image[,scaleFactor[,minNeighbors[,flags[,minSize[,maxSize]]]]]) -> objects**
```
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
```
Draw the rectangles around detected Regions of Interest [ROI], namely faces amd eyes using cv2.rectangle() for all detected objects in the image returned by the classifiers.
```
cv2.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) -> img
```
>Note: Since the eyes are a part of the face, we nest the classifier for the eyes. So we only look for eyes in areas identified as the face. This improves the accuracy.

Next, draw the rectangles around detected Regions of Interest [ROI] - faces
```
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
```

Since eyes are a part of face, limit eye detection to face regions to improve accuracy

```
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        # Draw the rectangles around detected Regions of Interest [ROI] - eyes
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
```
Finally display the result until dismissed and release all reseources used.
``` 
cv2.imshow('img',img)
# Show image until dismissed using GUI exit window
cv2.waitKey(0)
# Release all resources used
cv2.destroyAllWindows()
```
