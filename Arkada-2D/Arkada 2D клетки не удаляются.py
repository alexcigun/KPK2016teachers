from random import randrange as rnd, choice
from random import randint
from tkinter import *
  
root = Tk()
root.geometry('980x600')
  
canv = Canvas(root, bg = 'white')
canv.pack(fill = BOTH, expand = 1)
 
 
m = 48 # размер ячеек
d = 2 # размер поля вокруг ячейки
nr = 3 # количество строк
nc = 1000//(2*50) # количество столбцов
# x0 = m // 2 # отступ от левого края
# y0 = m // 2 # отступ от вернего края
x0 = 10 # отступ от левого края
y0 = 10 # отступ от вернего края
colors = ['red','yellow','cyan','green','blue']
  
class cell():
    def __init__(self, r, c): # при создании указываем номер строки и столбца,
        # в который помещаем
        self.n = rnd(10) # значение, с которым будем работать
        self.r = r # Номер стрoки в двумерном списке.
        self.c = c # Номер столбца ...
        self.color = choice(colors) # случайный цвет из списка
        self.id = canv.create_rectangle(0,-100, 200,-100,fill = self.color)
        # квадратик ячейки
        self.paint()
        self.live=1 # Активная ячейка
        print('Создание клеточки')
  
    def paint(self):
        x1 = x0 + self.c *2* m + d
        # рассчитать координаты левого верхнего угла.
        y1 = y0 + self.r * m + d
        # координаты правого нижнего угла.
        x2 = x1 + 2*m - 2*d # - r
        y2 = y1 + m - 2*d
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        canv.coords(self.id,x1,y1,x2,y2)
        canv.itemconfig(self.id,fill = self.color)
  
  
class Raketka:
    def __init__(self): 
        self.w = 200 
        self.h = 30
        self.x0=490-self.w/2
        self.x1=490+self.w/2
        self.y0=560
        self.y1=560+self.h
        self.id = canv.create_rectangle(self.x0,self.y0,\
                  self.x1,self.y1,fill = 'black')


    def right_r(self,event):
        if self.x1<=940:
            dx=50
            self.x0=self.x0+dx
            self.x1=self.x1+dx
            self.y0=self.y0
            self.y1=self.y1
            canv.coords(self.id,self.x0,self.y0,self.x1,self.y1)
        # canv.itemconfig(self.id,fill = self.color)

    def left_r(self,event):
        # print('Left')
        if self.x0>=0:
            dx=-50
            self.x0=self.x0+dx
            self.x1=self.x1+dx
            self.y0=self.y0
            self.y1=self.y1
            canv.coords(self.id,self.x0,self.y0,self.x1,self.y1)
      
        
class Ball:
    initial_number = 20
    minimal_radius = 15
    maximal_radius = 30
    available_colors = ['green', 'blue', 'red']

    def __init__(self):
        """
        Cоздаёт шарик в случайном месте игрового холста canvas,
        при этом шарик не выходит за границы холста!
        """
        R = randint(Ball.minimal_radius, Ball.maximal_radius)
        self._R = R
        x = randint(0, 980-2*self._R)
        y = randint(150+2*self._R,600-2*self._R)
        self._x = x
        self._y = y
             
        
        fillcolor = choice(Ball.available_colors)
        self._avatar = canv.create_oval(x, y, x+2*R, y+2*R,
                                          width=1, fill=fillcolor,
                                          outline=fillcolor)
        self._Vx = rnd (-5, 5)
        self._Vy = rnd (-5, 5)

        while self._Vx==0 or self._Vy==0:
            self._Vx = rnd(-4, +4)
            self._Vy = rnd(-4, +4)
            

    def fly(self):
        screen_width=980
        screen_height=600
        self._x += self._Vx
        self._y += self._Vy
        # отбивается от горизонтальных стенок
        if self._x < 0:
            self._x = 0
            self._Vx = -self._Vx
        elif self._x + 2*self._R >= screen_width:
            self._x = screen_width - 2*self._R - 1
            self._Vx = -self._Vx
        # отбивается от вертикальных стенок
        if self._y < 0:
            self._y = 0
            self._Vy = -self._Vy
        elif self._y + 2*self._R >= screen_height:
            self._y = screen_height - 2*self._R - 1
            self._Vy = -self._Vy
        elif self._y + 2*self._R >= raket.y0 and \
            self._x>=raket.x0 and self._x<=raket.x1:
            # self._y = screen_height - 2*self._R  - 1
            self._Vy = -self._Vy

        # отбивается от клеточек
        # проход по всем оставшимся клеточкам
        flag=0
        if self._y<152: 
            for r in range(3): # 3 строки
                for c in range(10): # в каждой строке - 10 элементов
                    # if self._y<=a[r][c].y2 and a[r][c].live==1 and self._x>a[r][c].x1 and self._x+self._x+2*self._R < a[r][c].x2:
                    if self._y<=a[r][c].y2 and a[r][c].live==1 and self._x+self._R >a[r][c].x1 and  self._x+self._R >a[r][c].x2 :
                        print(self._y)
                        print(self._Vy)
                        self._Vy = -self._Vy # Меняем вертикальную скорость шара при попадании в клеточку
                        print('Отскок')
                        self._y=a[r][c].y2
                        print(self._Vy)
                        flag=1
                        a[r][c].live=0 # Делаем ячейку неактивной
                        # Надо удалить её канвас
                        canv.itemconfig(a[r][c].id,fill = 'white',outline='white')
                        print('Удаление ячейки')
                        canv.delete(a[r][c].id)
                        break
                if flag==1:
                    break          
                        
                  
        
       
 
        canv.coords(self._avatar, self._x, self._y,self._x + 2*self._R, self._y + 2*self._R)


def timer_event():
    global ball
    timer_delay = 20
    ball.fly()      
    canv.after(timer_delay, timer_event)
    

def create_ball(event):
    global space, ball
    if space == 0:
        space+=1
        ball=Ball()
        timer_event()
    print('Пробел нажали')

space = 0
a = [] # массив клеточек

a=[[0] * nc for j in range(nr)]
# print(a)
for r in range(nr): # 3 строки
    for c in range(nc): # в каждой строке - 10 элементов
        #print ('r=',r,' c=',c)
        #print(cell(r,c).x1)
        cell(r,c)
        a[r][c]=cell(r,c) # добавляем очередной элемент в строку

raket=Raketka()

root.bind('<Right>',raket.right_r)
root.bind('<Left>',raket.left_r)
root.bind('<space>',create_ball)


for r in range(3): # 3 строки
    for c in range(10): # в каждой строке - 10 элементов
        print (a[r][c].y2,sep=' ',end=' ')
    print('\n')

 
root.mainloop()
