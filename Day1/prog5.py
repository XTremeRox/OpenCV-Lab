#!/usr/bin/python3
import cv2
import numpy as np 
import matplotlib.pyplot as plt 

#img = cv2.imread("lenna.tif", IMREAD_GRAYSCALE)
img = cv2.imread("lenna.tif", 0)

img[261,270] = img[261,271] + 150.0 # a pixel near the eye

plt.imshow(img, cmap="gray", interpolation=None)
plt.show()