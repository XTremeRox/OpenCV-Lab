#!/usr/bin/python3
import cv2
import numpy as np
img = cv2.imread('lungs.jpeg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img1=img.copy()
edges = cv2.Canny(gray,100,200,apertureSize = 3)
minLineLength = 70
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,15,minLineLength,maxLineGap)
for x in range(0, len(lines)):
    for x1,y1,x2,y2 in lines[x]:
        cv2.line(img1,(x1,y1),(x2,y2),(0,255,0),2)
cv2.imshow('Edges',edges)
cv2.imshow('Input',img)
cv2.imshow('Output',img1)
cv2.waitKey(0)