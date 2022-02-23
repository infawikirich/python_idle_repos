"""
This program draws a semicircle with a circle embedded in it

Author: Mr. Asiamah

Date: 20/10/21

"""

import turtle
import turtle as t

win = turtle.Screen()
win.setup(800, 640)
win.bgcolor('black')

t.color('blue')

t.width(2)


# lift the pen up to the point (200, 0)
t.up()
t.goto(300, 0)

# put the down to draw a semicircle with radius 200 (diameter = 400)
t.down()
t.left(90)

t.begin_fill()

t.circle(300, 180)

t.end_fill()

# done drawing the semicircle
# change the pen heading
t.left(90)
t.fd(600)


# move to home and draw a circle
t.up()
t.home()

t.pd()

t.color('white')

t.begin_fill()

t.circle(150)

t.end_fill()




# hide turtle
t.ht()


turtle.mainloop()
