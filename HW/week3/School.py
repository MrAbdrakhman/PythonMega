'''Создайте словарь, связав его с переменной school, и наполните
данными, которые бы отражали количество учащихся в разных
классах (1а, 1б, 2б, 6а, 7в и т. п.). Внесите изменения в словарь
согласно следующему: а) в одном из классов изменилось количество
учащихся, б) в школе появился новый класс, с) в школе был
расформирован (удален) другой класс. Вычислите общее количество
учащихся в школе.'''
school = { '1а' : 24, '1б' : 19, '1в' : 21, '2а' : 23, '2б' : 24 }
school.update({'1a': 30})
school.update({'10b': 30})
school.pop('1б')
s=0
n=list(school.values())
print(school)
for i in range(len(n)):
    s+=int(n[i])
print ('Общее количество учащихся в школе : ',s)