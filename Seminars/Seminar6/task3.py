""" � Добавьте в модуль с загадками функцию, которая
принимает на вход строку (текст загадки) и число (номер
попытки, с которой она угадана).
� Функция формирует словарь с информацией о результатах
отгадывания.
� Для хранения используйте защищённый словарь уровня
модуля.
� Отдельно напишите функцию, которая выводит результаты
угадывания из защищённого словаря в удобном для чтения
виде.
� Для формирования результатов используйте генераторное
выражение. """

_dict = {}


def some_func(question: str, count: int):
    answer = 'в правде'
    tries = 0
    while tries < count:
        variant = input('введите ответ:\n')
        if variant == answer:
            _dict[tries + 1] = 'Вы угадали'
            return
        else:
            _dict[tries + 1] = 'Вы не угадали'
            tries += 1


some_func("В чем сила:", 3)

print(_dict)