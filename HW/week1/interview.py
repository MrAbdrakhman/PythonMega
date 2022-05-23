lang=(input("Какие языки програмирования знает кандидат "))
age=int(input("Какой возраст кандидата "))
exp=int(input("Его опыт работы в годах "))
salary=int(input("Желаемая зарплата "))
print()
if (lang=="java" or lang=="python" or lang=="javascript") and age>=18 and age<=65 and exp>=3 and salary<=60000:
    print("Кандидат подходит")
else:
    print("Кандидат не подходит")
print("Язык программирования: ", lang)
print("Возраст: ", age)
print("Опыт: ", exp)
print("Желаемая зарплата: ", salary )

