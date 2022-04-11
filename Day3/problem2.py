a=int(input())
b=int(input())
c=int(input())
if a>b:
     max=a
     min=b
else:
    max=b
    min=a
if c>max:
    max=c
else c<min:
     min=c
print ("max =", max,'min= ',min)

