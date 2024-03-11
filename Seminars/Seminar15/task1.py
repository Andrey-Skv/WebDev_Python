"""
Задание №1
📌 Напишите программу, которая использует модуль logging для
вывода сообщения об ошибке в файл.
📌 Например отлавливаем ошибку деления на ноль.
"""

import logging

# logging.basicConfig(filename='example.log.', filemode='w',  encoding='utf-8', format='{levelname} - {asctime} в строке {lineno} ''функция "{funcName}()" : {msg}', style='{', level=logging.WARNING)

root_logger= logging.getLogger()
root_logger.setLevel(logging.WARNING) # or whatever
handler = logging.FileHandler('test.log', 'w', 'utf-8') # or whatever
handler.setFormatter(logging.Formatter('%(name)s %(message)s')) # or whatever
root_logger.addHandler(handler)

def func(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        logging.warning('Нельзя делить на ноль')
        return ''
    else:
        return res


print(func(5, 0))