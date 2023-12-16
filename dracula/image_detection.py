import sys
import cv2
import numpy as np

# Read image path
path = sys.argv[1]
img = cv2.imread(path)

# define mask for period color in BGR
lower_red = np.array([0,0,80])
upper_red = np.array([100,100,255])
period_mask = cv2.inRange(img, lower_red, upper_red)
period_contours, _ = cv2.findContours(period_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# detect towel contours
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 220, 200, cv2.THRESH_BINARY)
towel_contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# cv2.drawContours(img, towel_contours, contourIdx=-1, color=(0, 255, 0), thickness=15, lineType=cv2.LINE_AA)

# Compute area_period period
area_period = 0
for cnt in period_contours:
    # Get the area_period of each contour 
    area_period += cv2.contourArea(cnt)

#Compute area_compress 
area_compress = 0
for cnt in towel_contours:
    area_compress += cv2.contourArea(cnt)

area_compress += area_period

print("Area period: ", area_period)
print("Area compress: ", area_compress)
print("Ratio: ", area_period/area_compress*100)

# # Draw period contours on the original image
cv2.drawContours(img, towel_contours, -1, (0, 255, 0), 2)
cv2.imshow('image', img)
kc = cv2.waitKeyEx(0)
while kc != 27:
    kc = cv2.waitKeyEx(0) 
