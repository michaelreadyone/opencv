""" 
basic image process
the order in cv numpy is not RGB, is BGR

"""
## Create a img from numpy array
import cv2
import numpy as np
import random
# img = cv2.imread('colorcolor.jpg')
# print(img)
# print(type(img))

img = np.empty((300, 300, 3), np.uint8)

for row in range(300):
    for col in range(300):
        # img[row][col] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        img[row][col] = [0, 0, 255]

cv2.imshow('img', img)
cv2.waitKey(0)

## TODO change top 30% pixel dog image to random pixels

## TODO slice left top 150 X 200 picture from origin picture, any portion picture at different position.
