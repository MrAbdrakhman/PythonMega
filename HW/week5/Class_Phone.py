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

    def return1(self):
        return f'{self.number} {self.model} {self.weight}'

    def sendMassage(self):
        return self.number

    def phone_kays(self):
        return self.model

    def phone_values(self):
        return self.number

    def __str__(self):
        return f"Model: {self.model}  number: {self.number} адрес: {self.weight} "

samsung = Phone(number=+996705699767, model='Samsung', weight=200)
print(samsung.return1())
iphone = Phone(number=+996708699767, model='Iphone', weight=170)
print(iphone.return1())
huawei = Phone(number=+996700699767, model='Huawei', weight=250)
print(huawei.return1())
#print(f'{samsung} \n{iphone} \n{huawei}')
print(samsung.sendMassage(), iphone.sendMassage(), huawei.sendMassage())

phones = [samsung, iphone, huawei]

print({'Phones': {phone.model: phone.number for phone in phones}})
print(Phone)
print(Phone.__dict__)
