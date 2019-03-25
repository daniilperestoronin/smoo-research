from scipy.optimize import linprog

b_m = [22, 43, 59, 0, 0]

c_m = [-0.1, 0, -0.1, 0.01, 0.001]
A_m = [
    [-1, -1, -1, -1, -1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, -2, -10, -6],
    [0, 1, -1, -4, -8]
]

b_p = [22, 43, 59, 0, 0]

c_p = [1, 0.3, 1, 0.5, 0.8]
A_p = [
    [0, 0, 2, 1, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 3, 0, 1],
    [1, 0, -2, -4, -6],
    [0, 1, -1, -4, -8]
]

x0_bounds = (0, None)
x1_bounds = (0, None)
x2_bounds = (0, None)
x3_bounds = (0, None)
x4_bounds = (0, None)

res = linprog(c_m, A_ub=A_m, b_ub=b_p,
              bounds=(x0_bounds, x1_bounds, x2_bounds, x3_bounds, x4_bounds))
print(res.fun, res.x)

res = linprog(c_p, A_ub=A_p, b_ub=b_m,
              bounds=(x0_bounds, x1_bounds, x2_bounds, x3_bounds, x4_bounds))
print(res.fun, res.x)


