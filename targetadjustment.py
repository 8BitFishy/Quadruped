      
       
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
       
       
 