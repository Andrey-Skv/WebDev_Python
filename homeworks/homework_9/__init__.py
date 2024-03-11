import math
import json
import csv
from random import randint


def save_to_json(func):
    dict_list = []

    def wrapper(csv_filename):
        with open(csv_filename, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                result = ({"parameters": [*row], "result": func(*map(int, row))})
                dict_list.append(result)
        # print(dict_list)
        with open('result.json', 'w', newline='', encoding='utf-8') as file:
            json.dump(dict_list, file, ensure_ascii=False, indent=2)
        

    return wrapper



def generate_csv_file(file_name, rows):
    with open(file_name, 'w', encoding='utf-8', newline='') as file:
        csv_writer = csv.writer(file)
        for _ in range(rows):
            numbers = [randint(1, 20) for _ in range(3)]
            csv_writer.writerow(numbers)


@save_to_json
def find_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2 * a)
        return x
    else:
        return None

generate_csv_file("input_dat.csv", 101)
find_roots('input_dat.csv')