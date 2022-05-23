x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
b=5
if x1>0 and x2>0 and y1>0 and y2>0:
    print("Координаты 2х точек лежат в одной плоскости")
elif x1<0 and x2<0 and y1>0 and y2>0:
    print("Координаты 2х точек лежат в одной плоскости")
elif x1>0 and x2>0 and y1<0 and y2<0:
    print("Координаты 2х точек лежат в одной плоскости")
elif x1<0 and x2<0 and y1<0 and y2<0:
    print("Координаты 2х точек лежат в одной плоскости")
else:
    print("Координаты 2х точек НЕ лежат в одной плоскости")