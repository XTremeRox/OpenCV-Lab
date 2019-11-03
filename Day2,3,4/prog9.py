#!/usr/bin/python3
#Question number 9 (Histogram Equalisation and Matching)
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("lena512color.tiff",0)
img2 = cv2.equalizeHist(img)
#hist = cv2.calcHist([img],[0],None,[256],[0,256])

#histogram
plt.hist(img.ravel(),256,[0,256])
plt.show()
#equalisedHist image
plt.imshow(img2, cmap="gray", interpolation="bicubic")
plt.axis("off")

cv2.imshow("Image1", img)
cv2.imshow("Equalized Histogram", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()