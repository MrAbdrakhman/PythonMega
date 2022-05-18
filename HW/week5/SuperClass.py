''' Создайте класс Person с атрибутами: имя и возраст строки типа.
Создайте метод display(), который отображает имя и возраст объекта, созданного с помощью класса Person.
Создайте дочерний класс Student, который наследуется от класса Person и также имеет атрибут раздела.
Создайте метод displayStudent(), который отображает имя, возраст и раздел объекта, созданного с помощью класса Student.
Создайте объект Student через создание экземпляра в классе Student, а затем протестируйте метод displayStudent
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_per(self):
        print (f' Person name: {self.name}, \n Person age= {self.age}')

class Student(Person):
    def __init__(self, name, age, sec):
        super().__init__(name, age)
        self.sec=sec

    def display_student(self):
        print(f' Student name: {self.name}, \n Student  age= {self.age}, \n Student section= {self.sec}')

a=Person("Tomas Wild", 37)
a.display_per()

a1=Student("Albert", "18", "Mathematics")
a1.display_student()