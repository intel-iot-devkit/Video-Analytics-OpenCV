#!/usr/bin/env python

# Python 2/3 compatibility
from __future__ import print_function
# Allows use of print like a function in Python 2.x

# Import OpenCV and other needed Python modules
import numpy as np
import cv2

try:
	# Digital On-Screen Graphic aka DOG
	# Load two images
	# First image is the one that needs to be watermarked
	# Image Download URL - https://iqglobal.intel.com/iq-content-library/wp-content/uploads/sites/18/2017/04/Blue-Ridge-2-Skyglow-Desktop-Wallpapers.jpg
	# Rename as Intel_Wall.jpg
	img = cv2.imread('Intel_Wall.jpg')
	# Create a named window to show the source image
	cv2.namedWindow('Source Image', cv2.WINDOW_NORMAL)
	# Display the source image
	cv2.imshow('Source Image',img)
	# Second image is a watermark. Note that the image is PNG with transparent background.
	# https://newsroom.intel.com/wp-content/themes/newsroom/dist/images/favicon/mstile-150x150.png
	# Rename as Intel_Logo.png
	dog = cv2.imread('Intel_Logo.png')
	# Create a named window to handle intermediate outputs and resizing
	cv2.namedWindow('Result Image', cv2.WINDOW_NORMAL)
	# To put logo on top-left corner, create a Region of Interest (ROI)
	rows,cols,channels = dog.shape
	roi = img[0:rows, 0:cols ]
	# Convert the logo to grayscale
	dog_gray = cv2.cvtColor(dog,cv2.COLOR_BGR2GRAY)
	# Create a mask of the logo and its inverse mask
	ret, mask = cv2.threshold(dog_gray, 10, 255, cv2.THRESH_BINARY)
	mask_inv = cv2.bitwise_not(mask)
	# Now blackout the area of logo in ROI
	img_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
	# Now just extract the logo
	dog_fg = cv2.bitwise_and(dog,dog,mask = mask)
	# Next add the logo to the source image
	dst = cv2.add(img_bg,dog_fg)
	img[0:rows, 0:cols ] = dst
	# Display the Result
	cv2.imshow('Result Image',img)
	# Wait until windows are dismissed
	cv2.waitKey(0)
	# Release all resources used
	cv2.destroyAllWindows()

except cv2.error as e:
    print('Please correct OpenCV Error')