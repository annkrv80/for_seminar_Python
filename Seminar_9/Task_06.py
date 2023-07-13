#Доработайте прошлую задачу добавив декоратор wraps в
#каждый из декораторов.
from typing import Callable
from functools import wraps

from Task_02 import deco as control
from Task_03 import deco as save_param
from Task_04 import count as counter

@counter(3)
@save_param
@control
def game(num, chance):
    """ Игра угадай число"""
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
    game(10,6)
    print(game.__name__)

