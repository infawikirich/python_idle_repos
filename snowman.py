import turtle

t = turtle.Pen()

t.speed(1)

win = turtle.Screen()
win.bgcolor('lightgreen')

t.width(2)

# hat of snowman
t.up()
t.goto(0, 200)

t.color('black')
t.begin_fill()

t.pd()
t.fd(75)
t.lt(90)
t.fd(50)
t.lt(90)
t.fd(25)
t.rt(90)
t.fd(100)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(100)
t.rt(90)
t.fd(25)
t.lt(90)
t.fd(50)
t.lt(90)
t.fd(75)

t.end_fill()

# first circle
t.up()
t.goto(0, 120)
t.pd()
t.circle(50)

# second circle
t.circle(-75)

# third circle
t.up()
t.goto(0,-30)
t.pd()
t.circle(-150)


# draw the eyes
t.up()
t.goto(-25, 175)
t.pd()
t.circle(10)

t.up()
t.goto(25, 175)
t.pd()
t.circle(10)

# draw the mouth
t.up()
t.goto(25, 160)
t.pd()
t.fd(-50)





t.ht()
turtle.mainloop()
