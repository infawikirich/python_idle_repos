import turtle


t = turtle.Pen()
win = turtle.Screen()
win.bgcolor("lightgreen")
win.title("Colored Circle")
win.setup(800, 800)

#turtle.tracer(12)

t.speed(0)
t.width(2)


# first circle
t.pencolor("black")
t.fillcolor("black")
t.up()
t.sety(-200)
t.pd()
t.begin_fill()
t.circle(200)
t.end_fill()

# second circle
t.pencolor("navy")
t.fillcolor("navy")
t.up()
t.sety(-150)
t.pd()
t.begin_fill()
t.circle(150)
t.end_fill()

# second circle
t.pencolor("red")
t.fillcolor("red")
t.up()
t.sety(-100)
t.pd()
t.begin_fill()
t.circle(100)
t.end_fill()


# second circle
t.pencolor("yellow")
t.fillcolor("yellow")
t.up()
t.sety(-50)
t.pd()
t.begin_fill()
t.circle(50)
t.end_fill()

t.pencolor('black')
t.up()
t.goto(-150, 250)
t.pd()
t.write("Rings of Circle", font =("Times", 40, "bold"))


t.ht()
turtle.mainloop()




