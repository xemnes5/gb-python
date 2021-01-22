

class Road:
    def __init__(self,length,width):
        self._length = length
        self._width = width
    
    def mass(self):
        return self._length*self._width*25*5

a = Road(10,100)
b = Road(20,200)
print('Масса асфальта первого экземпляра =', a.mass())
print('Масса асфальта первого экземпляра =', b.mass())

