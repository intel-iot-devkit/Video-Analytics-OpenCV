# OpenCV Tutorial Sample 7: ocv_hw_info
[Sample 07](ocv_hw_info.py) is a simple diagnostic program that determines how many logical CPU's are available and then queries the hardware to check whether MMX™ and Intel® Streaming SIMD Extensions (Intel® SSE), Intel® Advanced Vector Extensions etc. are supported .

>Note: The OpenCV function cv2.checkHardwareSupport(feature) returns true if the host hardware supports the specified feature. When users call setUseOptimized(False), all the subsequent calls to cv2.checkHardwareSupport() will return false until cv2.setUseOptimized(True) is called. This way users can dynamically switch on and off the optimized code in OpenCV.

## Usage:
Launch the interactive tutorial by typing the following command in your comand window:

```
jupyter notebook ./ocv_hw_info.ipynb
```
OR

You may run the script using the command:

```
python ./ocv_hw_info.py
```
## Code Walkthrough:
Start with the usual initializations

```
#!/usr/bin/env python

# Python 2/3 compatibility
from __future__ import print_function
# Allows use of print like a function in Python 2.x

# Import the OpenCV2 module
import cv2
```
Check the number of logical CPUs available. This function returns the number of logical CPUs available

```
cpu = cv2.getNumberOfCPUs()
print()
print("Number of logical CPU's Available: ", end='')
print(cpu)
print()
```
**Console Output:**
```
Number of logical CPU's Available: 8
```

Now Reset Hardware Optimization Flags in case they were set by some other program.
```
cv2.setUseOptimized(True)
```
The functions below return true if the host hardware supports the specified feature. When user calls **setUseOptimized(False)**, all the subsequent calls to **checkHardwareSupport()** will return **(False)** until **setUseOptimized(True)** is called. This way user can dynamically switch on and off the optimized code in OpenCV.

```
# Assign ID to Features as labels don't seem to be working currently for Python
cv2.CPU_MMX = 1
cv2.CPU_SSE = 2
cv2.CPU_SSE2 = 3
cv2.CPU_SSE3 = 4
cv2.CPU_SSSE3 = 5
cv2.CPU_SSE4_1 = 6
cv2.CPU_SSE4_2 = 7
cv2.CPU_POPCNT = 8
cv2.CPU_AVX = 9
```
Now we can test and print support status for each hardware feature:

Returns True if CPU is **MMX** capable
```
mmx = cv2.checkHardwareSupport(cv2.CPU_MMX)
print("CPU MMX Capable?: ", end='')
print(mmx)
```
**Console Output:**
```
CPU MMX Capable?: True
```

Returns True if CPU is **SSE** capable
```
sse = cv2.checkHardwareSupport(cv2.CPU_SSE)
print("CPU SSE Capable?: ", end='')
print(sse)
```

**Console Output:**
```
CPU SSE Capable?: True
```

Returns True if CPU is **SSE2** capable
```
sse2 = cv2.checkHardwareSupport(cv2.CPU_SSE2)
print("CPU SSE 2 Capable?: ", end='')
print(sse2)
```
**Console Output:**
```
CPU SSE 2 Capable?: True
```

Returns True if CPU is **SSE3** capable
```
sse3 = cv2.checkHardwareSupport(cv2.CPU_SSE3)
print("CPU SSE 3 Capable?: ", end='')
print(sse3)
```
**Console Output:**
```
CPU SSE 3 Capable?: True
```

Returns True if CPU is **SSSE3** capable
```
ssse3 = cv2.checkHardwareSupport(cv2.CPU_SSSE3)
print("CPU SSSE 3 Capable?: ", end='')
print(ssse3)
```
**Console Output:**
```
CPU SSSE 3 Capable?: True
```

Returns True if CPU is **SSE4.1** capable
```
sse4_1 = cv2.checkHardwareSupport(cv2.CPU_SSE4_1)
print("CPU SSE 4.1 Capable?: ", end='')
print(sse4_1)
```
**Console Output:**
```
CPU SSE 4.1 Capable?: True
```

Returns True if CPU is **SSE4.2** capable
```
sse4_2 = cv2.checkHardwareSupport(cv2.CPU_SSE4_2)
print("CPU SSE 4.2 Capable?: ", end='')
print(sse4_2)
```
**Console Output:**
```
CPU SSE 4.2 Capable?: True
```

Returns True if CPU is **POP** capable
```
popcnt = cv2.checkHardwareSupport(cv2.CPU_POPCNT)
print("CPU POPCNT Capable?: ", end='')
print(popcnt)
```
**Console Output:**
```
CPU POPCNT Capable?: True
```

Returns True if CPU is **AVX** capable
```
avx = cv2.checkHardwareSupport(cv2.CPU_AVX)
print("CPU AVX Capable?: ", end='')
print(avx)
```
**Console Output:**
```
CPU AVX Capable?: True
```
