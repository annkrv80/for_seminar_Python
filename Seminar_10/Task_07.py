#Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
#данных), которые вы уже решали. Превратите функции в методы класса, а
#параметры в свойства. Задачи должны решаться через вызов методов экземпляра. 

import json
class WritingTxtJson:
    def __init__(self, filename):
        self.filename = filename
        
    def new_json_file(self):
        with (
            open(self, 'r', encoding ='utf-8') as f_txt,
            open('new_json_file.json', 'w', encoding = 'utf-8') as f_json
        ):
            dict_res = dict()
            for item in f_txt:
                key, value = item.replace("\n", "").split(" ")
                dict_res[key.capitalize()] = value
            json.dump(dict_res, f_json, ensure_ascii=False, indent=1) 



WritingTxtJson.new_json_file('name_num.txt')