import turtle as t
t.tracer(0)
t.bgcolor('black')
moon=t.Pen()
moon.color('yellow')
moon.shape('circle')
moon.shapesize(10)
moon.penup()
earth=t.Pen()
earth.speed(1)
earth.penup()
earth.color('black')
earth.shape('circle')
earth.shapesize(10)
x=300
earth.goto(x,0)
while True:
    x-=0.1
    earth.goto(x,0)
    t.update()
t.done()