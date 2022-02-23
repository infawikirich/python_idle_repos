



import turtle
import random


turtle.speed(0)
#turtle.tracer(12)

def wander():
    while True:
        turtle.fd(5)
        
        if turtle.xcor() >= 200 or turtle.xcor() <= -200 or turtle.ycor() <= -200 or turtle.ycor() >= 200:
            turtle.lt(random.randint(0, 90))



wander()
