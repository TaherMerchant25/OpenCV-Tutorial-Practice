import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread('Photos/Akshat Gupta.png')
cv.imshow('Akshat Gupta', img)

gray = cv.cvtColor( img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#HSV

hsv = cv.cvtColor( img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#L*a*b

LED = cv.cvtColor( img, cv.COLOR_BGR2LAB)

cv.imshow('LAB', LED)


# RGB
RGB = cv.cvtColor( img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', RGB)

plt.imshow(RGB)
plt.show()

cv.waitKey(0)