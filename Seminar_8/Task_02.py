import json
import os

def func(filename):
    if os.path.isfile(filename):
        with open (filename, 'r', encoding='utf-8') as f:
            dct = json.load(f)
    else:
        dct = {str(i): {}for i in range(1,8)}


    while True:
        data = input('Введите через пробел имя ID и уровень доспута: ')
        if not data:
            break
        user, id, access = data.split()
        if id not in dct[access]:
            dct.setdefault(access, {id:user})[id] = user
    print(dct)
    with open(filename, 'w', encoding='utf_8') as f_json:
        json.dump(dct, f_json, ensure_ascii=False, indent=1 )


if __name__ == '__main__':
    func('dct.json')