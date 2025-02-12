import math
import coord_funcs
from motors import xrzController

class EggBin():
    egg_array = []
    pos = (0, 0, 0)
    gap = 0 # dummy value: distance between each eggs

    def __init__(self, pos, gap, dimensions=(2,2)):
        self.pos = pos
        self.egg_array = [["f" for j in range(dimensions[1])] for i in range(dimensions[0])]
        self.gap = gap

    def egg_index_to_cartesian_pos(self, index):
        # |0  3|
        # |1  2|

        local_cylindrical_cord = (self.gap*(2**(1/2)),3*math.PI/4 + index*math.PI/2 + self.pos[1], self.pos[2])
        
        
        return coord_funcs.add_cartesian_coords(coord_funcs.cylindrical_to_cartesian(local_cylindrical_cord), 
                                                coord_funcs.cylindrical_to_cartesian(self.pos))
    

class EggBinCollection():
    z = 27959827592502 # supposed to be height or sm
    r = 91827492875982 # sps to be radius
    # the above two should be from xrzController that will be implemented by jeremy.

    bin_array = []
    def __init__(self, layers, edges, gap):
        for i in range(layers):

            for j in range(edges):
                pos = (self.r, 2*math.PI*j/edges, self.z*(1-i/edges))
                self.bin_array[i][j] = EggBin(pos, gap)

        # now you need to update the positions of each one, but im not sure if python thingy is copy by reference or value
        # not sure if order is correct


# index 0 should be the top layer
# index 0,0 should be the top, rightmost 