""" Задание №2
Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами
из диапазонов.
 """

from typing import Callable
from random import randint


def check_ranges(func: Callable) -> Callable:
    def wrapper(*args):
        if 1 <= args[0] <= 10 and 1 <= args[1] <= 100:
            return func(args[0], args[1])
        print('Generating random arguments.')
        return func(randint(1, 10), randint(1, 100))

    return wrapper


@check_ranges
def prompt(tries: int, num: int):
    while tries > 0:
        print(f'Осталось {tries} попыток.')
        attempt = int(input('Введите число:\n'))
        if attempt == num:
            print('Вы угадали.')
            return True
        else:
            print('Вы не угадали.')
            tries -= 1
            if tries == 0:
                print('Попытки закончились.')
                return False


prompt(1000, 60)