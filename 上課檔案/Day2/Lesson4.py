#運算子 Operator(Oprate)
#運算元 Operatee
#數學運算子
print(10+20)
print(10-20)
print(10*20)
print(10/2)
print(2**3) #次方（指數）：2^3 = 2*2*2 -> 2**3
#除法：8/3 = 2(商)...2(餘)
print(8//3)#(商)
print(8%3)#(餘)

#int op int -> int(大部分), 例外：除法 -> int op int -> float
#float op int -> float
#float op float -> float

#邏輯運算子 something op something -> bool
#>, <, >=, <=, ==(equal), !=(not equal)
print(2 > 3)
print(3 > 2)
print(3 >= 3)
print(3 <= 5)
print(2 == 2)
print(3 != 3)
#int op int -> bool

#邏輯閘 bool op bool -> bool
#not, or, and, xor

#not(否閘/反閘)
#不(not)錯(False) -> True
#錯 -> False
#不(not)行(True) -> False
#行 -> True
print(not False)
print(not True)
print(not(False))
print(not(True))

#or(或閘)
'''
math or english -> 3000
T    or F       -> T
F    or T       -> T
T    or T       -> T
F    or F       -> F
'''
print(True or False)
print(False or True)
print(True or True)
print(False or False)

#and(且閘)
'''
總統 and 部長 -> 發射？
T   and F   -> F
F   and T   -> F
T   and T   -> T
F   and F   -> F
'''
print(True and False)
print(False and True)
print(True and True)
print(False and False)

a = False
b = False
print(not(not(a) or not(b)))
#(1)a不發生
#(2)b不發生


#xor(excursive or 斥或閘)
'''
珍奶 xor 烏龍拿鐵 -> :)
T   xor F       -> T
F   xor T       -> T
T   xor T       -> F
F   xor F       -> F
'''
a = False
b = False
# print((a or b)and(not(a and b)))
#(1)至少拿一杯
#(2)不要拿兩杯給我

#in
l = [1,2,3]
print((1 in l) and (2 in l))

#字串運算
print('hi'+'hello')
print('hi' * 5)

#串列運算
print([1,2,3]+[4,5,6])
print([1,2,3]*5)