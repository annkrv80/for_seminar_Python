#Дорабатываем задачу 1.
#Превратите внешнюю функцию в декоратор.
#Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
#Если не входят, вызывать функцию со случайными числами
#из диапазонов.

from typing import Callable
from random import randint
from functools import wraps

def deco(func: Callable):
    @wraps(func)
    def wrapper(number, chance):
        if not 1 <= number <= 100 :
            number = randint(1, 100)
        if not 1 <= chance <= 10:
            chance = randint(1,10)
            func(number, chance)
        func(number, chance)
    return wrapper


@deco
def game(num, chance):
    count = 0
    while count < chance:
        dig = int(input(f'Попытка №{chance - count}. Отгадай число: '))
        count += 1
        if dig > num:
            print('Меньше')
        elif dig < num:
            print('Больше')
        elif dig == num:
            print('ПОБЕДА!!!')
            return True
            
        if count == chance:
            print(f'Увы! Загаданое число{num} ')
            return False
        
if __name__ == '__main__':
    game(6,9)
        
