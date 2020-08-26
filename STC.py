#!/usr/bin/env python3
import RPi.GPIO as GPIO

from RpiMotorLib import RpiMotorLib
    
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

# motor driver
#motor_go(clockwise, steptype, steps, stepdelay, verbose, initdelay)
#(Full, Half, 1/4, 1/8, 1/16)
t = True
f = False

clockwise = t
steptype = "1/8"
steps = 200#30steps
mymotortest.motor_go(clockwise, steptype , steps , .01, False, .05)

clockwise_2 = t
steptype_2 = "1/8"
steps_2 = 200#23steps
mymotortest_2.motor_go(clockwise_2, steptype_2 , steps_2 , .01, False, .05)
    
# good practise to cleanup GPIO at some point before exit
#GPIO.cleanup()

exit()