import numpy as np
from exercise343 import *

def validTransMat(T, e):
    # T is the potential 4x4 transformation matrix
    # e is the allowable error to still be a transformation matrix
    # returns true if T is within e of being a transformation matrix; false otherwise

    # init output to false (not a transformation matrix)
    output = False

    # check if first 3x3 portion of T is a rotational matrix
    R = [[T[0][0], T[0][1], T[0][2]],
         [T[1][0], T[1][1], T[1][2]],
         [T[2][0], T[2][1], T[2][2]]]
    
    valRot = validRotMat(R, e)
    
    if(valRot):
        # check if last row is all zeros except last column should be a 1
        lastRow = [T[3][0], T[3][1], T[3][2], T[3][3]]
        valRow = [0, 0, 0, 1]

        if(lastRow == valRow):
            output = True
        else:
            print("Last row not of form [0, 0, 0, 1]\n")
    else:
        print("Doesn't contain a rotational matrix\n")

    return output

T = [[1, 0, 0, 1],
     [0, 1, 0, 2],
     [0, 0, 1, 3],
     [0, 0, 0, 1]]
e = 0.1

out = validTransMat(T, e)
#print(out)
