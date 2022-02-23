"""

stamping my turtle

"""

import turtle

t = turtle.Pen()

win = turtle.Screen()
win.bgcolor('lightgreen')

t.speed(0)


t.shape('square')


for k in range(100):
    t.fd(200)
    t.stamp()
    t.lt(91)
