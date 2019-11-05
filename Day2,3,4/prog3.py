#!/usr/bin/python3
import numpy as np
import cv2
import matplotlib.pyplot as plt

img=np.float32(cv2.imread('lena512color.tiff',0))
print("Gray level required : ")
x=int(input())
img1=np.float32(img*(x/8))
plt.imshow(img1)plt.show()