import turtle
import random

t = turtle.getturtle()

win = turtle.Screen()
win.bgcolor('black')
win.title('Onscreenclick event')
win.setup(800, 600)

t.speed(0)
t.width(3)

colors = ['red', 'blue', 'green', 'navy',  'yellow', 'teal']


def star(x, y):
    t.pu()
    t.setpos(x,y)

    t.pd()
    t.color(random.choice(colors))
    for k in range(5):
        t.fd(90)
        t.lt(144)


win.onscreenclick(star)

turtle.done()
