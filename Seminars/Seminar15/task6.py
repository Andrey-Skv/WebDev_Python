import os
import logging
from collections import namedtuple

# Настройка логгирования
logging.basicConfig(filename='directory_content.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Создание объекта namedtuple для хранения информации о содержимом директории
FileItem = namedtuple('FileItem', ['name', 'extension', 'is_dir', 'parent_dir'])

def get_directory_content(directory_path):
    for item in os.listdir(directory_path):
        full_path = os.path.join(directory_path, item)
        name, extension = os.path.splitext(item)
        is_dir = os.path.isdir(full_path)
        parent_dir = os.path.basename(os.path.dirname(full_path))

        # Создание объекта namedtuple для текущего элемента
        file_item = FileItem(name=name, extension=extension, is_dir=is_dir, parent_dir=parent_dir)
        
        # Логирование информации о текущем элементе
        logging.info(f'Name: {name}, Extension: {extension}, Is Directory: {str(is_dir)}, Parent Directory: {parent_dir}')

if __name__ == '__main__':
    import sys

    if len(sys.argv) == 2:
        directory_path = sys.argv[1]
        if os.path.isdir(directory_path):
            get_directory_content(directory_path)
            print("Содержимое директории успешно собрано и записано в файл.")
        else:
            print("Указанный путь не является директорией.")
    else:
        print("Использование: python script.py <путь_до_директории>")
