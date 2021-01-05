
import re

mydict = {}

with open('test6.txt', 'r') as f:
    for line in f:
        key = line.split()[0]
        value = sum(int(x) for x in re.findall(r'\d+', line))
        mydict[key] = value
    f.close()

print(mydict)


