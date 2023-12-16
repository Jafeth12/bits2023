import cv2
import numpy as np

# Load the image
img = cv2.imread('ex1.jpg')

# define range of red color in HSV
lower_red = np.array([0,0,0])
upper_red = np.array([100,100,255])
mask = cv2.inRange(img, lower_red, upper_red)

color_img = cv2.bitwise_and(img, img, mask=mask)
    
# detect area and Perimeter of red color object
cv2.threshold(mask, 50, 255, 0, mask)
contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
M = cv2.moments(cnt)
area = cv2.contourArea(cnt)
perimeter = cv2.arcLength(cnt,True)

print("Area: ", area)
print("Perimeter: ", perimeter)

cv2.imshow('Color Image: ', color_img)

kc = cv2.waitKeyEx(0)
while kc != 27:
    kc = cv2.waitKeyEx(0) 
