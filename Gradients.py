import cv2 as cv
import numpy as np


img = cv.imread('Photos/Akshat Gupta.png')
cv.imshow('Akshat Gupta', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', img)

#Laplacian

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

#Sobel 

sobelX = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobelY = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined = cv.bitwise_or(sobelX, sobelY)

cv.imshow('SobelX', sobelX)
cv.imshow('SobelY', sobelY)
cv.imshow('Combined Sobel', combined)

Canny = cv.Canny( gray, 150, 175)
cv.imshow('Canny', Canny)

# sobelX = np.uint8(np.absolute(sobelX))
# sobelY = np.uint8(np.absolute(sobelY))

cv.waitKey(0)