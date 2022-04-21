f = open('python.txt', "w+")
f.write("#1 Tom grt title hjk asf xc n,. wert")
f.close()
with open('python.txt', 'r') as f:
    t_words=[]
    txt1=f.read()
    txt2=txt1.split()
    for i in txt2:
        if 't' in i or 'T' in i:
            t_words.append(i)
print(t_words)