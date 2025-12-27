import cv2 as cv
# import numpy as np
# import matplotlib.pyplot as plt

img = cv.imread('Photos/Akshat Gupta.png')
cv.imshow('Akshat Gupta', img)

# blank = np.zeros(img.shape[:2], dtype='uint8')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

#Simple Thresholding

threshold, thresh  = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Thresholding', thresh)

#Adaptive Thresholding

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 5)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)