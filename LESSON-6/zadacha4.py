
class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала.')

    def stop(self):
        print(f'{self.name} остановилась.')

    def turn(self,direction):
        print(f'{self.name} повернула на {direction}')

    def show_speed(self):
        print(f'Скорость {self.name} : {self.speed}')

class TownCar(Car):
    def show_speed(self):
        print(f'Скорость {self.name} : {self.speed}')
        if self.speed > 60:
            print('Скорость превышена!!!')

class WorkCar(Car):
    def show_speed(self):
        print(f'Скорость {self.name} : {self.speed}')
        if self.speed > 40:
            print('Скорость превышена!!!')

class SportCar(Car):
    pass

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police = True):
        Car.__init__(self, speed, color, name, is_police)

attr_t = '----------\nАттрибуты машины:\nname = {}\ncolor = {}\nspeed = {} \nЯвляется копом? : {}'

a = TownCar(61, 'green', 'Toyota-Town')
b = WorkCar(45, 'black', 'Scoda-Work')
c = SportCar('100', 'red', 'McLaren-Sport')
d = PoliceCar('70', 'blue-white', 'Оффицер Пончик')

for car in [a,b,c,d]:
    print('--------\n')
    print(attr_t.format(car.name, car.color, car.speed, car.is_police))
    print('\nМетоды машины:')
    car.go()
    car.turn('Somewhere Street')
    car.show_speed()
    car.stop()
