#Вспоминаем задачу из семинара 8 про сериализацию данных,
#где в бесконечном цикле запрашивали имя, личный
#идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
#Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
#Отдельно напишите функцию, которая считывает информацию
#из JSON файла и формирует множество пользователей.
import json

class User:
    def __init__(self, user_id, name, level):
        self.user_id = user_id
        self.name = name
        self.level = level

    def __str__(self):
        return f'Пользователь.\t Индентификационный номер: {self.user_id}, \t Имя: {self.name}, \t \
        Уровень доспупа: {self.level}'
    
    def __eq__(self, other):
        return self.user_id == other.user_id and self.name == other.name
    
def add_user_to_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            my_dict = json.load(f)
    except Exception:
        my_dict = {str(level) : {} for level in range(1,8)}
    while True:
        name, user_id, level = input('Введите имя, ID и уровень через пробел: ').split()
        try:
            if user_id not in my_dict[level].keys():
                my_dict[level].update({user_id: name})
                break
            else:
                print('ID должен быть уникальным!!!')
        except KeyError as e:
            print(f'Ошибка ввода уровня {e}')
    print(f'{my_dict = }')

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_dict, f, indent=1, ensure_ascii=False)
    
if __name__ == '__main__':
    #u_1 = User('1', 'ann', 5)
    #u_2 = User('1', 'ann', 6)
    #u_3 = User('2', 'max', 3)
    #print(u_1 == u_2)
    #print(u_1 == u_3)
    filename = 'users.json'
    add_user_to_file(filename)
        
