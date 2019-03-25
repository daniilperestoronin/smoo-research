from scipy.optimize import linprog

b_w = [
    [34, 49, 51, 0, 0],
    [37, 41, 53, 0, 0],
    [31, 45, 55, 0, 0],
    [29, 48, 56, 0, 0],
    [25, 47, 57, 0, 0],
    [24, 44, 58, 0, 0],
    [22, 43, 59, 0, 0]
]

c = [1, 0.3, 1, 0.5, 0.8]
A = [
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

x_r = []

for b in b_w:
    res = linprog(c, A_ub=A, b_ub=b, bounds=(x0_bounds, x1_bounds, x2_bounds, x3_bounds, x4_bounds))
    print(res)
    x_r.append(res.x)

print(x_r)


