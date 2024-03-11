# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

import csv
import json
from pathlib import Path

_PATH_1 = Path.cwd() / 'task_2' / 'users.json'
_PATH_2 = Path.cwd() / 'task_3' / 'users.csv'


def json_to_csv(source_path: Path = _PATH_1, output_path: Path = _PATH_2):
    with open(source_path, 'r', encoding='utf-8') as source, \
            open(output_path, 'w', encoding='utf-8', newline='') as output:
        data = json.load(source)
        data_list = []
        for access, person in data.items():
            for uid, name in person.items():
                data_list.append([uid, name, access])
        writer = csv.writer(output)
        writer.writerow(['uid', 'name', 'access'])
        writer.writerows(data_list)


if __name__ == '__main__':
    json_to_csv()
