import RPi.GPIO as IO
import time
from time import sleep
import os, sys
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((240, 240))
pygame.display.set_caption('Fred')
# (short for fredrick reed)

#right
rEn_a = 4
rIn1 = 17
rIn2 = 27
#left
lEn_a = 16
lIn1 = 20
lIn2 = 21

IO.setwarnings(False)
IO.setmode(IO.BCM)

# setup GPIO pins as output
IO.setup(rEn_a,IO.OUT)
IO.setup(rIn1,IO.OUT)
IO.setup(rIn2,IO.OUT)
IO.setup(lEn_a,IO.OUT)
IO.setup(lIn1,IO.OUT)
IO.setup(lIn2,IO.OUT)

print("w/s: acceleration")
print("a/d: steering")
print("esc: exit")

#hostname="google.com"
#response=os.system("ping -c 1 " + hostname)
p=IO.PWM(4,100)
#q=IO.PWM(27,100)
w=pygame.key.get_pressed()[pygame.K_w]
lPower = 0
rPower = 0
p.start(rPower)
#q.start(lPower)
stop = False
count=0

IO.output(rIn1,IO.LOW)
IO.output(rIn2,IO.LOW)
IO.output(lIn1,IO.LOW)
IO.output(lIn2,IO.LOW)

while (True):
	count+=1
    #if count == 50:
    ##if count == 50:
	#	response=os.system("ping -c 1 " + hostname)
	#	if response == 0:
	#		print 'is up'
	#	else:
	#		print 'I died'
	#		break

	#	count=0
	time.sleep(0.02)
	
	if stop == 1:
		IO.output(rIn1,IO.LOW)
		IO.output(rIn2,IO.LOW)
		IO.output(lIn1,IO.LOW)
		IO.output(lIn2,IO.LOW)
			
		break

	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == K_w:
				lPower = 60
				rPower = 60

				IO.output(rIn1,IO.LOW)
				IO.output(rIn2,IO.HIGH)
				
				IO.output(lIn1,IO.HIGH)
				IO.output(lIn2,IO.LOW)

				print("onward")

			elif event.key == K_s:
				lPower = 30
				rPower = 30

				IO.output(rIn1,IO.LOW)
				IO.output(rIn2,IO.HIGH)
				
				IO.output(lIn1,IO.LOW)
				IO.output(lIn2,IO.HIGH)
				
				print("backward")

			elif event.key == K_a:
				lPower = 30
				rPower = 60

				IO.output(rIn1,IO.LOW)
				IO.output(rIn2,IO.HIGH)
				
				IO.output(lIn1,IO.HIGH)
				IO.output(lIn2,IO.LOW)

				print("left")

			elif event.key == K_d:
				lPower = 60
				rPower = 30

				IO.output(rIn1,IO.LOW)
				IO.output(rIn2,IO.HIGH)
				
				IO.output(lIn1,IO.HIGH)
				IO.output(lIn2,IO.LOW)

				print("right")

			elif event.key == K_ESCAPE:
				lPower = 0
				rPower = 0
				stop = True

				print("dead")

			p.ChangeDutyCycle(rPower)
			q.ChangeDutyCycle(lPower)

		elif event.type == pygame.KEYUP:
			p.ChangeDutyCycle(0)
			q.ChangeDutyCycle(0)

