while True:
    z = input('введите знак ')
    a = float(input('введите 1 число '))
    b = float(input('введите 2 число '))
    try:
        if z == "+":
            print(a + b)
        elif z == "-":
            print(a - b)
        elif z == "*":
            print(a * b)
        elif z == "/":
            try:
                print(a / b)
            except ZeroDivisionError as zd:
                print('нельзя делить на ноль')
        else:
            print('ошибка ввода')
    except ValueError as vr:
        print('ошибка ввода')
    x = input("хотите закончить нажмите (Y) если нет то любое другую букву ")
    if x == "Y":
        break

