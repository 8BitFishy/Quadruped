import moveservos
import targetadjustment

def stepcycle(servolist, legs, up, down, midpoint, speed):
  print("\nWalk cycle beginning\n")
  phase = 0

  e = 0

  while phase < 4:
    print("Phase {}".format(phase))
    movelist = [0, 0]

    if (phase == 0):
      movelist = [legs[e][0], legs[e][1]]
      target = up
    
    elif (phase == 1):
      movelist = [legs[e][2]]
      target = up
    
    if (phase == 2):
      movelist = [legs[e][0], legs[e][1]]
      target = midpoint
    
    elif (phase == 3):
      movelist = [legs[e][2]]
      target = down
    

    for Servo in servolist:
      if (Servo.pin in movelist):
        Servo.target = target
        print("Moving servo {} from {} to {}".format(Servo.pin, Servo.position, Servo.target))

    servolist = moveservos.moveservos(servolist, speed)
    phase +=1

    '''

      for Servo in servolist:
        if Servo.sidex == 'left' and Servo.sidey == 'front':
          if Servo.part != 'hip':
            Servo.target = up
            print("Moving {} {} {} from {} to {}".format(Servo.sidey, Servo.sidex, Servo.part, Servo.position, Servo.target))
          

      servolist = moveservos(servolist)


      for Servo in servolist:
        if Servo.sidex == 'left' and Servo.sidey == 'front' and Servo.part == 'hip':
          Servo.target = up
          print("\nMoving {} {} {} from {} to {}".format(Servo.sidey, Servo.sidex, Servo.part, Servo.position, Servo.target))

      servolist = moveservos(servolist)

      for Servo in servolist:
          if Servo.sidex == 'left' and Servo.sidey == 'front':
            if Servo.part != 'hip':
              print("Moving {} {} {} from {} to {}".format(Servo.sidey, Servo.sidex, Servo.part, Servo.position, Servo.target))
              Servo.target = midpoint

      servolist = moveservos(servolist)

      for Servo in servolist:
    '''

  
  


  return

