with open('directories.txt', 'r') as f:
    if 'w' in f.read() or 'W' in f.read():
        print ("Да в тексте есть w")
    else:
        print('Нет')