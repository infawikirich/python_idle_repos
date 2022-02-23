
"""
 script file: koch_curve.py

 purpose: This program uses recursive approach to
          draw fractal

 author: Mr. Asiamah

 date: 09/11/21
"""

import turtle

t = turtle.Pen()

win = turtle.Screen()
win.title("Koch Curve")
win.bgcolor("lightgreen")

t.width(2)
t.speed(0)


def koch(L, n):
    """ To draw a Koch curve. L = size(length), n = order(number of division)
    """

    if n == 0:
        t.fd(L)
    else:
        koch(L/3, n - 1)
        t.lt(60)
        koch(L/3, n - 1)
        t.rt(120)
        koch(L/3, n - 1)
        t.lt(60)
        koch(L/3, n - 1)


# lift the pen
t.up()
t.goto(-250, 0)
t.pd()

koch(700, 4)

t.ht()

turtle.mainloop()




