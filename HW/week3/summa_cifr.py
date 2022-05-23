'''Ввести число любой длины.
Вывести на экран сумму его цифр.
'''
n=list(input())
sum=0
print(n)
for i in n:
    sum=sum+int(i)
print(sum)
