import time
import os
#from adafruit_servokit import ServoKit

 
# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
'''
kit = ServoKit(channels=16)

def Servocheck(servolist):
    for Servo in servolist:
        print("Moving servo {} to position {}".format(Servo.pin, midpoint))
        kit.servo[Servo.pin].angle = midpoint
        time.sleep(speed)
        
        if(Servo.inverted == 1):
            target = 180-up
            print("inverted, new target: {}".format(target))
        else:
            target = up
        
        print("Moving servo {} to up position: {}".format(Servo.pin, target))
        kit.servo[Servo.pin].angle = target
        time.sleep(speed)

        print("Moving servo {} to position {}".format(Servo.pin, midpoint))
        kit.servo[Servo.pin].angle = midpoint
        time.sleep(speed)
        
    return
        
 
 
 '''
 
        
        
        
       
def targetadjustment(position, target, inverted):
    #print("Servo position: {}, Servo target: {}, Servo inverted: {}".format(position, target, inverted))
    #invert target if required

    if (inverted == 1):
        target = 180-target
        #print("inverted, new target - {}".format(target))

    #step between position and target
    if (target < position):
        target = -target
        #print("Target smaller, new target - {}".format(target))

    #print("Servo position: {}, Servo target: {}, Servo inverted: {}".format(position, target, inverted))

    return target
       
       
       
      
       
def moveservos(servolist):

    maxoffset = 0
    
    for Servo in servolist:
        
        if Servo.position != Servo.target:

            print("\nAdjusting target for servo {}".format(Servo.pin))
            Servo.target = targetadjustment(Servo.position, Servo.target, Servo.inverted)
            if Servo.target < 0:
                Servo.position = -Servo.position
                
            if (abs(Servo.position - Servo.target)>maxoffset):
                maxoffset = abs(Servo.position - Servo.target)
                
            print("Target after adjustment {}".format(Servo.target))


    print("\nMaxoffset {}\n".format(maxoffset))     
    for i in range (0, maxoffset):
        #print("\nMovement - {}".format(i))
        for Servo in servolist:
            
            if abs(Servo.position != Servo.target):

                #print("Moving servo {} from position {} to position {}".format(Servo.pin, abs(Servo.position), Servo.target))
                #kit.servo[Servo.pin].angle = abs(Servo.position)
                time.sleep(speed)
                Servo.position = Servo.position + 1

                
    return



def stepcycle(servolist):

  for Servo in servolist:
    if Servo.sidex == 'left' and Servo.sidey == 'front':

      if Servo.part != 'hip':
        Servo.target = up
        print("Moving {} {} {} from {} to {}".format(Servo.sidey, Servo.sidex, Servo.part, Servo.position, Servo.target))
      
  moveservos(servolist)
  for Servo in servolist:
      Servo.position = Servo.target
      print("Servo {} now in position {}".format(Servo.pin, abs(Servo.position)))


  for Servo in servolist:
    if Servo.sidex == 'left' and Servo.sidey == 'front' and Servo.part == 'hip':
      Servo.target = up
      print("\nMoving {} {} {} from {} to {}".format(Servo.sidey, Servo.sidex, Servo.part, Servo.position, Servo.target))

  moveservos(servolist)




  
  


  return


   
    







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


speed = 0.001





if __name__ == '__main__':

    '''
    for i in range (0, 12): 

        kit.servo[i].angle = 90
    '''

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

    stepcycle(servolist)


    print("\n\n\nRun end\n\n\n")

        
    exit()

