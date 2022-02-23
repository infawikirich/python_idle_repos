import turtle

t = turtle.getturtle()

win = turtle.getscreen()
win.title('Recursive triangle')
win.bgcolor('lightgreen')
win.setup(800, 600)

t.speed(0)
print(turtle.window_width(), turtle.window_height())
turtle.setworldcoordinates(0, 0, turtle.window_width()/2, turtle.window_height()/2)

def triangle(sides, n):
    if n == 0:
        return None
            
    t.fd(sides)
    t.lt(120)
    sides += 10
    t.width((sides+1)/150)

    triangle(sides, n-1)
    
    


triangle(50, 100)

t.ht()
turtle.mainloop()
    
    
    
    



