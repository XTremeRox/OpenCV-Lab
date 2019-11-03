#!/usr/bin/python3
import cv2
import numpy as np 
import matplotlib.pyplot as plt 

def returngray(graylevel):
    # split16 = [0,31,32,63,54,95,96,127,128,159,160,191,192,223,224,255]
    # average = [16,47,79,111,143,175,207,240]
    temp = graylevel
    temp = temp//8
    temp = (temp*32) + 16
    print()

img1 = cv2.imread("lena512color.tiff", 0)


for i,j in enumerate(img1):
    print(i,j)
    #print("Type ", type(img1[i]))


#plotting
fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)
ax1.imshow(img1, cmap="gray", interpolation=None)
#ax2 = fig.add_subplot(1,2,2)
#ax2.imshow(img2, cmap="gray", interpolation=None)

#Remove Axis
ax1.axis("off")
#ax2.axis("off")
plt.show()