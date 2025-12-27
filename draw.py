import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)
# img = cv.imread('Photos/Akshat Gupta.png')
# cv.imshow('Akshat Gupta', img)

# #Paint the image
# # blank[200:300,300:400] = (255,0,0)
# # cv.imshow('Blue', blank)

# #Draw a rectangle
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
# cv.imshow('Rectangle', blank)

# #Draw a circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 60, (0,255,255), thickness=-1)
# cv.imshow('Circle', blank)

# #Draw a line
# cv.line(blank, (100,250),(300,400),(255,255,0), thickness=3)
# cv.imshow('Circle', blank)

#Write text
cv.putText(blank, 'Hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,0,255), 3)
cv.imshow('Text', blank)
cv.waitKey(0)