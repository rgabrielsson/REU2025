import numpy as np
from scipy.optimize import fsolve


def f(c):
    t = 0.5 * (np.sqrt((7/2)**2 + 3*c + c**2) - 5/2 - c)
    dense = (30 * (5 ** (5/2))) / (8*(c+t-0.5)**(c+t-0.5) * (3-c-t)**(3-c-t) * (2*t)**t * (0.5-t)**(0.5-t))
    return dense

def g(c):
    sparse = 162/(9-4*c)
    return sparse

def h(x):
    return f(x) - g(x)


def c2():
    intersection_x = fsolve(h, 2.0000)
    intersection_y = f(intersection_x[0])

    print(f"Intersection point: ({intersection_x[0]:.10f}, {intersection_y:.10f})")

c2()





# def c1():
#     for i in range(100000000):
#         c = 3/100000000 * (i+1)
#         if c < 1.9:
#             continue
#         if c > 2.1:
#             break
#         t = 0.5 * (np.sqrt((7/2)**2 + 3*c + c**2) - 5/2 - c)
#         dense = (30 * (5 ** (5/2))) / (8*(c+t-0.5)**(c+t-0.5) * (3-c-t)**(3-c-t) * (2*t)**t * (0.5-t)**(0.5-t))
#         try:
#             sparse = 162/(9-4*c)
#         except ZeroDivisionError:
#             continue

#         if sparse - .00001 < dense < sparse + .00001:
#             print(c)
#             print(dense)
#             print(sparse)
#             print("---------")
