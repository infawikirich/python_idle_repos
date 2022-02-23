from turtle import *
import random

title('Fibonacci Spiral')
screensize(960, 720, bg = 'black')

speed(1)


def square(L):
    for k in range(4):
        fd(L)
        lt(90)


def sq_arc(L):
    square(L)
    circle(L, 90)


# Fib
onacci series
L = [1, 2, 3, 5, 8, 13, 21, 34,55, 89, 144, 233, 377]

pu()
goto(-150, 100)
pd()

for i in L:
    color('blue')

    begin_fill()
    color((random.uniform(0, 1), random.uniform(0,1), random.uniform(0, 1)))
    sq_arc(i)


