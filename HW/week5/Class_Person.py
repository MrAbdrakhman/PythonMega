''''
a) поля fullName, age, place(address)
б) метод talk(), в которых просто вывести на консоль сообщение -"Такой-то  Person говорит". Метод
move()  будет менять его адрес
в) Добавьте  конструктор  с тремя параметрами fullName, address, age = 18
г) Настроить  метод __str__  (Сделать отображение всех полей объекта)'''


class Person:
    def __init__(self, fullName, age, place):
        self.fullName = fullName
        self.age = 18
        self.place = place

    def talk(self):
        print(f'{self.fullName} говорит')

    def move(self, new_place):
        self.place = new_place
        return print(f" name: {self.fullName} новый адрес: {self.place}")

    def __str__(self):
        return f"Name: {self.fullName}  Age: {self.age} адрес: {self.place} "

    def vvod(self):
        print(f'Введите новый адрес ')
        new_place=input()
        return new_place

ivan = Person("Иван", 20, "Bishkek")
ivan.talk()
print(ivan)
a=ivan.vvod()
ivan.move(a)
