''' Написать программу калькулятор оценок. Даны списки оценок с
предметами трех студентов. В каждом списке содержиться 7
предметов с оценками, необходимо сконвертировать в словарь и
найти средний балл оценок данных студентов. И выбрать лучшего
студента в группе.
Например:
ввод данных John = [[algebra“, 100], [„biologia“, 84], [„fizika“: 61]]
вывод: оценки

John   : {'algebra': 100, 'biologia': 84, 'fizika': 61}
Средний балл

John   : 81 балл
Лучшим студентом является: {имя студенто у которго больше всех
балл}
'''
John = [['algebra', 100], ['biologia', 100], ['fizika', 61],['geo', 50],['lang', 80],['lit', 50],['python', 100]]
Jack = [['algebra', 90], ["biologia", 85], ['fizika', 78],['geo', 60],['lang', 70],['lit', 50],['python', 90]]
Tomas = [['algebra', 80], ['biologia', 84], ['fizika', 80],['geo', 70],['lang', 60],['lit', 50],['python', 80]]
total_st={}
def dict_st(a):
    st1 = {}
    for i in a:
        st1.update({i[0]:i[1]})
    return st1
def aver_sc(a):
    s=0
    for i in a:
        x=int(a.get(i))
        s+=x
    return int(s/7)
print('John: ', dict_st(John))
print('средний балл : ')
print('John: ', aver_sc(dict_st(John)),'балл')
total_st.update({"John": aver_sc(dict_st(John))})
print()
print('Jack:' , dict_st(Jack))
print('средний балл : ')
print('Jack: ', aver_sc(dict_st(Jack)),'балл')
total_st.update({"Jack": aver_sc(dict_st(Jack))})
print()
print('Tomas :',  dict_st(Tomas))
print('средний балл : ')
print('Tomas: ', aver_sc(dict_st(Tomas)),'балл')
total_st.update({"Tomas": aver_sc(dict_st(Tomas))})
print()

print (total_st)
max_Score = max( zip(total_st.values(),total_st.keys()) )
print('Лучшим студентом является: ', max_Score)