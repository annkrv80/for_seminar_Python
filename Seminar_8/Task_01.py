import json

def new_json_file(filename):
    with (
        open(filename, 'r', encoding ='utf-8') as f_txt,
        open('new_json_file.json', 'w', encoding = 'utf-8') as f_json
    ):
        dict_res = dict()
        for item in f_txt:
            key, value = item.replace("\n", "").split(" ")
            dict_res[key.capitalize()] = value
        json.dump(dict_res, f_json, ensure_ascii=False, indent=1) 


new_json_file('name_num.txt')   
        
