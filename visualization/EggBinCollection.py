from egg import Egg

class EggBin():
    egg_array = []
    pos = (0,0)
    gap = 0 # dummy value: distance between each eggs

    def __init__(self, gap, dimensions=(2,2)):
        self.egg_array = [[Egg("f") for j in range(dimensions[1])] for i in range(dimensions[0])]
        self.gap = gap

    def egg_index_to_pos(self, index):
        raise NotImplementedError
        return None
        # implement this by adding pos centered on (0,0) locally in the EggBin 
    

class EggBinCollection():
    bin_array = []
    def __init__(self, dimensions, gap, bin_unit): # dimension, gap is a float of dist between top and bottom stuff, ex_machine_unit is an example of a machine unit
        # dimensions = 
        # define the machine array here, lowk forgot how to
        self.machine_array = [[bin_unit for j in range(dimensions[1])] for i in range(dimensions[0])]
        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                    self.bin_array[i][j].set_pos((i*gap,j*gap)) # this does not work 

        # now you need to update the positions of each one, but im not sure if python thingy is copy by reference or value
        # not sure if order is correct
