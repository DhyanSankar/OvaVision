# import gpiozero as GPIO
import time
import math
import sys
import os

# import DRV8825 as DRV8825
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(root_dir)

# from visualization.motors.DRV8825 import DRV8825
# from visualization.motors.zMotor import zMotor
# from visualization.motors.rMotor import rMotor


import DRV8825 as DRV8825
import zMotor as zMotor
import rMotor as rMotor
# from DRV8825 import DRV8825
# from zMotor import zMotor
# from rMotor import rMotor

class RZController:

    def __init__(self, rController, zController):
		
        self.rController = rController
        self.zController = zController


    def setR(self,degrees):
        self.rController.setRotation(degrees);
        print("r")

    def getR(self):
        return self.rController.rotation
    

    def setZ(self, percentOfHeight):
        self.zController.setBaseTo(percentOfHeight)
        print("z")
    
    def getZ(self):
        return self.zController.percentHeight
    
 
    def calibrateR(self, degrees = 0):

        self.rController.setStoredRotation(0)
        self.setR(degrees);
        self.rController.setStoredRotation(0)

    # Not sure how this should work actually, if we're using percents then calibration doesn't make much sense
    # Should always input negatives here?
    def calibrateZ(self, percentOfHeight):

        self.zController.setStoredHeightPercent(0)
        self.setZ(percentOfHeight);
        self.zController.setStoredHeightPercent(0)

    def resetRZ(self):
        self.rController.reset()
        self.zController.resetBase()
        print(f'Currently at r = {self.getR()}, z = {self.getZ()}')
        

    def setRZ(self, rDegrees, zPercentOfHeight):

        self.setR(rDegrees)
        self.setZ(zPercentOfHeight)
    
    def changeR(self,degrees):
        self.rController.turnDegreesForward(degrees);

    def changeZ(self,percentOfHeight):
        self.zController.raiseBase(percentOfHeight);

    
    def moveRZ(self, rDegrees, zPercentOfHeight):

        self.changeR(rDegrees)
        self.changeZ(zPercentOfHeight)

    # Given theta in radians, z is height
    def cylindricalToCartesian(r,theta,h):
        return (r*math.cos(theta), r*math.sin(theta), h)
    
    # Returns theta in [-pi/2, pi/2]
    def cartesianToCylindrical(x,z,y):
            theta = 0;
            if (x > 0):
                theta = math.atan(z/x)
            elif (x==0):
                if (z>0):
                    theta = math.pi/2
                else:
                    theta = -math.pi/2
            elif (x < 0 and z > 0):
                theta = math.atan(z/x)+math.pi
            else:
                theta = math.atan(z/x)-math.pi

            return (math.sqrt(x*x + z*z), theta, y)


# Currently for dev interaction, will link with x eventually
def rzLoop(rMotorCur, zMotorCur):

    controller = RZController(rMotorCur, zMotorCur)
    print(rMotorCur.rotation)

    print("Hello! What would you like to do?")
    print("- SET")
    print("- DISP")
    print("- CALR")
    print("- CALZ")
    print("- QUIT")
    print("Type one of the above codes: ",end='')

    action = input()

    while action != "QUIT":

        if action == "SET":
            print("Enter an r (from -180 to 180): ",end='')
            r = float(input())
            print("Enter an z (from 0 to 100): ",end='')
            z = float(input())
       
            controller.setRZ(r, z)
               

        elif action == "MOVE":
            print("Enter an r (from -180 to 180): ",end='')
            r = float(input())
            print("Enter an z (from 0 to 100): ",end='')
            z = float(input())
            try:
                controller.moveRZ(r, z)
                print(f"Moved to r = {controller.getR()}, z = {controller.getZ()}")
            except Exception as e:
                print("Oops, something went wrong!")
                print(e)

        elif action == "DISP":
            print(f'Currently at r = {controller.getR()}, z = {controller.getZ()}')

        elif action == "CALR":
            print("Enter an r (from -180 to 180): ",end='')
            r = float(input())
            controller.calibrateR(r)
            print("Reset r=0")
        
        elif action == "CALZ":
            print("Enter an z (from 0 to 100): ",end='')
            z = float(input())
            controller.calibrateZ(z)
            print("Reset z=0")
        
        else:
            print("INVALID ACTION")
            print("- SET")
            print("- DISP")
            print("- CALR")
            print("- CALZ")
            print("- QUIT")

        print("Type one of the above codes: ",end='')

        action = input()
    
    print("resetting")
    controller.resetRZ()
    print("reset complete!")
        


if __name__ == "__main__":
    Motor1 = DRV8825(dir_pin=13, step_pin=19, enable_pin=12, mode_pins=(16, 17, 20))
    Motor2 = DRV8825(dir_pin=24, step_pin=18, enable_pin=4, mode_pins=(21, 22, 27))

    rMotorCur = rMotor(Motor1)
    zMotorCur = zMotor(Motor2)

    # Main loop
    rzLoop(rMotorCur, zMotorCur)

