from turtle import *

def triangle():
    for i in range(3):
        forward(100)
        left(120)

def square():
    for i in range(4):
        forward(100)
        left(90)

def pentagon():
    for i in range(5):
        forward(100)
        left(72)

def hexagon():
    for i in range(6):
        forward(100)
        left(60)

def octagon():
    for i in range(8):
        forward(100)
        left(45)

def star():
    for i in range(5):
        forward(100)
        right(144)

def mycircle():
    width(1)
    circle(100)
    mainloop()
