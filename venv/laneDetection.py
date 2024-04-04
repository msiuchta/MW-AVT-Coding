import cv2
import numpy as np
import utils

def getLaneCurve(img):
    imgMask = utils.mask(img)
    cv2.imshow('thresh',imgMask)

    # In future, will return 
    return None
    


# Not currently working with test video, try again with camera footage.
# Update: works with labtop camera, will likely work with pi camera.
if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        img = cv2.resize(img,(240,360))
        getLaneCurve(img)

        cv2.imshow('Video',img)
        cv2.waitKey(1)

