"""
 script file: tracer_python.py

 purpose: This program makes of turtle tracer method
           instead of t.speed

 author: Mr. Asiamah

 Date: 30/08/21
"""

import turtle
import random

# create a turtle object
t = turtle.Turtle()

# create a screen object
win = turtle.Screen()


# set the background color of the canvas
win.bgcolor('lightgreen')
win.title('Using turtle Tracer method')
win.setup(width = 800, height = 500)


turtle.colormode(255)

turtle.tracer(10)
#t.speed(0)

a = random.randint(5, 30)
b = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


for i in range(1, 100):
    t.ht()
    t.dot(a, b)
    t.pu()
    t.setx(random.randint(-390, 390))
    t.sety(random.randint(-240, 240))
    t.pd()
    a = random.randint(5, 30)
    b = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))















    

