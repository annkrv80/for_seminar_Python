#Создайте класс Сотрудник.
#Воспользуйтесь классом человека из прошлого задания.
#У сотрудника должен быть:
#○ шестизначный идентификационный номер
#○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь

from random import randint

from Task_03 import Human


class Personal(Human):
    CONSTANT = 7
    def __init__(self, id_num, *args, **kwargs):
        self.id_num = self.get_id_num(id_num)
        self.level = self.level_gen()
        super().__init__(*args, **kwargs)
    
    def level_gen(self):
        return sum(map(int, str(self.id_num))) % self.CONSTANT

    def get_id_num(self, id_num):
        if len(str(id_num)) != 6:
            return randint(100000, 999999)
        return id_num
    
    def get_id(self):
        return self.id_num

    

if __name__ == '__main__':
    p1 = Personal(12524, 22, "Ivanova", "Maria", "Sergeevna")
    print(p1.full_name())
    print(p1.get_id())
    print(p1.level_gen())



