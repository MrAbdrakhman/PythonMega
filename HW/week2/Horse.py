a=int(input('Введите номер столбца коня ' ))
b=int(input('Введите номер строки коня ' ))
c=int(input('Введите номер столбца другой фигуры ' ))
d=int(input('Введите номер строки другой фигуры ' ))
if (c==a-2 and d==b-1) or (c==a-1 and d==b-2) or (c==a-1 and d==b+2) or(c==a-2 and d==b+1)or (c==a+2 and d==b+1)or (c==a+1 and d==b+2) or (c==a+1 and d==b-2)or(c==a+2 and d==b-1):
    print('Конь бьет другую фигуру')
else:
    print('Конь НЕ бьет другую фигуру')