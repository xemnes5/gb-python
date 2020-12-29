


def my_func(**kwargs):
    print(kwargs)

mydict = {'Имя': 'Pepa', 'Фамилия': 'Форчанович', 'Год рождения': 1900, 'Город': 'Пептаун', 
     'email': 'pupa@mail.ru', 'Телефон': '555-111-00' }

my_func(**mydict)


