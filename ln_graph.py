"""
 script file: tracer_python.py

 purpose: This program plots the graph of 1/x**2
 author: Mr. Asiamah

 Date: 30/08/21
"""

import turtle
import math

t = turtle.Turtle()

win = turtle.Screen()
win.setup(800, 500)

x_points = []
y_points = []

x_initial = 2
x_final = 399

n = 500

steps = (x_final - x_initial)/n

#Calculate thx values
for k in range(1000):
    x_initial += steps
    x_points.append(x_initial)

    
#Calculate thx values
for k in range(1000):
    y_points.append(50*math.log10(x_points[k]))
    
    
#t.up()
#t.goto(x_initial, math.log(x_initial))


t.down()
       
for k in range(1000):
    t.goto(x_points[k], y_points[k])




