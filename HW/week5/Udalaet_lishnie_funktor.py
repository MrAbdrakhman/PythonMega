class Stripchar:
    def __init__(self, chars):
        self.__count=0
        self.__chars=chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError("should be str")

        return args[0].strip(self.__chars)

s1 =Stripchar('?:!;,')
s2 =Stripchar(' ')
res = s1("Hello world!")
res2 = s2("  Hello world ! ")
print(res, res2, sep="\n")