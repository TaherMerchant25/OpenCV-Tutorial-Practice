import cv2 as cv
import numpy as np

img = cv.imread('Photos/Akshat Gupta.png')
cv.imshow('Akshat Gupta', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

merged = cv.merge([b,g,r])

cv.imshow('Merged', merged)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

cv.waitKey(0)