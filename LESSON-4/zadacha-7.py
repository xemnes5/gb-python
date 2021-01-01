

def fact(n):
    x = 1 
    a = 1
    while n >= a:
        yield x
        a += 1
        x *= a

n = int(input('Введите значение n! : '))

for el in fact(n):
    print(el)

