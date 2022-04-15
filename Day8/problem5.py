# 2 circles
list=[]
for i in range(10):
	list.append(i+1)
for i in range(9,0,-1):
	list.append(i)
print(list)

# 1 cirle

list=[]
f=10
i=1
while True:
	list.append(i)
	if  i==10:
		list.append(i)
		i=i-1
		if i==1:
			break
	i=i+1
print(list)
