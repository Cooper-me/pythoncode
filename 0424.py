import turtle as t
t.speed(0)
a=400
c=['red','white','red','blue']
for i in c:
    t.color(i)
    t.dot(a)
    a=a-80
t.penup()
t.left(90)
t.forward(25)
t.right(270)
t.forward(80)
t.right(180)
t.pendown()
t.color('white')
t.begin_fill()
for i in range(5):
    t.forward(153)
    t.right(144)
t.end_fill()
t.hideturtle()
t.done()