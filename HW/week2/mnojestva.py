# 1.Объединить 2 множества
# months_a = set(["Jan", "Feb", "March", "Apr", "May", "June"])
# months_b = set(["July", "Aug", "Sep", "Oct", "Nov"])
# 2.Добавить месяц, которого нету во множестве
# 3.Перебрать элементы множества
# 4.Вам даны 2 множества, узнать какие элементы пересекаются между ними.
# x = {1, 2, 3}

months_a = set(["Jan", "Feb", "March", "Apr", "May", "June"])
months_b = set(["July", "Aug", "Sep", "Oct", "Nov"])
z = months_a.union(months_b) 
print(z)
z.add('Dec')
for i in z:
    print(i)
x = {1, 2, 3}
y = {4, 3, 6}
s=x.intersection(y)
print(s)
