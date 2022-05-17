# Построить
# класс для описания плоской
# геометрической фигуры: Rectangle (Прямоугольник.).
# Класс
# должен содержать:
# Данные:
# длина и ширина прямоугольника
# Методы для операций с данными:
# Нахождения периметра, площади, изменения размеров,
# печати результата.
# Написать
# программу, демонстрирующую работу с этим классом.
# Pрограмма должна содержать
# меню, позволяющее осуществить проверку всех методов класса.


class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def square(self):
        return self.a * self.b

    def peri(self):
        return (self.a + self.b) * 2

    def change(self, newa, newb):
        self.a = newa
        self.b = newb

    def vyvod(self):
        print(f'Периметр нашего прямоугольника равна = {self.peri()}\nПлощадь нашего прямоугольника равна = {self.square()}')
Mon = Rectangle(3 , 5)

while True:
    print('''1 = per \n2 = izm''')
    a = int(input())
    if a == 1:
        Mon.vyvod()
    elif a == 2:
        newa = int(input('введите сторону а '))
        newb = int(input('введите сторону b '))
        Mon.change(newa, newb)
    else:
        print('Error')
