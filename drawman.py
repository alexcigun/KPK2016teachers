from turtle import Turtle
default_scale = 5

def init_drawman():
    ''' Инициализация черепашки '''
    global t, x_current, y_current, _drawman_scale
    t = Turtle()
    t.penup()
    x_current = 0
    y_current = 0
    t.goto(x_current, y_current)
    drawman_scale(default_scale)

def drawman_scale(scale):
    ''' Масштаб '''
    global _drawman_scale
    _drawman_scale = scale

def test_drawman():
    """
    Тестирование работы Чертёжника
    """
    col()
    size()
    axis()
    grid()
    edin()

    # pen_down()
    '''
    for i in range(5):
        # Пила, карочь
        on_vector(10, 20)
        on_vector(0, -20)
    '''
    # pen_up()

    # Возврат в начало
    to_point(0, 0)

def pen_down():
    t.pendown()

def pen_up():
    t.penup()

def on_vector(dx, dy):
    ''' Сместиться на вектор '''
    to_point(x_current + _drawman_scale*dx, y_current + _drawman_scale*dy)

def to_point(x, y):
    ''' Сместиться в точку с учетом масштаба '''
    global x_current, y_current
    x_current = x
    y_current = y
    t.goto(_drawman_scale*x_current, _drawman_scale*y_current)

def col(c='red'):
    ''' Цвет'''
    global t
    t.pencolor(c)

def size():
     global t,w,h, _drawman_scale
     w=600*_drawman_scale
     h=400*_drawman_scale
     t.screen.screensize(w,h)

def pen_width(w=2):
    global t
    t.width(w)

def axis():
     global t,w,h,_drawman_scale
     pass
     t.turtlesize(2)
    # Вертикальные линии
     t.width(3)
     t.home()

    # Горизонтальные линии
     # t.reset()
     # t.tracer(0)
     t.color('#000000')
#
     t.write('  0,0')
#
     x=0
     y=-h/2
     coords=" "+str(x)+", "+str(y)
     t.goto(x, y)
     t.write(coords)

#    Начинаем оси рисовать
     t.down()
     x=0
     y=h/2
     coords=str(x)+", "+str(y)
     t.goto(x, y)
     t.left(90)
     t.stamp()
     t.right(90)
     t.write(coords)
#
     t.up()
     x=-w/2
     y=0
     coords=str(x)+", "+str(y)
     t.goto(x, y)
     t.write(coords)
#
     t.down()
     x=w/2
     y=0
     coords=str(x)+", "+str(y)
     t.goto(x, y)

     t.stamp()
     t.write(coords)
#
def grid():
     global t,w,h,_drawman_scale,shag
     pass
     t.width(1)
     t.speed(10)
     # Вертикальные линии
     shag=50*_drawman_scale
     x=-w/2
     y=h/2
     col('gray')
     while x<=w/2:
         t.up()
         t.goto(x,y)
         t.down()
         if x!=0:
             t.goto(x,-h/2)
         x+=shag
     else:
         t.up()

     # Горизонтальные линии
     x=-w/2
     y=h/2
     # col('gray')
     while y>=-h/2:
         t.up()
         t.goto(x,y)
         t.down()
         if y!=0:
             t.goto(w/2,y)
         y-=shag
     else:
         t.up()

def edin():
    global t,w,h,_drawman_scale,shag
    # print ('Вошли в шаг')
    t.color('#000000')
    t.up()
    x=shag
    y=0
    coords=" "+str(x)
    t.goto(x, y)
    # t.down()
    t.write(coords)
    x=0
    y=shag
    coords=" "+str(y)
    t.goto(x, y)
    t.write(coords)


init_drawman()
if __name__ == '__main__':
    import time # Отсюда вынимаем sleep(sec.)
    '''  Вызываем функцию тестирования чертежника в главно модуле '''
    test_drawman()
    time.sleep(3)
