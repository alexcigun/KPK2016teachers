from turtle import Turtle
import time

def init_drawman():
    global t, x_current,y_current
    t = Turtle()
    t.penup()
    x_current = 0
    y_current = 0
    t.goto(x_current,y_current)

def test_drawman():
    pen_up()
    to_point(-300,0)
    pen_down()
    for i in range(5):
        on_vector(100,200)
        on_vector(50,-200)
    pen_up()
    to_point(0,0)

def pen_down():
    t.pendown()
    pass

def pen_up():
    t.penup()
    pass

def on_vector(dx,dy):
    global t, x_current,y_current
    x_current +=dx
    y_current +=dy
    t.goto(x_current,y_current)
    pass

def to_point(x,y):
    global x_current, y_current
    pass
    x_current = x
    y_current = y
    t.goto(x_current,y_current)

init_drawman()
if  __name__=='__main__':
    test_drawman()
    # time.sleep(10)
