import cv2
import numpy as np
import utils

curveList = []
frameCounter = 0
avgVal = 10
# Precision of curve estimate, +avgVal -> + precision, -efficiency
# display - 0 displays nothing, 1 displays result, 2 displays all steps
def getLaneCurve(img, display = 2):
    ## Creates the black and white filter
    imgMask = utils.mask(img)

    ## Creates the cropped window
    h, w, c = img.shape
    points = utils.valTrackbars()
    imgWarp = utils.warp(imgMask,points,w,h)
    # Creates sliders to calibrate cropped window 
    imgCopy = img.copy()
    imgWarpPoints = utils.drawPoints(imgCopy, points)

    ## Calculates and shows the average value of the white
    adjustedCenter, imgHist = utils.graphPoints(imgWarp, cutoff=0.5, display=True, reigon = 4)
    center, imgHist = utils.graphPoints(imgWarp, cutoff=0.5, display=True)
    curveRaw = center-adjustedCenter

    ## Approximate curve
    curveList.append(curveRaw)
    if len(curveList) >= avgVal:
        curveList.pop(0)
    curve = (int(sum(curveList)/len(curveList)))
    print(curve)

    ## TODO: Make it look pretty
    #print(img)
    #print("moo")
    #print(imgWarp)
    #cv2.imshow('Image | Warp Points | Graphed Points', np.hstack([img,imgWarpPoints,imgHist]))
    #cv2.imshow('Masked Image | Warped Image', np.hstack([imgMask,imgWarp]))
    #cv2.imshow('Masked Image', np.vstack((np.hstack([img,imgWarpPoints]), np.hstack([imgMask,imgWarp]))))
    
    cv2.imshow('Graphed Points', imgHist)
    cv2.imshow('Warped Image',imgWarp)
    cv2.imshow('Warped Points', imgWarpPoints)
    cv2.imshow('Masked Image', imgMask)
    cv2.imshow('Video',img)

    if abs(curve) > 1:
        round(curve)
    return None
    


# Not currently working with test video, try again with camera footage.
# Update: works with labtop camera, will likely work with pi camera.
if __name__ == '__main__':
    cap = cv2.VideoCapture(0)

    # Values of the array can be changed
    utils.initializeTrackbars([100 ,80 ,20 ,210])
    frames = 0
    while True:
        # loops a pre-recorded video
        frames += 1
        if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frames:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            frames = 0

        success, img = cap.read()
        img = cv2.resize(img,(480,240))
        getLaneCurve(img)

        k = cv2.waitKey(1)
        if k==ord('q'):
            print("break")
            break

