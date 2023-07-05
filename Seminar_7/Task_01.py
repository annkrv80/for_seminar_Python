#Напишите функцию, которая заполняет файл
#(добавляет в конец) случайными парами чисел.
# Первое число int, второе - float разделены вертикальной чертой.
# Минимальное число - -1000, максимальное - +1000.
# Количество строк и имя файла передаются как аргументы функции. 

from random import randint, uniform

MIN = -1000
MAX = 1000
COUNT_ROW = 5

def numbers(count, filename):
    for _ in range(count):
        with open(filename, 'a', encoding= 'utf-8') as f:
            f.write(f'{randint(MIN,MAX)}|{round(uniform(MIN,MAX),2)}\n')

if __name__=='__main__':
    numbers(5,'number.txt')