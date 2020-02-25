import time
import os
import targetadjustment
import stepcycle
import moveservos

#from adafruit_servokit import ServoKit

 
# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.


#kit = ServoKit(channels=16)



class Servos:
    
    def __init__(self):      
        self.pin = pin
        self.inverted = inverted
        self.part = part
        self.sidex = sidex
        self.sidey = sidey
        self.position = position
        self.target = target
      
      
      
      
      
midpoint = 90
up = 170
down = 10

servolist = []

legs = [[0, 4, 8],[1, 5, 9],[2, 6, 10],[3, 7, 11]]

speed = 0.001





if __name__ == '__main__':


    os.system('cls' if os.name == 'nt' else 'clear')


    for i in range (0, 12): 
        #assign body parts
        if(i <= 3):
            part = 'foot'
            
        elif(i>=4 and i<=7):
            part = 'leg'
            
        else:
            part = 'hip'
        
        #assign pin
        pin = i
        
        #assign sidex
        if(i==0 or i==1 or i==4 or i==5 or i==8 or i==9):
            sidex = 'left'
 
        else:
            sidex = 'right'
            
        #assign sidey
        if(i==0 or i==3 or i==4 or i==7 or i==8 or i==11):
            sidey = 'front'
        else:
            sidey = 'back'
        
        #assign inversion rule
        if (i<=3):
            inverted = 0
        elif (i==10 or i == 11):
            inverted = 0
        else:
            inverted = 1
           
        #Set position to 90 and register
        #kit.servo[i].angle = 90
        position = target = 90
        
        Servo = Servos()
        servolist.append(Servo)

        #print("Servo stats:\nServo {} in position {}{}{} with inversion {}".format(pin, sidey, sidex, part, inverted))





       
    print("\n\nBeginning Run\n\n")




    '''
    for Servo in servolist:
        if (Servo.pin == 0):
            Servo.target = 160
            print("Foot servo {} initial target {}".format(Servo.pin, Servo.target))
        
        elif (Servo.pin == 1):
            Servo.target = 40
            print("Foot servo {} initial target {}".format(Servo.pin, Servo.target))

        elif (Servo.pin == 3):
            Servo.target = 160
            print("Leg servo {} initial target {}".format(Servo.pin, Servo.target))
        
        elif (Servo.pin == 4):
            Servo.target = 40
            print("Leg servo {} initial target {}".format(Servo.pin, Servo.target))
        
        else:
            Servo.target = 90
    '''
    '''
    for Servo in servolist:
        if (Servo.pin == 1 or Servo.pin == 4):
            Servo.target = 70
            
        elif (Servo.pin == 0 or Servo.pin == 5):
            Servo.target = 100
            
        else:
            Servo.target = 90
       
    moveservos(servolist)
    for Servo in servolist:
      Servo.position = abs(Servo.target)
      print("Servo {} now at position {}".format(Servo.pin, Servo.position))
        
    '''

    stepcycle.stepcycle(servolist, legs, up, down, midpoint, speed)



    for Servo in servolist:
      print("Servo {} at position {}".format(Servo.pin, Servo.position))
    

    print("\n\n\nRun end\n\n\n")

        
    exit()

