#!/usr/bin/python3
import cv2
import numpy as np
img_in = cv2.imread("dots.jpeg", 0)
 
# Threshold f(x,y)>=200 = 0 | f(x,y)<200 = 255 
th, img_th = cv2.threshold(img_in, 220, 255, cv2.THRESH_BINARY_INV)
img_floodfill = img_th.copy()
 
# Zero padded mask
h, w = img_th.shape
mask = np.zeros((h+2, w+2), np.uint8)
 
# Start from (0, 0) -> Floodfill
cv2.floodFill(img_floodfill, mask, (0,0), 255)
 
# Invert floodfilled image
img_floodfill_inv = cv2.bitwise_not(img_floodfill)
 
# Combine the two images to get the foreground.
img_out = img_th | img_floodfill_inv
 
# Display images.
cv2.imshow("Original Image", img_in)
cv2.imshow("Thresholded Image", img_th)
cv2.imshow("Floodfilled Image", img_floodfill)
cv2.imshow("Inverted Floodfilled Image", img_floodfill_inv)
cv2.imshow("Foreground", img_out)
cv2.waitKey(0)
