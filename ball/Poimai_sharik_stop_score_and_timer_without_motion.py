from random import randrange as rnd
from tkinter import *
from random import choice, randint
import math

import time
time_finish=time.time()+10

flag_t=0 # Флаг времени

def tick():
    global time_finish, time_str, time_ost_text,flag_t
    
    # Количество минут и секунд
    time_test=round(time_finish-time.time())
    # print('*',time_test)
    m=time_test//60
    s=time_test%60
    # print('Min: ',m,' Sec: ',s)
   
    # canv.create_text(50, 5, text=time_test)
    if time_test>=0:
        change_timer(m,s)
        delay=1000
        canv.after(delay,tick)
        # Конец блока минут и секунд
       
    if time_test <= 0:
        flag_t=1
        pass




root = Tk()
w=800
h=600
root.geometry("%dx%d" % (w, h))
canv = Canvas(root, bg = 'white')
canv.pack(fill = BOTH, expand = 1)

scores=0

# print('Где консоль?')
 
class ball():
    def __init__(self):
        x = self.x = 0
        y = self.y = 0
        r = self.r = 0
        self.nap = 0
        self.nx=0
        self.ny=0
        self.width = 0
        self.color = ''
        self.pen_color = ''
        self.id = canv.create_oval(x-r,y-r,x+r,y+r, width = self.width, fill = self.color, outline = self.pen_color )
 
    def paint(self):
        x = self.x
        y = self.y
        r = self.r
        canv.coords(self.id,x-r,y-r,x+r,y+r)
        canv.itemconfig (self.id, width = self.width, fill = self.color, outline = self.pen_color)
 
balls = []
# Создаем шарики!!!
for z in range(20):
    new_ball = ball()
    new_ball.x = rnd(50,w-50)
    new_ball.y = rnd(50,h-50)
    new_ball.r = rnd(10,50)
    new_ball.nap = rnd(1,4)
    if new_ball.nap==1:
        new_ball.nx=1
        new_ball.ny=1
    if new_ball.nap==2:
        new_ball.nx=1
        new_ball.ny=-1
    if new_ball.nap==3:
        new_ball.nx=-1
        new_ball.ny=-1
    else:
        new_ball.nx=-1
        new_ball.ny=1
        
    new_ball.color = choice(['aqua', 'blue', 'fuchsia', 'green', 'maroon', 'orange',
                  'pink', 'purple', 'red','yellow', 'violet', 'indigo', 'chartreuse', 'lime'])
    balls += [new_ball]

'''
for b in balls:
    print(b.id,b.nap,b.nx,b.ny)
'''

def create_timer():
    global time_str, time_ost_text, time_finish
    # Количество минут и секунд
    time_test=round(time_finish-time.time())
    m=time_test//60
    s=time_test%60       
    time_str='Мин: '+str(m)+' Сек: '+str(s)
    time_ost_text = canv.create_text(600, 30,
                                     text="Времечко " + time_str,
                                     font="Sans 18")

def change_timer(m,s):
    global time_ost_text
    time_str=str(m)+' мин. '+str(s)+' сек.'
    canv.itemconfigure(time_ost_text, text="Времечко: " + time_str)



def create_scores_text():
    global scores_text
    scores_text = canv.create_text(120, 30,
                                     text="Ваши очёчки: " + str(scores),
                                     font="Sans 18")

def change_scores_text():
    canv.itemconfigure(scores_text, text="Ваши очёчки: " + str(scores))
 
for b in balls:
    b.paint()
    # print(b.id)

def click_ball(event):
    global scores, w, h, balls, flag_t
    """ Обработчик событий мышки для игрового холста canvas
    param event: событие с координатами клика
    По клику мышкой нужно удалять тот объект, на который мышка указывает.
    А также засчитываеть его в очки пользователя.
    """
    obj = canv.find_closest(event.x, event.y)
    try:
        x1, y1, x2, y2 = canv.coords(obj)
        radius=math.sqrt((x2-x1)**2+(y2-y1)**2)/2
        # print(radius)
        delta_scores=int(100/radius)
    except:
        x1,y1,x2,y2=0,0,0,0
        
    
    if x1 <= event.x <= x2 and y1 <= event.y <= y2 and flag_t==0: # Блок на возрастание очков при времени =0
        scores+=delta_scores
        # print(scores)
        change_scores_text()
        canv.delete(obj)
        # balls.remove(obj)
        # Создаем новый шарик
        new_ball = ball()
        new_ball.x = rnd(50,w-50)
        new_ball.y = rnd(50,h-50)
        new_ball.r = rnd(10,50)
        new_ball.nap = rnd(1,4)
        new_ball.nx = 1
        new_ball.ny = 1
        new_ball.color = choice(['aqua', 'blue', 'fuchsia', 'green', 'maroon', 'orange',
                  'pink', 'purple', 'red','yellow', 'violet', 'indigo', 'chartreuse', 'lime'])
        balls += [new_ball]
        b.paint()
        # balls += [new_ball]
        # print(balls)


def time_event():
    global balls, w,h
    # print('*')
    """ передвигает все шарики на чуть-чуть """
    for b in balls:
        if b.nx==1 and b.ny == 1:
            dx = 1
            dy = 1
        elif b.nx==-1 and b.ny == 1:
            dx = -1
            dy = 1
        elif b.nx==1 and b.ny == -1:
            dx = 1
            dy = -1
        else:
            dx = -1
            dy = -1
            
        # Двигаем шарики
        b.x=b.x+dx
        b.y=b.y+dy
        if b.x>w-b.r:
            #print('Выход из окна вправо')
            b.nx=-1
        if b.x<b.r:
            #print('Выход из окна влево')
            b.nx=1
        if b.y>h-b.r:
            b.ny=-1
            #print('Выход из окна вниз')
        if b.y<b.r:
            #print('Выход из окна вверх')
            b.ny=1

         # Перерисовка шариков   
        b.paint()
    if flag_t==0:
        canv.after(10, time_event) # Двигае шыры при наличии времени
         
create_scores_text()
create_timer()
delay=1000
canv.after(delay,tick)
# print('***')
time_event()

canv.bind("<Button>", click_ball)
# canv.bind("<Motion>", move_all_balls)
# canv.bind("<FocusIn>", move_all_balls)

mainloop()
