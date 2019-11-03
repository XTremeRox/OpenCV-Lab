#! /usr/bin/python3
# Detect horizontal vertical lines
import cv2 
import numpy as np
inputimg = cv2.imread("houses.jpeg",0)
# Line detection kernel
# Ref : http://aishack.in/tutorials/image-convolution-examples/
kernelh = np.array([[-1, 2, -1], 
                    [-1, 2, -1], 
                    [-1, 2, -1]], np.int32)
kernelv = np.array([[-1, -1, -1], 
                    [2, 2, 2], 
                    [-1, -1, -1]], np.int32)
dstimg = cv2.filter2D(inputimg,-1,kernelh)
dst2img = cv2.filter2D(inputimg,-1,kernelv)

#Display
cv2.imshow('Input Image' , inputimg)
cv2.imshow('Detection Vertical' , dstimg)
cv2.imshow('Detection Horizontal' , dst2img)
cv2.waitKey(0)
