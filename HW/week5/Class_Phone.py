'''
а) Создайте класс Phone, который содержит атрибуты number, model и weight.
б) Создайте три экземпляра этого класса.
в) Выведите на консоль значения их атрибутов.
г) Добавить конструктор в класс Phone, который принимает на вход три параметра для инициализации переменных класса - number, model и weight.
д) Создать метод sendMessage. Данный метод принимает на вход номера телефонов, которым будет отправлено сообщение. Метод выводит на консоль номера этих телефонов.
'''

class Phone:

    def __init__(self, number, model, weight):
        self.number = number
        self.model = model
        self.weight = weight

    def sebd_message(self):
        pass


phone = Phone(996441156, "nokia", 45)
print(dir(phone))
print(f'номер телефона {phone.number} модель {phone.model} вес {phone.weight} грамм')