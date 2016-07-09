from turtle import Turtle
default_scale = 1
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
    global _drawman_scale
    ''' Масштаб '''
    global _drawman_scale
    _drawman_scale = scale

def test_drawman():
    """
    Тестирование работы Чертёжника
    """
    novid()
    col()
    size()
    axis()
    grid()
    edin()

    pen_down()
    '''
    for i in range(5):
        # Пила, карочь
        on_vector(10, 20)
        on_vector(0, -20)
    '''
    col('black')
    # График функции
    col('lightblue')
    pen_width(wid=3)
    x = -5.0
    scale=shag/vod
    xe=x*scale
    pen_up()
    y=x*x
    ye=y*scale
    to_point(xe, ye)
    pen_down()
    while x <= 5:
        x += 0.2
        xe=x*scale
        y=x*x
        ye=y*scale
        to_point(xe,ye)
        
    pen_up()

    # Возврат в начало
    to_point(0, 0)

def novid():
    global t
    t.hideturtle()

def vid():
    global t
    t.showtirtle()

def pen_down():
    global t
    t.pendown()

def pen_up():
    global t
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
     '''Размеры холста'''
     global t,w,h, _drawman_scale,shag, vod
     shag=50
     vod=0.5 # Сколько в одном делении
     w=20*shag
     h=20*shag
     t.screen.screensize(w,h)

def pen_width(wid=2):
    '''Ширина пера'''
    global t
    t.width(wid)

def axis():
    global t,w,h,_drawman_scale,vod
    pass
    t.speed(10)
    # t.turtlesize(2)
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
    y=-10*shag
    coords=" "+str(x)+", "+str(-10*vod)
    t.goto(x, y)
    t.write(coords)

#    Начинаем оси рисовать
    t.down()
    x=0
    y=10*shag
    coords=str(x)+", "+str(10*vod)
    t.goto(x, y-shag/2)
    t.left(90)
    t.stamp()
    t.right(90)
    t.write(coords)
#
    t.up()
    x=-10*shag
    y=0
    coords=str(-10*vod)+", "+str(y)
    t.goto(x, y)
    t.write(coords)
#
    t.down()
    x=10*shag
    y=0
    coords=str(10*vod)+", "+str(y)
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
    # shag=50*_drawman_scale
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
    # col('lightngray')
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
    global t,w,h,_drawman_scale,shag,vod
    # print ('Вошли в шаг')
    t.color('#000000')
    t.up()
    #edin=shag # Единичный отрезок типо
    x=shag
    y=0
    coords=" "+str(vod)
    t.goto(shag, y)
    # t.down()
    t.write(coords)
    x=0
    y=shag
    coords="  "+str(vod)
    t.goto(x, shag)
    t.write(coords)



init_drawman()
if __name__ == '__main__':
    import time # Отсюда вынимаем sleep(sec.)
    '''  Вызываем функцию тестирования чертежника в главно модуле '''
    test_drawman()
    # t.mainloop()
    time.sleep(8)
