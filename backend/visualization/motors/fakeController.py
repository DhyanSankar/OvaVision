from xrzController import xrzController
import keyboard #does this import work


class fakeController(xrzController):
    def __init__():
        return # probably like super.init()
    
    '''modify the below'''
    def setX(self, targetX, motor = "GRAB"):
        # super().setX(targetX, motor)

        keyboard.write(f"X {targetX}")

    def setR(self,targetR, motor):   
        # if motor not in self.motorRotations.keys():
        #     super().setR((targetR )%360)
        # else:
        #     super().setR((targetR + self.motorRotations[motor])%360)
        keyboard.write(f"R {(targetR )%360}")

    def setZ(self,targetZ):        
        # super().setZ(targetZ)
        keyboard.write(f"Z {targetZ}")
    
    def resetXRZ(self):
        # self.resetX()
        # self.resetRZ()
        keyboard.write("RESET")
    
