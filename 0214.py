# 本金 b  利息 l 美元 m 汇率 h 人民币 r
# 本金*利息+本金 = 收益 s
# 人民币 * 汇率 = m   
# r= 700000  当前汇率m1= 6.82  利息 l=5.5 
print("当前人民币")
r=700000
print(r)
m1=6.82
print("当前汇率")
print(m1)
s=(r/m1)*5.5/100+(r/m1)
print("一年后美金本息一起是")
print(s)
print("按当前汇率人民币是")
print(s*m1)
r2=s*m1

for m2 in range(61,72):
    if  s/10*m2 < r:
        print("低于当前汇率开始亏一年前的本金")
        print(m2/10)
        print("亏损金额")
        print(r-s/10*m2)


 