#!/usr/bin/python3
import cv2
import numpy as np 
import matplotlib.pyplot as plt 

#img = cv2.imread("lenna.tif", IMREAD_GRAYSCALE)
img = cv2.imread("lenna.tif", 0)

#plt.imshow(img, cmap="gray", interpolation=None)
plt.imshow(img, cmap="gray", interpolation="bicubic")
plt.show()