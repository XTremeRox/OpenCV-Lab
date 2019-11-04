#! /usr/bin/python3
#Question number 1,2
import cv2 
import numpy as np
import matplotlib.pyplot as plt

inputimg = cv2.imread("man.jpeg",0)

#Structuring Element
#struct_element = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))

rows, cols = inputimg.shape
erosion = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))

#erosion
erimg=np.zeros((rows,cols),np.uint8)
for x in range(0, rows,3):
    for y in range(0,cols,3):
        if np.amin(inputimg[x:x+3, y:y+3]) != 0:
            erimg[x:x+3, y:y+3] = 255

#dilation
dilimg=np.zeros((rows,cols),np.uint8)
for x in range(0, rows):
    for y in range(0,cols):
        if np.amax(inputimg[x:x+3, y:y+3]) == 255:
            dilimg[x:x+3, y:y+3] = 255

#opening of eroded (erosion -> dilation)
tempimg = np.zeros((rows,cols),np.uint8)
opimg = np.zeros((rows,cols),np.uint8)
for x in range(0, rows):
    for y in range(0,cols):
        if np.amin(erimg[x:x+3, y:y+3]) != 0:
            tempimg[x:x+3, y:y+3] = 255
for x in range(0, rows):
    for y in range(0,cols):
        if np.amax(tempimg[x:x+3, y:y+3]) == 255:
            opimg[x:x+3, y:y+3] = 255

#Dilation of image obtained above
dil2img=np.zeros((rows,cols),np.uint8)
for x in range(0, rows):
    for y in range(0,cols):
        if np.amax(opimg[x:x+3, y:y+3]) == 255:
            dil2img[x:x+3, y:y+3] = 255

#Closing of image obtained in b (Dilation ->  Erosion)
tempimg = np.zeros((rows,cols),np.uint8)
climg = np.zeros((rows,cols),np.uint8)
for x in range(0, rows):
    for y in range(0,cols):
        if np.amax(erimg[x:x+3, y:y+3]) == 255:
            tempimg[x:x+3, y:y+3] = 255
for x in range(0, rows):
    for y in range(0,cols):
        if np.amin(tempimg[x:x+3, y:y+3]) != 0:
            climg[x:x+3, y:y+3] = 255

cv2.imshow('Input', inputimg)
# cv2.imshow('DilationImg', dilimg)
cv2.imshow('Erosion', erimg)
cv2.imshow('Opening of Eroded', opimg)
cv2.imshow('Dilation of b', dil2img)
cv2.imshow('Closing of b', climg)

#Every kernel which contains 1s and 0s is edge
cv2.imshow('Edge', dilimg-erimg)
# using inbuilt cv2 methods
# img = cv2.imread('man.jpeg', 0)

# kernel = np.ones((3,3), np.uint8)

# img_erosion = cv2.erode(img, kernel, iterations=1)
# img_dilation = cv2.dilate(img, kernel, iterations=1)

# cv2.imshow('Input', img)
# cv2.imshow('Erosion', img_erosion)
# cv2.imshow('Dilation', img_dilation)
# cv2.imshow('Edge' , img_dilation-img_erosion)
cv2.waitKey(0)
