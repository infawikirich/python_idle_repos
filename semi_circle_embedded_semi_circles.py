"""
This program draws a semicircle with a three semicircles embedded in it

Author: Mr. Asiamah

Date: 20/10/21

"""

import turtle
import turtle as t

win = turtle.Screen()
win.setup(1000, 840)
win.bgcolor('black')

t.width(2)


def semi_circle_big(radius, color):
    t.color(color)


    # lift the pen up to the point (200, 0)
    t.up()
    t.goto(400, -200)

    # put the down to draw a semicircle with radius 200 (diameter = 400)
    t.down()
    t.left(90)

    t.begin_fill()

    t.circle(radius, 180)

    t.end_fill()



semi_circle_big(400,'blue')

t.left(90)

t.fd(800)

t.left(90)

def semi_circle_small(radius, color):

    t.color('white')

    t.begin_fill()

    t.circle(radius, 180)

    t.end_fill()

semi_circle_small(400/3, 'white')

t.left(180)

semi_circle_small(400/3, 'white')

t.left(180)

semi_circle_small(400/3, 'white')

#t.ht()
turtle.mainloop()
