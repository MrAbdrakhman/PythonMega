a={"a":1, 'b':2, "c":3}

def convert(a):
    x=a.keys()
    y=a.values()
    return x,y

print(convert(a))