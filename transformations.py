import cv2 as cv
import numpy as np

img = cv.imread('Photos/Akshat Gupta.png')
cv.imshow('Akshat Gupta', img)

#Translation

def translate(img, x, y):
    transMAT = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[0], img.shape[1])
    return cv.warpAffine(img, transMAT, dimensions)

translated_img = translate(img, -100, -100)

cv.imshow('Translated Image', translated_img)

#Rotation

def rotate(img, angle, rotPoint= None):
    height, width = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

        rotMAT = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
        dimensions = (width, height)

        return cv.warpAffine(img, rotMAT, dimensions)
    
rotated_img = rotate(img, 45)

cv.imshow('Rotated Image', rotated_img)

rotated_rotated_img = rotate(rotated_img, -45)

cv.imshow('Rotated and Translated Image', rotated_rotated_img)

#Resizing
Resized = cv.resize(img, (500,500), interpolation= cv.INTER_LINEAR)

cv.imshow('Resized Image', Resized)  

#Flipping

flip = cv.flip(img,0)

cv.imshow('Flipped Image Horizontally', flip)

#Cropping

cropped = img[200:400, 300:500]

cv.imshow('Cropped Image', cropped)

#Drawing Shapes

cv.waitKey(0)
