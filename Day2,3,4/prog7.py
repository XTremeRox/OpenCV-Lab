#!/usr/bin/python3
import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img1 = cv2.imread("lena512color.tiff", 0)
img2 = img1 & (15) #00001111
img3 = img1-img2

#histogram_equalisation
img4 = cv2.equalizeHist(img3)

#plotting
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(img1, cmap="gray", interpolation=None)
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(img2, cmap="gray", interpolation=None)
ax3 = fig.add_subplot(2,2,3)
ax3.imshow(img3, cmap="gray", interpolation=None)
ax4 = fig.add_subplot(2,2,4)
ax4.imshow(img4, cmap="gray", interpolation=None)
#Remove Axis
ax1.axis("off")
ax2.axis("off")
ax3.axis("off")
ax4.axis("off")
plt.show()