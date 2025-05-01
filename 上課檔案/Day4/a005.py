t = int(input())
for index in range(t): #幾組數列
    #每一組數列的處理
    a=input().split() #拿一組數列
    if int(a[1])-int(a[0])==int(a[2])-int(a[1]):#等差
       d=int(a[1])-int(a[0])
       print(a[0],a[1],a[2],a[3],int(a[3])+d)
    else:#等比
       r=int(a[1])//int(a[0])#除法(/) -> float, 取商數(//) -> int
       print(a[0],a[1],a[2],a[3],int(a[3])*r)