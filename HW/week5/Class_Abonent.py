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
        self.id= id
        self.familia = familia
        self.ima = ima
        self.otchestvo = otchestvo
        self.adress = adress
        self.number_card = number_card
        self.debet = debet
        self.credit = credit
        self.time_c = time_city
        self.time_i = time_inter
        self.limit =500

    def set_val(self):
        pass

    def __repr__(self):
        return f'ID: {self.id}, Фамилия: {self.familia}, Имя: {self.ima}'# \nОтчество: {self.otchestvo}, \nАдрес: {self.adress}, \nНомер кредитной карточки {self.number_card}, \nДебeт: {self.debet}, \nКредит: {self.credit}, \nВремя междугородных переговоров: {self.time_i},\nВремя городских переговоров: {self.time_c} '

    def get_info(self):
        print (f'ID: {self.id},\nФамилия: {self.familia}, \nИмя: {self.ima}, \nОтчество: {self.otchestvo}, \nАдрес: {self.adress}, \nНомер кредитной карточки {self.number_card}, \nДебeт: {self.debet}, \nКредит: {self.credit}, \nВремя междугородных переговоров: {self.time_i},\nВремя городских переговоров: {self.time_c} ')

    def get_check_time(a):
        limit=500
        for abon in a:
            if abon.time_i > limit:
                print(f'abonent {abon.familia} время  {abon.time_c} секунд')

    def get_inter_call(a):
        for abon in a:
            if abon.time_i > 0:
                print(f'abonent {abon.familia} пользовался международной связью {abon.time_i} секунд')

    def sort(a):
        a.sort(key=lambda obj: obj.familia)  # после сортировки по фамилиии
        print(a)
        for i in a:
            print(f' familia: {i.familia}, id: {i.id}')

data_abon = []
a1 = Abonent("1281002", "Иванов", "Садыр", "Отчество1", "бишкек", "378282246310005", "400", "0", 110, 100)
data_abon.append(a1)
a2 = Abonent("1218492", "Амиров", "Жапар", "Отчество2", "ош", "37223246310045", "200", "0", 145, 0)
data_abon.append(a2)
a3 = Abonent("1218492", "Путин", "Нургожо", "Отчество3", "москва", "37223246310045", "400", "0", 600, 520)
data_abon.append(a3)
print(data_abon)
a1.get_info()

print(f"абонент превышаюший лимит переговоров 500 секунд: ")
Abonent.get_check_time(data_abon)

print(f"абонент  пользующиеся международной связью: ")
Abonent.get_inter_call(data_abon)


print("Сортировка по фамилиям абонентов")
print("ДО СОРТИРОВКИ  ПО фамилиям абонентов")
print(data_abon) # до сортировки (как распечатать что бы показывал ???????????????????
print("ПОСЛЕ СОРТИРОВКИ  ПО фамилиям абонентов")
Abonent.sort(data_abon)