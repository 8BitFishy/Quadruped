import targetadjustment
import time


def moveservos(servolist, speed):

    maxoffset = 0
    
    for Servo in servolist:
        
        if Servo.position != Servo.target:
            #print("Moving servo {}".format(Servo.pin))
            #print("\nAdjusting target for servo {}".format(Servo.pin))
            Servo = targetadjustment.targetadjustment(Servo)
                
            if (abs(Servo.position - Servo.target)>maxoffset):
                maxoffset = abs(Servo.position - Servo.target)
                print("{} - {} = {}".format(Servo.position, Servo.target, maxoffset))
                
            #print("Target after adjustment {}".format(Servo.target))


    print("\nMaxoffset {}\n".format(maxoffset))     
    for i in range (0, maxoffset):
        #print("\nMovement - {}".format(i))
        for Servo in servolist:
            
            if abs(Servo.position != Servo.target):

                #print("Moving servo {} from position {} to position {}".format(Servo.pin, abs(Servo.position), Servo.target))
                #kit.servo[Servo.pin].angle = abs(Servo.position)
                time.sleep(speed)
                Servo.position = Servo.position + 1

    print("Moving complete\n")

    for Servo in servolist:
      if Servo.inverted == 0:
        Servo.position = abs(Servo.target)
      else:
        Servo.position= Servo.target
    return servolist

