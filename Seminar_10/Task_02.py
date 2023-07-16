#Создайте класс прямоугольник.
#Класс должен принимать длину и ширину при создании экземпляра.
#У класса должно быть два метода, возвращающие периметр и площадь.
#Если при создании экземпляра передаётся только одна
#сторона, считаем что у нас квадрат.
class Rectangle:
    def __init__(self, length, width = None):
        if width == None:
            self.width = self.length = length
        else:
            self.length = length
            self.width = width

    def perimeter_rectagle(self):
        return 2 * (self.length + self.width)
        
    def area_rectagle(self):
        return self.length * self.width
    
p1 = Rectangle(10)
print(p1.perimeter_rectagle())
print(p1.area_rectagle())
        