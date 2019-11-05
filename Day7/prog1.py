#!/usr/bin/python3
import cv2
import matplotlib.pyplot as plt
import numpy as np
import random
def sp_noise(image,prob):
    output=np.zeros(image.shape,np.uint8)
    thres=1-prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn=random.random()
            if rdn <prob:
                output[i][j]=0
            elif rdn>thres:
                output[i][j]=255
            else:
                output[i][j]=image[i][j]
return output
def rayleigh_noise(image):
    meanvalue=100
    modevalue=np.sqrt(2/np.pi)*meanvalue
    s=np.random.rayleigh(modevalue,(256,256))
    noisy=image+s
    return noisy
def exponential_noise(image):
    row,col=image.shape
    exp=np.random.exponential(10.00,(row,col))
    #gauss=gauss.reshape(row,col)
    noisy=image+exp
    return noisy
def uniform_noise(image):
    row,col=image.shape
    uniform=np.random.uniform(-10,10,(row,col))#gauss=gauss.reshape(row,col)
    noisy=image+uniform
    return noisy
def gamma_noise(image):
    row,col=image.shape
    gamma=np.random.gamma(10.00,10.00,(row,col))
    #gauss=gauss.reshape(row,col)
    noisy=image+gamma
    return noisy
def gaussian_noise(image):
    row,col=image.shape
    mean=0
    var=250
    sigma=var**0.5
    gauss=np.random.normal(mean,sigma,(row,col))
    gauss=gauss.reshape(row,col)
    noisy=image+gauss
    return noisy
img=cv2.imread("F:\\Image Processing\\misc\\4.1.04.tiff",0)
noise_img=gaussian_noise(img)
plt.subplot(121)
plt.imshow(img,cmap='gray')
plt.xticks([]),plt.yticks([])
plt.title('Original')
plt.subplot(122)
plt.imshow(noise_img,cmap='gray')
plt.xticks([]),plt.yticks([])
plt.title('noisy image')
plt.show()
plt.hist(noise_img[100:200,100:200].ravel(),255,[0,255])
plt.show()
cv2.waitKey(0)