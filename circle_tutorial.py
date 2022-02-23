"""
This program draws a circle using turtle

Author: Mr. Asiamah

Date: 13/10/21

"""

import turtle,time
import turtle as t
#t = turtle.Pen()

t.width(2)

t.fillcolor("red")
t.pencolor("black")
t.shapesize(10, 10, 1)

for x in range(1):
    t.shape('turtle')
    t.fillcolor('red')
    time.sleep(3)

    t.shape('square')
    t.fillcolor('yellow')
    time.sleep(3)

    t.shape('classic')
    t.fillcolor('blue')
    time.sleep(3)

    t.shape('circle')
    t.fillcolor('green')
    time.sleep(3)

    t.shape('arrow')
    t.fillcolor('lightgreen')
    time.sleep(3)

    t.shape('triangle')
    t.fillcolor('gold')
    time.sleep(3)
    
t.done()

