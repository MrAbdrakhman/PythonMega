with open('database.txt.txt', 'w+') as f:
    f.write("log: asdf passw: qwe123 log: Sam passw we132")
    full_txt = f.read()
    print('Войдите или зарегистрируйтесь')
    enLog = input('Login: ')
    if enLog in f.read():
        print('такой логин уже существует')
        enPass = input('введите Password: ')
    else:
        f.write(enLog)
        enPass = input('введите Password: ')
        enPass1 = input('введите Password еще раз: ')
        if enPass==enPass1:
            f.write(enPass)
            print('вы успешно зарегились')
        else:
            print('ваши пароли не совпадают')