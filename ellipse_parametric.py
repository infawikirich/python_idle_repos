"""
Drawing an ellipse using a parametric equation
using turtle module

"""

import turtle, math
from turtle import *

speed(0)

# define the radius of the circle
r1 = 200
r2 = 300

# define the starting angle
startAngle = 0

# define the ending angle
endAngle = 2*math.pi

# define the number of steps
n = 500
step = startAngle

# create a list to hold the calculations
P_x = []
P_y = []

# set the for loop to calculate the points
for k in range(n):

    x = r1*math.cos(step)
    y = r2*math.sin(step)

    P_x.append(x)
    P_y.append(y)
    
    step += (endAngle - startAngle)/(n - 1)



up()
goto(r1, 0)
down()

for i in range(n):
    goto(P_x[i], P_y[i])


ht()
mainloop()
    
