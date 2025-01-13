class MachinePrison():
    machine_array = []

    def __init__(self, dimensions, distance, ex_machine_unit): # dimension, gap is a tuple, ex_machine_unit is an example of a machine unit
        # define the machine array here, lowk forgot how to
        self.machine_array = [[[ex_machine_unit for k in range(dimensions[2])] for j in range(dimensions[1])] for i in range(dimensions[0])]
        # not sure if order is correct
        return
        
        
        