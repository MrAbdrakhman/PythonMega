k=int(input("объем сковородки на котлеты ")) # kotlety na skovorodke
m=int(input("время обжарки стороны котлеты ")) # minuty
n=int(input("количество котлет ")) # kol kotlet
num_st=n*2 #kol storon kotlet
a=(num_st*m)/k
print('минимальное время обжарки котлет ', int(a), 'минут')