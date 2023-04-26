import turtle as t
import time
t.shape('turtle')
t.speed(1)


#螺旋矩形
t.penup()
t.goto(0,0)
t.pendown()
t.right(45)
for i in range(5,80,2): 
    t.forward(i)
    t.right(45+90)


'''
#长方体 
for i in range(1,5):
    if i%2 == 0: 
        t.forward(50)
        print(t.pos())
        t.right(45)
    else:
        t.forward(50)
        print(t.pos())
        t.right(180-45)
t.right(90)
t.forward(200)
t.penup()

t.goto(50,0)
t.pendown()
t.forward(200)
t.penup()

t.goto(14.64,-35.36)
t.pendown()
t.forward(200)
t.penup()

t.goto(-35.36,-35.36)
t.pendown()
t.forward(200)
t.penup()

t.goto(0.00,0.00)
t.pendown()
t.forward(200)
t.penup()

t.left(90)
t.pendown()
for i in range(1,5):
    if i%2 == 0: 
        t.forward(50)
        print(t.pos())
        t.right(45)
    else:
        t.forward(50)
        print(t.pos())
        t.right(180-45)
''' 
t.done()
 
 