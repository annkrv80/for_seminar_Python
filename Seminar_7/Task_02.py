# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы,
#состоять из 4-7 букв, среди которых
#обязательно должны быть гласные.
# Полученные имена сохраните в файл.
from random import sample, randint, choice

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
vowels = 'AEIOUY'
MIN_LEN = 4
MAX_LEN = 7
COUNT_ROW = 5

def names(count, filename):
    with open(filename, 'a', encoding='utf-8') as f:
        for _ in range(count):
            name = sample(letters, randint(MIN_LEN, MAX_LEN))
            if not set(name) & set(vowels):
                str(name).replace(choice(name), choice(vowels))             
            name = ''.join(name).capitalize()
            f.write(f'{name}\n')

if __name__=='__main__':
    names(5,'name.txt')