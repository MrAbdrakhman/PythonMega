RAM=int(input("Введите объем опер памяти в ГБ "))
mem=(input("Введите тип жесткого диска (SDD или HDD) "))
mem_v=int(input("Введите объем жест диска  ГБ "))
cost=int(input("Введите стоимость в долларах "))
cond=(input("Компьютер новый или старый "))
if cond=="новый":
    if RAM>=4 and RAM<= 8 and mem=="SDD" and mem_v>=256 and cost<=1000:
        print("покупаем")
    elif RAM>=4 and RAM<= 8 and mem=="HDD" and mem_v>=1000 and cost<=1000:
        print("покупаем")
    else:
        print("не покупаем")
else:
    print("не покупаем")

