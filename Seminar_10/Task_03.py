#Напишите класс для хранения информации о человеке:
#ФИО, возраст и т.п. на ваш выбор.
#У класса должны быть методы birthday для увеличения
#возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор.
#Убедитесь, что свойство возраст недоступно для прямого
#изменения, но есть возможность получить текущий возраст.
class Human:
    def __init__(self, age, surname, name, patronic):
        self.__age = age
        self.surname = surname
        self.name = name
        self.patronic = patronic

    def birthday(salf):
        salf.__age += 1

    def get_age(self):
        return self.__age
    
    def full_name(self):
        return f'{self.surname} {self.name} {self.patronic}'


if __name__=='__main__':
    p1 = Human(10, "Ivanova", "Maria", "Sergeevna")
    p1.birthday()
    print(p1.full_name(), p1.get_age())

        