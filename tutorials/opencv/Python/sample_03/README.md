# OpenCV Tutorial Sample 3: ocv_image_test
[Sample 03](sample_03/ocv_image_test.py) is a sanity test that uses OpenCV to display an Image file. This test serves to ensure that OpenCV installation is working and validates the development environment. It also shows how to overlay text on an image.

## Usage:

Launch the interactive tutorial by typing the following command in your comand window:

```
jupyter notebook ./ocv_image_test.ipynb
```
OR

You may run the script using the command:

```
python ./ocv_image_test.py
```
## Code Walkthrough:

First the Standard Python\* Shebang

```
#!/usr/bin/env python2
```
Next import print_function for Python 2/3 comptibility. This allows use of print like a function in Python 2.x
```
from __future__ import print_function
```

Import Numpy and OpenCV Python modules
```
import numpy as np
import cv2
```

Load an image from file using the OpenCV cv2.imread() function.
```
cv2.imread(filename[, flags]) -> retval
```
_**Parameters:**_

**filename – Name and path of file to be loaded.**

**flags:**

Flags specify how the image should be read:
```
  1 = cv2.IMREAD_COLOR - The Default flag, loads a color image. Any transparency data of image will be ignored.
  0 = cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
 -1 = cv2.IMREAD_UNCHANGED : Loads image without any modifications including alpha channel**_
```
Here we use the function to open a JPG file called intel-hq.jpg present in the sample_03 folder.
```
img = cv2.imread('intel-hq.jpg',1)
```
_The color information for images loaded by OpenCV are in reverse order (BGR) and are stored as a numpy array._

>Note: The following section between the lines, is only available in the interactive tutorial and not in the script.
----------------------------------------------------------------------------------------------------------------------------------------
To see how img is stored, see it's type. It is a Numpy ndarray.

```
print(type(img))
```

**<type 'numpy.ndarray'>**

Now print the array

```
print(img)
[[[147  95  54]
  [140  90  44]
  [156 108  60]
  ..., 
  [165 132  93]
  [161 127  91]
  [153 119  83]]

 [[142  93  45]
  [142  94  46]
  [139  96  47]
  ..., 
  [160 126  90]
  [156 122  86]
  [148 114  78]]

 [[136  91  40]
  [136  96  44]
  [116  80  34]
  ..., 
  [153 119  83]
  [148 113  79]
  [141 106  72]]

 ..., 
 [[180 177 192]
  [178 175 190]
  [177 174 189]
  ..., 
  [199 198 214]
  [200 199 215]
  [199 197 216]]

 [[179 176 191]
  [180 177 192]
  [179 176 191]
  ..., 
  [197 196 212]
  [198 196 215]
  [200 198 217]]

 [[178 175 190]
  [180 177 192]
  [181 178 193]
  ..., 
  [194 192 211]
  [195 193 212]
  [199 197 216]]]
```
You can also display this image inline with the interactive tutorial using matplotlib which processes images in RGB format to see that OpenCV loads images in BGR format

```
from matplotlib import pyplot as plt
plt.imshow(img)
plt.show()
```
This produces the image shown below:

![Image displayed in BGR format](https://github.com/vraoresearch/Intel-Digital-Signage-Reference/blob/master/tutorials/opencv/Python/sample_03/matplotlib_unconverted.png)

After conversion to RGB, the image properly displays. Here we use an OpenCV cv2.cvtColor() function to convert colors...

```
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img2)
plt.show()
```
This produces the converted image shown below:

![Image displayed in BGR format](https://github.com/vraoresearch/Intel-Digital-Signage-Reference/blob/master/tutorials/opencv/Python/sample_03/matplotlib_converted.png)

>Note: From this point on, we return to the script ...
----------------------------------------------------------------------------------------------------------------------------------------

Next we overlay text on top of the image using the OpenCV cv2.putText() function.
```
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "OpenCV Version:",(10,100), font, 2,(255,255,255),2,cv2.LINE_AA)
cv2.putText(img, cv2.__version__,(525,100), font, 2,(255,255,255),2,cv2.LINE_AA)
```
Now we create a GUI window to display the loaded image. We do this using the **cv2.namedWindow()** function. It is not necessary to use this function to display the image but using this function allows for better control over GUI windows.

>Note: Sometimes Jupyter Notebook\* based interactive tutorials may not open a GUI window when run locally. In such cases, use the function **cv2.startWindowThread()** as shown below, before calling namedWindow function.

```
cv2.startWindowThread()
cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
```
An empty window will open until an image is displayed. So lets create a GUI window to display the image

```
cv2.namedWindow('Sample_03: Displaying an Image', cv2.WINDOW_AUTOSIZE)
```

Now we display the previously loaded image with the overlay text inside this window using the OpenCV cv2.imshow() function.
Note: Since we are using an OpenCV function to display the image, there is no need for conversion from BGR to RGB. The image will not load until the event handler is called.

```
cv2.imshow('Sample_03: Displaying an Image',img)
```

_The cv2.imshow() function should be followed by the **cv2.waitKey()** which displays the image for the specified number of milliseconds. This function is also an event handler and can be bound to the keyboard as seen in our example.

```
# Exit on any keystroke
if cv2.waitKey(0):
    print('Exiting ...')
Exiting ...
```

Now we perform a cleanup and release all resources used using the function cv2.destroyAllWindows()

```
# Release resources used
cv2.destroyAllWindows()
```
Putting it all together with Exception handling:
```
try:
	# Load the image from file using OpenCV. The 1 means with color info
	example = cv2.imread('intel-hq.jpg',1)
	# Overlay text on the image using OpenCV
	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(example, "OpenCV Version:",(10,100), font, 2,(255,255,255),2,cv2.LINE_AA)
	cv2.putText(example, cv2.__version__,(525,100), font, 2,(255,255,255),2,cv2.LINE_AA)

	# Create a GUI window to display the image
	cv2.namedWindow('Image display', cv2.WINDOW_AUTOSIZE)

	# Display the Image
	cv2.imshow('Image display',example)
	# Exit on any keystroke
	if cv2.waitKey(0):
		print('Exiting ...')

	# Release resources used
	cv2.destroyAllWindows()

except cv2.error as e:
	print('Error:')
```
