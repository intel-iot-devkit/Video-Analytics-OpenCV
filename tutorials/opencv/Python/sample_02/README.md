# OpenCV Tutorial Sample 2: ocv_build_info

[Sample 02](sample_01/ocv_build_info.py) is a simple diagnostic program that displays the detailed OpenCV build information.

## Usage:
Launch the interactive tutorial by typing the following command in your comand window:

```
jupyter notebook ./ocv_build_info.ipynb
```
OR

You may run the script using the command:

```
python ./ocv_build_info.py
```
## Code Walkthrough:

First the standard Python\* shebang

```
#!/usr/bin/env python2
```
Next import print_function for Python 2/3 compatibility. This allows use of print like a function in Python 2.x

```
from __future__ import print_function
```
Import the OpenCV Python module

```
import cv2
```
Now obtain and print OpenCV Build Configuration. The function getBuildInformation() returns the full configuration time cmake output

```
try:
	buildinfo = cv2.getBuildInformation()
	print(buildinfo)

except cv2.error as e:
	print('Error:')
```  

**Program Output:**

```
General configuration for OpenCV 3.2.0 =====================================
  Version control:               3.2.0

  Platform:
    Timestamp:                   2016-12-23T14:50:36Z
    Host:                        Windows 10.0.14393 AMD64
    CMake:                       3.7.0
    CMake generator:             Visual Studio 14 2015
    CMake build tool:            C:/Program Files (x86)/MSBuild/14.0/bin/MSBuild.exe
    MSVC:                        1900

  C/C++:
    Built as dynamic libs?:      NO
    C++ Compiler:                C:/Program Files (x86)/Microsoft Visual Studio 14.0/VC/bin/cl.exe  (ver 19.0.24215.1)
    C++ flags (Release):         /DWIN32 /D_WINDOWS /W4 /GR /EHa  /D _CRT_SECURE_NO_DEPRECATE /D _CRT_NONSTDC_NO_DEPRECATE /D _SCL_SECURE_NO_WARNINGS /Gy /bigobj /arch:SSE2 /Oi /fp:fast  /wd4251 /wd4324 /wd4275 /wd4589 /MP8  /MT /O2 /Ob2 /DNDEBUG  /Zi
    C++ flags (Debug):           /DWIN32 /D_WINDOWS /W4 /GR /EHa  /D _CRT_SECURE_NO_DEPRECATE /D _CRT_NONSTDC_NO_DEPRECATE /D _SCL_SECURE_NO_WARNINGS /Gy /bigobj /arch:SSE2 /Oi /fp:fast  /wd4251 /wd4324 /wd4275 /wd4589 /MP8  /D_DEBUG /MTd /Zi /Ob0 /Od /RTC1 
    C Compiler:                  C:/Program Files (x86)/Microsoft Visual Studio 14.0/VC/bin/cl.exe
    C flags (Release):           /DWIN32 /D_WINDOWS /W3  /D _CRT_SECURE_NO_DEPRECATE /D _CRT_NONSTDC_NO_DEPRECATE /D _SCL_SECURE_NO_WARNINGS /Gy /bigobj /arch:SSE2 /Oi /fp:fast    /MP8  /MT /O2 /Ob2 /DNDEBUG  /Zi
    C flags (Debug):             /DWIN32 /D_WINDOWS /W3  /D _CRT_SECURE_NO_DEPRECATE /D _CRT_NONSTDC_NO_DEPRECATE /D _SCL_SECURE_NO_WARNINGS /Gy /bigobj /arch:SSE2 /Oi /fp:fast    /MP8  /D_DEBUG /MTd /Zi /Ob0 /Od /RTC1 
    Linker flags (Release):      /machine:X86  /NODEFAULTLIB:atlthunk.lib /NODEFAULTLIB:msvcrt.lib /NODEFAULTLIB:msvcrtd.lib /INCREMENTAL:NO  /debug /NODEFAULTLIB:libcmtd.lib
    Linker flags (Debug):        /machine:X86  /NODEFAULTLIB:atlthunk.lib /NODEFAULTLIB:msvcrt.lib /NODEFAULTLIB:msvcrtd.lib /debug /INCREMENTAL  /NODEFAULTLIB:libcmt.lib
    ccache:                      NO
    Precompiled headers:         YES
    Extra dependencies:          comctl32 gdi32 ole32 setupapi ws2_32 vfw32
    3rdparty dependencies:       zlib libjpeg libwebp libpng libtiff libjasper IlmImf ippicv

  OpenCV modules:
    To be built:                 core flann imgproc ml photo video imgcodecs shape videoio highgui objdetect superres features2d calib3d java stitching videostab python2
    Disabled:                    python3 world
    Disabled by dependency:      -
    Unavailable:                 cudaarithm cudabgsegm cudacodec cudafeatures2d cudafilters cudaimgproc cudalegacy cudaobjdetect cudaoptflow cudastereo cudawarping cudev ts viz

  Windows RT support:            NO

  GUI: 
    QT:                          NO
    Win32 UI:                    YES
    OpenGL support:              NO
    VTK support:                 NO

  Media I/O: 
    ZLib:                        build (ver 1.2.8)
    JPEG:                        build (ver 90)
    WEBP:                        build (ver 0.3.1)
    PNG:                         build (ver 1.6.24)
    TIFF:                        build (ver 42 - 4.0.2)
    JPEG 2000:                   build (ver 1.900.1)
    OpenEXR:                     build (ver 1.7.1)
    GDAL:                        NO
    GDCM:                        NO

  Video I/O:
    Video for Windows:           YES
    DC1394 1.x:                  NO
    DC1394 2.x:                  NO
    FFMPEG:                      YES (prebuilt binaries)
      avcodec:                   YES (ver 57.64.101)
      avformat:                  YES (ver 57.56.100)
      avutil:                    YES (ver 55.34.100)
      swscale:                   YES (ver 4.2.100)
      avresample:                YES (ver 3.1.0)
    GStreamer:                   NO
    OpenNI:                      NO
    OpenNI PrimeSensor Modules:  NO
    OpenNI2:                     NO
    PvAPI:                       NO
    GigEVisionSDK:               NO
    DirectShow:                  YES
    Media Foundation:            NO
    XIMEA:                       NO
    Intel PerC:                  NO

  Parallel framework:            Concurrency

  Other third-party libraries:
    Use IPP:                     9.0.1 [9.0.1]
         at:                     C:/build/master_winpack-bindings-win32-vc14-static/build/3rdparty/ippicv/ippicv_win
    Use IPP Async:               NO
    Use Lapack:                  NO
    Use Eigen:                   NO
    Use Cuda:                    NO
    Use OpenCL:                  YES
    Use OpenVX:                  NO
    Use custom HAL:              NO

  OpenCL:                        <Dynamic loading of OpenCL library>
    Include path:                C:/build/master_winpack-bindings-win32-vc14-static/opencv/3rdparty/include/opencl/1.2
    Use AMDFFT:                  NO
    Use AMDBLAS:                 NO

  Python 2:
    Interpreter:                 C:/utils/soft/python27-x86/python.exe (ver 2.7.12)
    Libraries:                   C:/utils/soft/python27-x86/Libs/python27.lib (ver 2.7.12)
    numpy:                       C:/utils/soft/python27-x86/lib/site-packages/numpy/core/include (ver 1.11.2)
    packages path:               C:/utils/soft/python27-x86/Lib/site-packages

  Python 3:
    Interpreter:                 C:/utils/soft/python35-x86/python.exe (ver 3.5.2)

  Python (for build):            C:/utils/soft/python27-x86/python.exe

  Java:
    ant:                         C:/utils/soft/apache-ant-1.9.7/bin/ant.bat (ver 1.9.7)
    JNI:                         C:/Program Files (x86)/Java/jdk1.8.0_112/include C:/Program Files (x86)/Java/jdk1.8.0_112/include/win32 C:/Program Files (x86)/Java/jdk1.8.0_112/include
    Java wrappers:               YES
    Java tests:                  NO

  Matlab:                        Matlab not found or implicitly disabled

  Tests and samples:
    Tests:                       NO
    Performance tests:           NO
    C/C++ Examples:              NO

  Install path:                  C:/build/master_winpack-bindings-win32-vc14-static/install

  cvconfig.h is in:              C:/build/master_winpack-bindings-win32-vc14-static/build
-----------------------------------------------------------------
```
