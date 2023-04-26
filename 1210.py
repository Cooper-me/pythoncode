from tkinter import *
from PIL import Image
import turtle as t
import random as r

t.penup()
x=-180
y=180
t.goto(x,y)
for k in range(9):
    for i in range(9):
        t.pendown()
        for j in range(4):
            t.forward(60)
            t.right(90)
        t.penup()
        t.goto(x+25,y-45)
        t.pendown()
        
        if r.randint(1,10)%2==0:
            if i<k:
                t.write(((i)+10-k),font=('宋体',40,'normal'))
            else:
                t.write((i-k+1),font=('宋体',40,'normal'))
        t.penup()
        t.goto(x+60,y)
        x=x+60
    t.penup()
    y=y-60
    x=-180
    t.goto(x,y)

##保存turtle图片并且转成jpg
ts = t.getscreen()
ts.getcanvas().postscript(file="d:/pythoncode/t1.eps")
img = Image.open("d:/pythoncode/t1.eps") #打开图片
img.save("d:/pythoncode/t1.jpeg") #保存图片

t.done()