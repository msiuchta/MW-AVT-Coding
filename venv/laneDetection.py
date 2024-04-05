import cv2
import numpy as np
import utils

def getLaneCurve(img):
    imgMask = utils.mask(img)

    h, w, c = img.shape
    points = utils.valTrackbars()
    imgWarp = utils.warp(img,points,w,h)

    # Flawless and very efficient workaround
    imgCopy = img.copy()
    imgWarpPoints = utils.drawPoints(imgCopy, points)

    cv2.imshow('Masked Image',imgMask)
    cv2.imshow('Warped Image',imgWarp)
    cv2.imshow('Warped Points', imgWarpPoints)
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

        cv2.imshow('Video',img)

        k = cv2.waitKey(1)
        if k==ord('q'):
            print("break")
            break

