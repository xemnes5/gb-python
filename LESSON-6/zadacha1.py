
from time import sleep

class TrafficLight:
    
    def __init__(self):
        self.__color = ""
    
    def running(self):
#        for color,secs in self.__colordict.items():
        for color,secs in {'RED' : 7, 'YELLOW' : 2, 'GREEN' : 5}.items():
            self.__color = color
            print(f'Traffic Light\'s current color : {color}')
            sleep(secs)

a = TrafficLight()
a.running()
