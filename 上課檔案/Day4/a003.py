date = input().split() #'M D' -> ['M','D']
s = (int(date[0])*2+int(date[0]))%3
luck = ['普通','吉','大吉']
print(luck[s])