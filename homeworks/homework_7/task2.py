""" Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.

Создайте файл __init__.py и запишите в него функцию rename_files """

your_code_from_7 = '''import os
import random
import string


# def create_test_files(num_files, ext):
#     folder_path = "test_folder"
#     os.makedirs(folder_path, exist_ok=True)

#     for i in range(1, num_files + 1):
#         file_name = f"file_{i}.{ext}"
#         with open(os.path.join(folder_path, file_name), "w") as file:
#             file.write("This is a test file.")


def rename_files(desired_name, num_digits, source_ext, target_ext):
    folder_path = "test_folder"
    files = [f for f in os.listdir(
        folder_path) if f.endswith("." + source_ext)]

    files.sort()

    for i, file_name in enumerate(files, 1):
        new_file_name = f"{desired_name}{i:0{num_digits}}.{target_ext}"
        os.replace(os.path.join(folder_path, file_name),
                   os.path.join(folder_path, new_file_name))'''

with open('__init__.py', 'w', encoding='utf-8') as f:
    f.write(your_code_from_7)