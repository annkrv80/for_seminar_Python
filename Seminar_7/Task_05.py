#Напишите функцию группового переименования файлов. Она должна:
#принимать в качестве аргумента желаемое конечное имя файлов. 
# При переименовании в конце имени добавляется порядковый номер.
#принимать в качестве аргумента расширение исходного файла. 
#Переименование должно работать только для этих файлов внутри каталога.
#принимать в качестве аргумента расширение конечного файла.

import os

def group_rename_files(dir, new_name, original_extension, new_extension):

    dir_path = os.chdir(os.path.join(os.getcwd(), 'dir' ))
    file_list = os.listdir()
   
    
    for i, file_name in enumerate(file_list,1):
        if file_name.endswith(original_extension):
            new_file_name = f"{new_name}{i}{new_extension}"
            os.rename(file_name, new_file_name)

            print(f"Файл {file_name} переименован в {new_file_name}")

group_rename_files('dir','file', '.txt', '.docx')