#Объедините функции из прошлых задач.
#Функцию угадайку задекорируйте:
# декораторами для сохранения параметров,
# декоратором контроля значений и
# декоратором для многократного запуска.
#Выберите верный порядок декораторов.
from typing import Callable

from Task_02 import deco as control
from Task_03 import deco as save_param
from Task_04 import count as counter

@counter(3)
@save_param
@control
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
    game(10,6)