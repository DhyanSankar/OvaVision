# import gpiozero as GPIO
class XController:

	def __init__(self, motors):
		self.motors = []
		self.motors = motors;
	
	def setX(self, x, motorName):
		
		haveFound = 0
		for motor in self.motors:
			if motor.name == motorName:
				motor.setX(x)
				haveFound = 1
		
		if (not haveFound):
			print(f"Failed to find motor {motorName}")
    
	def getX(self):
		motorPositions = []
		
		for motor in self.motors:
			motorPositions.append((motor.name,motor.getX()));
		
		return motorPositions;
       
	def calibrateX(self, degrees = 0):

		for motor in self.motors:
			motor.calibrateX(degrees);
    # Not sure how this should work actually, if we're using percents then calibration doesn't make much sense
	def resetX(self):
		for motor in self.motors:
			motor.reset();

        


  

    