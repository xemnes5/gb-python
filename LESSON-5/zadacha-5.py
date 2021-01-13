

with open('test5.txt', 'w') as f:
    pr = input('Введите числа через пробел: ')
    f.write(pr)
    f.close()

with open('test5.txt', 'r') as f2:
    nums = f2.read()
    print('Сумма чисел = ', sum([int(x) for x in nums.split()]))
    f2.close()
