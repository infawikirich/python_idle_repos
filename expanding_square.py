import turtle

t = turtle.Turtle()

win = turtle.Screen()
win.setup(800, 600)
win.title('Expanding square')
win.bgcolor('lightgreen')


def square(size, x, y):
    t.width(3)
    t.color('red')
    
    for k in range(4):
        t.fd(size)
        t.lt(90)
    t.pu()
    t.goto(x, y)
    t.pd()
    
        

size = 50
x, y = 12, 12
for k in range(1,20):
    square(size, -x*k, -y*k)
    size += abs(-x-y)


t.ht()
turtle.done()
    
