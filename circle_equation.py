"""
Script file: circle_equation

Purpose: This program uses the equation x = radius*math.cos(t) and y =
        radius*math.sin(t)


Author: Mr. Asiamah

Date: 09/09/21


"""
import turtle, math
from turtle import *


win = turtle.Screen()
win.title('Circle')
win.bgcolor('lightgreen')

speed(0)



# ask the user the enter the radius
radius = numinput("Radius of Circle", "Enter the radius of the circle")


n = 500 # number of points on each ellipse
# X, Y is the cne center of the circle
# P is the list of coordinates of the points on the ellipse
# ts is the starting angle, te is the ending angle

def drawCircle(X, Y, ts, te, radius, P):
    t = ts
    up()

    for i in range(n):
        x = radius*math.cos(t)
        y = radius*math.sin(t)
        P.append((x + X, y + Y))
        goto(x + X, y + Y)
        down()

        t += (te - ts)/(n-1)
P = []      # starting from the empty list


drawCircle(0, 0, 0, math.pi, radius, P)         # taller top half
drawCircle(0, 0, 0, 2*math.pi, radius, P)         # taller top half

    


done()
mainloop()







