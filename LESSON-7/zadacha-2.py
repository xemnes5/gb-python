
from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def __init__(self):
        pass

class Tuxedo(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    def volume_cl(self):
        return round(self._height*2 + 0.3, 2)

class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    def volume_cl(self):
        return round(self._size/6.5 + 0.5, 2)

a = Tuxedo(1.78)
print(f'При росте {a.height} м. нужно для костюма: {a.volume_cl()} метров ткани')

b = Coat(10)
print(f'При размере {b.size} (US) нужно для пальто: {b.volume_cl()} метров ткани')

