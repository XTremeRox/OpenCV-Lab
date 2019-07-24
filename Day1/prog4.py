#!/usr/bin/python3
import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img1 = cv2.imread("lenna.tif", 1)
img2 = cv2.imread("barbara_gray.bmp", 1)

#img3 = img1+img2
img3 = img1-img2

#plt.imshow(img, cmap="gray", interpolation=None)
plt.imshow(img3, cmap="gray", interpolation="bicubic")
plt.show()