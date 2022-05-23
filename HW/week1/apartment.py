district=(input("Введите район где находится дом " ))
price=int(input("Введите стоимость дома "))
mat=(input("Введите материал постройки (кирпича, пескоблок др) "))
s=int(input("Введите размер участка в сотках "))

if district=="чон арык" or district=="байтик" or district=="ортосай" :
    if mat=='кирпич' and s<=4 and price<=50000:
        print("Рассматриваем")
    elif mat=="пескоблок" and s<= 5 and price<=45000:
        print("Рассматриваем")
    elif mat!=1 and mat!=2:
        print("Не подходит по материалу")
    else:
        print("Не рассматриваем")
else:
    print("не рассматриваем")

