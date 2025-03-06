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

    def __init__(self,xMotorCur = 0, rMotorCur = 0, zMotorCur = 0):
		
        if rMotorCur == 0:
            
            rMotorCur = rMotor(DRV8825(dir_pin=13, step_pin=19, enable_pin=12, mode_pins=(16, 17, 20)))
            

        if zMotorCur == 0:
        
            zMotorCur = zMotor(DRV8825(dir_pin=24, step_pin=18, enable_pin=4, mode_pins=(21, 22, 27)))

        if xMotorCur == 0:
            # PUT REAL X
            xMotorCur = zMotorCur;

        XController.__init__(self, xMotorCur)  # Initialize Employee
        RZController.__init__(self, rMotorCur,zMotorCur) 

        self.status_X = 'AVAILABLE' 
        self.status_R = 'AVAILABLE' 
        self.status_Z = 'AVAILABLE'
     

  
    def moveEgg(startX, startR, startZ, endX, endR, endZ):
        pass       
    
    def setXRZWithThreading(self,targetX,targetR,targetZ):
        print(f"Started setting to (x = {targetX}, r = {targetR}, z = {targetZ})")

        XRZThread = threading.Thread(target=self.setXRZ, args=(targetX,targetR,targetZ,))
        XRZThread.start()
        print("Starting thread")    

    def getXRZ(self):
        return (self.getX(),self.getR(),self.getZ())
    
    def setXRZ(self,targetX,targetR,targetZ):

        self.setX(0)
        self.setR(targetR)
        self.setZ(targetZ)
        self.setX(targetX)
       
      
        print(f"Finished setting to (x = {self.getX()}, r = {self.getZ()}, z = {self.getZ()})")


    def setX(self, motor, targetX):
        self.status_X = 'UNAVAILABLE' 
        time.sleep(5)
        super().setX(motor, targetX)
        self.status_X = 'AVAILABLE' 

    def setR(self,targetR):
        self.status_R = 'UNAVAILABLE' 
        time.sleep(5)
        super().setR(targetR)
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
        print("  Z:  " + self.status_R + " - " + str(self.getR()))
        print("  R:  " + self.status_Z + " - " + str(self.getZ()))

        entire_str += "Motor Status:\n" + "\tX:\t" + self.status_X + "\n\tR:\t" + self.status_R + "\n\tZ:\t" + self.status_Z + "\n" 
        

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
            print("Enter an x (from 0 to 100): ",end='')
            x = float(input())
            print("Enter an r (from -180 to 180): ",end='')
            r = float(input())
            print("Enter an z (from 0 to 100): ",end='')
            z = float(input())
       
            controller.setXRZWithThreading(x,r, z)
               

      

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

