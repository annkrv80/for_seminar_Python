#Создайте класс прямоугольник.
#Класс должен принимать длину и ширину при создании экземпляра.
#У класса должно быть два метода, возвращающие периметр и площадь.
#Если при создании экземпляра передаётся только одна
#сторона, считаем что у нас квадрат.
class Rectangle:
    """Rectangle class with specified sides."""
    def __init__(self, length, width = None):
        if width == None:
            self.width = self.length = length
        else:
            self.length = length
            self.width = width

    def perimeter_rectagle(self):
        """Calculating the perimeter."""
        return 2 * (self.length + self.width)
        
    def area_rectagle(self):
        return self.length * self.width
    
    def __add__(self, other):
        p = self.perimeter_rectagle() + other.perimeter_rectagle()
        return Rectangle(p // 2 - self.width, self.width)
    
    def __sub__(self, other):
        p = self.perimeter_rectagle() - other.perimeter_rectagle()
        return Rectangle(abs(p // 4))
    
    def __eq__(self, other):
        return self.area_rectagle() == other.area_rectagle()
    
    def __gt__(self, other):
        return self.area_rectagle() > other.area_rectagle()
    
    def __lt__(self, other):
        return self.area_rectagle() < other.area_rectagle()
    
    def __ge__(self, other):
        return self.area_rectagle() >= other.area_rectagle()
    
    def __le__(self, other):
        return self.area_rectagle() <= other.area_rectagle()
    
    def __str__(self):
        return f'Экземпляр класса Прямоугольник со сторонами {self.length} и {self.width}'
    
    def __repr__(self) :
        return f'Rectangle ({self.length}, {self.width})'

if __name__ == '__main__':
    rec_1 = Rectangle(5,6)
    rec_2 = Rectangle(4,6)
    print(rec_1)
    print(rec_2)
    print(rec_1.perimeter_rectagle())
    print(rec_2.perimeter_rectagle())
    print(rec_1.__add__(rec_2))