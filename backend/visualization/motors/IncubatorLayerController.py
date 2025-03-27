import time
import DRV8825 as DRV8825

class IncubatorLayerController:
	
    # Going to be 4 layers typically I think?
    numOfLayers = 4
    layers = []
    extended = []
    def __init__(self, layers):
        self.layers = layers
        for i in range(4):
            self.extended.append(False)
        


    def extend(self,layerNumber):
        # Make the thing extend
        self.extended[layerNumber] =True
        pass

    def retract(self,layerNumber):
        # Make the thing retracted
        self.extended[layerNumber] =False
        pass

    def reset(self):
        for i in range(self.numOfLayers):
            self.retract(i)