# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
# и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).
n=int(input('Введите номер месяца '))
vesna=[3,4,5]
leto=[6,7,8]
osen=[9,10,11]
zima=[12,1,2]
def sezon(a):
    if a in vesna:
        return 'весна'
    if a in leto:
        return 'лето'
    if a in osen:
        return 'осень'
    if a in zima:
        return 'зима'
print(sezon(n))