#Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
#загрузка данных (функция из задания 4)
#вход в систему - требует указать имя и id пользователя. Для
#проверки наличия пользователя в множестве используйте
#магический метод проверки на равенство пользователей.
#Если такого пользователя нет, вызывайте исключение
#доступа. А если пользователь есть, получите его уровень из множества пользователей.
#добавление пользователя. Если уровень пользователя
#меньше, чем ваш уровень, вызывайте исключение уровня доступа

import json
from Task_04 import User
from Task_03 import AccessExeption, LevelExeption

class Project:
    def __init__(self, users):
        self.users = users
        self.admin = None
       

    @classmethod
    def load(cls, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                users_dict = json.load(f)
        except Exception as e:
            print(f'При открытии файла {filename} возникла ошибка {e}')
        else:
            print(f'{users_dict = }')
            users = []
            for level, user in users_dict.items():
                for user_id, name in user.items():
                    users.append(User(user_id, name, level))
            return Project(users)
    
    def __str__(self):
        return str(self.users)
    
    def login(self, user_id, name):
        user_new = User(user_id, name, '')
        if user_new not in self.users:
            raise AccessExeption(user_id)
        for user in self.users:
            if user_new == user:
                self.admin = user
             
    def add_user(self, user_id, name, level):
        if int(self.admin.level) >= int(level) :
            raise LevelExeption(level, name)
        self.users.append(User(user_id, name, level))


if __name__ == '__main__':
    filename = 'users.json'
    project = Project.load(filename)
    print(project)
    project.login('3', 'Anderson')
    print(project.admin)
    project.add_user('014', 'Boss', 1)
    print(*project.users)

