#!/usr/bin/env python

# Python 2/3 compatibility
from __future__ import print_function
# Allows use of print like a function in Python 2.x

# Import OpenCV and other needed Python modules
import numpy as np
import cv2

try:
	# Load the image from file using OpenCV. The 1 means with color info
	img = cv2.imread('intel-hq.jpg',1)
	# Overlay text on the image using OpenCV
	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(img, "OpenCV Version:",(10,100), font, 2,(255,255,255),2,cv2.LINE_AA)
	cv2.putText(img, cv2.__version__,(525,100), font, 2,(255,255,255),2,cv2.LINE_AA)

	# Create a GUI window to display the image
	cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)

	# Display the Image
	cv2.imshow('image',img)
	# Exit on any keystroke
	if cv2.waitKey(0):
		print('Exiting ...')

	# Release resources used
	cv2.destroyAllWindows()

except cv2.error as e:
	print('Error:')


