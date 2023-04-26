import turtle as t
t.penup()
t.goto(-200,200)
t.pendown()
for i in range(4):
    t.forward(400)
    t.right(90)
t.penup()
t.goto(0,0)
t.color('red')
t.pendown()
for i in range(4):
    t.forward(200)
    t.backward(200)
    t.right(90)
t.done()











