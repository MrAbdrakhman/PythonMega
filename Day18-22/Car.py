''' Создайте класс Car. Пропишите в конструкторе параметры make, model, year,
odometer, fuel. Пусть у показателя odometer будет первоначальное значение 0,
а у fuel 70. Добавьте метод drive, который будет принимать расстояние в км. В
самом начале проверьте, хватит ли вам бензина из расчета того, что машина
расходует 10 л / 100 км (1л - 10 км) . Если его хватит на введенное расстояние,
то пусть этот метод добавляет эти километры к значению одометра, но не
напрямую, а с помощью приватного метода __add_distance. Помимо этого
пусть метод drive также отнимет потраченное количество бензина с помощью
приватного метода __subtract_fuel, затем пусть распечатает на экран “Let’s
drive!”. Если же бензина не хватит, то распечатайте “Need more fuel, please, fill
more!” '''


class Car():
    """ Модель автомобиля."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.fuel = 70

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def drive(self, km):
        a = km / self.fuel
        print(a)


'''
    def rodometer(self): #Выводит пробег машины в км
        print(f"На одометре {self.odometer} km.")

    def update_odometer(self, km): #обновляет километраж
        if km >=self.odometer:
            self.odometer=km
        else:
            print("Вы не можете уменьшить километраж")

    def change_odometer(self, km):
        self.odometer += km'''


# def add_distanse(self):
#    pass

def subtract_fuel(self):
    print("Need more fuel, please, fill more!")
    print("let's drive!")


new_car = Car('audi', 'a4', 2019)
car2 = Car('honda', 'crv', 2003)
print(new_car.get_descriptive_name())
print(drive(45))

# new_car.rodometer()
# new_car.odometer =23
# new_car.rodometer()
# new_car.update_odometer(26)
# new_car.rodometer()
# new_car.change_odometer(60)
# new_car.rodometer()
# print(car2.get_descriptive_name())

