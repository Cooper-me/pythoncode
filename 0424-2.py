import turtle as t
import random as r
t.speed(0)
t.colormode(255)
r=255
g=255
b=0
a=0
while True:
    t.color(r,g,b)
    for i in range(4):
        t.fd(a)
        t.lt(91)
    a+=1
    r-=1
    b+=1
    g-=1
    if r==0:
        r=255
    if g==0:
        g=255
    if b==255:
        b=0
t.done()
