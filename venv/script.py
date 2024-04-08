from motorModule import Motor
from laneDetection import getLaneCurve

def getImg(display=False, size=[480,240]):
	_,img = cap.read(0)
	img = cv2.resize(img, (size[0],size[1]))
	if display:
		cv2.imshow('Camera', img)
	return img
	

motorR = Motor(16, 20, 21, 11, 10, 9)
motorL = Motor(4, 17, 27, 12, 1, 7)

if __name__ == '__main__' :
	while True:
		getImg(True)
		main()