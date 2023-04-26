#斐波那契数列
n=int(input("请输入斐波那契数列数量："))
a=0
b=1
if n==1:
    print(0,end=" ")
if n==2:
    print(a,b,end=" ")
else: 
    print(a,end=" ")
    print(b,end=" ")
    for i in range(3,n+1):
        m=a+b
        a=b
        b=m
        print(m,end=" ")
print("")
i=input("按任意字符关闭窗口")            

  
