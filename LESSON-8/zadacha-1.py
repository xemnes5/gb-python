

class Data:
    def __init__(self, dates):
        self.dates = dates
        
    @classmethod
    def meth_1(cls, dates):
        day, month, year = [int(i) for i in dates.split('-')]
        return day, month, year
    
    @staticmethod    
    def meth_2(day, month, year):
        if day not in range(1,32):
            return  'Day is incorrect!'
        if month not in range(1,13):
            return 'Month is incorrect!'
        if year not in range(1,2022):
            return 'Year is incorrect!'

    def __str__(self):
        return f'{Data.meth_1(self.dates)}'

d1 = Data('1-20-2030')
#print(d1.meth_1('1-20-2030'))
#print(d1.meth_2(1,20,2030))
#print(d1.meth_2(1,12,2030))
Data.meth_2(5,10,2020)
