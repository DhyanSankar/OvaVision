# import gpiozero as GPIO
import time
import math
import threading;

from DRV8825 import DRV8825
from zMotor import zMotor
from rMotor import rMotor

from xController import XController;
from rzController import RZController;



class XRZController(XController, RZController):

    def __init__(self,xMotor, rMotor, zMotor):
		
        XController.__init__(self, xMotor)  # Initialize Employee
        RZController.__init__(self, rMotor,zMotor) 

    # Need to figure out threading

  
         
    
    def setXRZWithThreading(self,targetX,targetR,targetZ):
        print(f"Started setting to (x = {targetX}, r = {targetR}, z = {targetZ})")

        t1 = threading.Thread(target=self.setXRZ, args=(targetX,targetR,targetZ,))
        t1.start()
        print("Starting thread")    

    def getXRZ(self):
        return (self.getX(),self.getR(),self.getZ())
    
    def setXRZ(self,targetX,targetR,targetZ):
        self.setX(targetX)
        self.setR(targetR)
        self.setZ(targetZ)
        print(f"Finished setting to (x = {self.getX()}, r = {self.getZ()}, z = {self.getZ()})")




    def print_status(self):
        entire_str = ""

        status_X = 'UNAVAILABLE' # theoretically this should print whether motor is in use and current position of the motor.
        status_Z = 'UNAVAILABLE'
        status_R = 'UNAVAILABLE'
        estimate = 'UNAVAILABLE'

        print("Motor Status:")
        print("  X:  " + status_X + " - " + str(self.getX()))
        print("  Z:  " + status_Z + " - " + str(self.getR()))
        print("  R:  " + status_R + " - " + str(self.getZ()))

        entire_str += "Motor Status:\n" + "\tX:\t" + status_X + "\n\tZ:\t" + status_Z + "\n\tR:\t" + status_R + "\n" 


if __name__ == "__main__":
 
    Motor1 = DRV8825(dir_pin=13, step_pin=19, enable_pin=12, mode_pins=(16, 17, 20))
    Motor2 = DRV8825(dir_pin=24, step_pin=18, enable_pin=4, mode_pins=(21, 22, 27))

    rMotorCur = rMotor(Motor1)
    zMotorCur = zMotor(Motor2)

    # Main loop
 
    xMotorCur = zMotorCur

    mainController = XRZController(xMotorCur, rMotorCur, zMotorCur)
    mainController.setXRZWithThreading(10,11, 19)
    mainController.print_status()