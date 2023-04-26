j=0
for bai in range(1,5):
    for shi in range(1,5):
        for ge in range(1,5):
            if bai==shi or shi ==ge or bai==ge:
                i=1
            else:
                j +=1
                print(bai,shi,ge,end='\n')
print(j)                