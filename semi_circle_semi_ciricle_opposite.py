"""
This program draws a semicircle with a three semicircles embedded in it

Author: Mr. Asiamah

Date: 20/10/21

"""

import turtle
import turtle as t

win = turtle.Screen()
win.setup(1000, 840)
win.bgcolor('lightgreen')

t.width(2)




def semi_circle_big(radius, color,  pcolor):

    t.pencolor(pcolor)
    t.fillcolor(color)
    

    # lift the pen up to the point (200, 0)
    t.up()
    t.goto(400, -200)

    # put the down to draw a semicircle with radius 200 (diameter = 400)
    t.down()
    t.left(90)

    t.begin_fill()

    t.circle(radius, 180)

    t.end_fill()



semi_circle_big(400,'teal', 'black')

t.up()
t.setx(400)
t.pd()


def semi_circle_small(radius, color, pcolor):

    t.pencolor(pcolor)

    t.fillcolor(color)

    t.begin_fill()

    t.circle(radius, 180)

    t.end_fill()

semi_circle_small(-400/2, 'teal', 'black')

t.left(-90)

for k in range(20):
    t.fd(10)
    t.up()
    t.fd(10)
    t.pd()


t.ht()
turtle.mainloop()
