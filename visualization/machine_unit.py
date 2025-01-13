class MachineUnit():
    z_reach = 0
    x_reach = 0
    eggs_stored = [] # location of eggs are based on the index or in the egg class itself
    # should also probably have a maximum value of eggs stored
    position = (0,0,0) # maybe a 3-tuple

    def __init__(self, x_reach, z_reach, position, eggs_stored=[]) :
        self.x_reach = x_reach
        self.z_reach = z_reach
        self.position = position
        self.eggs_stored = eggs_stored
        # a machine unit should have a position.
        # i would also assume there may be multiple machine units possible, but then this will get extremely wonky. 

    # probably want an update eggs function
    def get_egg_pos(self, index):
        raise NotImplementedError
        return None
    
    def add_egg(self, new_egg, index):
        self.eggs_stored[index] = new_egg

    def egg_pos_empty(self, index):
        return self.eggs_stored[index] == 0 # placeholder 0 for null value
    
    # probably want putting egg into somewhere
    def move_egg(self, current_index, other_unit, move_to_index):
        if other_unit.egg_pos_empty(move_to_index):
            other_unit.add_egg(self.eggs_stored[current_index])
            self.eggs_stored[current_index] = 0
            return "done" # placeholder return values
        else:
            return "unable"
        
    # in the future, depending on how stuff is moved, claim that a machine unit is being used and is unable to move
    # also possibly record the positions of the machine arms? 
    # the above is used to actually visualize the movements
    # need a python something to import to visualize. unsure of what to use.
    # when we do move_egg, we would want to in theory know how exactly we move the egg.