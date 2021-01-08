


def f_del(arg_1, arg_2):
    if arg_2 == 0:
        return print('На ноль делить нельзя!')
    else:
        return arg_1 / arg_2
a,b = input('Введите два числа через пробел: ').split()

f_del(int(a),int(b))
print(f_del(int(a),int(b)))
