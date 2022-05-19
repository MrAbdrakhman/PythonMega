class Calculator:
    def __init__(self, value):
        self.value = value
        if not isinstance(second, float):
            raise TypeError('Введите действительные числа!')
        self.sc = second % self.DAY

    def __add__(self, other):
        return self.value + other # +

    def __sub__(self, other):
        pass # -

    def mul(self, other):
        pass # *

    def truediv(self, other):
        pass # /

    def floordiv(self, other):
        pass # //

    def mod(self, other):
        pass # %

    def iadd(self, other):
        return self.value + other  # +

    def __isub(self, other):
        pass  # -

    def imul(self, other):
        pass  # *

    def itruediv(self, other):
        pass  # /

    def ifloordiv(self, other):
        pass  # //

    def imod(self, other):
        pass  # %

    def radd(self, other):
        return self + other  # +

    def rsub(self, other):
        pass  # -

    def rmul(self, other):
        pass  # *

    def rtruediv(self, other):
        pass  # /

    def rfloordiv(self, other):
        pass  # //

    def rmod(self, other):
        pass  # %

print("Ноль в качестве знака операции"
      "\nзавершит работу программы")
while True:
    s = input("Знак (+,-,*,/): ")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print(x.__add__(y))
            # print("%.2f" % (x+y))
        elif s == '-':
            print(x.__sub__(y))
            # print("%.2f" % (x-y))
        elif s == '*':
            print(x.__mul__(y))
            # print("%.2f" % (x*y))
        elif s == '/':
            if y != 0:
                print(x.__truediv__(y))
                # print("%.2f" % (x/y))
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")

