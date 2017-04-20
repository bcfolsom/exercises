import matplotlib.pyplot as plot
import math
from numpy import arange

temp = int(input("Temperature in C? "))

def f(x):
    return temp * 1.8 + 32

xs = list(range(-100, 100))
ys = []
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()
