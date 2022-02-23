"""
script file: quadrilateral.py

purpose: This program draws square, rectangle
         rhombus and parallelogram using turtle

author: Mr. Asiamah

date: 29/09/21

"""
import turtle
import turtle as t

turtle.delay(150)

t.penup()
t.goto(50, 50)

# square
t.pendown()
t.forward(150)
t.left(90)

t.forward(150)
t.left(90)

t.forward(150)
t.left(90)

t.forward(150)
t.left(90)

t.penup()
t.home()

# rectangle
t.goto(-50, 50)
t.down()
t.left(90)

t.fd(150)
t.lt(90)

t.fd(200)
t.lt(90)

t.fd(150)
t.lt(90)

t.fd(200)
t.lt(90)

t.penup()
t.home()










