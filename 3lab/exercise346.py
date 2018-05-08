from exercise345 import *

def validse3(T, e):
    # T is the potential 4x4 twist matrix in se(3)
    # e is the allowable error to still be a twist matrix
    # returns true if T is within e of being an element of se(3); false otherwise

    # matrix should be of form:
    # [w] v
    # 0   0
    # w is a 3x3 skew-symmetric matrix
    # v is a 3x1 linear velocity of the origin

    # check if w is a valid 3x3 skew-symmetric matrix in so(3)
    w = [[T[0][0], T[0][1], T[0][2]],
         [T[1][0], T[1][1], T[1][2]],
         [T[2][0], T[2][1], T[2][2]]]

    valso3 = validso3(w, e)

    # assume v is the proper linear velocity

    # check last row is all zeros within e
    upper = [e, e, e, e]
    lower = [-e, -e, -e, -e]
    lastRow = [T[3][0], T[3][1], T[3][2], T[3][3]]

    if(lastRow <= upper and lastRow >= lower):
        isValRow = True
    else:
        isValRow = False

    return valso3 and isValRow

# test twist matrix
T = [[0, -1, 2, 1],
     [1, 0, -3, 2],
     [-2, 3, 0, 3],
     [0, 0, 0, 0]]
e = 0.1

out = validse3(T, e)
#print(out)
