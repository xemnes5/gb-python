

def my_func(x,y):
    res = 1/x
    for n in range(1,abs(y)):
        res *= 1/x
    return res

x = float(input('Введите действительное положительное число x: '))
y = int(input('Введите целое отрицательное число y: '))

z = my_func(x,y)
print(f'{x} в степени {y} = ', z)

