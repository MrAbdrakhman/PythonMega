a=int(input())
b=int(input())
c=int(input())
d=int(input())
if a>b and a>c and a>d:
    max=a
else:
    if b>a and b>c and b>d:
        max=b
    else:
        if c>b and c>a and c>d:
            max=c
        else:
            max=d
print (max)
