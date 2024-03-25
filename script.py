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

pwm.start(0)
#right
en_a = 4
in1 = 17
in2 = 27

IO.setwarnings(False)
IO.setmode(IO.BCM)

IO.setup(en_a,IO.OUT)
IO.setup(in1,IO.OUT)
IO.setup(in2,IO.OUT)

print("w/s: acceleration")
print("a/d: steering")
print("UP/DOWN: tilt")
print("esc: exit")

#hostname="google.com"
#response=os.system("ping -c 1 " + hostname)
p=IO.PWM(4,100)
#q=IO.PWM(27,100)
w=pygame.key.get_pressed()[pygame.K_w]
lPower = 0
rPower = 0
p.start(lPower)
#q.start(rPower)
stop = False
count=0

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)

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
		GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)

				#GPIO.output(in4,GPIO.LOW)
        		#GPIO.output(in3,GPIO.LOW)	
        break
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
				lPower = 60
				rPower = 60
                GPIO.output(in1,GPIO.HIGH)
                GPIO.output(in2,GPIO.LOW)

				#GPIO.output(in4,GPIO.HIGH)
        		#GPIO.output(in3,GPIO.LOW)

				print("onward")
            elif event.key == K_s:
				lPower = 30
				rPower = 30
				GPIO.output(in1,GPIO.LOW)
        		GPIO.output(in2,GPIO.HIGH)

         		#GPIO.output(in4,GPIO.LOW)
         		#GPIO.output(in3,GPIO.HIGH)
				
				print("backward")
			elif event.key == K_a:
				lPower = 30
				rPower = 60
				GPIO.output(in1,GPIO.HIGH)
        		GPIO.output(in2,GPIO.LOW)

         		#GPIO.output(in4,GPIO.LOW)
         		#GPIO.output(in3,GPIO.LOW)
				print("left")
			elif event.key == K_d:
				lPower = 60
				rPower = 30
				GPIO.output(in1,GPIO.LOW)
        		GPIO.output(in2,GPIO.HIGH)

        		#GPIO.output(in4,GPIO.LOW)
        		#GPIO.output(in3,GPIO.LOW)
				print("right")
            elif event.key == K_ESCAPE:
				lPower=0
				rPower=0
                stop = True
				print("dead")
            p.ChangeDutyCycle(lPower)
			#q.ChangeDutyCycle(rPower)


    	elif event.type == pygame.KEYUP:
			p.ChangeDutyCycle(0)
			#q.ChangeDutyCycle(0)

		#	if((pygame.key.get_pressed()[pygame.K_w] != 0 and pygame.key.get_pressed()[pygame.K_a] != 0) or (pygame.key.get_pressed()[pygame.K_w] !=0 and pygame.key.get_pressed()[pygame.K_d] != 0)):
		#		GPIO.output(in1,GPIO.LOW)
         #       GPIO.output(in2,GPIO.LOW)
#
#				#GPIO.output(in4,GPIO.LOW)
 #       		#GPIO.output(in3,GPIO.LOW)		
#			elif((pygame.key.get_pressed()[pygame.K_s] != 0 and pygame.key.get_pressed()[pygame.K_a] != 0) or (pygame.key.get_pressed()[pygame.K_s] !=0 and pygame.key.get_pressed()[pygame.K_d] != 0)):
#				GPIO.output(in1,GPIO.LOW)
 #               GPIO.output(in2,GPIO.LOW)
#
#				#GPIO.output(in4,GPIO.LOW)
 #       		#GPIO.output(in3,GPIO.LOW)	
###              GPIO.output(in2,GPIO.LOW)
#
#				#GPIO.output(in4,GPIO.LOW)
 #       		#GPIO.output(in3,GPIO.LOW)	
#			elif(pygame.key.get_pressed()[pygame.K_s] != 0):
##               GPIO.output(in2,GPIO.LOW)
#
#				#GPIO.output(in4,GPIO.LOW)
 #       		#GPIO.output(in3,GPIO.LOW)	
#			elif(pygame.key.get_pressed()[pygame.K_a] != 0):
#				GPIO.output(in1,GPIO.LOW)
 #               GPIO.output(in2,GPIO.LOW)
#
#				#GPIO.output(in4,GPIO.LOW)
        		#GPIO.output(in3,GPIO.LOW)	
#			elif(pygame.key.get_pressed()[pygame.K_d] != 0):
#				GPIO.output(in1,GPIO.LOW)
 #               GPIO.output(in2,GPIO.LOW)

				#GPIO.output(in4,GPIO.LOW)
        		#GPIO.output(in3,GPIO.LOW)	
#			else:
#				GPIO.output(in1,GPIO.LOW)
 #               GPIO.output(in2,GPIO.LOW)

				#GPIO.output(in4,GPIO.LOW)
        		#GPIO.output(in3,GPIO.LOW)	
#			t.ChangeDutyCycle(throttle)
#			s.ChangeDutyCycle(steer)
		
            
        