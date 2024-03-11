""" Задание №3
Напишите декоратор, который сохраняет в json файл
параметры декорируемой функции и результат, который она
возвращает. При повторном вызове файл должен
расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ
json словаря.
Для декорирования напишите функцию, которая может
принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой
функции. """

import json
import os
from typing import Callable, Any


def save_to_json(filename: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Any:
            result = func(*args, **kwargs)

            data = {
                'function_name': func.__name__,
                'args': args,
                'kwargs': kwargs,
                'result': result
            }

            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    existing_data = json.load(file)

                existing_data.append(data)

                with open(filename, 'w') as file:
                    json.dump(existing_data, file, indent=2)
            else:
                with open(filename, 'w') as file:
                    json.dump([data], file, indent=2)

            return result

        return wrapper

    return decorator


# @save_to_json("function_data.json")
def example_function(a: int, b: int, c: int = 3) -> int:
    return a + b + c


# example_function(34, 56, c=555)
#
# example_function(4666, 5666, c=666)

save_to_json('function_data.json')(example_function)(10, 100, 1000)

#

from random import randint
import functools
import json


def nums_decorator(func):
    @functools.wraps(func)
    def wrapper():
        hidden_num = int(input('Задайте число от 1 до 100: '))
        if not 0 < hidden_num < 101:
            hidden_num = randint(1, 100)
        attempts_num = int(input('Установите число попыток от 1 до 10: '))
        if not 0 < attempts_num < 11:
            attempts_num = randint(1, 10)
        result = func(hidden_num, attempts_num)
        result_dict = {f'{hidden_num}, {attempts_num}': result}
        with open(f'{func.__name__}.json', 'a', encoding='utf-8') as f:
            json.dump(result_dict, f, ensure_ascii=False, separators=(',\n', ': '))
        return result

    return wrapper


@nums_decorator
def guess_num(hidden_num=0, attempts_num=0):
    for i in range(attempts_num):
        user_num = int(input('Введите своё число: '))
        if user_num == hidden_num:
            return f'Вы угадали c {i + 1} попытки!'
    return 'Попытки закончились, вы не угадали!'


print(guess_num())