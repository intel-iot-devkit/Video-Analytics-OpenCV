#!/usr/bin/env python

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

# Setup Classifiers
face_cascade = cv2.CascadeClassifier(pri_cascade_file)
eye_cascade = cv2.CascadeClassifier(sec_cascade_file)

try:
	# Initialize Default Camera
	webcam = cv2.VideoCapture(0)
	# Check if Camera initialized correctly
	success = webcam.isOpened()
	if success == True:
		print('Grabbing Camera ..')
		# Uncomment and adjust according to your webcam capabilities
		#webcam.set(cv2.CAP_PROP_FPS,30);
		#webcam.set(cv2.CAP_PROP_FRAME_WIDTH,1024);
		#webcam.set(cv2.CAP_PROP_FRAME_HEIGHT,768);
	elif success == False:
		print('Error: Camera could not be opened')

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
		# Print to console the number of faces detected
		print('Number of faces detected: ' + str(len(faces)))
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
				# Draw the rectangles around detected Regions of Interest [ROI] - faces
				cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

		cv2.imshow('Facetracker', out)
		# Wait for Esc Key to quit
		if cv2.waitKey(5) == 27:
			break
	# Release all resources used
	webcam.release()
	cv2.destroyAllWindows()

except cv2.error as e:
	print('Please correct OpenCV Error')