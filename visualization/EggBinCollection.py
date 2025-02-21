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
    controller = None # xrzController

    bin_array = []
    def __init__(self, layers, edges, gap, controller):
        self.controller = controller

        for i in range(layers):

            for j in range(edges):
                pos = (self.r, 2*math.PI*j/edges, self.z*(1-i/edges))
                self.bin_array[i][j] = EggBin(pos, gap)


    def print_status(self):
        entire_str = ""

        status_X = 'UNAVAILABLE' # theoretically this should print whether motor is in use and current position of the motor.
        status_R = 'UNAVAILABLE'
        status_Z = 'UNAVAILABLE'
        estimate = 'UNAVAILABLE'

        print("Motor Status:")
        print("  X:  " + status_X)
        print("  R:  " + status_R)
        print("  Z:  " + status_Z)


        entire_str += "Motor Status:\n" + "\tX:\t" + status_X + "\n\tR:\t" + status_R + "\n\tZ:\t" + status_Z + "\n" 

        for layer in self.bin_array:
            top_string = ""
            bottom_string = ""

            for bin in layer:
                top_string += "|" + bin.egg_array[0] + " " + bin.egg_array[3] + "|  "
                bottom_string += "|" + bin.egg_array[1] + " " + bin.egg_array[2] + "|  "
            
            print(top_string)
            print(bottom_string)
            print("\n")

            entire_str += top_string + "\n" + bottom_string + "\n\n"

        print("Estimated Sorting Time Remaining: " + estimate)
        entire_str += "Estimated Sorted Time Remaining: " + estimate

        return entire_str
        



# index 0 should be the top layer
# index 0,0 should be the top, rightmost 