#Доработаем задачи 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
from Task_05 import Animals, Fish, Bird, Mammals


class Factory:
    def __init__(self, factory_type, **kwargs):
        self.factory_type = factory_type


    def create_instance(factory_type,*args, **kwargs):
        if factory_type == 'Fish':
            return Fish(*args, **kwargs)
        elif factory_type == 'Bird':
            return Bird(*args,**kwargs)
        elif factory_type == 'Mammals':
            return Mammals(*args,**kwargs)
        else:
            return f'Не удалось опреледить тип животного'


p1 = Factory.create_instance('Fish', True, 10, 'Щука') 
print(f'Название: {p1.name}. {p1.specific()}. {p1.check_deep()}')
p2 = Factory.create_instance('Bird',5 ,'Орел' )
print(f'Название: {p2.name}. Размах крыла: {p2.specific()}')
p3 = Factory.create_instance('Mammals', True, 'Медведь')
print(f'Название: {p3.name}. {p3.specific()}')