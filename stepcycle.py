import moveservos
import targetadjustment


def stepcycle(servolist, legs, up, down, midpoint, speed):
    print("\nWalk cycle beginning\n")
    phase = 0
    e = 0
    i = 0
    while i < 4:
        while e < 4:
            while phase < 4:
                print("Phase {}".format(phase))
                movelist = [0, 0]

                if (phase == 0):
                    movelist = [legs[e][0], legs[e][1]]
                    target = up
            
                elif (phase == 1):
                    movelist = [legs[e][2]]
                    target = up
            
                elif (phase == 2):
                    movelist = [legs[e][0], legs[e][1]]
                    target = down
            
                elif (phase == 3):
                    movelist = [legs[e][2]]
                    target = down
            

                for Servo in servolist:
                    if (Servo.pin in movelist):
                        Servo.target = target
                        print("Moving servo {} from {} to {}".format(Servo.pin, Servo.position, Servo.target))

                servolist = moveservos.moveservos(servolist, speed)
                phase +=1
            print("\n\n\nE={}".format(e))
            phase = 0
            e+=1
        i+=1
        e=0
    return

