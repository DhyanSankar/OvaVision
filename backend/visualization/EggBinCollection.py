import math
import random
import coord_funcs
import motors.xrzController as xrzController
import copy

class EggBin():
    egg_array = [0,0,0,0]
    pos = (0, 0, 0)
    gap = 0 # dummy value: distance between each eggs

    def __init__(self, pos, gap, dimensions=(2,2)):
        self.pos = pos
        self.egg_array = [["f" for j in range(dimensions[1])] for i in range(dimensions[0])]
        self.gap = gap

    def __init__(self, pos, gap, egg_array, dimensions=(2,2)):
        self.__init__(pos, gap, dimensions)
        self.egg_array = egg_array

    def egg_index_to_cartesian_pos(self, index):
        # |0  3|
        # |1  2|

        local_cylindrical_cord = (self.gap*(2**(1/2)),3*math.pi/4 + index*math.pi/2 + self.pos[1], self.pos[2])
        
        return coord_funcs.add_cartesian_coords(coord_funcs.cylindrical_to_cartesian(local_cylindrical_cord), 
                                                coord_funcs.cylindrical_to_cartesian(self.pos))
        
class EggBinCollection():
    # controller = xrzController() # xrzController
    bin_array = []

    def __init__(self, layers, edges, gap):

        for i in range(layers):
            self.bin_array.append([])
            for j in range(edges):
                pos = (4, 2*math.pi*j/edges, 2*(1-i/edges)) # 4 and 2 should be turned into controller.r and controller.z
                self.bin_array[i].append(EggBin(pos, gap))

    def randomize_sex_for_test(self):
        for layer in self.bin_array:
            for bin in layer:
                bin.egg_array = ["f" if random.random()<.5 else "m" for i in range(4)]
        return
    
    def is_goal_state(self, goal):
        if len(self.bin_array)!=len(goal.bin_array) or len(self.bin_array[0]!=len(goal.bin_array[0])):
            return False
        
        for i in range(len(self.bin_array)):
            for j in range(len(self.bin_array[0])):
                if self.bin_array[i][j].egg_array != goal.bin_aray[i][j].egg_array:
                    return False
                
        return True
    
    def get_next_state(self, action):
        state = copy.deepcopy(self)
        state.bin_array[action[1][0]][action[1][1]].egg_array[action[1][2]] = state.bin_array[action[0][0]][action[0][1]].egg_array[action[0][2]]
        state.bin_array[action[0][0]][action[0][1]].egg_array[action[0][2]] = "0"

        return state
    
    def get_all_actions(self):
        # select a male or female, select empty squares.
        empty_positions = []
        filled_positions = []

        for i in range(len(self.bin_array)):
            for j in range(len(self.bin_array[0])):
                for k in range(4):
                    if self.bin_array[i][j].egg_array[k] == "0":
                        empty_positions.append([i,j,k])
                    else:
                        filled_positions.append([i,j,k])

        return [[f,e] for f in filled_positions for e in empty_positions]
    

    # we need to get all next states
    # we need to check if it is a goal state
    
class EntireMachinery(EggBinCollection):
    controller = xrzController()

    def __init__(self, layers, edges, gap, controller):
        super.__init__(layers, edges, gap)
        self.controller = controller

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
