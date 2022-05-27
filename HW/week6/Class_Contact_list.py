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

    def search_by_name(self, name):
        for i in all_contacts:
            

    return (next(x for x in all_contacts if x["name"] == name))


    def add_contact(self):
        all_contacts.append()

# class ContactList(List):
#     def __init__(self):
#         super(ContactList, self).__init__()
#         pass
    def __repr__(self):
        return f"id: {self.id}  name: {self.name} surname: {self.surname} phone: {self.phone} "

    def __str__(self):
        return f"id: {self.id}, name: {self.name}, surname: {self.surname}, phone: {self.phone} "

all_contacts = [ ]
a=List(name="Jhon", surname="Menning", idn=123, phone='15447892')
all_contacts.append(a)
b=List("Jake", "Henning", 124, '05447892')
all_contacts.append(b)
c=List("Michel", "Obama", 125, '05451456')
all_contacts.append(c)
print(all_contacts)
print(a)
# search_by_name('Jhon')
# print(next(x for x in all_contacts if x["name"] == "Jake"))
# all_contacts = ContactList()
print([x for x in all_contacts if x['name'] == 'Jake'][1])