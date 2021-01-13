

from sys import argv

def my_func(*args):
    '''Расчет зп работника'''
    if not args:
        print('Вызовите скрипт с доп параметрами: python zadacha-1.py {выработка в часах} {ставка в час} {премия}')
    else:
        vira, stav, prem = args
        print('Итоговая зп = ', int(vira)*int(stav)+int(prem))


my_func(*argv[1:])

