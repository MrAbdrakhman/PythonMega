marka=(input("Введите марку авто "))
god=int(input("Введите год выпуска авто "))
probeg=int(input("Введите пробег авто в км "))
color=(input("Введите цвет авто "))
rul=(input("Руль авто (правый или левый) "))
owners=int(input("Сколько было собственников? "))
price=int(input("Введите цену на авто "))
if marka==('Toyota' or marka=='Lexus') and probeg<=150000 and god>=2004 and (color=='white' or color=='grey') and owners<=2 and  rul=='left' and price<=10000:
    print("Покупаем")
elif marka==('Toyota' or marka=='Lexus') and probeg<=200000 and god>=2004 and (color=='white' or color=='grey') and owners<=2 and  rul=='left' and price<=8000:
    print("Покупаем")
else:
    print('Не покупаем')