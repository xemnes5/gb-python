


class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __str__(self):
        return f'{self.cells}'

    def __add__(self, other):
        return Cell(self.cells + other.cells)
    
    def __sub__(self, other):
        if self.cells - other.cells > 0:
            return Cell(self.cells - other.cells)
        else:
            raise Exception('Разность должна быть больше нуля!')

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(self.cells // other.cells)

    def make_order(self, num):
        rows = self.cells // num
        remain = self.cells % num
        return ((num*'*'+'\n')*rows + remain*'*')

c1 = Cell(8)
c2 = Cell(13)
c3 = Cell(25)
c4 = Cell(50)
c5 = c1*c2
print(f'Сложение клеток c1(8) + c2(13) : {c1+c2}')
print(f'Вычитание клеток c3(25) - c1(8) : {c3-c1}')
print(f'Умножение клеток c1(8) * c2(13) : {c1*c2}')
print(f'Деление клеток c4(50) / c1(8) : {c4/c1}')
print(f'Клетка c3(25) - упорядочивание(7): \n{c3.make_order(7)}', end='\n')
print(f'Клетка c2(13) - упорядочивание(5): \n{c2.make_order(5)}')



