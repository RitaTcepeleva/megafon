from random import choice

'''
координаты соседей
000
010
000

сама точка имеет коорд х, у
первая строка
x-1, y-1
x-1, y
x-1, y+1
вторая
x, y-1
x, y+1
третья
x+1, y-1
x+1, y
x+1, y+1
'''

#макс размер поля MAX_SIZE x MAX_SIZE
MAX_SIZE = 10

#константы для хранения состояния
DEAD ='0'
ALIVE = '1'


#первое поколение
pole = [
    [choice([DEAD, ALIVE]) for x in range(MAX_SIZE)] for y in range(MAX_SIZE)
]


#создание пустого поля
def fresh_pole():
    return [[DEAD for x in range(MAX_SIZE)] for y in range(MAX_SIZE)]


#вывод поля построчно
def show(pole):
    for x in range(MAX_SIZE):
        print(''.join(pole[x]))


#проверка соседей
def is_alive(pole, neib_x, neib_y):
    return 0 <= neib_y < MAX_SIZE and 0 <= neib_x < MAX_SIZE and pole[neib_x][neib_y] == ALIVE


#рассчет коорд соседей, см коммент вверху
def neib_coord(x, y):
    for delta_x, delta_y in (
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1)
    ):
        yield x + delta_x, y + delta_y


while True:
    input('press smth')
    show(pole)
    new_pole = fresh_pole()
    #начинаем обходить массив клеток
    for x in range(MAX_SIZE):
        for y in range(MAX_SIZE):
            condition = pole[x][y]
            neighbours = 0
            for neib_x, neib_y in neib_coord(x, y):
                if is_alive(pole, neib_x, neib_y):
                    neighbours += 1
            if condition == DEAD:
                new_pole[x][y] = ALIVE if neighbours == 3 else DEAD
            else:
                new_pole[x][y] = ALIVE if neighbours in(2, 3) else DEAD

    if pole == new_pole:
        break

    pole = new_pole
