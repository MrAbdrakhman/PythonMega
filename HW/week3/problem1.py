def distanse(a,b,c,d):
    res=((a-c)**2+(b-d)**2)**0.5
    return res
a=int(input())
b=int(input())
c=int(input())
d=int(input())
print(distanse(a,b,c,d))