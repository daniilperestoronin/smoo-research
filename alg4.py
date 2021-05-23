import numpy as np
import polytope as pc
import sympy


c_1 = [-1.2, -1, -1.8, -2.5, -4.5]
c_2 = [0, 0, 1, 2.2, 3.5]

A = np.array([
    [0, 0, 2, 1, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 3, 0, 1],
    [1, 0, -2, -4, -6],
    [0, 1, -1, -4, -8],
    [-1, -1, 0, 0, 0],
    [1, 1, 0, 0, 0],
])

b_w = np.array([
    [34, 49, 51, 0.5, 0.1, 3009, 990],
    [37, 41, 53, 0.1, 0.5, 3010, 1006],
    [31, 45, 55, 0.3, 0.3, 2900, 1010]
])

b_m = b_w.min(axis=0)
b_p = b_w.max(axis=0)

p2_m = np.diag(np.concatenate((np.ones(5), -1 * np.ones(5)), axis=None))

_, inds = sympy.Matrix(A).T.rref()
A_d = np.linalg.inv(A[list(inds)])

b = np.array([0, 0, 0, 0, 0])

p = pc.Polytope(-1*A_d, b)  # in the form of Ax<=b
p2 = pc.Polytope(p2_m, np.concatenate((b_p, -1*b_m), axis=None))

p_r = p.intersect(p2)

alpha = pc.volume(p_r)/np.prod(b_p-b_m)

print(alpha)
