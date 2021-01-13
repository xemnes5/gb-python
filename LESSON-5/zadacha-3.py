
import re

with open('test3.txt', 'r') as f:
    data = f.read()
    f.close()

print('Оклад менее 20000: ')
for lines in data.rstrip().split('\n'):
    line = lines.split()
    if int(line[-1]) < 20000:
        print(line[0])

ave = sum(int(x) for x in re.findall(r'\d+',data)) // len(re.findall(r'\d+',data)) 
print(f'-----------\nСредний доход всех сотрудников: {ave}')
