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

    def __init__(self, idd, familia, ima, otchestvo, adress, number_card, debet, credit, time):
        self.idd= idd
        self.idd = idd
        self.familia = familia
        self.ima = ima
        self.otchestvo = otchestvo
        self.adress = adress
        self.number_card = number_card
        self.debet = debet
        self.credit = credit
        self.time = time

    def set_val(self):
        pass

    def get_val(self):
        pass
    def vivod(self):

