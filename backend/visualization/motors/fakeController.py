# import stuff


class fakeController(xrzController):
    def __init__():
        return # probably like super.init()
    
    '''modify the below'''
    def setX(self, targetX, motor = "GRAB"):
        self.status_X = 'UNAVAILABLE' 
  
        super().setX(targetX, motor)
        self.status_X = 'AVAILABLE' 

    def setR(self,targetR, motor):
        self.status_R = 'UNAVAILABLE' 
   
        if motor not in self.motorRotations.keys():
            super().setR((targetR )%360)
        else:
            super().setR((targetR + self.motorRotations[motor])%360)
        self.status_R = 'AVAILABLE' 

    def setZ(self,targetZ):
        self.status_Z = 'UNAVAILABLE' 
        
        super().setZ(targetZ)
        self.status_Z = 'AVAILABLE' 
    
    def resetXRZ(self):
        self.resetX()
        self.resetRZ()
    
