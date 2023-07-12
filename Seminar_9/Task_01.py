#Создайте функцию-замыкание, которая запрашивает два целых
#числа:
# от 1 до 100 для загадывания,
# от 1 до 10 для количества попыток
#Функция возвращает функцию, которая через консоль просит
#угадать загаданное число за указанное число попыток.

from random import randint

def make(num, chance):
    def game():
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
                print(f'Увы! Загаданое число{num}')
                return False
        
    return game


if __name__ == '__main__':
    number = 10
    chance = 5
    res = make(number, chance)
    res()
