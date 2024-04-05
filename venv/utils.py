# Contains functions used to move the RC motors

import cv2
import numpy as np

def mask(img):
    imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #arrays need to be calibrataed
    lowerWhite = np.array([15,0,0])
    upperWhite = np.array([100,255,255])
    maskWhite = cv2.inRange(imgHsv, lowerWhite, upperWhite)
    return maskWhite

def warp(img, points, w, h):
    pts1 = np.float32(points)
    pts2 = np.float32([[0,0],[w,0],[0,h],[w,h]])
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