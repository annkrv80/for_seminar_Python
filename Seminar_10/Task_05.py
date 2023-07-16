#Создайте три (или более) отдельных классов животных.
#Например рыбы, птицы и т.п.
#У каждого класса должны быть как общие свойства,
#например имя, так и специфичные для класса.
#Для каждого класса создайте метод, выводящий
#информацию специфичную для данного класса.


class Animals:
    def __init__ (self, name):
        self.name = name

    
    def name_amimal(self):
        return self.name

class Fish(Animals):
    def __init__ (self, fresh_water, deep, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fresh_water = fresh_water
        self.deep = deep
    
    def specific(self):
        if self.fresh_water:
            return "Пресноводная"
        return "Водится в соленой воде"
    
    def check_deep(self):
        if self.deep < 3:
            return(f'Мелководная до {self.deep} метров')
        elif 3 <=self.deep < 20:
            return(f'Средневодная до {self.deep} метров')
        return (f'Грубоководная более {self.deep} метров')


class Bird(Animals):
    def __init__(self, wingspan, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wingspan = wingspan

    def specific(self):
        wing_length = self.wingspan / 2
        return wing_length
    
class Mammals(Animals):
    def __init__(self, hibernate, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hibernate = hibernate

    def specific(self):
        if self.hibernate:
            return 'Впадает в спячку'
        return 'Невпадает в спячку'

if __name__ =='__main__':
    dog = Mammals(False, 'Собака')
    print(f'Название {dog.name}. Спячка {dog.hibernate}')

    f = Fish(False, 105, 'Акула')
    print(f'Название: {f.name}. {f.specific()}. {f.check_deep()}')

    f2 = Fish(True, 15, 'Окунь')
    print(f'Название: {f2.name}. {f2.specific()}. {f2.check_deep()}')

    b1 = Bird(3, 'Ласточка')
    print(f'Название{b1.name}. Размах крыла {b1.specific()}')
