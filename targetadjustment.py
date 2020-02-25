      
       
def targetadjustment(Servo):
    #print("Servo position: {}, Servo target: {}, Servo inverted: {}".format(position, target, inverted))
    #invert target if required

    if (Servo.inverted == 1):
        Servo.target = 180-Servo.target
        #print("inverted, new target - {}".format(target))

    #step between position and target
    if (Servo.target < Servo.position):
        Servo.target = -Servo.target
        Servo.position = -Servo.position
        #print("Target smaller, new target - {}".format(target))

    #print("Servo position: {}, Servo target: {}, Servo inverted: {}".format(position, target, inverted))

    return Servo
       
       
 