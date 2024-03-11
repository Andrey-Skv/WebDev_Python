""" Напишите функцию группового переименования файлов в папке test_folder под названием rename_files.
 Она должна:

a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый 
номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно работать только для этих 
файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы
 с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. 
 Далее счётчик файлов и расширение.
f. Папка test_folder доступна из текущей директории

Пример использования.

На входе:


rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")
На выходе:


new_file_008.doc, test.doc, new_file_004.doc, new_file_005.doc, new_file_007.doc, new_file_001.doc,
 new_file_006.doc, new_file_003.doc, new_file_002.doc, new_file_009.doc, new_file_010.doc """

# import os

# def rename_files(desired_name, num_digits, source_ext, target_ext, name_range):
#     folder_path = "test_folder"
#     files = [f for f in os.listdir(folder_path) if f.endswith("." + source_ext)]

#     files.sort()

#     for i, file_name in enumerate(files, 1):
#         original_name_range = slice(name_range[0] - 1, name_range[1])
#         original_name = file_name[original_name_range]

#         new_file_name = f"{desired_name}{original_name}_{i:0{num_digits}}.{target_ext}"
#         os.replace(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))
#         print(new_file_name)

# # Пример использования
# rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc", name_range=(3, 6))

import os
import random
import string


def create_test_files(num_files, ext):
    folder_path = "test_folder"
    os.makedirs(folder_path, exist_ok=True)

    for i in range(1, num_files + 1):
        file_name = f"file_{i}.{ext}"
        with open(os.path.join(folder_path, file_name), "w") as file:
            file.write("This is a test file.")


def rename_files(desired_name, num_digits, source_ext, target_ext):
    folder_path = "test_folder"
    files = [f for f in os.listdir(
        folder_path) if f.endswith("." + source_ext)]

    files.sort()

    for i, file_name in enumerate(files, 1):
        new_file_name = f"{desired_name}{i:0{num_digits}}.{target_ext}"
        os.replace(os.path.join(folder_path, file_name),
                   os.path.join(folder_path, new_file_name))
        print(new_file_name, end=', ')


# Создание тестовых файлов в папке
create_test_files(10, "txt")

# Переименование файлов с указанными параметрами
rename_files(desired_name="new_file", num_digits=3,
             source_ext="txt", target_ext="doc")
