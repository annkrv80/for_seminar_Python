#Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой 
#чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import csv
import os
import json
from random import randint
from typing import Callable


def deco(func:Callable):
    def wrapper(csv_file):
        with open(csv_file, 'r', encoding='utf-8') as f_csv:
            csv_rider = csv.reader(f_csv)
            for line in csv_rider:
                a,b,c = map(int, line)
                roots = func(a,b,c)
    return wrapper

def save_param(func):
    def wrapper(*args, **kwargs):
        filename = f'{func.__name__}.json'       
        if os.path.exists(filename):
            with open (filename, 'r', encoding='utf-8') as f_json:
                list_file = json.load(f_json)
        else:
            list_file = []
        result = func(*args, **kwargs)
        list_file.append({
            'args':(args, kwargs),
            'result' : result
        })
        with open(filename, 'w', encoding='utf-8') as f_json:
            json.dump(list_file, f_json, indent=1)
    return wrapper

def random_number(csv_file):
    with open (csv_file, 'w', encoding= 'utf-8',newline='') as f_csv:
        csv_write = csv.writer(f_csv, )
        for _ in range(100):
            row = [randint(-100,100) for _ in range(3)]
            csv_write.writerow(row)



@deco
@save_param
def square_equalignment(a,b,c)  :
    d = b ** 2 - 4 * a * c
    if d > 0:
        x_1 = ((-1) * b + pow(d, 0.5)) / 2 * a
        x_2 = ((-1) * b - pow(d, 0.5)) / 2 * a
        return x_1, x_2
    elif d == 0:
        x = -b / (2*a)
        return x_1
    else:
        return None

if __name__ == '__main__':
    random_number('numbers.csv')
    square_equalignment('numbers.csv')