from tkinter import *
from random import choice, randint as rnd

import time
from math import sin, cos, pi

class Gun:
    def __init__(self,canvas,width=30,x=100,y=500):
        self.canvas = canvas
        self.x=x
        self.y=y
        self.w=width
        self.id = canvas.create_line(30,570,self.x,self.y,width=self.w,fill='black')
    

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
        self.id = canvas.create_oval(self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r, fill='grey')
                                     
               


def snaryad(tetta=45,v0=100):
    # задаёмся переменными
    x0=100    # координата х
    # tetta=60 # начальный угол 
    g=9.81   # ускорение свободного падения (м/с**2), можно подставить значение и для Луны
    # v0=100   # начальная скорость (м/с), типовая скорость снаряда
    y0=500   # начальная вертикальная координата 
 
    # сразу задаёмся радианами
    rad=180/pi
    tetta_r=tetta/rad # вместо градусов получили количество радиан     
    a=Ball(canvas,15,'red',x0,y0)
    t=0
    x=50
    while x<1000+a.r:
        v0x=v0*cos(tetta_r)
        v0y=v0*sin(tetta_r)
        sx=v0x*t
        sy=-v0y*t+(g*t**2)/2
        x=x0+sx
        y=y0+sy
        # --- Сравнение x y снаряда --- с коор каждой оставшейся мишени
        # ---------------------------
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
        time.sleep(0.3)

if __name__=='__main__':
    tk = Tk()
    tk.title("Game")
    tk.resizable(0, 0)
    tk.wm_attributes("-topmost", 1)
    canvas = Canvas(tk, width=1000, height=600, bd=0, highlightthickness=0)
    canvas.pack()
    # Рисуем пушку
    our_gun=Gun(canvas)
    # Расставляем случайно мишени
    targets_count=rnd(2,6)
    targets=[]
    for i in range(targets_count):
        t=Target(canvas)
        targets.append(t)
    tk.update()                                     
    v0=100   # начальная скорость (м/с), типовая скорость снаряда
    tetta=60 # начальный угол
    # Запускаем снаряд
    snaryad(tetta,v0)
