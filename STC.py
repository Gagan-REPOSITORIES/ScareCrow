#!/usr/bin/env python3
import RPi.GPIO as GPIO
import RpiMotorLib

#Change the width and height as per the capturing dimensions
width = 640
height = 480
RequiredSteps = 400 # based on the steptype variable i.e 400

#define GPIO pins
GPIO_pins = (17, 27, 22) # Microstep Resolution MS1-MS3 -> GPIO Pin
direction= 6       # Direction -> GPIO Pin
step = 5      # Step -> GPIO Pin

GPIO_pins_2 = (18,23,24)
direction_2 = 12
step_2 = 25

# Initialize the pins
mymotortest = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")
mymotortest_2 = RpiMotorLib.A4988Nema(direction_2, step_2, GPIO_pins_2, "A4988")

steptype = steptype_2 = "1/8" #(Full, Half, 1/4, 1/8, 1/16)


def motorgoto(x = 1, y = 1):
    prevPosition = readPosition()
    xChange = x - int(prevPosition[0]) #previous stored x position
    yChange = y - int(prevPosition[1]) # previous stored y position
    clockwise = True if xChange > 0 else False # if the detect object is right from center frame then clockwise else anticlock wise
    clockwise_2 = True if yChange > 0 else False # if the detect object is right from center frame then clockwise else anticlock wise
    # formula to calculate number of steps required to move to object position
    motor1steps = int(round(((RequiredSteps/width) * abs(xChange)) , 0))
    motor2steps = int(round(((RequiredSteps/height) * abs(yChange)), 0))
    writePosition(x,y)
    #motor_go(clockwise, steptype, steps, stepdelay, verbose, initdelay)
    if motor1steps > 0:
        mymotortest.motor_go(clockwise, steptype , motor1steps , .01, False, .05)#connected to left side of GPIO extention
    if motor2steps > 0:
        mymotortest_2.motor_go(clockwise_2, steptype_2 , motor2steps , .01, False, .05)#connected to right side of GPIO extention
    print("Laser current position x = ",x," y = ", y)

def writePosition(xcor, ycor):
    with open("laserPosition.txt", 'w', encoding = 'utf-8') as f:
        f.write(str(xcor) + "\n")
        f.write(str(ycor) + "\n")

def readPosition():
    with open("laserPosition.txt", 'r', encoding = 'utf-8') as f:
        return f.readlines()


# good practise to cleanup GPIO at some point before exit
#GPIO.cleanup()

exit()