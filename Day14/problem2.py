def user(log,passwd):
    with open('users.txt', 'w') as f:
        f.write(f'{log}:{passwd}')
log=input()
passwd=input()
user(log,passwd)