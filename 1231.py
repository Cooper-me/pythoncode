import turtle as t
n=int(input ('输入边的数量'))
m=int(input('输入边长'))
if n<3:
    print('输入错了')
else:
    for i in range(n):
        t.forward(m)
        t.right(180-(180*(n-2))/n)
t.done()
