#!/usr/bin/python3
# Program to demonstrate basics of filtering and HPF with histograms
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena512color.tiff',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
#Applying High Pass Filter mask in center of FFT 
rows, cols = img.shape
crow,ccol = int(rows/2) , int(cols/2)
for i in range(crow-30, crow +30):
	for j in range(ccol - 30, ccol +30):
		fshift[i][j] = 0 + 0j

#Invertuing FFT
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

#Display Output
plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.hist(img_back.ravel(),256,[0,256])
plt.title('Histogram'), plt.xticks([]), plt.yticks([])
plt.show()