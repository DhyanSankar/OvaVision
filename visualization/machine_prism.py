class MachinePrison():
    machine_array = []

    def __init__(self, dimensions, gaps, ex_machine_unit): # dimension, gap is a tuple, ex_machine_unit is an example of a machine unit
        # define the machine array here, lowk forgot how to
        self.machine_array = [[[ex_machine_unit for k in range(dimensions[2])] for j in range(dimensions[1])] for i in range(dimensions[0])]
        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                for k in range(dimensions[2]):
                    self.machine_array[i][j][k].set_pos((i*gaps[0],j*gaps[1],k*gaps[2]))

        # now you need to update the positions of each one, but im not sure if python thingy is copy by reference or value
        # not sure if order is correct
