import RPi.GPIO as IO
from time import sleep

IO.setwarnings(False)
IO.setmode(IO.BCM)

class Motor():
    
    # Defines a Constructor to Input GPIO Pin Numbers and Starting PWM Cycle
    def __init__(self, enA, in1A, in2A, enB, in1B, in2B):
        self.enA = enA
        self.in1A = in1A
        self.in2A = in2A
        self.enB = enB
        self.in1B = in1B
        self.in2B = in2B
        
        # Setup GPIO Pins as Output
        IO.setup(self.enA, IO.OUT)
        IO.setup(self.in1A, IO.OUT)
        IO.setup(self.in2A, IO.OUT)
        IO.setup(self.enB, IO.OUT)
        IO.setup(self.in1B, IO.OUT)
        IO.setup(self.in2B, IO.OUT)
        
        self.pwmA = IO.PWM(self.enA, 100)
        self.pwmB = IO.PWM(self.enB, 100)
        self.pwmA.start(0)
        self.pwmB.start(0)
        self.mySpeed = 0
    
    # Function to Move
    def move(self, speed = 0.5, turn = 0, t = 0):
        speed *= 100
        turn *= 70
        leftSpeed = speed - turn
        rightSpeed = speed + turn
        
        if leftSpeed > 100:
            leftSpeed = 100
        elif leftSpeed < -100:
            leftSpeed = -100
            
        if rightSpeed > 100:
            rightSpeed = 100
        elif rightSpeed < -100:
            rightSpeed = -100
            
        self.pwmA.ChangeDutyCycle(abs(leftSpeed))
        self.pwmB.ChangeDutyCycle(abs(rightSpeed))
        
        # Move Forward, have to check if ina1 and a2 are connected
        # to left or right wheels
        if leftSpeed > 0:
            IO.output(self.in1A, IO.HIGH)
            IO.output(self.in2A, IO.LOW)
        # Move Backward
        else:
            IO.output(self.in1A, IO.LOW)
            IO.output(self.in2A, IO.HIGH)
            
        if rightSpeed > 0:
            IO.output(self.in1B, IO.HIGH)
            IO.output(self.in2B, IO.LOW)
        else:
            IO.output(self.in1B, IO.LOW)
            IO.output(self.in2B, IO.HIGH)
            
        sleep(t)
        
    def stop(self, t=0):
        self.pwmA.ChangeDutyCycle(0)
        self.pwmB.ChangeDutyCycle(0)
        self.mySpeed = 0
        print("stopped")
        sleep(t)
        
# for testing
def main():
    motor1.move(0.5, 0.2)
    motor1.stop(2)
    motor1.move(-0.5, 0.2)
    motor1.stop(2)
    motor1.move(0, 0.5, 2)
    motor1.stop(2)
    motor1.move(0, -0.5, 2)
    motor1.stop(2)
    
# GPIO PINS and allows script to be executed directly from this module for testing
if __name__ == '__main__':
    motor1 = Motor(4, 17, 27, 1, 1, 1)
    motor2 = Motor(16, 20, 21, 1, 1, 1)
    main()
