'''
while True:
    year = int(input())
    if (year%4==0 and year%100!=0) or year%400==0:
        print('閏年')
    else:
        print('平年')
'''
import sys
for index in sys.stdin:
    year = int(index)
    if (year%4==0 and year%100!=0) or year%400==0:
        print('閏年')
    else:
        print('平年')