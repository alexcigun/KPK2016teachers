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
        self.r = choice([10,20,30,40,50])
        slovar={'10':5,'20':4,'30':3,'40':2,'50':1}
        # self.score = self.r//10
        self.score=slovar[str(self.r)]
        self.popali=0
        self.id = canvas.create_oval(self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r, fill='grey')
        self.score_text = canvas.create_text(self.x,self.y,text=self.score)
                                     
def popadalka(targets):
    global score_all,kv,a
    pass
    for t in targets:
        if abs(a.x - t.x) <= (a.r + t.r) and abs(a.y - t.y) <= (a.r + t.r) and t.popali==0:
            print('Попадание!')
            t.popali=1
            print('+Очков: ', t.score)
            score_all+=t.score
            print('Всего очков: ',score_all )
            canvas.delete(t.score_text)
            canvas.delete(t.id)
            # Удаляем снаряд
            canvas.delete(a.id)
            # Изменяем очки
            ochki='Количество очков: '+str(score_all)+'     '
            label1.config(text=ochki,font='Sans 16 italic',fg='grey')
            label1.pack(side=LEFT)
            # выводим цену выcтрела
            ko=score_all
            cv=ko/kv
            print('Цена выстрела: ',cv,'Очки: ',ko,'Выстрелы: ',kv)
            cena_v='Цена выстрела: '+str(cv)[0:5]
            label3.config(text=cena_v,font='Sans 16 italic',fg='red')
            # ---------------------------------------------
       
                
def snaryad(tetta=45,v0=100):
    global x_vyl,y_vyl,kv,score_all,a
    # + 1 выстрел
    kv+=1
    # выводим цену выcтрела
    ko=score_all # наплодил сдуру сущностей одинаковых
    cv=ko/kv
    print('Цена выстрела: ',cv,'Очки: ',ko,'Выстрелы: ',kv)
    cena_v='Цена выстрела: '+str(cv)[0:5]
    label3.config(text=cena_v,font='Sans 16 italic',fg='red')
    # ---------------------------------------------
    print('Количество выстрелов: ',kv)
    vystrely='     Количество выстрелов: '+str(kv)
    label2.config(text=vystrely,font='Sans 16 italic',fg='grey')
    label2.pack(side=RIGHT)
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
        popadalka(targets)
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
        if t==2:
              canvas.delete(a.id)


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
    score_all=0
    tk = Tk()
    tk.title("Game")
    tk.resizable(0, 0)
    tk.wm_attributes("-topmost", 1)
    w=1000
    h=600
    # Метка с очками и выстрелами
    ko=0 # Количество очков
    kv=0 # Количество выстрелов
    cv=0 # Цена выстрела
    canvas_top = Canvas(tk, width=w, height=h, bd=0, highlightthickness=0)
    canvas_top.pack()

    ochki='Количество очков: '+str(ko)+'     '
    label1=Label(canvas_top,text=ochki)
    label1.config(font='Sans 14 italic',fg='grey')
    label1.pack(side=LEFT)

    vystrely='     Количество выстрелов: '+str(kv)
    label2=Label(canvas_top,text=vystrely)
    label2.config(font='Sans 14 italic',fg='grey')
    label2.pack(side=RIGHT)

    cena_v='Цена выстрела: '+str(cv)
    label3=Label(canvas_top,text=cena_v)
    label3.config(font='Sans 14 italic',fg='red')
    label3.pack(side=TOP)

    # ---------------------------------------------------------------
    canvas = Canvas(tk, width=w, height=h, bd=0, highlightthickness=0)
    canvas.pack()
    v0=100   # начальная скорость (м/с), типовая скорость снаряда
    tetta=45 # начальный угол
    width=30
    # Рисуем пушку
    # self,canvas,v0,tetta,width=30
 
    
    
    # ----------------------------
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
    
    tk.mainloop()
    


    
