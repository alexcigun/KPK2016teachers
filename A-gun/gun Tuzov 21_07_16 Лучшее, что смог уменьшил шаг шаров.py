from tkinter import *
from random import choice, randint
import math

screen_width = 1000
screen_height = 600
timer_delay = 20


class Ball:
    initial_number = 20
    minimal_radius = 15
    maximal_radius = 40
    available_colors = ['green', 'blue', 'red']

    def __init__(self):
        """
        Cоздаёт шарик в случайном месте игрового холста canvas,
        при этом шарик не выходит за границы холста!
        """
        R = randint(Ball.minimal_radius, Ball.maximal_radius)
        x = randint(0, screen_width-1-2*R)
        y = randint(0, screen_height-1-2*R)
        self._R = R
        self._x = x
        self._y = y
        fillcolor = choice(Ball.available_colors)
        self._avatar = canvas.create_oval(x, y, x+2*R, y+2*R,
                                          width=1, fill=fillcolor,
                                          outline=fillcolor)
        self._Vx = randint(-1, +1)
        self._Vy = randint(-1, +1)

    def fly(self):
        self._x += self._Vx
        self._y += self._Vy
        # отбивается от горизонтальных стенок
        if self._x < 0:
            self._x = 0
            self._Vx = -self._Vx
        elif self._x + 2*self._R >= screen_width:
            self._x = screen_width - 2*self._R -1
            self._Vx = -self._Vx
        # отбивается от вертикальных стенок
        if self._y < 0:
            self._y = 0
            self._Vy = -self._Vy
        elif self._y + 2*self._R >= screen_height:
            self._y = screen_height - 2*self._R - 1
            self._Vy = -self._Vy

        canvas.coords(self._avatar, self._x, self._y,
                      self._x + 2*self._R, self._y + 2*self._R)


class Ball_shell:
  
    available_colors = ['green', 'blue', 'red']

    def __init__(self):
        """
        Cоздаёт шарик в случайном месте игрового холста canvas,
        при этом шарик не выходит за границы холста!
        """
        R = 0
        x = 0
        y = 0
        self._R = R
        self._x = x
        self._y = y
        fillcolor = choice(Ball_shell.available_colors)
        self._avatar = canvas.create_oval(x, y, x+2*R, y+2*R,
                                          width=1, fill=fillcolor,
                                          outline=fillcolor)
        self._Vx = randint(-2, +2)
        self._Vy = randint(-2, +2)


class Gun:
    def __init__(self):
        ''' Вход  '''
        self._x = 0
        self._y = screen_height+2 # подправил
        self._tetta_g=80 # Угол наклона пушки
        tetta_g=self._tetta_g
        rad=180/math.pi
        tetta_r=tetta_g/rad # вместо градусов получили количество радиан    
        self._l=100 # Cкорость вылета снаряда
        self._lx =self._l* math.cos(tetta_r)
        self._ly =-self._l* math.sin(tetta_r)
        
        self._avatar = canvas.create_line(self._x, self._y,
                                          self._x+self._lx,
                                          self._y+self._ly,
                                          width=20)

    def shoot(self):
        """
        :return возвращает объект снаряда (класса Ball_shell)
        """
        shell = Ball_shell() # Создаем объект
        shell._R = 5
        shell._t=0
        shell._x0 = self._x - shell._R + self._lx # исправил
        shell._y0= self._y - shell._R + self._ly  # исправил
        shell._tetta_g=self._tetta_g # под каким углом станряд вылетел из пушки!!!
        # print('Создали снаряд')
        return shell


    def speed_up(self,event):
        ''' Увеличиваем нач. скорость снаряда'''
        print('Увеличиваем скорость')
        if self._l<200:
            self._l+=5
        # self._tetta_g=80 # Угол наклона пушки
        tetta_g=self._tetta_g
        rad=180/math.pi
        tetta_r=tetta_g/rad # вместо градусов получили количество радиан  
        self._lx =self._l* math.cos(tetta_r)
        self._ly =-self._l* math.sin(tetta_r)    
        canvas.coords(self._avatar,self._x, self._y,
                      self._x+self._lx,self._y+self._ly,)
        
        
    def speed_down(self,event):
        ''' Уменьшаем нач. скорость снаряда'''
       
        print('Уменьшаем скорость')
        if self._l>50:
            self._l-=5
        
        # self._tetta_g=80 # Угол наклона пушки
        tetta_g=self._tetta_g
        rad=180/math.pi
        tetta_r=tetta_g/rad # вместо градусов получили количество радиан  
        self._lx =self._l* math.cos(tetta_r)
        self._ly =-self._l* math.sin(tetta_r)    
        canvas.coords(self._avatar,self._x, self._y,
                      self._x+self._lx,self._y+self._ly,)

    def change_tetta(self,event):
        ''' Поворачивам пушку '''
        #print('Поворачиваем пушку')
        #print('x=',event.x,' y=',screen_height-event.y)
        # self._tetta_g=80 # Угол наклона пушки
        tetta_r=math.atan((screen_height-event.y)/event.x)
        # print('Угол в радианах: ',tetta_r)
        self._tetta_g=180*tetta_r/math.pi
        self._lx =self._l* math.cos(tetta_r)
        self._ly =-self._l* math.sin(tetta_r)    
        canvas.coords(self._avatar,self._x, self._y,
                      self._x+self._lx,self._y+self._ly,)
        
        
def init_game():
    global tetta_r
    """
    Создаём необходимое для игры количество объектов-шариков,
    а также объект - пушку.
    """
    global balls, gun, shells_on_fly
    balls = [Ball() for i in range(Ball.initial_number)]
    gun = Gun()
    shells_on_fly = []
    #tetta_r=math.tan(abs(gun._lx)/abs(gun._ly))
    print('Up key')
    root.bind('<Up>',gun.speed_up)
    print('Down key')
    root.bind('<Down>',gun.speed_down)
    canvas.bind('<Motion>',gun.change_tetta)
    

def init_main_window():
    global root, canvas, scores_value,scores_label
    root = Tk()
    root.title("Пушка")

    scores_label=Label(root,text='Ваши очёчки: ')
    scores_value=0
    
    canvas = Canvas(root, width=screen_width, height=screen_height, bg="white")
    
    canvas.grid(row=1, column=0, columnspan=3)
    scores_label.grid(row=0, column=2)

    canvas.bind('<Button-1>', click_event_handler)
  

def check_for_hit():
    global scores_value,scores_label
    ''' Проверка на попадание '''
    pass
    shell_del=[] # Список номеров удаляемых снарядов
    ball_del=[]  # Список номеров удаляемых шаров
    # Обход по спискам шаров и снарядов
    for i in range(len(shells_on_fly)):
        flag=0
        for j in range(len(balls)):
            if abs(shells_on_fly[i]._x - balls[j]._x) <= (shells_on_fly[i]._R + balls[j]._R)\
                and  abs(shells_on_fly[i]._y - balls[j]._y) <= (shells_on_fly[i]._R + balls[j]._R):
                # print('Попали')
                scores_value+=1
                scores_label.config(text='Ваши очёчки: '+str(scores_value))
                canvas.delete(balls[j]._avatar)   # Удаляем аватары шаров
                balls.pop(j)
                canvas.delete(shells_on_fly[i]._avatar)  # Удаляем аватары снарядофф
                shells_on_fly.pop(i)
                flag=1
            if flag==1:
                break
        if flag == 1:
            break
            
          
  
   
def timer_event():
    global v0,tetta_g
    # все периодические рассчёты, которые я хочу, делаю здесь
    for ball in balls:
        ball.fly()
    # ----------------- Движение снаряда --------------------
    for shell in shells_on_fly:
        # Расчет нового положения снаряда
        g=9.81
        shell._t+=0.1
        # tetta=shell._tetta_r
        # v0=100
        v0=gun._l
        #tetta_g=60
        tetta_g=shell._tetta_g
        rad=180/math.pi
        tetta_r=tetta_g/rad # вместо градусов получили количество радиан    
        v0x=v0*math.cos(tetta_r)
        v0y=v0*math.sin(tetta_r)
        x0=shell._x0
        y0=shell._y0
        # v0y=shell._V0y
        # v0x=shell._Vx
        # ---------------------------------------
        Sx=v0x*shell._t
        Sy=-v0y*shell._t+(g*shell._t**2)/2
        # ---------------------------------------
        shell._x = x0+Sx
        shell._y = y0+Sy
        # print('Перед вызовом функции: ',shell._x,shell._y)
        canvas.coords(shell._avatar, shell._x, shell._y,
                      shell._x + 2*shell._R, shell._y + 2*shell._R)

        # -------------------------------------------------------
        check_for_hit() # Проверка на попадание
        # -------------------------------------------------------
    canvas.after(timer_delay, timer_event)


def click_event_handler(event):
    global shells_on_fly
    shell = gun.shoot()
    shells_on_fly.append(shell)

if __name__ == "__main__":
    init_main_window()
    init_game()
    
    timer_event()
    root.mainloop()
