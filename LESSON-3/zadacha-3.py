



def my_func(arg_1,arg_2,arg_3):
    my_list = [arg_1, arg_2, arg_3]
    my_list.sort()
    s = my_list[-1] + my_list[-2]
    return s

a = int(input('Введите 1е число: '))
b = int(input('Введите 2е число: '))
c = int(input('Введите 3е число: '))

print('Сумма наибольших двух чисел из этих: ', my_func(a,b,c))

