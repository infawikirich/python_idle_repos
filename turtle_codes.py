from turtle import *
import math

win = Screen()
win.setup(600, 540)
win.bgcolor((0, 0, 0))
win.title('Return Turtle')



# don't let turtle draw
up()
shape('turtle')
turtlesize(5, 5, 3)

#Take input from the user
num = float(numinput("Distance", "Enter the distance"))

# get the coordinates
x_positive, x_negative = math.floor(window_width()/2), math.ceil(-window_width()/2)

while num != 0:
    fd(num)
    if xcor() > x_positive():
        fd(-num)
    else:
        fd(-num)
        
    

mainloop()
