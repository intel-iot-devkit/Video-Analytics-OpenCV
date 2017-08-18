# Installing OpenCV for Python

## On Windows 

### Using Windows 10 is highly recommended due to updated drivers
Recommended Build: Windows 10 Anniversary Edition or Creators Update.

### Install Anaconda for Windows

Download and install Anaconda for Windows by following this installation document (https://docs.continuum.io/anaconda/install-windows)

It is recommended that you install Python 2.7.x as pre-built OpenCV 3.2.0 ships with 2.7.x compatible packages. Either 32-bit or 64-bit versions are OK depending on your OS and hardware.

### Install Intel® Python Distribution using Anaconda

Install the Intel® Python Distribution and Intel® Performance libraries in a virtual environment by following this installation document (https://software.intel.com/en-us/articles/using-intel-distribution-for-python-with-anaconda)

It is recommended that you install the full distibution ***intelpython2_full*** for Python 2. 

#### Verify that Numpy and Matplotlib are installed

OpenCV uses Numpy arrays to manipulate image and video data and is a mandatory requirement. Matplotlib is used in a number of tutorials found in the OpenCV package. Installing the full distribution of Intel® Python would install optimized versions of both packages.

1. Numpy Version

``` 
(idp) $/>python -c "import numpy; print (numpy.__version__)"
1.12.1
```

2. Matplotlib

```
(idp) $/>python -c "import matplotlib; print (matplotlib.__version__)"
2.0.0
```
### OpenCV Installation Steps using pre-built library

1. Download the pre-built OpenCV release for Windows from the OpenCV repository on Github. Ensure that you get Release tag 3.2.0 or higher from 
(https://github.com/opencv/opencv/releases/latest)

	For example, download **_opencv-3.2.0-vc14.exe_** for Release 3.2.0

2. Extract the archive to a short path such as C:\OpenCV

3. Go to opencv/build/python/2.7 folder and then into x64 or x86 depending on your Windows installation.

5. Copy **_cv2.pyd_** to the **_site-packages_** folder inside your Intel Python Distribution environment.

6. Add a System Environment variable **OPENCV_DIR** that points to the location of the OpenCV folder in Step 2. For example, it should point to **C:\OpenCV** if you followed the recommendation above.

	The procedure to add a System Environment Variable can be found in this document. (https://msdn.microsoft.com/en-us/library/bb726962.aspx)

7. Add a System Environment variable **OPENCV_VER** with the version number of the installed OpenCV without the decimal point separators. 
	
	For example, the value of **OPENCV_VER** for OpenCV 3.2.0 would be **320**.

8. Add a System Environment variable **FFMPEG_BIN** that points to the location of the FFMPEG dlls included in OpenCV appropriate for your architecture. For both 32-bit and 64-bit it should point to **C:\OpenCV\opencv\build\bin**. This allows the use of FFMPEG to encode and decode media for OpenCV.

## On Ubuntu Linux
### Using Ubuntu 16.04.2 is highly recommended due to updated drivers

OpenCV is not available pre-built for Linux distributions. You will need to build OpenCV on Ubuntu and then install the Python bindings. Please refer to Building OpenCV for Python. (TBD)

## OpenCV Verification

```
(idp) $/>python -c "import cv2; print (cv2.__version__)"
3.2.0
```
This indictates that OpenCV 3.2.0 is working properly with Python.

### Sanity Tests

Included in the code samples are instructions to run some basic sanity tests to ensure that your environment is properly functioning.

1. [Build Information - Sample_01](https://github.com/vraoresearch/Intel-Digital-Signage-Reference/blob/master/tutorials/opencv/Python/sample_01/ocv_info.py)
2. [Image Test - Sample_03](https://github.com/vraoresearch/Intel-Digital-Signage-Reference/blob/master/tutorials/opencv/Python/sample_03/ocv_image_test.py)
3. [Video Capture Test - Sample_04](https://github.com/vraoresearch/Intel-Digital-Signage-Reference/blob/master/tutorials/opencv/Python/sample_04/ocv_video_test.py)

### OpenCV Information

To learn more about the compiler flags used to build OpenCV:

[Build Information - Sample_02](https://github.com/vraoresearch/Intel-Digital-Signage-Reference/blob/master/tutorials/opencv/Python/sample_02/ocv_build_info.py)

