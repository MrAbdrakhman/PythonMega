'''Создайте класс Student, конструктор которого имеет параметры name, lastname,
department, year_of_entrance. Добавьте метод get_student_info, который
возвращает имя, фамилию, год поступления и факультет в
отформатированном виде: “Вася Иванов поступил в 2017 г. на факультет: Программирование.”'''

class Student:
    def __init__(self,name, lastname, year_of_entrance, department):
        self.name=name
        self.lastname = lastname
        self.department = department
        self.year_of_entrance = year_of_entrance

    def get_student_info(self):
        return f'{self.name} {self.lastname} поступил в {self.year_of_entrance} г. на факультет: {self.department}.'

st1=Student( "Вася", "Иванов", 2017, "Програмирование")
st2=Student( "Иван", "Жапаров", 2022, "Физкультура")
st3=Student( "Алмаз", "Капаров", 2005, "Физика")
print(st1.get_student_info())
print(st2.get_student_info())
print(st3.get_student_info())