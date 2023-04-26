import turtle as t
color=['red','white','red','blue']
cpen=t.Pen()
r=500
for c in color:
    cpen.color(c)
    cpen.dot(r)
    r=r-100
starpen=t.Pen()
starpen.penup()
starpen.goto(-95,25)
starpen.pendown()
starpen.color('white')
starpen.begin_fill()
for i in range(4):
    starpen.forward(190)
    starpen.right(144)
starpen.end_fill()
t.done()