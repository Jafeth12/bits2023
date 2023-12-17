import cv2
import numpy as np


def write_contours(img, contours):
    cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
    cv2.imshow('image', img)
    kc = cv2.waitKeyEx(0)
    while kc != 27:
        kc = cv2.waitKeyEx(0) 

# Write area and contour detection functions here
def write_period(img, area_period, period_contours):
    print("Area of period: ", area_period)
    # Draw period contours on the original image
    write_contours(img, period_contours)

# Write area and contour detection functions here
def write_towel(img, area_towel, towel_contours):
    print("Area of period: ", area_towel)
    # Draw period contours on the original image
    write_contours(img, towel_contours)

# Get area of period
def get_area_period(img): 
    # define mask for period color in BGR
    lower_red = np.array([0,0,80])
    upper_red = np.array([100,100,255])
    period_mask = cv2.inRange(img, lower_red, upper_red)
    period_contours, _ = cv2.findContours(period_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # Compute area_period period
    area_period = 0
    for cnt in period_contours:
        # Get the area_period of each contour 
        area_period += cv2.contourArea(cnt)
    write_period(img, area_period, period_contours)
    return area_period

# Get area of towel
def get_total_area(img):
    # define mask for towel color in BGR
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 200, 200, cv2.THRESH_BINARY)
    towel_contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # Compute area_towel 
    area_towel = 0
    for cnt in towel_contours:
        area_towel += cv2.contourArea(cnt)
    area_period = get_area_period(img)
    write_towel(img, area_towel, towel_contours)
    return area_towel+area_period, area_period 

def compute_percentage(img):
    area_towel,area_period = get_total_area(img)
    percentage = area_period/area_towel
    return percentage*100

def get_score(path):
    img = cv2.imread(path)
    percentage = compute_percentage(img)
    score = 0
    if percentage >= 50:
        score = 20
    elif percentage >= 25:
        score = 5
    else:
        score = 1
    return score,percentage


