import json
import csv


def func(file_json):
    with (
        open(file_json, 'r', encoding='utf-8') as f_json,
        open('new_csv.csv', 'w', encoding='utf-8', newline='') as f_cvs
    ):
        json_dict = json.load(f_json)
        print(json_dict)
        rows = []
        for level, id_dict in json_dict.items():
            for id, name in id_dict.items():
                rows.append({'id':id,'name':name, 'level': level})
            
        print(rows)
        csv.writer = csv.DictWriter(f_cvs, fieldnames=['id', 'name', 'level'])
        csv.writer.writeheader()
        csv.writer.writerows(rows)
       


if __name__ == '__main__':
    func('dct.json')

