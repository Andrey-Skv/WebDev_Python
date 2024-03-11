""" Задание №1
Создайте функцию, которая запрашивает числовые данные от
пользователя до тех пор, пока он не введёт целое или
вещественное число.
Обрабатывайте не числовые данные как исключения. """


import codecs


def get_numeric_input():
    while True:
        try:
            user_input = float(input("Введите число: "))
            return user_input
        except ValueError as e:
            print(f'Ваш ввод привёл к ошибке ValueError: {e}\n'
                  f'Попробуйте снова')
            

# Пример использования функции
numeric_data = get_numeric_input()
print("Вы ввели числовое значение:", numeric_data)
