import cv2 as cv

img = cv.imread('Photos/Akshat Gupta.png')
cv.imshow('Akshat Gupta', img)

#Converting to Grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

#Blurring the image

blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#Canny Edge Detection(Edge Cascade)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

#Dilation of the image

dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow('Dilated', dilated)

#Erosion of the image

eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

#Resize the image

resized = cv.resize(img, (500,500))
cv.imshow('Resized', resized)

#Cropping the image

cropped = img[100:200, 200:300]
cv.imshow('Cropped', cropped)


cv.waitKey(0)