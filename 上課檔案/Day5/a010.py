a = int(input())
for index in range(2, a+1):
    count = 0
    while a % index == 0:
        count += 1
        a //= index
    if a != 1:
        if count > 1:
            print(index,'^',count,sep='',end=' * ')
        elif count == 1:
            print(index,end=' * ')
    else:
        if count > 1:
            print(index,'^',count,sep='')
        elif count == 1:
            print(index)