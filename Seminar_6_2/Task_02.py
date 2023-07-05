def guess_riddle(riddle, answer, chance=3):
    count = 1
    while count <= chance:
        ans = input(f'Отгадай загадку {riddle}. Попытка № {count}!: ').lower()
        if ans in answer:
            print(f'УРА! Вы отгадали c {count}!')
            return count
        else:
            print(f'Ошибка!')
            count += 1
        if count > chance:
            print(f'Вы исчерпали попытки')
            return 0


def collection_riddles():
    riddle_dict ={'Двенадцать братьев друг за другом бродят, друг друга не обходят.': ['месяц', 'месяцы'],\
        'Два бочка, четыре ушка, это мягкая...': ['подушка','подушечка'],\
        'Не огонь, А жжется.':['крапива', 'крапивушка']
    }

    for key, values in riddle_dict.items():
        riddle_result(key, guess_riddle(key, values))


def riddle_result(riddle, count): 
    _result_dict[riddle]=count
    return _result_dict

def print_dict():
    output = "\n".join([f'Загадка "{k}" отгадана с {v} попытки' for k, v in _result_dict.items()])
    print(output)


_result_dict = {}    

if __name__ == '__main__':
    collection_riddles()
    print_dict()

__all__ = ['collection_riddles', 'print_dict']