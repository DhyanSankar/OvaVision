# import gpiozero as GPIO
import time
import math
import threading
import sys
import os

# Add the root directory to sys.path
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(root_dir)

from DRV8825 import DRV8825

from DRV8825 import DRV8825
from zMotor import zMotor
from rMotor import rMotor
from xMotor import xMotor
from xController import XController
from rzController import RZController

# from DRV8825 import DRV8825
# from zMotor import zMotor
# from rMotor import rMotor


# from xController import XController;
# from rzController import RZController;



class XRZController(XController, RZController):

    motorRotations = {"GRAB":0, "CAM":180};

    def __init__(self,xMotorsCur = 0, rMotorCur = 0, zMotorCur = 0):
		
        if rMotorCur == 0:
            
            rMotorCur = rMotor(DRV8825(dir_pin=13, step_pin=19, enable_pin=12, mode_pins=(16, 17, 20)))
            

        if zMotorCur == 0:
        
            zMotorCur = zMotor(DRV8825(dir_pin=24, step_pin=18, enable_pin=4, mode_pins=(21, 22, 27)))

        if xMotorsCur == 0:
            # PUT REAL X
            xMotorsCur = []

            # Dummy motors
            xMotorsCur.append(xMotor(DRV8825(dir_pin=24, step_pin=18, enable_pin=4, mode_pins=(21, 22, 27)), "GRAB"))
            xMotorsCur.append(xMotor(DRV8825(dir_pin=24, step_pin=18, enable_pin=4, mode_pins=(21, 22, 27)), "CAM"))

        XController.__init__(self, xMotorsCur)  # Initialize Employee
        RZController.__init__(self, rMotorCur,zMotorCur) 

        self.status_X = 'AVAILABLE' 
        self.status_R = 'AVAILABLE' 
        self.status_Z = 'AVAILABLE'
     

  
    def moveEgg(startX, startR, startZ, endX, endR, endZ):
        pass       
    
    def setXRZWithThreading(self,targetX,targetR,targetZ,motor):
        print(f"Started setting to (x = {targetX}, r = {targetR}, z = {targetZ})")

        XRZThread = threading.Thread(target=self.setXRZ, args=(targetX,targetR,targetZ,motor))
        XRZThread.start()
        print("Starting thread")    

    def getXRZ(self):
        return (self.getX(),self.getR(),self.getZ())
    
    def setXRZ(self,targetX,targetR,targetZ, motor = "GRAB"):

        self.setX(targetX, motor)
        self.setR(targetR, motor)
        self.setZ(targetZ)
       
      
        print(f"Finished setting to (x = {self.getX()}, r = {self.getZ()}, z = {self.getZ()})")


    def setX(self, targetX, motor = "GRAB"):
        self.status_X = 'UNAVAILABLE' 
        time.sleep(5)
        super().setX(targetX, motor)
        self.status_X = 'AVAILABLE' 

    def setR(self,targetR, motor):
        self.status_R = 'UNAVAILABLE' 
        time.sleep(5)
        super().setR((targetR + self.motorRotations[motor])%360)
        self.status_R = 'AVAILABLE' 

    def setZ(self,targetZ):
        self.status_Z = 'UNAVAILABLE' 
        time.sleep(5)
        super().setZ(targetZ)
        self.status_Z = 'AVAILABLE' 
    
    def resetXRZ(self):
        self.resetX()
        self.resetRZ()
    

    def print_status(self):
        entire_str = ""

        print("Motor Status:")
        print("  X:  " + self.status_X + " - " + str(self.getX()))
        print("  R:  " + self.status_R + " - " + str(self.getR()))
        print("  Z:  " + self.status_Z + " - " + str(self.getZ()))

        entire_str += "Motor Status:\n" + "\tX:\t" + self.status_X + "\n\tR:\t" + self.status_R + "\n\tZ:\t" + self.status_Z + "\n" 
        return entire_str

def xrzLoop(xMotorCur, rMotorCur, zMotorCur):

    controller = XRZController()
 

    print("Hello! What would you like to do?")
    print("- SET")
    print("- STAT")
    print("- QUIT")
    print("Type one of the above codes: ",end='')

    action = input()

    while action != "QUIT":

        if action == "SET":
            print("Enter a motor name: ",end='')
            motorName = input()
            print("Enter an x (from 0 to 100): ",end='')
            x = float(input())
            print("Enter an r (from 0 to 360): ",end='')
            r = float(input())
            print("Enter an z (from 0 to 100): ",end='')
            z = float(input())
       
            controller.setXRZWithThreading(x,r, z,motorName)
               

      

        elif action == "STAT":
            print(f'Currently at x = {controller.getX()}r = {controller.getR()}, z = {controller.getZ()}')
            controller.print_status()

    
        
        else:
            print("INVALID ACTION")
            print("- SET")
            print("- STAT")
            print("- QUIT")

        print("Type one of the above codes: ",end='')

        action = input()
    
    print("resetting")
    controller.resetXRZ()
    print("reset complete!")
        



if __name__ == "__main__":
    
    # Probably will need definitions of motors stored somewhere
    Motor1 = DRV8825(dir_pin=13, step_pin=19, enable_pin=12, mode_pins=(16, 17, 20))
    Motor2 = DRV8825(dir_pin=24, step_pin=18, enable_pin=4, mode_pins=(21, 22, 27))

    rMotorCur = rMotor(Motor1)
    zMotorCur = zMotor(Motor2)

    # Main loop
 
    xMotorCur = zMotorCur
    xrzLoop(xMotorCur,rMotorCur,zMotorCur)
    # mainController = XRZController(xMotorCur, rMotorCur, zMotorCur)
    # mainController.setXRZWithThreading(10,11, 19)
    # mainController.print_status()

