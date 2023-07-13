#Создайте декоратор с параметром.
#Параметр - целое число, количество запусков декорируемой функции.
from functools import wraps
def count(n):
    def deco(func):
        res_list = []
        @wraps(func)
        def wrapper(*args):
            for _ in range(n):
                res_list.append(func(*args))
            print(res_list)
        return wrapper
    return deco


@count(3)
def my_func(*args):
    return args
  

if __name__ == '__main__':
    my_func('Hello, world')
    my_func('Привет, мир')