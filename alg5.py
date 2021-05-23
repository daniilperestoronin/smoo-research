from scipy.optimize import linprog
import numpy as np


al = 0.8
bt = 0.2

c_1 = [-1.2, -1, -1.8, -2.5, -4.5]
c_2 = [0, 0, 1, 2.2, 3.5]

A = [
    [0, 0, 2, 1, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 3, 0, 1],
    [1, 0, -2, -4, -6],
    [0, 1, -1, -4, -8],
    [-1, -1, 0, 0, 0],
    [1, 1, 0, 0, 0],
]

b_w = [
    [34, 49, 51, 0, 0, 3000, 1000],
    [37, 41, 53, 0, 0, 3000, 1000],
    [31, 45, 55, 0, 0, 3000, 1000]
]

b = np.average(np.array(b_w), axis=0)
c = np.array(c_1) * al + np.array(c_2) * bt

x1_bounds = (0, None)
x2_bounds = (0, None)
x3_bounds = (0, None)
x4_bounds = (0, None)
x5_bounds = (0, None)

res = linprog(c, A_ub=A, b_ub=b, bounds=(
    x1_bounds, x2_bounds, x3_bounds, x4_bounds, x5_bounds))
print(res.x)
