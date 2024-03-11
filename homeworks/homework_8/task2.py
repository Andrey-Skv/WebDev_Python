""" Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.

Создайте файл __init__.py и запишите в него все функции:
get_dir_size,
save_results_to_json,
save_results_to_csv,
save_results_to_pickle, traverse_directory. """

code = '''import os
import json
import csv
import pickle

def count_files_and_folders(directory):
    total_files = 0
    total_folders = 0

    for root, dirs, files in os.walk(directory):
        total_files += len(files)
        total_folders += len(dirs)
    
    return total_files, total_folders

def get_dir_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
        for d in dirnames:
            dp = os.path.join(dirpath, d)
            total_size += get_dir_size(dp)
    return total_size

def traverse_directory(directory):
    results = []

    for root, dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            size = os.path.getsize(path)
            results.append({'Path': path, 'Type': 'File', 'Size': size})
        
        for name in dirs:
            path = os.path.join(root, name)
            size = get_dir_size(path)
            results.append({'Path': path, 'Type': 'Directory', 'Size': size})

    return results

def save_results_to_json(results, output_file):
    with open(output_file, 'w') as f:
        import json
        json.dump(results, f, indent=4)

def save_results_to_csv(results, output_file):
    with open(output_file, mode='w', newline='') as f:
        import csv
        writer = csv.DictWriter(f, fieldnames=['Path', 'Type', 'Size'])
        writer.writeheader()
        for result in results:
            writer.writerow(result)

def save_results_to_pickle(results, output_file):
    with open(output_file, 'wb') as f:
        import pickle
        pickle.dump(results, f)

# Укажите вашу целевую директорию
directory_path = "your_directory_path"

# Получаем результаты обхода директории
results = traverse_directory(directory_path)

# Сохраняем результаты в различных форматах
save_results_to_json(results, "results.json")
save_results_to_csv(results, "results.csv")
save_results_to_pickle(results, "results.pkl")'''

with open('__init__.py', 'w', encoding='utf-8') as f:
    f.write(code)