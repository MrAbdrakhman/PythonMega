a=17391
b=546
c=936
q=a%17
w=b%17
e=c%17
if q<w and q<e:
	max=q
elif w<q and w<e:
	max=w
else:
	max=e
print (q,w,e)
print ('min ostatok = ', max)
