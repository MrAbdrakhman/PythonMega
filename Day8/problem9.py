k=0
t=0
j=0
for i in range(-100,100,1):
	j=+1
	if i%13==0 and i%2==0:
		i=i**2
		k+=1
		print(i, end=" ")
	if j%7==0 :
		print(i, end=" ") 
		t+=1

print("1-cond= ", k)
print("2-cond= ", t)
