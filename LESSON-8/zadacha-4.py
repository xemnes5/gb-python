

class Sklad:
    pass

class Orgtech:
    def __init__(self, model, vendor, warranty):
        self.model = model
        self.vendor = vendor
        self.warranty = warranty
    
    def __str__(self):
        return f'\nМодель: {self.model} \nВендор: {self.vendor} \nГарантия: {self.warranty}'


class Printer(Orgtech):
    def __init__(self, *attrs, powders):
        Orgtech.__init__(self, *attrs)
        self.powders = powders
    def __str__(self):
        return f'{super().__str__()} \nПорошка: {self.powders}'

class Scaner(Orgtech):
    def __init__(self, *attrs, scans):
        Orgtech.__init__(self, *attrs)
        self.scans = scans
    def __str__(self):
        return f'{super().__str__()} {self.scans}'

class Xerox(Orgtech):
    def __init__(self, *attrs, xers):
        Orgtech.__init__(self, *attrs)
        self.xers = xers
    def __str__(self):
        return f'{super().__str__()} {self.xers}'

a1 = Printer('model-1', 'cisco', 4, powders=500)
b1 = Scaner('model-2', 'junip', 2, scans=150)
c1 = Xerox('model-3', 'xerow', 3, xers=10)
#print(a1.model, a1.vendor)
print(a1)
print(b1)
print(c1)
