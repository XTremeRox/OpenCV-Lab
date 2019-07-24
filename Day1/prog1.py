#!/usr/bin/python3
import cv2
import numpy as np 

# IMREAD_UNCHANGED = -1
# IMREAD_GRAYSCALE = 0 
# IMREAD_COLOR = 1 

#img = cv2.imread("lenna.tif", IMREAD_COLOR)
img = cv2.imread("lenna.tif", 1)
cv2.imshow("OpenCV Window", img)
cv2.waitKey(0)
cv2.destroyAllWindows()