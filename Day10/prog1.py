#!/usr/bin/python3
#Spot Detection
import cv2 
import numpy as np

inputimg = cv2.imread("umbrella.jpeg",0)
#kernel used for detection
kernel = np.array([[0, 0, 0], 
                    [1, -8, 1], 
                    [0, 0, 0]], np.int32)
dstimg = cv2.filter2D(inputimg,-1,kernel)
cv2.imshow('Input Image' , inputimg)
cv2.imshow('Detect Dots' , dstimg)
cv2.waitKey(0)
