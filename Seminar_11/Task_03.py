#Дорабатываем класс прямоугольник из прошлого семинара.
#Добавьте возможность сложения и вычитания.
#При этом должен создаваться новый экземпляр прямоугольника.
#Складываем и вычитаем периметры, а не длинну и ширину.
#При вычитании не допускайте отрицательных значений.

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
    rec_1 = Rectangle(4,10)
    rec_2 = Rectangle(4,6)
    print(rec_1)
    print(rec_2)
    print(repr(rec_1))
    print(repr(rec_2))
    print(f'{rec_1.perimeter_rectagle()}, {rec_2.perimeter_rectagle()}')
    rec_3 = rec_1 + rec_2
    print(f'{rec_3.length, rec_3.width}')
    rec_4 = rec_1 - rec_2
    print(f'{rec_4.length, rec_4.width}')
    print(f'{rec_1.area_rectagle()}, {rec_2.area_rectagle()}')
    print(rec_1 == rec_2)
    print(rec_1 > rec_2)
    print(rec_1 < rec_2)
    print(rec_1 >= rec_2)
    print(rec_1 <= rec_2)
    