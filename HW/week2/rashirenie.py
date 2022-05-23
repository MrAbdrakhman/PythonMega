a=input()
b=a.split('.')
if len(b)>1:
    print('расширение файла= ', b[-1])
else:
    print('расширение файла не найдено')
