#!/usr/bin/env python

# Python 2/3 compatibility
from __future__ import print_function
# Allows use of print like a function in Python 2.x

# Import Python modules
import numpy as np
import cv2
import matplotlib as mpl
import os
import sys

# Safe way to check if Environmental Variable is present
try:
    pyth_path = os.environ['PYTHONPATH'].split(os.pathsep)
except KeyError:
    pyth_path = []

try:
    ocv2_path = os.environ['OPENCV_DIR']
except KeyError:
    ocv2_path = []

try:
    ffmp_path = os.environ['FFMPEG_BIN']
except KeyError:
    ffmp_path = []

# Program Outputs
print()
print('OpenCV Environment Information Sample')
print()
print('Please ensure that the following Environment Variables are set correctly before proceeding!')
print()
print('Python Environment Variable - PYTHONPATH:', pyth_path)
print('OpenCV Environment Variable - OPENCV_DIR:', ocv2_path)
print('FFMPEG Environment Variable - FFMPEG_BIN:', ffmp_path)
print()
print('Version Information:')
print()
print(sys.version)
print('OpenCV Version:', cv2.__version__)
print('Numpy Version:', np.__version__)
print('Matplotlib Version:', mpl.__version__)
print()