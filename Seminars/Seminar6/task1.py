""" � Создайте модуль с функцией внутри.
� Функция принимает на вход три целых числа: нижнюю и
верхнюю границу и количество попыток.
� Внутри генерируется случайное число в указанных границах
и пользователь должен угадать его за заданное число
попыток.
� Функция выводит подсказки “больше” и “меньше”.
� Если число угадано, возвращается истина, а если попытки
исчерпаны - ложь. """

# from random import randint


# def guess_number(start, end, attempts):
#     number = randint(start, end)
#     while attempts > 0:
#         my_number = int(input('Введите число: '))
#         if my_number < number:
#             print('Больше')
#         elif my_number > number:
#             print('Меньше')
#         else:
#             print(f'Число угадано. Число оставшихся попыток {attempts - 1}!')
#             return True
#         attempts -= 1
#     else:
#         print(f'Попытки закончились. Это было число {number}')
#         return False


# if __name__ == '__main__':
#     print(guess_number(1, 100, 10))

def is_attacking(q1, q2):
    # Проверяем, бьют ли ферзи друг друга по вертикали, горизонтали или диагоналям
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])

def check_queens(queens):
    # Проверяем все возможные пары ферзей
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if is_attacking(queens[i], queens[j]):
                return False
    return True

# Пример использования
queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]
result = check_queens(queens)
print(result)
