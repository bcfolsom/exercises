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
#    mainloop()
#triangle(pink, 400)

from turtle import *
def square(pen, fill, size):
    color(pen, fill)
    begin_fill()
    for i in range(4):
        forward(size)
        left(90)
    end_fill()
    mainloop()

from turtle import *
def pentagon(pen, fill, size):
    color(pen, fill)
    begin_fill()
    for i in range(5):
        forward(100)
        left(72)
    end_fill()
    mainloop()

from turtle import *
def hexagon(pen, fill, size):
    color(pen, fill)
    begin_fill()
    for i in range(6):
        forward(size)
        left(60)
    end_fill()
    mainloop()

from turtle import *
def octagon(pen, fill, size):
    color(pen, fill)
    begin_fill()
    for i in range(8):
        forward(size)
        left(45)
    end_fill()
    mainloop()

from turtle import *
def star(pen, fill, size):
    color(pen, fill)
    begin_fill()
    for i in range(5):
        forward(size)
        right(144)
    end_fill()
    mainloop()

from turtle import *
def mycircle(pen, fill, size):
    color(pen, fill)
    begin_fill()
    width(1)
    circle(size)
    end_fill()
    mainloop()
