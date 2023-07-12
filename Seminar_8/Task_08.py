#Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и
#все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
#Для дочерних объектов указывайте родительскую директорию.
#Для каждого объекта укажите файл это или директория. Для файлов сохраните его размер в байтах, 
#а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
import json
import csv
import json
import os
import pickle

def get_dir_size(directory):
    size = 0
    for root, dir, file in os.walk(directory):
        dir_path = os.path.abspath(root)
        size  += sum(os.path.getsize(os.path.join(dir_path, file_name)) for file_name in file)
    return size

def get_info_dir(dir_):

    dir_info={}
    for root, dir, file in os.walk(dir_):
        dir_path = os.path.abspath(root)
        dir_file = []
        for file_name in file:
            file_path = os.path.join(dir_path, file_name)
            file_size = os.path.getsize(file_path)
            file_info = {'name': file_name, 'type': 'file', 'size': file_size, 'parent': dir_path }
            dir_file.append(file_info)
        for dir_name in dir:
            inter_dir_path = os.path.join(dir_path, dir_name)
            inter_dir_size = get_dir_size(inter_dir_path)
            inter_dir_info = {'name': dir_name, 'type': 'directory', 'size': inter_dir_size, 'parent': dir_path }
            dir_file.append(inter_dir_info)
        dir_info[dir_path] = dir_file

    with (
        open('info_dir_json.json', 'w', encoding='utf-8') as f_json,
        open('info_dir_csv.csv', 'w', encoding='utf-8') as f_csv,
        open('info_dir_pickle.pickle', 'wb') as f_pickle

    ):
        json.dump(dir_info, f_json, indent=1 )
        pickle.dump(dir_info, f_pickle)
        colums = ['name', 'type', 'size','parent']
        writer = csv.DictWriter(f_csv, fieldnames=colums)
        writer.writeheader()
        for dir_path, file_info in dir_info.items():
            for file in file_info:
                writer.writerow(file)



if __name__ == '__main__':
    get_info_dir(os.getcwd())