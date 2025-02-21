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


  