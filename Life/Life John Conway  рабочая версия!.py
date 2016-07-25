from tkinter import *
from time import sleep
root = Tk()
n=10
w=50*n
h=50*n
npokolen=0
root.geometry("%dx%d" % (510, 550))
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
    global squares
    x=event.x
    y=event.y
    for row in squares:
        for elem in row:
            if event.x>elem.x0 and event.x<elem.x1 \
              and event.y>elem.y0 and event.y<elem.y1:
                # print('Отметили клетку')
                if elem.color == 'white':
                    elem.color = 'black'
                    canv.itemconfig(elem.id, fill='black')
                elif elem.color == 'black':
                    elem.color = 'white'
                    canv.itemconfig(elem.id, fill='white')
           
def proverka(i,j):
    # Проверка 8-ми соседних ячеек
    global squares, s_new, n_izm
    # исследуемая ячейка
    okr=0
    # смотрим соседние 8 ячеек
    pass
    if squares[i][j].color == 'white':
        # ячейка не живая
        # Обходим 8 ячеек
        for it in range(i-1,i+2):
            for jt in range(j-1,j+2):
                if it==i and jt==j:
                    # print('Пропуск ячейки',it,jt,'n= ',n)
                    pass
                else:
                    if it>=0 and jt>=0 and it<=n-1 and jt<=n-1:
                        # print ('Обходимая ячейка',it,jt,'цвет',squares[it][jt].color)
                        if squares[it][jt].color == 'black':
                            okr+=1
                            # print('Изменение в окружении: ',okr)
        if okr == 3:
            s_new [i][j]=1
            n_izm+=1
        # print('Адрес белой ячейки ',i,j,' Окружение ',okr)
        # sleep(1)

    else:
        # ячейка живая
        # Обходим 8 ячеек
        for it in range(i-1,i+2):
            for jt in range(j-1,j+2):
                if it==i and jt==j:
                    # print('Пропуск ячейки',it,jt,'n= ',n)
                    pass
                else:
                    if it>=0 and jt>=0 and it<=n-1 and jt<=n-1:
                        # print ('Обходимая ячейка',it,jt,'цвет',squares[it][jt].color)
                        if squares[it][jt].color == 'black':
                            okr+=1
        if okr == 2 or okr ==3:
            s_new [i][j]=1
        else:
            # print('Адрес черной ячейки ',i,j,' Подсчитано окружение ',okr)
            # print('Ячейка умирает!')
            # sleep(1)
            s_new [i][j]=0
            n_izm+=1
        
        
    # Конец функции проверки

def timer_event():
    global squares, s_new, npokolen, n_izm
    # print(' ----- Смена поколений -----')
    timer_delay = 1000
    # Создаем пустую матрицу
    s_new=[0]*n
    for i in range(n):
        s_new[i]=[0]*n
    # print(s_new)
    # обходим прежнюю матрицу
    n_izm=0 # Количество изменений в матрице
    for i in range(n):
        for j in range(n):
            proverka(i,j)            
                
    # Новая матрица жизни
    for i in range(n):
       for j in range(n):
           print(s_new[i][j], end ='')
       print()   
    # Перерисовка матрицы
    print(' ----- Новая матрица жизни ------ ')
    squares=[0]*n
    for i in range(n):
        squares[i]=[0]*n
    for i in range(n):
        for j in range(n):
            squares[i][j] = Cell(i,j)
            if s_new[i][j] == 1:
                squares[i][j].color = 'black'
                canv.itemconfig(squares[i][j].id, fill='black')
                
    # sleep(1000)
    npokolen+=1
    l.config(text='Прошло поколений:  '+str(npokolen))
    if n_izm == 0:
        print ('Останов')
    else:
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

b1=Button(root,text="Run",command=run)
b1.pack(side=LEFT)

b2=Button(root,text="Close",command=root.destroy)
b2.pack(side=RIGHT)

l=Label(root,text='Прошло поколений:     ')
l.pack(side=TOP)


mainloop()
