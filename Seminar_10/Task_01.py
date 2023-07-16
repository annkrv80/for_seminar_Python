#Создайте класс окружность.
#Класс должен принимать радиус окружности при создании экземпляра.
#У класса должно быть два метода, возвращающие длину окружности и её площадь.
from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def len_circle(self):
        return 2 * pi * self.radius
    
    def area_circle(self):
        return pi * self.radius ** 2

a = Circle(5)
print(a.len_circle())
print(a.area_circle())