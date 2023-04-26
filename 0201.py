import turtle as t
'''
##t.speed(100000000000000000000000000000)
for i in range(100):
    t.color('blue')
    for i in range(4):
        t.forward(60)
        t.right(90)
    t.right(360/100)
    t.color('red')
    for i in range(4):
        t.forward(60)
        t.right(90)
    t.right(360/100)
    t.color('green')
    for i in range(4):
        t.forward(60)
        t.right(90)
'''        
a=['green','red','blue','yellow','black']
for i in a:
    t.color(i)
    for i in range(4):
        t.forward(60)
        t.right(90)
    t.right(360/5)
t.done()
