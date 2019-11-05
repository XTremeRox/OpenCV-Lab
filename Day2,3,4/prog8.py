#!/usr/bin/python3
#Question number 8
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("lowcontrast.png",0)
img2 = img.copy()

#alpha (1.0-3.0) Contrast Control
alpha = 2
beta = 0
# x*alpha + beta

#low contrast image enhancement
for i,graylevel in enumerate(img2):
   img2[i] =np.clip(alpha*img2[i] + beta,0,255)

#max gray value
print("Highest : ", np.amax(img2))

#min gray value
print("Lowest : ", np.amin(img2))

cv2.imshow("Image1", img)
cv2.imshow("Enhanced Image", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()