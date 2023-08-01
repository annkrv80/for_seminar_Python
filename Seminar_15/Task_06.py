#Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
#Соберите информацию о содержимом в виде объектов namedtuple.
#Каждый объект хранит:
#○ имя файла без расширения или название каталога,
#○ расширение, если это файл,
#○ флаг каталога,
#○ название родительского каталога.
#В процессе сбора сохраните данные в текстовый файл используя логирование.
import os
from collections import namedtuple
import logging

FORMAT = '{levelname} - {asctime}. {msg}'

logging.basicConfig(format=FORMAT, style='{',filename='log_dir', filemode='a', encoding='utf-8', level=logging.INFO)
loger = logging.getLogger(__name__)

def get_info_dir(dir_):
    
    info_dir = os.scandir(dir_)

    Item = namedtuple('Item', ['name', 'expansion', 'is_directory', 'parent_directory'])
    items = []

    for i in info_dir:
        name = os.path.splitext(i.name)[0]
        expansion = os.path.splitext(i.name)[1]
        is_directory = i.is_dir()
        parent_directory = os.path.basename(os.path.normpath(dir_))
        item = Item(name, expansion, is_directory, parent_directory)
        loger.info(f'{name} {expansion} {is_directory} {parent_directory}')
        items.append(item)

    return items

if __name__ == '__main__':
    get_info_dir(os.getcwd())

    #python for_seminar_Python\Seminar_15\Task_06.py