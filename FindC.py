import numpy as np

min = 0
minc = 0
for i in range(100):
    c = 3/100 * (i+1)
    t = 0.5 * (np.sqrt((7/2)**2 + 3*c + c**2) - 5/2 - c)
    pg = (30 * (5 ** (5/2))) / (8*(c+t-0.5)**(c+t-0.5) * (3-c-t)**(3-c-t) * (2*t)**t * (0.5-t)**(0.5-t))
    print(pg)
    print(c)
    if pg < min:
        min = pg
        minc = c
print(min)
print(minc)