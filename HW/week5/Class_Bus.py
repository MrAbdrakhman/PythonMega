'''Дом задание: Создайте класс Bus, унаследованный от класса Vehicle. Задайте аргументу capacity
Bus.seating_capacity() значение по умолчанию 50
Используйте следующий код для родительского класса Vehicle. Вам нужно использовать переопределение метода.
'''

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

    def get_info(self):
        long_name=f"марка: {self.name} километраж: {self.mileage} скорость: {self.max_speed}"
        return long_name.title()

    def cargo(self):
        print("грузовой отсек 1-10 тонн")

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)
        self.capacity = 50

    def cargo(self):
        print("нет грузового отсека")

a1=Vehicle("Honda", "100", 200)
b1=Bus('Ikarus', "100", "500")
print(a1.get_info())
print(a1.cargo())
print(b1.get_info())
print(b1.seating_capacity(20))
print(b1.cargo())
