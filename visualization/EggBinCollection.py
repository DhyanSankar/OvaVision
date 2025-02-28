import math
import random
import coord_funcs
# import motors.xrzController

class EggBin():
    egg_array = [0,0,0,0]
    pos = (0, 0, 0)
    gap = 0 # dummy value: distance between each eggs

    def __init__(self, pos, gap, dimensions=(2,2)):
        self.pos = pos
        self.egg_array = [["f" for j in range(dimensions[1])] for i in range(dimensions[0])]
        self.gap = gap

    def egg_index_to_cartesian_pos(self, index):
        # |0  3|
        # |1  2|

        local_cylindrical_cord = (self.gap*(2**(1/2)),3*math.pi/4 + index*math.pi/2 + self.pos[1], self.pos[2])
        
        return coord_funcs.add_cartesian_coords(coord_funcs.cylindrical_to_cartesian(local_cylindrical_cord), 
                                                coord_funcs.cylindrical_to_cartesian(self.pos))
    

class EggBinCollection():
    controller = xrzController() # xrzController
    bin_array = []

    def __init__(self, layers, edges, gap):

        for i in range(layers):
            self.bin_array.append([])
            for j in range(edges):
                pos = (4, 2*math.pi*j/edges, 2*(1-i/edges)) # 4 and 2 should be turned into controller.r and controller.z
                self.bin_array[i].append(EggBin(pos, gap))

    def __init__(self, layers, edges, gap, controller):
        self.__init__(layers, edges, gap)
        self.controller = controller


    def randomize_sex_for_test(self):
        for layer in self.bin_array:
            for bin in layer:
                bin.egg_array = ["f" if random.random()<.5 else "m" for i in range(4)]
        return

    def print_status(self):
        entire_str = self.controller.print_status()
        
        estimate = 'NOT AVAILABLE'

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