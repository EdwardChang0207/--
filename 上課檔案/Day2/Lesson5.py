name = 'alan'
age = 18
# print('my name is', name, ',nice to meet you')
# print('my name is {}, nice to meet you'.format(name))
# print(f'my name is {name}, nice to meet you')

# %
#格式符號
'''
%s -> str
%d -> int
%f -> float
'''
# print('my name is %s, nice to meet you, I am %d years old' % (name, age))
print('name:%5s score:%3d'%('kevin',60))
print('name:%5s score:%3d'%('mary',70))
print('name:%5s score:%3d'%('alan',100))
print('%.3f'%3.1415926)

# #.format . -> 1.的, 2.對...做...
# print('my name is {:s}, nice to meet you, I am {:d} years old'.format(name, age))
print('name:{:5s} score:{:3d}'.format('kevin',60))
print('name:{:5s} score:{:3d}'.format('mary',70))
print('name:{:5s} score:{:3d}'.format('alan',100))
print('{:.3f}'.format(3.1415926))

# #f-string
# print(f'my name is {name}, niceto meet you, I am {age} years old')
# print(f'1+1={1+1}')
name, score = 'kevin', 60
print(f'name:{name:5s} score:{score:3d}')
name, age = 'mary', 70
print(f'name:{name:5s} score:{score:3d}')
name, age = 'alan', 100
print(f'name:{name:5s} score:{score:3d}')
pi = 3.1415926
print(f'{pi:.3f}')


