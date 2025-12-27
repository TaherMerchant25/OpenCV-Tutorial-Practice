import cv2 as cv
import numpy as np

img = cv.imread('Photos/Akshat Gupta.png')
cv.imshow('Akshat Gupta', img)

#averaging

average = cv.blur(img, (3,3))
cv.imshow('Averaging', average)

#Gaussian Blur

gaussian = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gaussian)

#Median Blur

median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

#Bilateral Blur

bilateral = cv.bilateralFilter(img, 15, 35, 25)
cv.imshow('Bilateral Blur', bilateral)

cv.waitKey(0)