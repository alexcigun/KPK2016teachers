from tkinter import *
from random import choice, randint as rnd

import time
from math import sin, cos, pi

class Gun:
    
    def __init__(self,canvas,v0,tetta,width=30):
        global x_vyl,y_vyl 
         # сразу задаёмся радианами
        rad=180/pi
        tetta_r=tetta/rad # вместо градусов получили количество радиан     
        self.canvas = canvas
        length=v0
        dx=length*cos(tetta_r)
        dy=length*sin(tetta_r)
        self.w=width
        self.id = canvas.create_line(50,550,50+dx,550-dy,width=self.w,fill='black')
        x_vyl=50+dx
        y_vyl=550-dy
        
    

class Ball:
    def __init__(self,canvas,r,color,x=100,y=300):
        self.canvas = canvas
        self.x=x
        self.y=y
        self.r=r
        self.color=color
        self.id = canvas.create_oval(self.x-r,self.y-r,self.x+r,self.y+r, fill=self.color)

class Target:
     def __init__(self,canvas):
        self.canvas = canvas
        self.x = rnd(700,1000-100)
        self.y = rnd(100,500)
        self.r = rnd(10,50)
        self.popali=0
        self.id = canvas.create_oval(self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r, fill='grey')
                                     
def popadalka(a,targets):
    pass
    for t in targets:
        if abs(a.x - t.x) <= (a.r + t.r) and abs(a.y - t.y) <= (a.r + t.r) and t.popali==0:
            print('Попадание!')
            t.popali=1
            canvas.delete(t.id)
        
            # print(t.id,t.x,t.y,t.r,sep='  ')
            # print(a.id,a.x,a.y,a.r,sep='--')

def snaryad(tetta=45,v0=100):
    global x_vyl,y_vyl 
    # задаёмся переменными
    x0=x_vyl    # координата х
    # tetta=60 # начальный угол 
    g=9.81   # ускорение свободного падения (м/с**2), можно подставить значение и для Луны
    # v0=100   # начальная скорость (м/с), типовая скорость снаряда
    y0=y_vyl # начальная вертикальная координата 
 
    # сразу задаёмся радианами
    rad=180/pi
    tetta_r=tetta/rad # вместо градусов получили количество радиан     
    a=Ball(canvas,15,'red',x0,y0)
    t=0
    x=x0+a.r
    while x<1000+a.r:
        v0x=v0*cos(tetta_r)
        v0y=v0*sin(tetta_r)
        sx=v0x*t
        sy=-v0y*t+(g*t**2)/2
        x=x0+sx
        y=y0+sy

        # - Сравнение x, y снаряда - с коор оставшихся мишеней
        popadalka(a,targets)
        # -----------------------------------------------------
        obj=a.id
        try:
            canvas.delete(obj)
            col='red'
            a = Ball(canvas,15,col,x,y)
            tk.update_idletasks()
            tk.update()
        except:
            pass
        t+=0.5
        time.sleep(0.1)


def speed_up(event):
    global v0,tetta,our_gun
    pass
    if v0<200:
        v0+=5
    # print('speed rise')
    # изменяем пушку
    canvas.delete(our_gun.id)
    our_gun=Gun(canvas,v0,tetta,width)


def speed_down(event):
    global v0,tetta,our_gun
    pass
    if v0>50:
        v0-=5
    # print('speed down')
    # изменяем пушку
    canvas.delete(our_gun.id)
    our_gun=Gun(canvas,v0,tetta,width)
    

def ugol_down(event):
    global v0,tetta,our_gun
    pass
    if tetta>0:
        tetta-=5
    # print('Угол: ',tetta)
    # изменяем пушку
    canvas.delete(our_gun.id)
    our_gun=Gun(canvas,v0,tetta,width)


def ugol_up(event):
    global v0,tetta,our_gun
    pass
    if tetta<90:
        tetta+=5
    # print('Угол: ',tetta)
    # изменяем пушку
    canvas.delete(our_gun.id)
    our_gun=Gun(canvas,v0,tetta,width)
    
def babah(event):
    global tetta,v0
    snaryad(tetta,v0)

if __name__=='__main__':
    tk = Tk()
    tk.title("Game")
    tk.resizable(0, 0)
    tk.wm_attributes("-topmost", 1)
    w=1000
    h=600
    canvas = Canvas(tk, width=w, height=h, bd=0, highlightthickness=0)
    canvas.pack()
    v0=100   # начальная скорость (м/с), типовая скорость снаряда
    tetta=45 # начальный угол
    width=30
    # Рисуем пушку
    # self,canvas,v0,tetta,width=30
    our_gun=Gun(canvas,v0,tetta,width)
    # Расставляем случайно мишени
    targets_count=rnd(2,6)
    targets=[]
    for i in range(targets_count):
        t=Target(canvas)
        targets.append(t)
    tk.update()                                     
    
    # Запускаем снаряд
    
    tk.bind('<Up>',ugol_up)
    tk.bind('<Down>',ugol_down)
    tk.bind('<Right>',speed_up)
    tk.bind('<Left>',speed_down)
    tk.bind('<space>',babah)
    
    


    
