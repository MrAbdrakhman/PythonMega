#1. Вывести на экран 10 раз своё имя
name="Abdrakhman"
for i in range(1,11):
    print (i,name)
#2. Вывести на экран числа от 1 до 100
print('числа от 1 до 100')
for i in range (1,101):
    print(i, end=' ')
print()
#3. Вывести на экран все четные числа от 1 до 100
print('четные числа до 100 ')
for i in range(1,101):
    if i%2==0:
        print(i, end=' ')
print()
#4. Вывести на экран все числа от 1 до 100 кратные 4
print('числа кратные 4 до 100')
for i in range(1,101):
    if i%4==0:
        print(i,end=' ')