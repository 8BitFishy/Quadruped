import targetadjustment
import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)
def moveservos(servolist, speed):

    maxoffset = 0
    
    for Servo in servolist:
        
        if Servo.position != Servo.target:
            #print("Moving servo {}".format(Servo.pin))
            print("\nAdjusting target for servo {}".format(Servo.pin))
            Servo = targetadjustment.targetadjustment(Servo)
                
            if (abs(Servo.position - Servo.target)>maxoffset):
                maxoffset = abs(Servo.position - Servo.target)
                
            print("Target after adjustment {}".format(Servo.target))


    print("\nMaxoffset {}\n".format(maxoffset))     
    for i in range (0, maxoffset):
        for Servo in servolist:
            
            if abs(Servo.target != Servo.position):

                print("Servo {} position {} target {}".format(Servo.pin, Servo.position, Servo.target))
                kit.servo[Servo.pin].angle = abs(Servo.position)
                time.sleep(speed)
                Servo.position = Servo.position + 1
                
            

    print("Moving complete\n")

    for Servo in servolist:
        print("Servo {} in position {} with target {}".format(Servo.pin, Servo.position, Servo.target))


    
    return servolist

