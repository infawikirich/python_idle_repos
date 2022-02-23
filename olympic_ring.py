"""
 file : olympic_ring.py

 purpose: This program uses turtle to draw an olympic ring logo

 author: Mr. Asiamah

 date: 27/10/21

"""

import turtle

t = turtle.Pen()

win = turtle.Screen()
win.setup(800, 700)
win.bgcolor("teal")

t.width(20)

t.up()
t.setx(-300)
t.down()

# draw the first circle with a radius of 125
t.pencolor("blue")
t.circle(125)


t.up()
t.home()
t.down()

# draw the second circle with a radius of 125
t.pencolor('black')
t.circle(125)


t.up()
t.setx(300)
t.down()

# draw the third circle with a radius of 125
t.pencolor("red")
t.circle(125)


t.up()
t.goto(-150, -100)
t.down()

# draw the fourth circle with a radius of 125
t.pencolor("yellow")
t.circle(125)


t.up()
t.goto(150, -100)
t.down()

# draw the fifthe circle with a radius of 125
t.pencolor("green")
t.circle(125)


t.ht()

turtle.mainloop()












