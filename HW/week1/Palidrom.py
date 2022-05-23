words = ['Anna', 'Civic', 'Kayak', 'Level', 'Madam', 'Mom', 'Noon', 'Racecar', 'Radar', 'еще', 'кабак', 'шалаш', 'лишил','language', 'which', 'means', 'vendor', 'слова', 'фраза', 'введите', 'слово', 'кнопку',]
for i in range(len(words)):
    a=(words[i])
    c=a.lower()
    b=c[::-1]
    if c==b:
        print(c,"=",b, ': палидром')
    else:
        print(c,"-",b, ': НЕ палидром')
