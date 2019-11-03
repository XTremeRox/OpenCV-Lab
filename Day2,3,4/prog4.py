#!/usr/bin/python3
import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img1 = cv2.imread("lena512color.tiff", 0)

# Reduction new = (old/bit)*bit 
x = int(input("Enter the required gray level : "))
img1 = img1//(256/x)

plt.imshow(img1, cmap="gray", interpolation=None)
plt.show()