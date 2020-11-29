from scipy.optimize import linprog
import numpy as np


def dual_simplex(objective, constraints, values):
    A = np.array(constraints)
    b = np.array(values)
    c = np.array(objective)
    result = linprog(c, A_ub=A, b_ub=b, bounds=(0, None), method="revised simplex")
    return result


# result = dual_simplex([3,2,1],[[-3,-1,-1],[3,-3,-1],[1,1,1],[-1,0,0],[0,-1,0],[0,0,-1]],[-3,-6,3,0,0,0])
# print(result)

# A  = np.array([[-3,-1,-1],[3,-3,-1],[1,1,1],[-1,0,0],[0,-1,0],[0,0,-1]])
# b = np.array([-3,-6,3,0,0,0])
# c = np.array([3,2,1])
#
#
# result = linprog(c,A_ub=A,b_ub=b,bounds=(0,None),method="revised simplex")
# print(result)
