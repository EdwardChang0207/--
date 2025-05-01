m, d = input().split() #'2 3' -> ['2','3'] -> m='2', d='3'
m, d = int(m), int(d)#m=2, d=3
s = (m*2+d)%3 #0 or 1 or 2
k = ['普通','吉','大吉']
#      0    1    2
print(k[s])