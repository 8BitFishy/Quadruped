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
        
 