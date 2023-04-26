#小明单位发了100元的购物卡，小明到超市买三类洗化用品：洗发水（15元）、香皂（2元）、牙刷（5元）。要把100元正好花掉，可有哪些购买组合？
m=100
n=0
for i in range(0,100//15+1):
    money=m-15*i
    print(i)
    for j in range(0,money//2+1):
        money=money-j*2
        print("剩余的钱",money)
        for k in range(0,money//5+1):
            money=money-k*5
            print("洗发水：",i,"香皂：",j,"牙刷：",k,"剩余的钱",money)
         
        