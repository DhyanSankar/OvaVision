# import gpiozero as GPIO
import time
from DRV8825 import DRV8825

# Should restructure to make it so we pass in a specific motor, do class constructions

class rMotor:

	def __init__(self, motor):
		
		self.motor = motor
		self.rotation = 0

		# Full rotation: 6400 steps (actually should be checked)
		self.STEPS = 6400


	def reset(self):
		# Perhaps should make it so it stores its position always, maybe in a text file?
		self.turnDegreesBackward(self.rotation)



	def setRotation(self,degrees):
		if degrees > self.rotation:
			self.turnDegreesForward(degrees-self.rotation)
		if degrees < self.rotation:
			self.turnDegreesBackward(self.rotation-degrees)
	 

	def setStoredRotation(self,degrees):
		
		self.rotation = degrees

		if self.rotation > 180:
			self.rotation = 180

		if self.rotation < -180:
			self.rotation = -180
		

	def changeStoredRotation(self,degrees):
		self.rotation += degrees

		if self.rotation > 180:
			print("Rotation > 180")

		if self.rotation < -180:
			print("Rotation < -180")
		
		


	def turnDegreesForward(self, degrees=360):

		if (degrees < 0):
			self.turnDegreesBackward(-degrees)

		else:
			if self.rotation + degrees > 180:
				print("> 180, setting to 180")
				degrees = 180-self.rotation

			self.motor.Start()
			self.motor.TurnStep(Dir='forward', steps=self.STEPS*degrees/360, stepdelay = 0.005)
			self.motor.Stop()
			self.changeStoredRotation(degrees)
        

	def turnDegreesBackward(self, degrees=360):
		
		if (degrees < 0):
			self.turnDegreesForward(-degrees)
			
		else:
			if self.rotation - degrees < -180:
				print("< -180, setting to -180")
				degrees = self.rotation + 180

			self.motor.Start()
			self.motor.TurnStep(Dir='backward', steps=self.STEPS*degrees/360, stepdelay = 0.005)
			self.motor.Stop()

			self.changeStoredRotation(-degrees)
				
			
