'''Создайте класс ContactList, который должен наследоваться от
встроенного класса list. В нем должен быть реализован метод
search_by_name, который должен принимать имя, и возвращать список
всех совпадений. Замените all_contacts = [ ] на all_contacts =
ContactList(). Создайте несколько контактов, используйте метод
search_by_name.'''
class List:
    def __init__(self, name, surname, idn, phone):
        self.name=name
        self.surname=surname
        self.id=idn
        self.phone=phone

    def search_by_name(self):
        pass

class ContactList(List):
    def __init__(self):
        super(ContactList, self).__init__()
        pass

all_contacts = [ ]



all_contacts = ContactList()


