from drawman import *
# График функции
shag=20
vod=0.5

novid()
col()
size()
axis()
grid()
edin()

col('red')
pen_width(wid=3)
x = -5.0
scale=shag/vod
xe=x*scale
pen_up()
y=x**2
ye=y*scale
to_point(xe, ye)
pen_down()
while x <= 5:
    x += 0.2
    xe=x*scale
    y=x**2
    ye=y*scale
    to_point(xe,ye)
        
pen_up()
