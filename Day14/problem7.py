'''Создайте текстовый файл ->
Записать в него построчно данные, которые вводит пользователь
Окончание ввода должен принимать пустую строку'''
with open('text1.txt','w') as f:
    while True:
        a=input("введите данные \n", )
        if a =='':
            break
        f.write(a)