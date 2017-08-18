#!/usr/bin/env python

# Python 2/3 compatibility
from __future__ import print_function
# Allows use of print like a function in Python 2.x

# Import the OpenCV2 module
import cv2

try:
	# Returns the number of logical CPUs available
	cpu = cv2.getNumberOfCPUs()
	#Reset Hardware Optimization Flags
	cv2.setUseOptimized(True)
	# The functions below return true if the host hardware 
	# supports the specified feature
	# When user calls setUseOptimized(false), 
	# all the subsequent calls to checkHardwareSupport() will return false
	# until setUseOptimized(true) is called. 
	# This way user can dynamically switch on and off the optimized code in OpenCV.

	# Assign ID to Features as this doesn't seem to be working currently
	cv2.CPU_MMX = 1
	cv2.CPU_SSE = 2
	cv2.CPU_SSE2 = 3
	cv2.CPU_SSE3 = 4
	cv2.CPU_SSSE3 = 5
	cv2.CPU_SSE4_1 = 6
	cv2.CPU_SSE4_2 = 7
	cv2.CPU_POPCNT = 8
	cv2.CPU_AVX = 9

	# Returns True if CPU is MMX capable
	mmx = cv2.checkHardwareSupport(cv2.CPU_MMX)
	# Returns True if CPU is SSE capable
	sse = cv2.checkHardwareSupport(cv2.CPU_SSE)
	# Returns True if CPU is SSE2 capable
	sse2 = cv2.checkHardwareSupport(cv2.CPU_SSE2)
	# Returns True if CPU is SSE3 capable
	sse3 = cv2.checkHardwareSupport(cv2.CPU_SSE3)
	# Returns True if CPU is SSSE3 capable
	ssse3 = cv2.checkHardwareSupport(cv2.CPU_SSSE3)
	# Returns True if CPU is SSE4.1 capable
	sse4_1 = cv2.checkHardwareSupport(cv2.CPU_SSE4_1)
	# Returns True if CPU is SSE4.2 capable
	sse4_2 = cv2.checkHardwareSupport(cv2.CPU_SSE4_2)
	# Returns True if CPU is POP capable
	popcnt = cv2.checkHardwareSupport(cv2.CPU_POPCNT)
	# Returns True if CPU is AVX capable
	avx = cv2.checkHardwareSupport(cv2.CPU_AVX)

	#Program Output
	print()
	print('OpenCV - HW Info sample')
	print()

	print("Number of logical CPU's Available: ", end='')
	#print(cv2.getNumberOfCPUs())
	print(cpu)
	print()
	print("CPU MMX Capable?: ", end='')
	#print(cv2.getNumberOfCPUs())
	print(mmx)
	print("CPU SSE Capable?: ", end='')
	#print(cv2.getNumberOfCPUs())
	print(sse)
	print("CPU SSE 2 Capable?: ", end='')
	#print(cv2.getNumberOfCPUs())
	print(sse2)
	print("CPU SSE 3 Capable?: ", end='')
	#print(cv2.getNumberOfCPUs())
	print(sse3)
	print("CPU SSSE 3 Capable?: ", end='')
	#print(cv2.getNumberOfCPUs())
	print(ssse3)
	print("CPU SSE 4.1 Capable?: ", end='')
	#print(cv2.getNumberOfCPUs())
	print(sse4_1)
	print("CPU SSE 4.2 Capable?: ", end='')
	#print(cv2.getNumberOfCPUs())
	print(sse4_2)
	print("CPU POPCNT Capable?: ", end='')
	#print(cv2.getNumberOfCPUs())
	print(popcnt)
	print("CPU AVX Capable?: ", end='')
	#print(cv2.getNumberOfCPUs())
	print(avx)
	print()

except cv2.error as e:
	print('Error:')