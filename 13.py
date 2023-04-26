#题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

#程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
#(1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
#(2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
#(3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。
from operator import truediv
import time 
m=[]
i=int(input("输入一个正整数: "))
n=i
k=0
while n != 1:
    for j in range(2,n+1):
            if n%j==0:
                n=n//j
                m.append(j)
                k+=1
                break
for i in range(0,k):
    if i == k-1:
        print(m[i])
    else:
        print(m[i],"*",end="")
