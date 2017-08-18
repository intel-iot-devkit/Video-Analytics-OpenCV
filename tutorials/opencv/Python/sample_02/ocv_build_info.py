#!/usr/bin/env python

# Python 2/3 compatibility
from __future__ import print_function
# Allows use of print like a function in Python 2.x

# Import OpenCV Python module
import cv2

# This function returns the full configuration time cmake output
try:
	buildinfo = cv2.getBuildInformation()
	print(buildinfo)

except cv2.error as e:
	print('Error:')


