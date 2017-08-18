#!/usr/bin/env python

# Python 2/3 compatibility
from __future__ import print_function
# Allows use of print like a function in Python 2.x

# Import the OpenCV2 module
import cv2
print()
print('OpenCV - OpenCL Info sample')
print()

try:
	# Returns True if OpenCL is present
	ocl = cv2.ocl.haveOpenCL()
	# Prints whether OpenCL is present
	print("OpenCL Supported?: ", end='')
	print(ocl)
	print()
	# Enables use of OpenCL by OpenCV if present
	if ocl == True:
		print('Now enabling OpenCL support')
		cv2.ocl.setUseOpenCL(True)
		print("Has OpenCL been Enabled?: ", end='')
		print(cv2.ocl.useOpenCL())

except cv2.error as e:
	print('Error:')

# OpenCV Python module does not currently support enumeration of OpenCL devices.
# Disabling OpenCL can be done as follows:

try:
	ocl_en = cv2.ocl.useOpenCL()
	if ocl_en ==True:
		print('Now disabling OpenCL support')
    	cv2.ocl.setUseOpenCL(False)
    	
   	print("Checking - Is OpenCL still Enabled?: ", end='')
	print(cv2.ocl.useOpenCL())
	print()

except cv2.error as e:
	print('Error:')