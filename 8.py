
j=1
for i in range(1,10):
    for j in range(1,i+1):
        b=i*j
        print(j,"*",i,"=",b,end=" | ")
    print("")
i=input("按任意字符关闭窗口")