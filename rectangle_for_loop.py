"""
    file  - rectangle.py

    purpose - This program uses turtle to draw a rectangle

    author  - Mr. Asiamah

    date    - 03/11/2021
     
"""

import turtle

t = turtle.Pen()

t.width(2)

#turtle.tracer(12)

 
for k in range(2):
    t.fd(200)
    t.lt(90)

    t.fd(100)
    t.lt(90)



t.ht()

turtle.mainloop()
