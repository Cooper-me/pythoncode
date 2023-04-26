import turtle as t
bc=int(input('请输入边长'))
t.goto(0,0)
a=0
x=0
y=0
for i in range(5):
    for i in range(4):
        t.forward(bc+a*2)
        t.right(90)
    t.penup()
    x=x-20
    y=y+20
    t.goto(x,y)
    t.pendown()
    a=a+20
t.penup()
t.goto(0,0)
t.done()









