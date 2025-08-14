import numpy as np
from scipy.optimize import fsolve

#define dense function
def f(c):
    t = 0.5 * (np.sqrt((7/2)**2 + 3*c + c**2) - 5/2 - c)
    dense = (30 * (5 ** (5/2))) / (8*(c+t-0.5)**(c+t-0.5) * (3-c-t)**(3-c-t) * (2*t)**t * (0.5-t)**(0.5-t))
    return dense

#define sparse function
def g(c):
    sparse = 74.2431818181818*2/(9-4*c)
    return sparse

#find differences between pg limit for dense and sparse
def h(x):
    return f(x) - g(x)

#find the appropriate c and pg limit where the two functions are equal (lowest point for all graphs)
def c2():
    intersection_x = fsolve(h, 2.0000)
    intersection_y = f(intersection_x[0])

    print(f"Intersection point: ({intersection_x[0]:.10f}, {intersection_y:.10f})")

c2()