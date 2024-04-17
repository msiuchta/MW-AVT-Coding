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

    ## Creates a cropped window
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
    print("curveList", (curveList))
    curve = (int(sum(curveList)/len(curveList)))
    curve = curve/100

     # Doesn't allow a curve greater than 1
    if abs(curve) > 1:
        print("round!")
        curve = round(curve)

    print(curve)
    #print(img)
    #print("moo")
    #print(imgWarp)
    if display != 0:
        #imgMask = cv2.cvtColor(imgMask, cv2.COLOR_GRAY2BGR)
        imgWarp = cv2.cvtColor(imgWarp, cv2.COLOR_GRAY2BGR)
        imgInvWarp = utils.warp(imgWarp, points, w, h, invert=True)
        #imgInvWarp = cv2.cvtColor(imgInvWarp, cv2.COLOR_GRAY2BGR
        imgInvWarp[0:h//3, 0:w] = 0,0,0
        
        imgFinal = np.zeros_like(imgInvWarp)
        imgFinal[:] = 0,255,0
        imgFinal = cv2.bitwise_and(imgInvWarp,imgFinal)
        imgFinal = cv2.addWeighted(img, 1, imgFinal, 1, 0)

        cv2.putText(imgFinal, "".join(["center: ",str(center-240)]), (20,20), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 1)
        cv2.putText(imgFinal, "".join(["curve: ",str(curve)]), (20,38), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 1)
        
        if display == 2:
            cv2.imshow('Display All', np.vstack((np.hstack([img,imgWarp,imgHist]), np.hstack([imgWarpPoints,imgInvWarp, imgFinal]))))
        elif display ==1:
            cv2.imshow('Display Final', imgFinal)

    return curve
    

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
        curve = getLaneCurve(img)

        k = cv2.waitKey(1)
        if k==ord('q'):
            print("break")
            break

