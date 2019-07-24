#!/usr/bin/python3
import cv2
import numpy as np 

#img = cv2.imread("lenna.tif", IMREAD_GRAYSCALE)
img = cv2.imread("lenna.tif", 0)
#cv2.imshow("OpenCV Window", img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

cv2.imwrite("grayscale.jpg", img)