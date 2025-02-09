import gpiozero as GPIO
import time
from DRV8825 import DRV8825



class zMotor:
	def __init__(self, motor):
		
		self.motor = motor
		self.percentHeight = 0
		

		# EDIT THIS ONCE HEIGHT ADJUSTMENT TO Z MOVEMENT IS FIGURED OUT
		self.conversion = 1
		self.maxHeight = 1

    
	def __init__(self, motor):
		
		self.motor = motor

	def resetBase(self):

		# If storing r position, can also store z position
		self.lowerBase(self, 100)
		
	def changeHeightPercent(self,percentOfHeight):
		
		self.percentHeight += percentOfHeight
		if (self.percentHeight > 1):
			self.percentHeight = 1
		if (self.percentHeight < 0):
			self.percentHeight = 0


	def raiseBase(self,percentOfHeight = 100):
		# Will turn forward or backward, need to figure out which way it goes once we can actually connect
		
		self.turnDegreesForward(self, percentOfHeight * self.conversion)
		
	
	def lowerBase(self, percentOfHeight = 100):

		self.turnDegreesBackward(self, percentOfHeight * self.conversion)
		



	def turnDegreesForward(self, degrees=360):

		self.motor.Start()
		self.motor.TurnStep(Dir='forward', steps=160*degrees/9, stepdelay = 0.005)
		self.motor.Stop()
        
	def turnDegreesBackward(self, degrees=360):
		
		self.motor.Start()
		self.motor.TurnStep(Dir='backward', steps=160*degrees/9, stepdelay = 0.005)
		self.motor.Stop()

		
	"""
	# 1.8 degree: nema23, nema14
	# softward Control :
	# 'fullstep': A cycle = 200 steps
	# 'halfstep': A cycle = 200 * 2 steps
	# '1/4step': A cycle = 200 * 4 steps
	# '1/8step': A cycle = 200 * 8 steps
	# '1/16step': A cycle = 200 * 16 steps
	# '1/32step': A cycle = 200 * 32 steps
	#
	# while True:
	# 	Motor1.SetMicroStep('hardward','fullstep')
	# 	Motor1.TurnStep(Dir='backward', steps=6400, stepdelay = 0.005)
	# 	time.sleep(0.5)
	# 	if input("continue?") !="yes":
	# 		break
	# 	Motor1.TurnStep(Dir='backward', steps=6400, stepdelay = 0.005)
	# 	time.sleep(0.5)
	# 	if input("continue?") !="yes":
	# 		break
	# Motor1.Stop()

	
	# # 28BJY-48:
	# # softward Control :
	# # 'fullstep': A cycle = 2048 steps
	# # 'halfstep': A cycle = 2048 * 2 steps
	# # '1/4step': A cycle = 2048 * 4 steps
	# # '1/8step': A cycle = 2048 * 8 steps
	# # '1/16step': A cycle = 2048 * 16 steps
	# # '1/32step': A cycle = 2048 * 32 steps
	# """
	#while True:
	#	Motor2.SetMicroStep('hardward' ,'fullstep')    
	#	Motor2.TurnStep(Dir='forward', steps=6400, stepdelay=0.002)
	#	time.sleep(0.5)
	#	Motor2.TurnStep(Dir='backward', steps=6400, stepdelay=0.002)
	#	time.sleep(0.5)
	#	if input("continue?") !="yes":
	#		break
	#Motor2.Stop()

# 	Motor1.Stop()
# 	Motor2.Stop()
    
# except:
#     # GPIO.cleanup()
#     print("\nMotor stop")
#     Motor1.Stop()
#     Motor2.Stop()
#     exit()
