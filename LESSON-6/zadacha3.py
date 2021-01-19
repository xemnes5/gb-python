

class Worker:
    def __init__(self,name,surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage' : wage, 'bonus': bonus}
        
class Position(Worker):
    def get_full_name(self):
        return self.name +' '+ self.surname

    def get_total_income(self):
        return sum(self._income.values())

attr_t = '-Атрибуты- \nName: {}\nSurname: {}\nPosition: {}'

a = Position('Vasya', 'Pupov', 'Повар', 100, 50)
b = Position('Pupa', 'Vasev', 'Кот', 200, 100)

for person in [a,b]:
    print(attr_t.format(person.name, person.surname, person.position))
    print('-Методы- \nПолное Имя : {} \nTotal income : {} \n------------'.format(person.get_full_name(), person.get_total_income()))
