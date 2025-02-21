# import gpiozero as GPIO
import time
import math
from DRV8825 import DRV8825
from zMotor import zMotor
from rMotor import rMotor

from xController import xController;
from rzController import rzController;


class xrzController(xController, rzController):

    def __init__(self,xMotor, rMotor, zMotor):
		
        xController.__init__(self, xMotor)  # Initialize Employee
        rzController.__init__(self, rMotor,zMotor)    


    def print_status(self):
        entire_str = ""

        status_X = 'UNAVAILABLE' # theoretically this should print whether motor is in use and current position of the motor.
        status_Z = 'UNAVAILABLE'
        status_R = 'UNAVAILABLE'
        estimate = 'UNAVAILABLE'

        print("Motor Status:")
        print("  X:  " + status_X)
        print("  Z:  " + status_Z)
        print("  R:  " + status_R)

        entire_str += "Motor Status:\n" + "\tX:\t" + status_X + "\n\tZ:\t" + status_Z + "\n\tR:\t" + status_R + "\n" 