import turtle as t
t.color('pink')
t.dot(250)
t.color('white')
t.pensize(20)
for i in range(37):
    t.pendown()
    t.circle(i*5,10)
    t.left(10)
    t.penup()
t.right(90)
t.pendown()
t.forward(200)
t.backward(200)
t.hideturtle
t.done()