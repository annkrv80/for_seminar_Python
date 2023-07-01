from random import randint
import sys

START = 10
STOP = 100
chance = 10

def lottery(start, stop, count):
    count = 0
    num = randint(start, stop)

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
            print(f'Увы! Загаданое число{num}')
            return False

if __name__ == '__main__':
    _, START, STOP, CHANGE = sys.argv
    #print(start, stop, chance)
    lottery(int(START), int(STOP), int(CHANGE))

__all__ = ['lottery']