

with open('test2.txt', 'r') as f:
    data = f.readlines()
    print('Количество строк в файле = ', len(data))
    for lines in data:
        line = lines.strip('\n')
        print(f'Количество слов в строчке "{line}" = ', len(line.split()))
    f.close()

