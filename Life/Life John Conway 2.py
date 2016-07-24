from tkinter import *
from time import sleep
root = Tk()
n=10
w=50*n
h=50*n
root.geometry("%dx%d" % (w, h))
root.title('Жизнь Джона Конвея')
canv = Canvas(root, bg = 'white')
canv.pack(fill = BOTH, expand = 1)
class Cell:
    def __init__(self,line,col):
        self.x0=col*50
        self.y0=line*50
        self.x1=(col+1)*50
        self.y1=(line+1)*50
        self.color='white'
        self.id=canv.create_rectangle(self.x0,
                self.y0, self.x1, self.y1 , width=2, fill="white")

def check_cell(event):
    x=event.x
    y=event.y
    for row in squares:
        for elem in row:
            if event.x>elem.x0 and event.x<elem.x1 \
              and event.y>elem.y0 and event.y<elem.y1:
                print('Отметили клетку')
                if elem.color == 'white':
                    elem.color = 'black'
                    canv.itemconfig(elem.id, fill='black')
                elif elem.color == 'black':
                    elem.color = 'white'
                    canv.itemconfig(elem.id, fill='white')
           
    print('x=',x,'y=',y)


def timer_event():
    print(' ----- Смена поколений -----')
    timer_delay = 1000
    # Создаем пустую матрицу
    s_new=[0]*n
    for i in range(n):
        s_new[i]=[0]*n
    # print(s_new)
    # обходим прежнюю матрицу
    for i in range(n):
        for j in range(n):
            # исследуемая ячейка
            # смотрим соседние 8 ячеек
            pass
            if squares[i][j].color == 'white':
                # ячейка не живая
                okr=0
                # Обходим 8 ячеек
                for it in range(i-1,i+2):
                    for jt in range(j-1,j+2):
                        if i-1<0 or j-1<0 or i+1>n-1 or j+1>n-1:
                            continue
                        else:
                            if squares[it][jt].color == 'black':
                                okr+=1
                if okr == 3:
                    s_new [i][j]=1
                    
            else: # ячейка живая
                okr=0
                # Обходим 8 ячеек
                for it in range(i-1,i+2):
                    for jt in range(j-1,j+2):
                        if i-1<0 or j-1<0 or i+1>n-1 or j+1>n-1:
                            continue
                        else:
                            if squares[it][jt].color == 'black':
                                okr+=1
                if okr == 2 or okr ==3:
                    s_new [i][j]=1
                else:
                    s_new [i][j]=0
                
                pass
    # Новая матрица жизни
    print('Новая матрица жизни')
    for i in range(n):
        for j in range(n):
            print(s_new[i][j], end ='')

            if s_new[i][j]==1:
                canv.itemconfig(squares[i][j].id, fill='black')
            else:
                canv.itemconfig(squares[i][j].id, fill='white')
            
        print()
    canv.after(timer_delay, timer_event)


def run():
    timer_event()

        

squares=[0]*n
for i in range(n):
    squares[i]=[0]*n  
for i in range(n):
    for j in range(n):
        squares[i][j] = Cell(i,j)

canv.bind("<Button-1>",check_cell)

b=Button(root,text="Run",command=run)
b.pack(side=LEFT)

l=Label(root,text='Прошло поколений:     ')
l.pack(side=BOTTOM)

mainloop()
