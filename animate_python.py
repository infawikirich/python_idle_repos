"""
script file: animate_python.py

purpose: This program animate various movement in
         turtle programming

author: Mr. Asiamah

date: 31/08/21
"""


import turtle

t = turtle.Turtle()

win = turtle.Screen()
win.setup(800, 540)
win.bgcolor('lightgreen')


t.turtlesize(5, 5, 3)


turtle.delay(500)
t.fd(200)
t.lt(90)
