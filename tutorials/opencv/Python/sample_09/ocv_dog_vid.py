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
		# Display the resulting frame
		cv2.imshow('Watermark',frame)
		# Wait for exit key "q" to quit
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	
	# Release all resources used
	webcam.release()
	cv2.destroyAllWindows()

except cv2.error as e:
	print('Please correct OpenCV Error')