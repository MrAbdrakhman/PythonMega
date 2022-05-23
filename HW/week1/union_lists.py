list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
l1=set(list_1)
l2=set(list_2)
l3=l1.union(l2)
list_3=list(l3)
print(list_3)