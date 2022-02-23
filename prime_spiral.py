from turtle import *
from sympy import *
import random

speed(0)

title('Fibonacci Spiral')
screensize(960, 720, bg = 'black')



def square(L):
    for k in range(4):
        fd(L)
        lt(90)


def sq_arc(L):
    square(L)
    circle(L, 90)


# Prime number
L = []
for k in range(1,101):
    L.append(composite(k))
    


pu()
goto(-150, 100)
pd()

for i in L:
    color('blue')

    begin_fill()
    color((random.uniform(0, 1), random.uniform(0,1), random.uniform(0, 1)))
    sq_arc(i)


mainloop()

