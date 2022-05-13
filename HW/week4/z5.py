# Дано
dict_one = {'a':1, 'b':2, 'c':3}
dict_two = {'d':4, 'e':5, 'f':6}
dict_three = {'g':7, 'h':8, 'i':9}
dict_four = {}
# С помощью цикла for необходимо собрать три первых словаря в словарь dict_four

# Подсказка: Для удобства итерации, первые три словаря можно записать в кортеж (dict_one, dict_two, dict_three
a=tuple(dict_one.items())
b=tuple(dict_two.items())
c=tuple(dict_three.items())
d=a+b+c
for i in d:
    dict_four.update({i[0]:i[1]})
print(dict_four)