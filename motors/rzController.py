# import gpiozero as GPIO
import time
from DRV8825 import DRV8825
from zMotor import zMotor
from rMotor import rMotor

class rzController:



    def __init__(self, rController, zController):
		
        self.rController = rController
        self.zController = zController


    def calibrate(self, rDegrees, zDegrees):
        self.rController.setRotation(rDegrees);
        self.manualSetR(0)
        

    def setR(self,degrees):
        self.rController.setRotation(degrees);
    

    def setZ():
        pass

    def manualSetR(self, degrees):
        self.rController.setStoredRotation(degrees)
        
        
    def manualSetZ():
        pass

    def setRZ(self, rDegrees, zDegrees):

        self.setR(rDegrees)
        self.setZ(zDegrees)



def rzLoop(rMotorCur, zMotorCur):
    pass

def main():
    Motor1 = DRV8825(dir_pin=13, step_pin=19, enable_pin=12, mode_pins=(16, 17, 20))
    Motor2 = DRV8825(dir_pin=24, step_pin=18, enable_pin=4, mode_pins=(21, 22, 27))

    rMotorCur = rMotor(Motor1)
    zMotorCur = zMotor(Motor2)

    # Main loop
    rzLoop(rMotorCur, zMotorCur)





main()