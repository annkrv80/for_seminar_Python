import sys

data = [1, 'hello', -25, 4.16, frozenset([5]), 'hello']


for i, elem in enumerate(data, 1):
    print(i, elem, id(elem), sys.getsizeof(elem), hash(elem))

    if isinstance(elem, int) and int(elem) > 0:
        print(f'Элемент {elem} целое число больше ноля')
    if isinstance(elem, str):
        print(f'Элемент {elem} - строка ')
    


