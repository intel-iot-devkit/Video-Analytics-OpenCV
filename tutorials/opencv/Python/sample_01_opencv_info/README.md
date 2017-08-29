# OpenCV Tutorial Sample_01: ocv_info

[Sample 01](ocv_info.py) is a simple diagnostic program that queries the development environment and ensures that all the prerequisites have been met and displays the version information. It also checks to see if Environment variables have been set and displays the path for diagnostics if necessary.

>Note: If you are using pre-built OpenCV, you need to use Python\* 2.7.x to run the samples. If you have built OpenCV from source, then you can use either Python 3.x or Python 2.x.

## Usage:
Launch the interactive tutorial by typing the following command in your comand window:

```
jupyter notebook ./ocv_info.ipynb
```
OR

You may run the script using the command:

```
python ./ocv_info.py
```
## Code Walkthrough:

First the Standard Python Shebang

```
#!/usr/bin/env python2
```
Next import print_function for Python 2/3 comptibility. This allows use of print like a function in Python 2.x

```
from __future__ import print_function
```

OpenCV uses Numpy arrays to manipulate image and video data and is a mandatory requirement. So import numpy module first.

```
import numpy as np
```

Now print the version. In the script this is done at the end in the Program Outputs block

```
print('Numpy Version:', np.__version__)
```
**Numpy Version: 1.12.1**

Next import the OpenCV python module

```
import cv2
```

Now print the version. In the script this is done at the end in the Program Outputs block

```
print('OpenCV Version:', cv2.__version__)
```
**OpenCV Version: 3.2.0**

Import the other required python modules for this script. Matplotlib is used in a number of tutorials found in the OpenCV package and OS and sys are needed to test whether the OpenCV environment variables are properly setup.

```
import matplotlib as mpl
import os
import sys
```

Now print the versions here. In the script this is done at the end in the Program Outputs block

```
print('Matplotlib Version:', mpl.__version__)
print(sys.version)
```
**Matplotlib Version: 2.0.12.7.13 |Anaconda custom (32-bit)| (default, Dec 19 2016, 13:36:02) [MSC v.1500 32 bit (Intel)]**

Now we check to see if the OpenCV environment variables have been properly set. We need to do this in a safe way to prevent the script from crashing in case no variable has been set. So use standard python exception handling...

```
try:
    pyth_path = os.environ['PYTHONPATH'].split(os.pathsep)
except KeyError:
    pyth_path = []
```    

Now print the environment variable. In the script this is done at the end in the Program Outputs block.

```
print('Python Environment Variable - PYTHONPATH:', pyth_path)
```
**Python Environment Variable - PYTHONPATH: ['C:\\Users\\vinay\\Anaconda2\\Library\\bin']**

Next check the OpenCV environemnt variables

```
try:
    ocv2_path = os.environ['OPENCV_DIR']
except KeyError:
    ocv2_path = []
    
try:
    ocv2_vers = os.environ['OPENCV_VER']
except KeyError:
    ocv2_path = []
```

Now print the environment variable. In the script this is done at the end in the Program Outputs block

```
print('OpenCV Environment Variable - OPENCV_DIR:', ocv2_path)
print('OpenCV Environment Variable - OPENCV_VER:', ocv2_vers)
OpenCV Environment Variable - OPENCV_DIR: C:\opencv_pre\
OpenCV Environment Variable - OPENCV_VER: 320
```

Finally check the FFMPEG environment variable

```
try:
    ffmp_path = os.environ['FFMPEG_BIN']
except KeyError:
    ffmp_path = []
```

Now print the environment variable. In the script this is done at the end in the Program Outputs block

```
print('FFMPEG Environment Variable - FFMPEG_BIN:', ffmp_path)
```

**FFMPEG Environment Variable - FFMPEG_BIN: C:\opencv_pre\build\bin**

If you did not see any errors, you are to be congratulated on setting up your OpenCV environment correctly.

**Congratulations!**
