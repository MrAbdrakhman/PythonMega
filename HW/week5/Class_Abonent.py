'''
Идентификационный номер, Фамилия, Имя, Отчество, Адрес, Номер кредитной карточки,
Дебет, Кредит, Время междугородных и городских переговоров; Конструктор;
Методы: установка значений атрибутов, получение значений атрибутов, вывод информации.
Создать массив объектов данного класса.
Вывести сведения относительно абонентов, у которых время городских переговоров
превышает заданное.
Сведения относительно абонентов, которые пользовались междугородной связью.
Список абонентов в алфавитном порядке.
'''

class Abonent:

    def __init__(self, id, familia, ima, otchestvo, adress, number_card, debet, credit, time_city, time_inter):
        self.idd= id
        self.familia = familia
        self.ima = ima
        self.otchestvo = otchestvo
        self.adress = adress
        self.number_card = number_card
        self.debet = debet
        self.credit = credit
        self.time = time_city
        self.time = time_inter

    def set_val(self):
        pass

    def info(self):
        print(f'ID: {self.id},')
        ''''\nФамилия: {self.familia}, \nИмя: {self.ima}, \nОтчество: {self.otchestvo},'
              f'\nАдресс: {self.adress}, Номер кредитной карточки {self.number_card}, \nДебeт: {self.debet}, '
              f'\nКредит: {self.credit}, "\nВремя междугородных переговоров: {self.time_inter},'
              f'\nВремя городских переговоров: {self.time_city} ')
'''
data_abon = []
a1 = Abonent("1281002", "Фамилия1", "Имя1", "Отчество1", "Какой-то адресс", "378282246310005", "400", "0", "1:10", "0:05")
data_abon.append(a1)
a2 = Abonent("1218492", "Фамилия2", "Имя2", "Отчество2", "Какой-то адресс", "37223246310045", "200", "0", "0:45", "0:35")
data_abon.append(a2)
a3 = Abonent("1218492", "Фамилия3", "Имя3", "Отчество3", "Какой-то адресс", "37223246310045", "400", "0", "1:00", "0:55")
data_abon.append(a3)
print(a1)
a1.info