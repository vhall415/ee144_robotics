import numpy as np
from modern_robotics import *

def validRotMat(R, e):
    # R is the potential 3x3 rotation matrix
    # e is the allowable error to still be a rotation matrix
    # returns true if R is within e of being a rotation matrix; false otherwise

    # find column vectors
    col1 = [R[0][0], R[1][0], R[2][0]]
    col2 = [R[0][1], R[1][1], R[2][1]]
    col3 = [R[0][2], R[1][2], R[2][2]]
    
    # determine if column vectors are unit vectors
    zeroVec = [0, 0, 0]
    isNorm = True
    if(col1 != zeroVec):
        norm1 = Normalize(col1)
    else:
        isNorm = False
    if(col2 != zeroVec):
        norm2 = Normalize(col2)
    else:
        isNorm = False
    if(col2 != zeroVec):
        norm3 = Normalize(col3)
    else:
        isNorm = False
    
    e_vec = [e, e, e]
    col1_lower = np.subtract(col1, e_vec)
    col1_upper = np.add(col1, e_vec)
    col2_lower = np.subtract(col2, e_vec)
    col2_upper = np.add(col2, e_vec)
    col3_lower = np.subtract(col3, e_vec)
    col3_upper = np.add(col3, e_vec)

    if(isNorm and (norm1 <= col1_upper).all() and (norm1 >= col1_lower).all() and (norm2 <= col2_upper).all() and (norm2 >= col2_lower).all() and (norm3 <= col3_upper).all() and (norm3 >= col3_lower).all()):
        isNorm = True
    else:
        print("not unit vectors")
        isNorm = False

    # determine if column vectors are pairwise orthogonal
    # col1_t * col2
    orth1 = np.dot(col1, col2)
    # col1_t * col3
    orth2 = np.dot(col1, col3)
    # col2_t * col3
    orth3 = np.dot(col2, col3)
    
    if(orth1 <= e and orth1 >= -e and orth2 <= e and orth2 >= -e and orth3 <= e and orth3 >= -e):
        isOrth = True
    else:
        print("not pair-wise orthogonal")
        isOrth = False

    # check if R_t*R = I
    R_t = RotInv(R)
    val = np.matmul(R_t, R)
    I = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    e_mat = [e_vec, e_vec, e_vec]
    I_upper = np.add(I, e_mat)
    I_lower = np.subtract(I, e_mat)

    if((val <= I_upper).all() and (val >= I_lower).all()):
        isI = True
    else:
        print("not identity matrix")
        isI = False

    # check if det R = 1
    det = np.linalg.det(R)
    if((det <= 1+e) and (det >= 1-e)):
        isDet1 = True
    else:
        print("determinant not 1")
        isDet1 = False

    # determine nearest R matrix

    return isNorm and isOrth and isI and isDet1   

# init potential rotation matrix and allowable error
R = [[1, 0, 0],
     [0, 1.01, 0],
     [0, 0, 1]]
e = 0.1

out = validRotMat(R, e)
#print(out)
