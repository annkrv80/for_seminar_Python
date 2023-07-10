#Напишите функцию, которая преобразует pickle файл
#хранящий список словарей в табличный csv файл.
#Для тестированию возьмите pickle версию файла из задачи
#4 этого семинара.
#Функция должна извлекать ключи словаря для заголовков
#столбца из переданного файла.



import pickle
import csv
import os

def func(pickle_file):
    with (
        open(pickle_file, 'rb') as f_pickle,
        open('pic_csv.csv', 'w', encoding='utf-8',newline='') as f_csv

    ):  
        pickle_list = pickle.load(f_pickle)
        csv_colums = list(pickle_list[0].keys())
        writer = csv.DictWriter(f_csv, fieldnames=csv_colums)

        writer.writeheader()
        for item in pickle_list:
            writer.writerow(item)
              
        
     
            

     
    
      




if __name__ == '__main__':
    func('dct_new.pickle')