'''
print(1)
print(2)
print(3)
print(4)
print(5)
...
'''

#迴圈 Loop
#while 當
'''
index = 1
while index <= 10:
    print(index)
    index += 1
print(index)
'''

#for Loop
#(1)List
'''
for index in ['鮭魚','鮪魚','玉子燒']:
    print(index)
'''

#(2)String
'''
for index in 'hello':
    print(index)
'''

#(3)range(start, end, interval) -> 數字
#from start to end-1, increase interval
'''
for index in range(5, 18, 3):
    print(index)
'''
#1 range(end): start init:0, interval init: 1

#2 range(start, end): interval init: 1

#3 range(start, end, interval)

#ex.1 1~20

#for loop
'''
for index in range(1,21):
	print(index)
'''
#while loop
'''
index=1
while index<=20:
	print(index)
	index +=1
'''
	
#ex.2 1, 3, 5, ..., 21

#for loop
'''
for index in range(1,22,2):
    print(index)
'''
#while loop
'''
index = 1
while index<=21:
    print(index)
    index +=2
'''

#ex.3 10~1

#for loop
'''
for index in range(10,0,-1):
    print(index)
'''

#while loop
'''
index=10
while index<=0:
    print(index)
    index -=1
'''

#continue(skip), break(stop)
'''
for index in range(10):
    if index == 6:
        continue
    if index == 8:
        break
    print(index)
'''
index=0
while index<=10:
     if index==6:
        index += 1
        continue
     if index==8:
        break
     print(index)
     index += 1
