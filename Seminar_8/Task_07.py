#Прочитайте созданный в прошлом задании csv файл без
#использования csv.DictReader.
#Распечатайте его как pickle строку.
import csv
import pickle
import os

def func(file_csv):
    with(open(file_csv, 'r', encoding='utf-8') as f_csv):
        file = [*csv.reader(f_csv)]
        header_id, header_name, header_level, header_hash = file[0]
        lst = []
        for id, name, level, hash in file[1:]:
            lst.append({header_id: id, header_name: name, header_level: level, header_hash: hash})

        res = pickle.dumps(lst)
        print(f'{res = }')


if __name__ == '__main__':
    func('pic_csv.csv')

        
