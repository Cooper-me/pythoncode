#打印100-200之间的素数
import time

for i in range(1,201):
    flag=1
    for j in range(2,i):
         if i%j==0:
            flag=0
            break
    if flag:
        print(i,"是质数")
         
    
