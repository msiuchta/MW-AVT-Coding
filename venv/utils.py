# Contains functions used to move the RC motors

import cv2
import numpy as np

# Masks the image to create a black/white filter
def mask(img):
    imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #arrays need to be calibrataed
    lowerWhite = np.array([15,0,0])
    upperWhite = np.array([100,255,255])
    maskWhite = cv2.inRange(imgHsv, lowerWhite, upperWhite)
    return maskWhite

# Distorts the image to the area enclosed by 'points'
def warp(img, points, w, h, invert = False):
    pts1 = np.float32(points)
    pts2 = np.float32([[0,0],[w,0],[0,h],[w,h]])
    if invert:
        matrix = cv2.getPerspectiveTransform(pts2, pts1)
    else:
        matrix = cv2.getPerspectiveTransform(pts1, pts2)

    imgWarp = cv2.warpPerspective(img,matrix,(w,h))
    return imgWarp

def nothing(a):
    pass

def initializeTrackbars(initializeTrackbarVals,w2=480,h2=240):
    cv2.namedWindow("Trackbars")
    cv2.resizeWindow("Trackbars", 360, 240)
    cv2.createTrackbar("Top Width", "Trackbars", initializeTrackbarVals[0], w2//2, nothing)
    cv2.createTrackbar("Top Height", "Trackbars", initializeTrackbarVals[1], h2, nothing)
    cv2.createTrackbar("Bottom Width", "Trackbars", initializeTrackbarVals[2], w2//2, nothing)
    cv2.createTrackbar("Bottom Height", "Trackbars", initializeTrackbarVals[3], h2, nothing)

def valTrackbars(w2=480, h2=240):
    wTop = cv2.getTrackbarPos("Top Width", "Trackbars")
    hTop = cv2.getTrackbarPos("Top Height", "Trackbars")
    wLow = cv2.getTrackbarPos("Bottom Width", "Trackbars")
    hLow = cv2.getTrackbarPos("Bottom Height", "Trackbars")
    points = np.float32([(wTop, hTop), (w2-wTop, hTop), 
                        (wLow, hLow), (w2-wLow, hLow)])

    return points

def drawPoints(img, points):
    for x in range(len(points)):
        cv2.circle(img, (int(points[x][0]), int(points[x][1])), 10, (0,0,255), cv2.FILLED)
    return img


# Cutoff (float) is the percentage of white pixels that need to be present in a column to identify it as part of the lane
# Display (boolean) reveals the center
# Reigon (float) proportion of screen used to calculate center. Starts at bottom
def graphPoints(img, cutoff=0.1, display=False, reigon=1):
    if reigon == 1:
        cords = np.sum(img, axis=0)
    else:
        cords = np.sum(img[img.shape[0]//reigon:,:], axis=0)
    # Upper bound for counting pixels as a curve 
    max = np.max(cords)

    indexArray = np.where(cords >= (max*cutoff))
    center = int(np.average(indexArray))
    #print(img)
    if display:
        imgHist = np.zeros((img.shape[0],img.shape[1],3), np.uint8)

        # x, itensity -> index, value
        for x,intensity in enumerate(cords):
            # Avg of whitespace
            cv2.line(imgHist, (x,img.shape[0]), (x,img.shape[0] - int(intensity//255//reigon)), (255,255,255), 1)
            # Midpoint of image
            cv2.line(imgHist, (img.shape[1]//2, img.shape[0]), (img.shape[1]//2, 9*img.shape[0]//10), (0,255,0), 2)
            # Center of whitespace
            cv2.line(imgHist, (center,img.shape[0]), (center,(5*img.shape[0])//6), (0,0,255), 3)
            if reigon != 1:
                cv2.line(imgHist, (0, img.shape[0]-img.shape[0]//reigon), (img.shape[1], img.shape[0]-img.shape[0]//reigon), (0,255,255),1)
        return center, imgHist
    #print(cords)
    #print(center)
    return(center)