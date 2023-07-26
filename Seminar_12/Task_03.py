#Доработайте класс прямоугольник из прошлых семинаров.
#Добавьте возможность изменять длину и ширину
#прямоугольника и встройте контроль недопустимых значений (отрицательных).
#Используйте декораторы свойств.

class Rectangle:
    def __init__(self, length, width = None):
        if width == None:
            self.width = self.length = length
        else:
            self.length = length
            self.width = width

    @property
    def length_1(self):
        return self.length
    
    @property
    def wigth_1(self):
        return self.wigth
    
    @length_1.setter
    def length_1(self, value):
        if value > 0:
            self.length = value
        else:
            print(f'{value} значение не может быть отрицательным')

    @wigth_1.setter
    def wigth(self, value):
        if value > 0:
            self.wigth = value
        else:
            print(f'{value} значение не может быть отрицательным')

    def perimeter_rectagle(self):
        return 2 * (self.length + self.width)
        
    def area_rectagle(self):
        return self.length * self.width
    def __str__(self):
        return f'Экземпляр класса Прямоугольник со сторонами {self.length} и {self.width}'
    
    def __repr__(self) :
        return f'Rectangle ({self.length}, {self.width})'
    
if __name__ == '__main__':
    rec_1 = Rectangle(4,5)
    print(rec_1)
    print(f'{rec_1.perimeter_rectagle()}')
    print(f'{rec_1.area_rectagle()}')
    rec_1.length = 6
    print(rec_1)
    print(f'{rec_1.perimeter_rectagle()}')
    print(f'{rec_1.area_rectagle()}')
    
 
