
import json

mydict = {}

with open('test7.txt', 'r') as f:
    data = f.readlines()
    for lines in data:
        line = lines.rstrip().split()
        key = line[0]
        value = int(line[-2]) - int(line[-1])
        mydict[key] = value
    f.close()

ave = sum(x for x in mydict.values() if x>0) // len([x for x in mydict.values() if x>0])

data_json = json.dumps([mydict, {'average_profit' : ave}])

with open('test7.json', 'w') as f2:
    f2.write(data_json)
    f2.close()
