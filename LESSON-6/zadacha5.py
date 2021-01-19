

class Stationery:
    def __init__(self, title):
        self.title = title
    
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Отрисовка Ручки!')

class Pencil(Stationery):
    def draw(self):
        print('Отрисовка Карандаша!')

class Handle(Stationery):
    def draw(self):
        print('Отрисовка Маркера!')


a,b,c,d = Stationery('Объект родительского класса'), Pen('Ручка'), Pencil('Карандаш'), Handle('Маркер')

for i in [a,b,c,d]:
    i.draw()

