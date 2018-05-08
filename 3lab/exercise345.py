from exercise344 import *

def validso3(S, e):
    # S is the potential 3x3 skew-symmetric matrix in so(3)
    # e is the allowable error to still be a skew-symmetric matrix
    # returns true if S is within e of being an element of so(3); false otherwise

    # matrix should be of form:
    #  0  -x3  x2
    #  x3  0  -x1
    # -x2  x1  0

    # get x1, x2, x3, -x1, -x2, -x3 values
    x1 = S[2][1]
    x2 = S[0][2]
    x3 = S[1][0]
    x1_neg = S[1][2]
    x2_neg = S[2][0]
    x3_neg = S[0][1]

    # check if opposite x-values match within e
    if(x1 <= e-x1_neg and x1 >= -x1_neg-e and x2 <= e-x2_neg and x2 >= -x2_neg-e and x3 <= e-x3_neg and x3 >= -x3_neg-e):
        sameX = True
    else:
        sameX = False

    # check if S = -transpose(S) within e
    S_trans = np.array(S).T
    e_mat = [[e, e, e],
             [e, e, e],
             [e, e, e]]
    S_trans_upper = np.add(-S_trans, e_mat)
    S_trans_lower = np.subtract(-S_trans, e_mat)

    if((S <= S_trans_upper).all() and (S >= S_trans_lower).all()):
        isNegTrans = True
    else:
        isNegTrans = False

    return sameX and isNegTrans

# testing so3
S = [[0, -1, 2],
     [1, 0, -3],
     [-2, 3, 0]]
e = 0.1

out = validso3(S, e)
#print(out)
