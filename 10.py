#古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
#       月份 一    二  三  四  五  六  七  八  九  十  十一    十二
#能生产的兔子2     2   2   2   4   8   
#小兔子      2    4   6    8   
#     
#m是月份，t是兔子数量，每当m+1的时候t+t*2 ，每当m是3的倍数的时候t额外增加t/2的数量
#从1月开始到12月结束
 
t=1
for m in range(1,13):
    t=t*2
    if m%3==0:
        a=t/2
        t=t+a
     
    print("当前是",m,"月",end=" ")
    print("当月兔子是",t)


     
                                   