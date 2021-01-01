
from itertools import count,cycle

c = 0
ite1 = count(3)
ite2 = cycle(['uno','dos','tres'])
print(f'итератор count:\n-------')
for el in ite1:
    if el > 10:
        break
    print(el)

print(f'\nитератор cycle:\n-------')
while c < 3:
    print(next(ite2))
    print(next(ite2))
    print(next(ite2))
    c += 1


