'''Создайте класс ContactList, который должен наследоваться от
встроенного класса list. В нем должен быть реализован метод
search_by_name, который должен принимать имя, и возвращать список
всех совпадений. Замените all_contacts = [ ] на all_contacts =
ContactList(). Создайте несколько контактов, используйте метод
search_by_name.'''

all_contacts = ['Jibek', 'Emir', 'Tilek', 'Dastan', 'Aiperi', 'Sanjar', 'Dadahan', 'Ivan']
name_found=[]

class List:
    def __init__(self, name):
        self.name=name

class ContactList(List):
    def __init__(self):
        super().__init__(self)

    def search_by_name(self):
        while True:
            a= input ('введите имя: ' )
            if a in all_contacts:
                print ('имя найдено')
                name_found.append(a)
            else:
                print (f'имя {a} не найдено' )
                break
        return name_found

contact=ContactList()
print(all_contacts)

print(f'Список найденных имен \n{contact.search_by_name()}')