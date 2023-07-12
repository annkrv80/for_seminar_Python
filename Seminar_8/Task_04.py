import json
import csv

def func(csv_file, json_file):
    with (
        open(csv_file, 'r', encoding='utf-8') as f_csv,
        open(json_file, 'w', encoding='utf-8') as f_json
    ):
        file = [*csv.reader(f_csv)]
        header_id, header_name, header_access = file[0]
        lst = []
        for id, name, access in file[1:]:
            lst.append({header_id: id, header_name: name, header_access: access, 'hash': hash(name + id)})
        
        json.dump(lst, f_json, ensure_ascii=False, indent=2)
        

if __name__=='__main__':
    func('new_csv.csv', 'dct_new.json')      
              
