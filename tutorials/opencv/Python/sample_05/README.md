# OpenCV Tutorial Sample_05: ocv_ocl_info
[Sample 05](ocv_ocl_info.py) is a simple diagnostic program that determines whether OpenCL™ is available for use within OpenCV, Enables OpenCL, checks whether it has been enabled and then disables it. The program then checks if OpenCL has been disabled and exits.

## What is OpenCL™?
**OpenCL™ (Open Computing Language)** is the open standard for parallel programming. Using OpenCL, one can use the GPU for parallel computing tasks other than just for graphics programming. Once can also use DSP's, FPGA's and other types of processors using OpenCL.

## How does OpenCV use OpenCL™?
In Computer Vision many algorithms can run on a GPU much more effectively than on a CPU: e.g. image processing, matrix arithmetic, computational photography, object detection etc. OpenCV 3.x is able to accelerate and optimize performaance by using an architectural concept called _Transparent API (T-API)_ to transparently speed up certain tasks if supported by the underlying hardware.

## Usage:
Launch the interactive tutorial by typing the following command in your comand window:

```
jupyter notebook ./ocv_ocl_info.ipynb
```
OR

You may run the script using the command:

```
python ./ocv_ocl_info.py
```
## Code Walkthrough:

Start with the usual initialization

```
#!/usr/bin/env python2

# Python 2/3 compatibility
from __future__ import print_function
# Allows use of print like a function in Python 2.x

# Import the OpenCV2 module
import cv2
```


Using the OpenCV API **cv2.ocl.haveOpenCL()** returns **(True) if OpenCL is supported. 

If it is supported, OpenCL can be enabled using **cv2.ocl.setUseOpenCL(True)** and disabled using **cv2.ocl.setUseOpenCL(False)**. 

To check if OpenCL has been enabled or disabled, use **cv2.ocl.useOpenCL()** which will return **(True)** or **(False)** as the case may be.

>Note: OpenCV Python module does not currently support enumeration of OpenCL devices.

The enable OpenCL with exception handling and check whether it was enabled, run the following code:

```
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
```

The disable OpenCL with exception handling and check whether it has been disabled, run the following code:

```
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
```

