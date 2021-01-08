

def int_func(*words):
    a = []
    mylist = words[0].split()
    for word in mylist:
        a.append(word.capitalize())
    return ' '.join(a)


print('Пример 1. Исходная строка = "text"')
print(int_func('text'))
print('Пример 2. Исходная строка = "la li lu le lo"')
print(int_func('la li lu le lo'))
pr = input('Пример 3. Введите слова с маленькой буквы через пробел: ')
print(int_func(pr))

