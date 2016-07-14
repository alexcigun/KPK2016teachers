import turtle
from math import sin

t = turtle.Turtle()
# t.shape("turtle")
t.color("darkgreen", "yellow")
t.shapesize(2)
t.speed(5)

def main():
    t.penup()
    t.backward(200)

    digit_one(50)
    t.forward(60)
    digit_two(50)
    t.forward(60)
    digit_three(50)
    t.forward(60)
    digit_four(50)
    t.forward(30)
    digit_five(50)
   # t.forward(60)
    # t.hideturtle()

    

def digit_one(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    t.penup()
    t.forward(length/2)
    t.pendown()
    t.left(90)
    t.forward(length)
    t.left(90+45)
    t.forward(length*sin(45*3.141592/180))
    #обратный ход
    t.backward(length*sin(45*3.141592/180))
    t.right(90+45)
    t.backward(length)
    t.right(90)
    t.penup()

def digit_two(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L1 = length/2
    L2 = (length/2)*2**0.5
    B = [180, -135, 45, 90]
    A = [ L1,   L2, L1, L1]
    

    t.penup()
    t.forward(L1)
    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)
    t.penup()
   
def digit_three(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L1 = length/2
    L2 = (length/2)*2**0.5
    
    B = [-135, 135, -135,135]
    A = [L2, L1, L2, L1]
    

    t.penup()
    t.left(-180)
    t.pendown()

    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)
    t.penup()
    t.left(180)
    t.forward(length)
   
def digit_four(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L1 = length/2
    L2 = (length/2)*2**0.5

    B = [90, 180, -90,-90]
    A = [length, L1, L1, L1]
    
    
    t.penup()
    #t.left(-180)
    t.pendown()

    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)
    t.penup()
    # t.left(180)
    t.forward(L2)
   
def digit_five(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L1 = length/2
    L2 = (length/2)*2**0.5

    B = [0, 90, 90, -90, -90]
    A = [L1, L1, L1, L1, L1]
    

    t.penup()
    #t.left(-180)
    t.pendown()

    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)
    t.penup()
    # t.left(180)
    t.forward(L2)
   


main()

#t.left(30)
#t.right(30)
#t.forward(200)
#t.backward(200)
#t.penup()
#t.pendown()
#t.begin_fill()
#t.end_fill()
