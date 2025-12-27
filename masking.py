import cv2 as cv
import numpy as np

img = cv.imread('Photos/Akshat Gupta.png')
cv.imshow('Akshat Gupta', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('blank_img', blank)

mask = cv.circle(blank, (img.shape[1]//2 +45, img.shape[0]//2+ 25), 100, 255, -1)
cv.imshow('mask_img', mask)

masked_img = cv.bitwise_and(img, img, mask=mask)

cv.imshow('masked_img', masked_img)

cv.waitKey(0)