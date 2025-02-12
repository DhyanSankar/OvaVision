from egg import Egg
import math
import coord_funcs

class EggBin():
    egg_array = []
    pos = (0, 0, 0)
    gap = 0 # dummy value: distance between each eggs

    def __init__(self, gap, dimensions=(2,2)):
        self.egg_array = [[Egg("f") for j in range(dimensions[1])] for i in range(dimensions[0])]
        self.gap = gap

    def egg_index_to_cartesian_pos(self, index):
        # |0  3|
        # |1  2|

        local_cylindrical_cord = (self.gap*(2**(1/2)),3*math.PI/4 + index*math.PI/2 + self.pos[1], self.pos[2])
        
        
        return coord_funcs.add_cartesian_coords(coord_funcs.cylindrical_to_cartesian(local_cylindrical_cord), 
                                                coord_funcs.cylindrical_to_cartesian(self.pos))
    

class EggBinCollection():
    bin_array = []
    def __init__(self, layers, edges, gap, bin_unit): # dimension, gap is a float of dist between top and bottom stuff, ex_machine_unit is an example of a machine unit
        # dimensions = 
        # define the machine array here, lowk forgot how to
        self.machine_array = [[bin_unit for j in range(edges)] for i in range(layers)]
        for i in range(layers):
            for j in range(edges):
                    self.bin_array[i][j].set_pos((i*gap,j*gap)) # this does not work 

        # now you need to update the positions of each one, but im not sure if python thingy is copy by reference or value
        # not sure if order is correct


# index 0 should be the top layer
# index 0,0 should be the top, rightmost 