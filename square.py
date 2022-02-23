"""
    file  - square.py

    purpose - This program uses turtle to draw a square

    author  - Mr. Asiamah

    date    - 03/11/2021
     
"""

import turtle

t = turtle.Pen()

win = turtle.Screen()
win.bgcolor('black')


t.width(2)
t.pencolor('yellow')
t.fillcolor('red')

t.speed(0)

#turtle.tracer(12)

t.begin_fill()

for k in range(4):
    t.fd(200)
    t.lt(90 )

t.end_fill()


t.ht()

turtle.mainloop()
