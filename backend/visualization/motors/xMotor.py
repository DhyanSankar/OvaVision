# import gpiozero as GPIO
class xMotor:

	# Would be

	def __init__(self, motor,name):
		self. motor = motor
		self.name = name;
		self.extendedDistance = 0;
	
	def setX(self,distance):
		self.extendedDistance = distance;
		print("x")
		pass
    
	def getX(self):
		return self.extendedDistance
       
	def calibrateX(self, distance = 0):

		pass
    # Not sure how this should work actually, if we're using percents then calibration doesn't make much sense
	def resetX(self):
		pass

	def changeX(self):
		pass
        


  

    