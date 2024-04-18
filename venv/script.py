from motorModule import Motor
from laneDetection import getLaneCurve
import cv2

motorR = Motor(16, 20, 21, 11, 10, 9)
motorL = Motor(4, 17, 27, 12, 1, 7)

def getImg(display=False, size=[480,240]):
	_,img = cap.read(0)
	img = cv2.resize(img, (size[0],size[1]))
	if display:
		cv2.imshow('Camera', img)
	return img
	
def main():
	img = getImg()
	# Returns a curve [1,-1]
	curve = getLaneCurve(img, 1)
	
	sens = 1.3
	maxSpeed = 0 
	if curve > maxSpeed:
		curve = maxSpeed
	elif curve < -maxSpeed:
		curve = -maxSpeed

	if curve > 0:
		sen=1.7
		# 0.05 deadzone
		if curve < 0.05: 
			curve = 0
	else:
		if curve > -0.08:
			curve = 0
	# 0.2 is base speed
	motor.move(0.20, curve*sen, 0.05)
	cv2.waitKey(1)


if __name__ == '__main__' :
	while True:
		getImg(True)
		main()