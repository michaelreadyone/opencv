"""How to read image, video, camera
"""
import cv2

# '''Read image'''
# img = cv2.imread('colorcolor.jpg')
# # img = cv2.resize(img, (300, 300))  # absolute value
# img = cv2.resize(img, (0, 0), fx=0.2, fy=0.2)  # time

# cv2.imshow('img', img)
# cv2.waitKey(0)

'''Read video'''
# cap = cv2.VideoCapture('thumb.mp4')
cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    # frame = cv2.resize(frame, (0,0), fx=0.2, fy=0.2)
    if ret:
        cv2.imshow('video', frame)
    else:
        break

    cv2.waitKey(1)
