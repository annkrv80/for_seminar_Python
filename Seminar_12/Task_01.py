#Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
#Экземпляр должен запоминать последние k значений.
#Параметр k передаётся при создании экземпляра.
#Добавьте метод для просмотра ранее вызываемых значений и их факториалов.

from math import factorial
from typing import Any
import json

class Factorial:
    def __init__(self, k):
        self.k = k 
        self.history = []

    def __call__(self, n):
        result = factorial(n)
        self.history.append({n: result})
        self.history = self.history[-self.k:]
        return result

    
    def get_history(self):
        return self.history
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        filename = 'factorial.json'
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.history, f)



if __name__ == '__main__':
    fact = Factorial(5)   
    with fact as f:
        for i in range(3,9):
            fact(i)
       
    