a=set()
list1=[]
minset=0
for i in range(5):
    n=int(input('введите число '))
    a.update(str(n))
    list1.append(n)
print(a)
print(list1)
from functools import reduce
print(reduce(lambda x, y: x if x < y else y, list1))
print(reduce(min,list1))