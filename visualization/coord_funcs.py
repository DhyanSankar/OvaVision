import math

def cylindrical_to_cartesian(cyl_pos):
    return (cyl_pos[0]*math.cos(cyl_pos[1]), cyl_pos[0]*math.sin(cyl_pos[1]), cyl_pos[2])

def add_cartesian_coords(pos1, pos2):
    return (pos1[i] + pos2[i] for i in range(3))