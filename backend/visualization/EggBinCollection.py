import math
import random
import backend.visualization.coord_funcs as coord_funcs
import backend.visualization.motors.xrzController as xrzController
import copy
        
class EggBinCollection():
    # controller = xrzController() # xrzController
    parent = None
    previous_action = None
    bin_array = []
    r = 1 # perhaps set this to default vals later, or use this later to pass in params for xrzController
    z = 1
    path_cost = 0

    def __init__(self, full_arr):
        self.bin_array = full_arr

    def __lt__(self, other):
        return False

    def randomize_sex_for_test(self):
        for layer in self.bin_array:
            for bin in layer:
                bin = ["f" if random.random()<.33 else "0" if random.random()<.33 else "m" for i in range(4)]
        return
    
    def is_goal_state(self, goal):
        if len(self.bin_array)!=len(goal.bin_array) or len(self.bin_array[0])!=len(goal.bin_array[0]):
            return False
        
        for i in range(len(goal.bin_array)):
            for j in range(len(goal.bin_array[0])):
                if goal.bin_array[i][j] == "0" and self.bin_array[i][j] != "0":
                    return False
                elif goal.bin_array[i][j] != "0" and self.bin_array[i][j] not in ["0", goal.bin_array[i][j]]:
                    return False
                
        # whether for each thing in the goal array, if the current array either has everything 0 or m/f
        # have remaining ones be empty
                
        return True
    
    def get_next_state(self, action):
        state = copy.deepcopy(self)
        state.bin_array[action[1][0]][action[1][1]][action[1][2]] = state.bin_array[action[0][0]][action[0][1]][action[0][2]]
        state.bin_array[action[0][0]][action[0][1]][action[0][2]] = "0"

        state.previous_action = action
        state.parent = self

        return state
    
    def get_all_actions(self):
        # select a male or female, select empty squares.
        empty_positions = []
        filled_positions = []

        for i in range(len(self.bin_array)):
            for j in range(len(self.bin_array[0])):
                for k in range(4):
                    if self.bin_array[i][j][k] == "0":
                        empty_positions.append([i,j,k])
                    else:
                        filled_positions.append([i,j,k])

        return [[f,e] for f in filled_positions for e in empty_positions]
    
    def output_as_array(self): # refactor stuff using this
        arr = copy.deepcopy(self.bin_array)
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                arr[i][j]=arr[i][j].egg_array

        return arr
    
    def print_status(self):        
        entire_str = ""
        for layer in self.bin_array:
            top_string = ""
            bottom_string = ""

            for bin in layer:
                top_string += "|" + bin[0] + " " + bin[3] + "|  "
                bottom_string += "|" + bin[1] + " " + bin[2] + "|  "
            
            print(top_string)
            print(bottom_string)
            print("\n")

            entire_str += top_string + "\n" + bottom_string + "\n\n"

        return entire_str
    
class EntireMachinery(EggBinCollection):
    controller = xrzController.XRZController()
    sorter = -1
    r = 1 # default values
    z = 1
    gap = 1

    def __init__(self, layers, edges, sorter, gap=1, controller=None):
        super().__init__(layers, edges, gap)
        self.sorter = sorter
        if self.controller != None:
            self.controller = controller
    
    def __init__(self, arr, sorter, gap=1, controller=xrzController.XRZController()):
        super().__init__(arr)
        self.sorter = sorter
        self.gap = gap
        if self.controller != None:
            self.controller = controller

    def eggbin_pos_cylindrical(self, i, j): # i, j are the first two positions in the array
        return (self.r, self.z*math.pi*j/len(self.bin_array[0]), self.z*(1-i/len(self.bin_array[0]))) # r, z from controller itself?
    
    def egg_pos_cartesian(self, i, j, k): # specifies the exact position of egg in the stuff
        # |0  3|
        # |1  2|

        local_cylindrical_cord = (self.gap*(2**(1/2)),3*math.pi/4 + k*math.pi/2 + self.eggbin_pos_cylindrical[1], self.eggbin_pos_cylindrical[2])
        
        return coord_funcs.add_cartesian_coords(coord_funcs.cylindrical_to_cartesian(local_cylindrical_cord), 
                                                coord_funcs.cylindrical_to_cartesian(self.eggbin_pos(i,j)))


    def print_status(self):
        entire_str = self.controller.print_status()
        
        estimate = 'NOT AVAILABLE'

        entire_str += "\n" + super().print_status()

        print("Estimated Sorting Time Remaining: " + estimate)
        entire_str += "Estimated Sorted Time Remaining: " + estimate

        return entire_str
