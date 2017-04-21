from turtle import *
from random import *

#speed()
#color('black', 'purple')
#filling()
#begin_fill()
#def size():
#    for i in range
#def fill():
#    for i in range
#def color():

def triangle(pen, fill, size):
    color(pen, fill)
    begin_fill()
    for i in range(3):
        forward(size)
        left(120)
    end_fill()

def square(pen, fill, size):
    begin_fill()
    for i in range(4):
        forward(100)
        left(90)
    end_fill()

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
    end_fill()

mainloop()
