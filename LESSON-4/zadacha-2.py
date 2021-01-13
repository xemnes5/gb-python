

lst1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
lst2 = [el for el in lst1[1:] if el > lst1[lst1.index(el)-1]]

print(f'Исходный список: {lst1}')
print(f'Полученный список: {lst2}')

