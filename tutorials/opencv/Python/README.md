# Python Code Samples for Video Analytics with OpenCV
#### *- With a focus on Digital Signage

Modern retail settings incorporate computer vision technologies for video analytics as well as attribution purposes. These tutorial samples are intended for developers of computer vision and analytics and uses the widely used Open-Source Computer Vision (OpenCV) library for computer vision.

To learn more about the use of Computer Vision and Video Analytics refer to the following article:

[Introduction to Developing and Optimizing Display Technology](https://software.intel.com/en-us/articles/introduction-to-developing-and-optimizing-display-technology)

To learn how to install OpneCV for these tutorial samples, refer to the following document:

[Installing OpenCV for Python\*](../../../docs/OpenCV/Python/InstallOpenCV_Python.md)

## Code Samples
The code samples are mainly in two categories: Diagnostics and Application

Diagnostic Samples:

	Sample 01 - Version information and environment variables
	Sample 02 - OpenCV* build information
	Sample 03 - Basic image test - overlay text
	Sample 04 - Basic video test - stream and overlay text
	Sample 05 - Checks for OpenCL availability
	Sample 07 - Checks for hardware extension support

Application Samples:

	Sample 06 - Video steam and capture image
	Sample 08 - Watermarking still image
	Sample 09 - Watermarking display stream
	Sample 10 - Still image face and eye detection
	Sample 11 - Real-time video face detection and tracking
	Sample 12 - Real-time people counter

### Usage
All the code samples have an individual README how to use the sample as well as an Interactive Jupyter Notebook\* based tutorial. In addition, the code samples are extensively commented.

### OpenCV Information

[Sample 01](sample_01/ocv_info.py) is a simple diagnostic program that queries the development environment and ensures that all the prerequisites have been met and displays the version information. It also checks to see if Environment variables have been set and displays the path for diagnostics if necessary.

### OpenCV Build Information

[Sample 02](sample_02/ocv_build_info.py) is a simple diagnostic program that displays the detailed OpenCV build information.

### OpenCV Image Test

[Sample 03](sample_03/ocv_image_test.py) is a sanity test that uses OpenCV to display an Image file. This test serves to ensure that OpenCV installation is working and validates the development environment. It also shows how to overlay text on an image.

### OpenCV Video Test

[Sample 04](sample_04/ocv_video_test.py) is a sanity test that uses OpenCV to connect to a WebCam and display the video stream. This test serves to ensure that OpenCV WebCam installation is working and further validates the development environment. It also shows how to overlay text on video streams.

### OpenCV with OpenCL™

[Sample 05](sample_05/ocv_ocl_info.py) is a simple diagnostic program that determines whether OpenCL is available for use within OpenCL™, Enables OpenCL, checks whether it has been enabled and then disables it. The program then checks if OpenCL has been disabled and exits.

> _**Note:**_ OpenCV v3.2.0 pre-built binary release can use OpenCL if it has been properly installed. The Intel optimized OpenCL drivers are installed as part of the integrated Intel® Graphics Driver. OpenCL is currently supported better in C++ rather than on Python where you can only display status and enable or disable use of an OpenCL resource.

### OpenCV Video Capture

[Sample 06](sample_06/ocv_vid_cap.py) is a simple program that uses OpenCV to connect to a WebCam in order to capture and save an image. This example is the basic first step for most video analytics programs. The video output of the WebCam is displayed and when the user inputs a keystroke, the frame is captured and written to an image file.

### OpenCV Hardware Info

[Sample 07](sample_07/ocv_hw_info.py) is a simple diagnostic program that determines how many logical CPU's are available and then queries the hardware to check whether MMX™ and Intel® Streaming SIMD Extensions (Intel® SSE), Intel® Advanced Vector Extensions etc. are supported .

> _**Note:**_ The OpenCV function cv2.checkHardwareSupport(feature) returns true if the host hardware supports the specified feature. When users call setUseOptimized(False), all the subsequent calls to cv2.checkHardwareSupport() will return false until cv2.setUseOptimized(True) is called. This way users can dynamically switch on and off the optimized code in OpenCV.

### OpenCV DOG Image

[Sample 08](sample_08/ocv_dog_img.py) is a program that overlays a **Digital On-Screen Graphic (DOG)** onto a still image. DOG is a form of digital watermarking routinely used on broadcast TV to show the TV channel logo. It can also be used on digital signage to watermark content. 

### OpenCV DOG Video

[Sample 09](sample_09/ocv_dog_vid.py) is a program that overlays a **Digital On-Screen Graphic (DOG)** on the display stream. This program uses the same principles as used for the previous example. 

### OpenCV Face and Eyes Detection - Still Image

[Sample 10](sample_10/ocv_face_img.py) is a basic Face and Eye Detection program that uses OpenCV to analyze an image and detect human faces and eyes. The detected areas or Regions of Interest (ROI) are demarcated with rectangles. The program uses the OpenCV built-in pre-trained Haar feature-based cascade classifiers in order to perform this task.

### OpenCV Real-Time Video Face Detection and Tracking

[Sample 11](sample_11/ocv_face_vid.py) is a basic Face and Eye Detection program that uses OpenCV to analyze real-time video and detect human faces and eyes. The detected areas or Regions of Interest (ROI) are demarcated with rectangles. The program uses the OpenCV built-in pre-trained Haar feature-based cascade classifiers in order to perform this task.

### OpenCV Real-Time Video People Counter using Face Detection

[Sample 12](sample_12/ocv_face_cnt_vid.py) is a basic People Counter using the previous Face and Eye Detection program that uses OpenCV to analyze real-time video and detect human faces and eyes. In addition to detecting Faces and Eyes, the program also returns the number of faces detected to the console.
