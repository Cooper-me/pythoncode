import turtle as t#导入海龟模块
t.speed(0)
color=['blue','red','yellow','green','white'] #列表赋值颜色
r=100 # 定义半径
for c in color: # 循环颜色列表
    print(c)
    t.color(c) # 更改颜色
    #t.color('blue')
    for i in range(5):
        t.begin_fill()
        t.circle(r,360,5) 
        t.end_fill()
        t.hideturtle()
        t.right(70)
    t.right(11)
    r=r-20
    
t.done()

''' 
#t.color('red')
    for i in range(5):
        t.begin_fill()
        t.circle(80,360,5)
        t.end_fill()
        t.hideturtle()
        t.right(70)
    t.right(11)
    #t.color('yellow')
    for i in range(5):
        t.begin_fill()
        t.circle(40,360,5)
        t.end_fill()
        t.hideturtle()
        t.right(70)
    t.right(11)
    #t.color('green')
    for i in range(5):
        t.begin_fill()
        t.circle(20,360,5)
        t.end_fill()
        t.hideturtle()
        t.right(70)
    t.right(11)
    #t.color('white')
    for i in range(5):
        t.begin_fill()
        t.circle(10,360,5)
        t.end_fill()
        t.hideturtle()
        t.right(70)
'''