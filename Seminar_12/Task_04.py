#Изменяем класс прямоугольника.
#Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.

class Range:

    def __set_name__(self, owner, name):
        self.param_name = ' ' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)
      
    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if value <= 0:
            raise TypeError(f'Значение {value} должно быть больше 0')
        

class Rectangle:

    length = Range()
    width = Range()

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
    def __str__(self):
        return f'Экземпляр класса Прямоугольник со сторонами {self.length} и {self.width}'
    
    def __repr__(self) :
        return f'Rectangle ({self.length}, {self.width})'
    
if __name__ == '__main__':
    rec_1 = Rectangle(4,5)
    print(rec_1)
    print(f'{rec_1.perimeter_rectagle()}')
    print(f'{rec_1.area_rectagle()}')
    rec_1.length = 10
    print(rec_1)
    print(f'{rec_1.perimeter_rectagle()}')
    print(f'{rec_1.area_rectagle()}')
  
    