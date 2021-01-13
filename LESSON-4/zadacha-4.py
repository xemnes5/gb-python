


lst1 =  [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(f'исходный лист : {lst1}')
print(f'полученный лист : ', [el for el in lst1 if lst1.count(el) == 1])
