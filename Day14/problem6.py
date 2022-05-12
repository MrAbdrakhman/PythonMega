#Напишите программу которая спрашивает от пользователя 2 вещи:
#1.Путь до картинки которую нужно изменить.
#2.Путь до картинки НА которую нужно изменить.
#Если оба пути существуют перепишите первую картинку на вторую, если нет скажите пользователю какой картинке не существует.


def check_format():
    if ('jpeg' or 'png' or 'jpg') not in file_name.split('.') [-1]:
        raise exception(f'формат файла {file_name} не правильный')

while True:
    try:
        first = input("Введите путь до картинки которую нужно изменить ")
        check_format(first)
        second = input("Введите путь до картинки на которую нужно изменить ")
        check_format(second)
    except Exception:
        print()
    else:
        f1=open(first,'wb')
        f2=open(second,'rb')
        f1.write(f2.read())
        break