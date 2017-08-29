from __future__ import print_function
#!/usr/bin/env python

# Python 2/3 compatibility
from __future__ import print_function
# Allows use of print like a function in Python 2.x

# Import the Numby and OpenCV2 Python modules
import numpy as np
import cv2

# This section selects the Haar Cascade Classifer File to use
# Ensure that the path to the xml files are correct
# In this example, the files have been copied to the local folder
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Some Additional Samples - Only one imread should be active. So be sure to comment out all others.
# Image download URL - http://blogs.intel.com/iot/files/2016/04/ASBRparticpants.jpg
#img = cv2.imread('ASBRparticpants.jpg')
# Image download URL - http://blogs.intel.com/iot/files/2016/09/bmw-group-intel-mobileye-3.jpg
#img = cv2.imread('bmw-group-intel-mobileye-3.jpg')
# Image download URL - https://upload.wikimedia.org/wikipedia/commons/1/17/Intel_Board_of_Directors.jpg
#img = cv2.imread('Intel_Board_of_Directors.jpg')
try:
	# Image download URL - https://simplecore.intel.com/newsroom/wp-content/uploads/sites/11/brian-krzanich_2.jpg
	# Load image to analyze
	img = cv2.imread('brian-krzanich_2.jpg')
	# Converion to Grayscale
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# Face detection using Haar Cascades
	# Detects objects of different sizes in the input image. The detected objects are returned as a list of rectangles.
	# cv2.CascadeClassifier.detectMultiScale(image[,scaleFactor[,minNeighbors[,flags[,minSize[,maxSize]]]]]) -> objects
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	# Draw the rectangles around detected Regions of Interest [ROI] - faces
	# cv2.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) -> img
	for (x,y,w,h) in faces:		
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    	roi_gray = gray[y:y+h, x:x+w]
    	roi_color = img[y:y+h, x:x+w]
    	# Since eyes are a part of face, limit eye detection to face regions to improve accuracy
    	eyes = eye_cascade.detectMultiScale(roi_gray)
    	for (ex,ey,ew,eh) in eyes:
    		# Draw the rectangles around detected Regions of Interest [ROI] - eyes
        	cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

	# Display the result        
	cv2.imshow('img',img)
	# Show image until dismissed using GUI exit window
	cv2.waitKey(0)
	# Release all resources used
	cv2.destroyAllWindows()


except cv2.error as e:
	print('Please correct OpenCV Error')