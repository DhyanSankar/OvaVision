import time

class IncubatorController:
	
    incubators = []

    def __init__(self, incubators):
        self.incubators = incubators;

    def get(self,index):
        return self.incubators[index];