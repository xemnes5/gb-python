

with open('test4.txt','r') as f:
    data = f.readlines()

mydict = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}

with open('test4-2.txt','w') as f2:
    for line in data:
        f2.write(line.replace(line[:line.find(' ')],mydict[line[:line.find(' ')]]))

f.close()
f2.close()

