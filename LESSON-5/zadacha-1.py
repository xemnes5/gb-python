

pr = ' '
with open('test1.txt', 'w') as f:
    while pr:
        pr = input('Введите что угодно: ')
        f.write(pr+'\n')
f.close()
