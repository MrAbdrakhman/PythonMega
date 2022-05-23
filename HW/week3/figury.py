n=int(input())
print("1")
for i in range(n+1):
    print("*"*i)

print('2')
for i in range(n+1):
    print("*"*i)
for j in range(n+1,0,-1):
    print("*" * j)

print('3')
for i in range(0,n):
    print(' '*(n-i),"*"*i*2)
for j in range(n,0,-1):
    print(' '*(n-j),"*"*j*2)