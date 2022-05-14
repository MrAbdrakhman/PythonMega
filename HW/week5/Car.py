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
        self.odometer= 0
        self.fuel= 70

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def drive(self,km):
        a = self.fuel / km
        if a < 0.1:
            print("Need more fuel, please, fill more!")
        else:
            self.__subtract_fuel(km)
            print("let's drive!")
            print(f"осталось бензина {self.fuel} литра")
            self.__add_distance(km)

    def __subtract_fuel(self,km):
            self.fuel=self.fuel - (km / 10)

    def __add_distance(self,km):
        self.odometer +=km
        print(f'одометр показывает {self.odometer} км')


new_car = Car('audi', 'a4', 2019)
car2 = Car('honda', 'crv', 2003)
print(new_car.get_descriptive_name())
new_car.drive(500)
new_car.drive(150)