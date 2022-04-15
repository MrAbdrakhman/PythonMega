a=int(input())
b=len(str(a))
if b==3:
	print("трехзначное")
else:
	print("не 3хзначное")
if a>0 and a%2==0:
	print("число положительное и четное")
else:
	print("число НЕ положительное и четное")
if a//31==0:
	print("число делится на 31 без остатка")
else:
	print("число НЕ делится на 31")
if (a>100 and a//17==0) or (a>150 and a==13**2):
	print (a)
else:
	print()
